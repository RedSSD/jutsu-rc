import requests

from config.settings import TELEGRAM_WEBHOOK_URL, TELEGRAM_API_URL


def start_telegram_bot():
    """Set a webhook for Telegram bot."""
    url = f"{TELEGRAM_API_URL}setWebhook?url={TELEGRAM_WEBHOOK_URL}"
    response = requests.post(url).json()
    print(f"Webhook status: {response['description']}")
