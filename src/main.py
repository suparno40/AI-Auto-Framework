import logging
import json
import os
import sys
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Konfigurasi Logging Standard
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

# Memaksa Python memasang root folder 'src' ke dalam path pencarian lokal
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Menggunakan Import Langsung yang Selaras dengan Struktur Struktur Folder Anda
try:
    from prompt_engine.builder import build_prompt
    from ai_provider.groq import ask_ai
    from job_search import JobSearchEngine, RemotiveSource, JobParser
    from storage import GoogleSheetsStorage
    from document_generator import CoverLetterGenerator
except ImportError:
    # Fallback jika dijalankan dari root luar lingkungan tertentu
    from src.prompt_engine.builder import build_prompt
    from src.ai_provider.groq import ask_ai
    from src.job_search import JobSearchEngine, RemotiveSource, JobParser
    from src.storage import GoogleSheetsStorage
    from src.document_generator import CoverLetterGenerator

def main():
    # 1. Menerima Input Kata Kunci Pencarian dari Pengguna
    user_input = input("Masukkan pekerjaan yang dicari (e.g., Python): ")
    if not user_input: 
        logging.warning("Input kosong. Program dihentikan.")
        return

    # 2. Eksekusi Mesin Pencari Lowongan Kerja (Job Search Engine)
    logging.info(f"Memulai pencarian lowongan kerja untuk kata kunci: '{user_input}'...")
    engine = JobSearchEngine()
    engine.add_source(RemotiveSource())
    raw_jobs = engine.execute_search(user_input)
    
    if not raw_jobs:
        print("\nTidak ada lowongan ditemukan dari API Sumber.")
        return

    # 3. Standarisasi Format Data Lowongan Kerja ke JSON Bersih
    clean_jobs = JobParser.parse_remotive(raw_jobs)
    logging.info(f"Berhasil memproses dan menstandardisasi {len(clean_jobs)} data lowongan.")

    # 4. Pengiriman Data ke Modul Penyimpanan (Storage)
    print("\n[Storage] Mencoba Menyimpan Data ke Google Sheets...")
    storage = GoogleSheetsStorage(spreadsheet_id="lintas-akun-spreadsheet-id")
    storage.save_jobs(clean_jobs)

    # 5. Konversi Data Lowongan ke String JSON untuk Konteks Prompt AI
    json_jobs = json.dumps(clean_jobs, indent=2)

    # 6. Pembuatan Prompt Menggunakan Prompt Engine
    prompt = build_prompt(role="job_hunter", task="search_job", output="json")
    prompt += f"\n\nUSER REQUEST:\n{user_input}\n"
    prompt += f"\nREAL JOB VACANCIES (STANDARDIZED JSON):\n{json_jobs}\n"

    # 7. Eksekusi Analisis Menggunakan Groq AI Provider
    print("\n[AI] Mengirim data standar ke Groq AI untuk dianalisis...")
    try:
        final_output = ask_ai(prompt)
        print("\n================ OUTPUT FINAL AI ================")
        print(final_output)
        print("=================================================")
    except Exception as e:
        logging.error(f"Gagal mendapatkan respons dari Groq AI: {str(e)}")
        final_output = "Analisis AI tidak tersedia."

    # 8. Pembuatan Dokumen Otomatis (Cover Letter Generator)
    if clean_jobs:
        print("\n[Generator] Membuat Berkas Cover Letter Otomatis...")
        job_target = clean_jobs[0]  
        doc_gen = CoverLetterGenerator()
        doc_gen.generate(job_details=job_target, ai_analysis=final_output)

if __name__ == "__main__":
    main()
