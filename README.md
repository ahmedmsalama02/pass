# Password Cracker Tool 🔓

برنامج احترافي لكسر كلمات المرور باستخدام قائمة كلمات معروفة (Wordlist-based Cracking).

## ⚠️ تحذير قانوني
**هذا البرنامج يجب استخدامه فقط:**
- ✅ مع إذن موثق وكتابي من صاحب النظام
- ✅ لأغراض اختبار الأمان المشروع (Penetration Testing)
- ✅ على الأنظمة التي تملكها أو لديك إذن صريح لاختبارها

**الاستخدام غير المشروع قد يترتب عليه:**
- ❌ مسؤولية جنائية
- ❌ عقوبات قانونية
- ❌ مسؤولية مدنية

---

## المميزات 🎯

✨ دعم تنسيقات Hash متعددة:
- MD5
- SHA-1
- SHA-256
- SHA-512
- bcrypt

✨ خيارات متقدمة:
- معالجة متوازية (Multi-threading)
- دعم قوائم كلمات مخصصة
- تقديم النتائج في الوقت الفعلي
- تسجيل الجلسات (Logging)
- دعم ملفات CSV و JSON

---

## التثبيت 📦

```bash
git clone https://github.com/ahmedmsalama02/pass.git
cd pass
pip install -r requirements.txt
```

---

## الاستخدام 🚀

### مثال 1: كسر كلمة مرور واحدة

```bash
python password_cracker.py --hash "5f4dcc3b5aa765d61d8327deb882cf99" --type md5
```

### مثال 2: كسر من ملف

```bash
python password_cracker.py --file hashes.txt --type sha256
```

### مثال 3: حفظ النتائج

```bash
python password_cracker.py --hash "abc..." --output results.json
```

---

## كود Python البسيط

```python
from modules.cracker import PasswordCracker
from modules.hasher import HashProcessor

# توليد Hash
password = "password123"
hash_val = HashProcessor.get_hash(password, 'md5')
print(f"Hash: {hash_val}")

# كسر الـ Hash
cracker = PasswordCracker('wordlists/common.txt')
result = cracker.crack(hash_val, 'md5')
print(f"Password: {result}")
```

---

## الملفات المهمة 📁

- `password_cracker.py` - البرنامج الرئيسي
- `modules/hasher.py` - معالج الـ Hash
- `modules/cracker.py` - محرك الكسر
- `modules/logger.py` - نظام التسجيل
- `wordlists/common.txt` - قائمة كلمات شهيرة
- `examples/` - أمثلة الاستخدام

---

**آخر تحديث:** 2026-06-30