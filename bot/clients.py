import requests

from config.settings import TELEGRAM_API_URL


def send_message(method, data):
    """Sends a message to Telegram API."""
    url = f"{TELEGRAM_API_URL}{method}"
    return requests.post(url, data)
