"""
Hash Processing Module
يتعامل مع مختلف أنواع الـ Hash والتحقق منها
"""

import hashlib
import bcrypt
from typing import Optional


class HashProcessor:
    """معالج الـ Hash لأنواع مختلفة"""
    
    SUPPORTED_TYPES = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
        'bcrypt': None
    }
    
    @staticmethod
    def get_hash(password: str, hash_type: str = 'md5', salt: str = '') -> str:
        """
        توليد Hash من كلمة مرور
        
        Args:
            password: كلمة المرور الأصلية
            hash_type: نوع الـ Hash (md5, sha1, sha256, sha512, bcrypt)
            salt: الملح (للبيانات الآمنة)
        
        Returns:
            القيمة المشفرة
        """
        if hash_type not in HashProcessor.SUPPORTED_TYPES:
            raise ValueError(f"نوع Hash غير مدعوم: {hash_type}")
        
        if hash_type == 'bcrypt':
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        if salt:
            password = password + salt
        
        hash_obj = HashProcessor.SUPPORTED_TYPES[hash_type]
        return hash_obj(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, stored_hash: str, hash_type: str = 'md5', salt: str = '') -> bool:
        """
        التحقق من تطابق كلمة المرور مع الـ Hash
        
        Args:
            password: كلمة المرور المدخلة
            stored_hash: الـ Hash المخزن
            hash_type: نوع الـ Hash
            salt: الملح إن وجد
        
        Returns:
            True إذا تطابقت، False إذا لم تتطابق
        """
        if hash_type == 'bcrypt':
            try:
                return bcrypt.checkpw(password.encode(), stored_hash.encode())
            except Exception:
                return False
        
        calculated_hash = HashProcessor.get_hash(password, hash_type, salt)
        return calculated_hash == stored_hash
    
    @staticmethod
    def identify_hash_type(hash_value: str) -> Optional[str]:
        """
        محاولة تحديد نوع الـ Hash تلقائياً بناءً على طوله
        
        Args:
            hash_value: قيمة الـ Hash
        
        Returns:
            نوع الـ Hash المتوقع أو None
        """
        hash_len = len(hash_value)
        
        length_map = {
            32: 'md5',
            40: 'sha1',
            64: 'sha256',
            128: 'sha512',
        }
        
        if hash_len in length_map:
            return length_map[hash_len]
        
        if hash_value.startswith(('$2a$', '$2b$', '$2y$')):
            return 'bcrypt'
        
        return None
