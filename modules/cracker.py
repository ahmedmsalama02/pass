"""
Password Cracking Engine
محرك كسر كلمات المرور الرئيسي
"""

import os
from typing import Optional, List, Dict
from .hasher import HashProcessor
from .logger import Logger
from tqdm import tqdm


class PasswordCracker:
    """محرك كسر كلمات المرور"""
    
    def __init__(self, wordlist_file: str, threads: int = 4, log_file: Optional[str] = None, verbose: bool = True):
        """
        تهيئة محرك الكسر
        
        Args:
            wordlist_file: مسار ملف قائمة الكلمات
            threads: عدد الخيوط
            log_file: ملف تسجيل النتائج
            verbose: طباعة التفاصيل
        """
        self.wordlist_file = wordlist_file
        self.threads = threads
        self.verbose = verbose
        self.logger = Logger(log_file=log_file, verbose=verbose)
        self.wordlist = self._load_wordlist()
        self.stats = {'total_attempts': 0, 'found': 0, 'not_found': 0}
    
    def _load_wordlist(self) -> List[str]:
        """تحميل قائمة الكلمات من الملف"""
        if not os.path.exists(self.wordlist_file):
            raise FileNotFoundError(f"ملف قائمة الكلمات غير موجود: {self.wordlist_file}")
        
        with open(self.wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
            wordlist = [line.strip() for line in f if line.strip()]
        
        if self.verbose:
            self.logger.info(f"تم تحميل {len(wordlist)} كلمة من قائمة الكلمات")
        
        return wordlist
    
    def crack(self, target_hash: str, hash_type: str = 'md5', salt: str = '') -> Optional[str]:
        """
        كسر كلمة مرور واحدة
        
        Args:
            target_hash: الـ Hash المراد كسره
            hash_type: نوع الـ Hash
            salt: الملح إن وجد
        
        Returns:
            كلمة المرور إذا تم العثور عليها، None غير ذلك
        """
        self.logger.info(f"بدء كسر الـ Hash: {target_hash[:20]}... (النوع: {hash_type})")
        
        for word in tqdm(self.wordlist, disable=not self.verbose, desc="محاولة الكسر"):
            self.stats['total_attempts'] += 1
            
            if HashProcessor.verify_password(word, target_hash, hash_type, salt):
                self.logger.success(f"✓ تم العثور على كلمة المرور: {word}")
                self.stats['found'] += 1
                return word
        
        self.logger.warning(f"✗ لم يتم العثور على كلمة المرور في القائمة")
        self.stats['not_found'] += 1
        return None
    
    def crack_batch(self, hashes: List[Dict[str, str]], hash_type: str = 'md5') -> Dict[str, Optional[str]]:
        """
        كسر عدة كلمات مرور
        
        Args:
            hashes: قائمة من الـ Hashes
            hash_type: نوع الـ Hash
        
        Returns:
            قاموس بالنتائج
        """
        results = {}
        total = len(hashes)
        
        self.logger.info(f"بدء كسر {total} كلمة مرور")
        
        for idx, hash_dict in enumerate(tqdm(hashes, desc="معالجة الـ Hashes"), 1):
            target_hash = hash_dict.get('hash')
            salt = hash_dict.get('salt', '')
            result = self.crack(target_hash, hash_type, salt)
            results[target_hash] = result
        
        return results
    
    def print_stats(self):
        """طباعة الإحصائيات"""
        total = self.stats['found'] + self.stats['not_found']
        rate = (self.stats['found'] / max(1, total) * 100) if total > 0 else 0
        
        print("\n" + "="*50)
        print("📊 إحصائيات الكسر")
        print("="*50)
        print(f"إجمالي المحاولات: {self.stats['total_attempts']}")
        print(f"عدد النجاحات: {self.stats['found']}")
        print(f"عدد الفشل: {self.stats['not_found']}")
        print(f"نسبة النجاح: {rate:.2f}%")
        print("="*50)
