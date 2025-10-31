#!/usr/bin/env bash
set -o errexit

# نصب پکیج‌ها از requirements.txt
pip install -r requirements.txt

# اجرای مهاجرت‌های دیتابیس
python manage.py migrate

# ساخت سوپر یوزر بدون ورودی (اطلاعات باید از طریق env تعریف شده باشه)
python manage.py createsuperuser --noinput || echo "Superuser already exists or environment variables missing."

# جمع‌آوری فایل‌های استاتیک
python manage.py collectstatic --no-input
