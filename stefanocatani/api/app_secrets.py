# api/app_secrets.py
# NON committare questo file su Git!

# Django/JWT secret key
SECRET_KEY = "django-insecure-s)8)#o9mzev5aa3hxd8%d&+w)rqzq$bp=blxeqomwrok%b(3#7"

# PayPal (Live)

PAYPAL_CLIENT_ID = "AYTmOHHAQ7JbsuubIKtqzSWFuntXMqQ7OcB5Qzljao4NGSBiVzEpehH-K8ib0rknJJUu7jaOTaP8Je1t"
PAYPAL_CLIENT_SECRET = "EB2Sksvbt0z4gU0ZR6MFjxzcWQFk92Qp7jYNBywcndPlTqg-xVoPHVwEqfmngKaRBCrGH3IxBXjTe2ZX"
PAYPAL_MODE = "live"

# Database (opzionale, ma più sicuro)
DATABASE_URL = "postgresql://postgres:treX39@stefanocatani.it:5432/incanto"

# api/app_secrets.py
# ... (credenziali esistenti)

# Configurazione Email (esempio con SendGrid)
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "carlo.zanieri@gmail.com"  # Per SendGrid l'utente è letteralmente 'apikey'[reference:1]
SMTP_PASSWORD = "wkhg vxnh elyh dhff"
EMAIL_FROM = "ordini@stefanocatani.it"  # L'indirizzo che apparirà come mittente