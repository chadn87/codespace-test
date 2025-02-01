from abc import ABC, abstractmethod
from typing import List, Dict


class BankParser(ABC):
    @staticmethod
    @abstractmethod
    def parse_csv(file_path: str) -> List[Dict]:
        """Parse CSV statement"""
        pass

    @staticmethod
    @abstractmethod
    def parse_pdf(file_path: str) -> List[Dict]:
        """Parse PDF statement"""
        pass

    @staticmethod
    @abstractmethod
    def identify(file_path: str) -> bool:
        """Check if file matches this bank's format"""
        pass
