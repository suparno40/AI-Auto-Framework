import requests
import logging
from typing import List, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)

class RemotiveSource:
    """
    Job search source dari Remotive API
    """
    BASE_URL = "https://remotive.com/api/remote-jobs"
    
    def search(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Cari lowongan kerja berdasarkan keyword
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            List[Dict]: List lowongan kerja
        """
        try:
            params = {
                "search": keyword,
                "limit": 10
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Berhasil mengambil {len(data.get('jobs', []))} lowongan dari Remotive")
            return data.get('jobs', [])
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error saat mengakses Remotive API: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error di RemotiveSource: {str(e)}")
            return []


class JobParser:
    """
    Parser untuk standardisasi format lowongan kerja
    """
    
    @staticmethod
    def parse_remotive(raw_jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Standardisasi format lowongan dari Remotive API
        
        Args:
            raw_jobs (List[Dict]): Raw data dari Remotive API
            
        Returns:
            List[Dict]: Lowongan yang sudah di-standardisasi
        """
        clean_jobs = []
        
        for job in raw_jobs:
            try:
                clean_job = {
                    "id": job.get("id"),
                    "title": job.get("title", "N/A"),
                    "company": job.get("company_name", "N/A"),
                    "description": job.get("description", "N/A")[:500],  # Truncate untuk efficiency
                    "url": job.get("url", "N/A"),
                    "job_type": job.get("job_type", "N/A"),
                    "salary_range": job.get("salary", "Not specified"),
                    "posted_at": job.get("publication_date", datetime.now().isoformat())
                }
                clean_jobs.append(clean_job)
            except Exception as e:
                logger.warning(f"Error parsing job {job.get('id')}: {str(e)}")
                continue
        
        logger.info(f"Berhasil parse {len(clean_jobs)} lowongan kerja")
        return clean_jobs


class JobSearchEngine:
    """
    Engine untuk mencari lowongan kerja dari berbagai sumber
    """
    
    def __init__(self):
        self.sources = []
        logger.info("JobSearchEngine initialized")
    
    def add_source(self, source):
        """
        Tambah sumber pencarian lowongan
        
        Args:
            source: Job source (e.g., RemotiveSource)
        """
        self.sources.append(source)
        logger.info(f"Added source: {source.__class__.__name__}")
    
    def execute_search(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Eksekusi pencarian lowongan dari semua sumber
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            List[Dict]: Hasil gabungan dari semua sumber
        """
        all_jobs = []
        
        if not self.sources:
            logger.warning("Tidak ada sumber pencarian yang terdaftar")
            return []
        
        for source in self.sources:
            try:
                jobs = source.search(keyword)
                all_jobs.extend(jobs)
                logger.info(f"Berhasil mengambil data dari {source.__class__.__name__}")
            except Exception as e:
                logger.error(f"Error saat search dari {source.__class__.__name__}: {str(e)}")
                continue
        
        logger.info(f"Total {len(all_jobs)} lowongan ditemukan dari semua sumber")
        return all_jobs
