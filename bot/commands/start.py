import json
import secrets

from bot.message_templates import *
from bot.clients import send_message

from core_app.models import User

def start_command(chat_id):
    welcome_text = WELCOME_TEXT

    """Sends a welcome message with a keyboard to the user."""
    if not User.objects.filter(telegram_id=chat_id).exists():
        token = secrets.token_hex(13)
        print(token)
        User.objects.create(telegram_id=chat_id, token=token)
        welcome_text += f"\n Your token: {token}"

    payload = {
        "chat_id": chat_id,
        "text": welcome_text,
        "reply_markup": json.dumps(BOT_KEYBOARD)
    }
    response = send_message("sendMessage", payload)
    print(response.text)