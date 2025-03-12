import json

from bot.message_templates import *
from bot.clients import send_message

def start_command(chat_id):
    """Sends a welcome message with a keyboard to the user."""
    payload = {
        "chat_id": chat_id,
        "text": WELCOME_TEXT,
        "reply_markup": json.dumps(BOT_KEYBOARD)
    }
    response = send_message("sendMessage", payload)
    print(response.text)