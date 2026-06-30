#!/usr/bin/env python3
"""
مثال بسيط: كسر كلمة مرور واحدة
"""

import sys
sys.path.insert(0, '..')

from modules import PasswordCracker, HashProcessor

# خطوة 1: توليد Hash لكلمة مرور
password = "password123"
hash_value = HashProcessor.get_hash(password, 'md5')

print(f"\n🔐 كلمة المرور الأصلية: {password}")
print(f"🔒 الـ Hash: {hash_value}\n")
print("="*50)

# خطوة 2: محاولة كسر الـ Hash
cracker = PasswordCracker(wordlist_file='../wordlists/common.txt', verbose=True)
result = cracker.crack(hash_value, 'md5')

print("="*50)
if result:
    print(f"\n✅ نجح! كلمة المرور هي: {result}")
else:
    print(f"\n❌ فشل! لم يتم العثور على كلمة المرور")

cracker.print_stats()
