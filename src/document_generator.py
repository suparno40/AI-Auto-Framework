import os
import logging
from typing import Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class CoverLetterGenerator:
    """
    Generator untuk membuat cover letter otomatis
    """
    
    def __init__(self):
        self.output_dir = "outputs"
        self._ensure_output_dir()
        logger.info("CoverLetterGenerator initialized")
    
    def _ensure_output_dir(self):
        """
        Pastikan output directory ada
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logger.info(f"Created output directory: {self.output_dir}")
    
    def generate(self, job_details: Dict[str, Any], ai_analysis: str) -> str:
        """
        Generate cover letter berdasarkan job details dan AI analysis
        
        Args:
            job_details (Dict): Detail lowongan kerja
            ai_analysis (str): Analisis dari AI
            
        Returns:
            str: Path file yang dibuat
        """
        try:
            job_title = job_details.get("title", "Unknown Position")
            company_name = job_details.get("company", "Unknown Company")
            
            # Generate cover letter content
            cover_letter = self._build_cover_letter(job_details, ai_analysis)
            
            # Generate filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cover_letter_{timestamp}.txt"
            filepath = os.path.join(self.output_dir, filename)
            
            # Save to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cover_letter)
            
            logger.info(f"Cover letter berhasil dibuat: {filepath}")
            print(f"\n✅ Cover letter telah dibuat: {filepath}")
            
            return filepath
            
        except Exception as e:
            logger.error(f"Error saat generate cover letter: {str(e)}")
            return ""
    
    def _build_cover_letter(self, job_details: Dict[str, Any], ai_analysis: str) -> str:
        """
        Build content cover letter
        
        Args:
            job_details (Dict): Detail lowongan
            ai_analysis (str): Analisis AI
            
        Returns:
            str: Content cover letter
        """
        job_title = job_details.get("title", "Position")
        company_name = job_details.get("company", "Company")
        job_description = job_details.get("description", "")
        
        cover_letter = f"""
=== COVER LETTER ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

--- JOB INFORMATION ---
Position: {job_title}
Company: {company_name}

--- JOB DESCRIPTION PREVIEW ---
{job_description[:300]}...

--- AI ANALYSIS & RECOMMENDATIONS ---
{ai_analysis}

--- DRAFT LETTER ---

Dear Hiring Manager,

I am writing to express my strong interest in the {job_title} position at {company_name}.

Based on the job requirements and my qualifications, I believe I am an excellent fit for this role.
The position aligns perfectly with my career goals and expertise.

[Add your custom content here based on the AI analysis above]

I am excited about the opportunity to contribute to your team and would welcome the chance 
to discuss how my background can add value to {company_name}.

Thank you for considering my application.

Best regards,
[Your Name]

=== END OF COVER LETTER ===
"""
        return cover_letter
