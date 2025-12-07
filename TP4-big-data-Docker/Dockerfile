# 1. استخدم نسخة خفيفة من Python
FROM python:3.11-slim

# 2. تثبيت الأدوات الأساسية
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 3. تعيين مجلد العمل داخل الصورة
WORKDIR /app

# 4. نسخ ملف المتطلبات وتثبيت المكتبات
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. نسخ ملفات المشروع إلى داخل الصورة
COPY bigdata_tp4.py /app/bigdata_tp4.py
COPY Real_Estate_Sales_2001-2022_GL.csv /app/Real_Estate_Sales_2001-2022_GL.csv
COPY RealEstate_Final_For_PowerBI.csv /app/RealEstate_Final_For_PowerBI.csv
COPY entrypoint.sh /app/entrypoint.sh

# 6. مجلدات المشاركة (اختياري)
VOLUME ["/data", "/output"]

# 7. فتح المنفذ 8000
EXPOSE 8000

# 8. تحديد أمر التشغيل الافتراضي
ENTRYPOINT ["/app/entrypoint.sh"]

