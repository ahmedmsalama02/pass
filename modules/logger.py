"""
Logging Module
نظام تسجيل العمليات والنتائج
"""

import logging
from pathlib import Path
from typing import Optional
from colorama import Fore, Back, Style


class Logger:
    """نظام التسجيل المتقدم"""
    
    def __init__(self, log_file: Optional[str] = None, verbose: bool = True):
        self.log_file = log_file
        self.verbose = verbose
        self.logger = self._setup_logger()
    
    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger('PasswordCracker')
        logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        if self.log_file:
            Path(self.log_file).parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger
    
    def info(self, message: str):
        self.logger.info(message)
        if self.verbose:
            print(f"{Fore.CYAN}ℹ {message}{Style.RESET_ALL}")
    
    def success(self, message: str):
        self.logger.info(message)
        if self.verbose:
            print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    
    def warning(self, message: str):
        self.logger.warning(message)
        if self.verbose:
            print(f"{Fore.YELLOW}⚠ {message}{Style.RESET_ALL}")
    
    def error(self, message: str):
        self.logger.error(message)
        if self.verbose:
            print(f"{Fore.RED}✗ {message}{Style.RESET_ALL}")
