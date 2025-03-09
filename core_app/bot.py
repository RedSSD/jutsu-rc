import requests

from config.settings import TELEGRAM_WEBHOOK_URL, TELEGRAM_API_URL

def start_telegram_bot():
    url = f"{TELEGRAM_API_URL}setWebhook?url={TELEGRAM_WEBHOOK_URL}"
    response = requests.post(url).json()
    if response['ok']:
        print("Webhook set successfully")
