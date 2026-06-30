"""
Password Cracker Tool - Modules Package
"""

from .hasher import HashProcessor
from .cracker import PasswordCracker
from .logger import Logger

__version__ = "1.0.0"
__author__ = "Ahmed Salama"

__all__ = ['HashProcessor', 'PasswordCracker', 'Logger']
