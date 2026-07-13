import os
import logging
from typing import List, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

logger = logging.getLogger(__name__)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class GoogleSheetsStorage:
    """
    Storage untuk menyimpan data lowongan ke Google Sheets
    """
    
    def __init__(self, spreadsheet_id: str):
        """
        Initialize Google Sheets connection
        
        Args:
            spreadsheet_id (str): ID dari Google Sheet
        """
        self.spreadsheet_id = spreadsheet_id
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """
        Authenticate ke Google Sheets API
        """
        try:
            credentials_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
            
            if not credentials_path:
                logger.warning("GOOGLE_SHEETS_CREDENTIALS tidak ditemukan di .env")
                logger.info("Storage akan bekerja dalam mode demo (tanpa penyimpanan sebenarnya)")
                return
            
            if not os.path.exists(credentials_path):
                logger.warning(f"File credentials tidak ditemukan: {credentials_path}")
                return
            
            try:
                # Coba authenticate dengan service account
                credentials = service_account.Credentials.from_service_account_file(
                    credentials_path, scopes=SCOPES)
                self.service = build('sheets', 'v4', credentials=credentials)
                logger.info("Berhasil authenticate ke Google Sheets API")
            except Exception as e:
                logger.warning(f"Tidak bisa authenticate: {str(e)}")
                
        except Exception as e:
            logger.error(f"Error di authentication: {str(e)}")
    
    def save_jobs(self, jobs: List[Dict[str, Any]]) -> bool:
        """
        Simpan data lowongan ke Google Sheets
        
        Args:
            jobs (List[Dict]): List lowongan kerja
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        try:
            if not self.service:
                logger.info("[DEMO MODE] Data lowongan akan ditampilkan di console:")
                for idx, job in enumerate(jobs, 1):
                    print(f"\n[Job {idx}]")
                    for key, value in job.items():
                        print(f"  {key}: {value}")
                logger.info(f"Total {len(jobs)} lowongan di-process dalam mode demo")
                return True
            
            # Jika service ada, simpan ke Google Sheets
            values = [
                ["ID", "Title", "Company", "Description", "URL", "Type", "Salary", "Posted At"]
            ]
            
            for job in jobs:
                values.append([
                    job.get("id", ""),
                    job.get("title", ""),
                    job.get("company", ""),
                    job.get("description", "")[:100],
                    job.get("url", ""),
                    job.get("job_type", ""),
                    job.get("salary_range", ""),
                    job.get("posted_at", "")
                ])
            
            body = {'values': values}
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range='Sheet1!A1',
                valueInputOption='RAW',
                body=body
            ).execute()
            
            logger.info(f"Berhasil simpan {len(jobs)} lowongan ke Google Sheets")
            return True
            
        except Exception as e:
            logger.error(f"Error saat menyimpan ke Google Sheets: {str(e)}")
            return False
