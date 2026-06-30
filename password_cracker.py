#!/usr/bin/env python3
"""
Password Cracker CLI
واجهة سطر الأوامر
"""

import argparse
import json
import csv
import sys
from pathlib import Path
from modules import PasswordCracker, HashProcessor


def main():
    parser = argparse.ArgumentParser(
        description='🔓 برنامج احترافي لكسر كلمات المرور',
        epilog='مثال: python password_cracker.py --hash "5f4dcc3b5aa765d61d8327deb882cf99" --type md5'
    )
    
    parser.add_argument('--hash', '-H', type=str, help='الـ Hash المراد كسره')
    parser.add_argument('--file', '-F', type=str, help='ملف يحتوي على عدة Hashes')
    parser.add_argument('--type', '-t', type=str, default='md5', choices=['md5', 'sha1', 'sha256', 'sha512', 'bcrypt'])
    parser.add_argument('--wordlist', '-w', type=str, default='wordlists/common.txt')
    parser.add_argument('--output', '-o', type=str, help='ملف الإخراج')
    parser.add_argument('--threads', '-T', type=int, default=4)
    parser.add_argument('--salt', '-s', type=str, default='')
    
    args = parser.parse_args()
    
    if not args.hash and not args.file:
        print("❌ يجب توفير --hash أو --file")
        parser.print_help()
        return False
    
    if not Path(args.wordlist).exists():
        print(f"❌ ملف قائمة الكلمات غير موجود: {args.wordlist}")
        return False
    
    try:
        cracker = PasswordCracker(wordlist_file=args.wordlist, threads=args.threads, verbose=True)
        
        if args.hash:
            result = cracker.crack(args.hash, args.type, args.salt)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump({'hash': args.hash, 'password': result}, f, ensure_ascii=False, indent=2)
                print(f"✓ تم حفظ النتائج في: {args.output}")
        
        elif args.file:
            hashes = []
            with open(args.file, 'r', encoding='utf-8') as f:
                for line in f:
                    h = line.strip()
                    if h:
                        hashes.append({'hash': h, 'salt': args.salt})
            
            results = cracker.crack_batch(hashes, args.type)
            
            if args.output:
                if args.output.endswith('.json'):
                    with open(args.output, 'w', encoding='utf-8') as f:
                        json.dump(results, f, ensure_ascii=False, indent=2)
                elif args.output.endswith('.csv'):
                    with open(args.output, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Hash', 'Password'])
                        for h, p in results.items():
                            writer.writerow([h, p or '❌ Not Found'])
                print(f"✓ تم حفظ النتائج في: {args.output}")
        
        cracker.print_stats()
        return True
    
    except Exception as e:
        print(f"❌ خطأ: {str(e)}")
        return False


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
