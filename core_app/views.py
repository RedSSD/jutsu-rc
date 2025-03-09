import json
import requests

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from config.settings import TELEGRAM_API_URL, TELEGRAM_WEBHOOK_URL

from .message_templates import BOT_KEYBOARD


def setwebhook(request):
    """Sets the webhook for the Telegram bot."""



@csrf_exempt
def telegram_bot(request):
    """Handles incoming messages from Telegram."""
    if request.method == 'POST':
        try:
            update = json.loads(request.body.decode('utf-8'))
            handle_update(update)
            return HttpResponse('ok')
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON')
    return HttpResponseBadRequest('Bad Request')


def handle_update(update):
    """Processes the incoming update and responds to the message."""
    message = update.get('message')
    if not message:
        return

    chat_id = message['chat']['id']
    text = message.get('text')

    if text == '/start':
        send_welcome_message(chat_id)
    elif text == 'V+':
      send_message(
        "sendMessage",
        {
        'chat_id': chat_id,
        'text': "VOLUME UP",
        }
      )


def send_welcome_message(chat_id):
    """Sends a welcome message with a keyboard to the user."""
    payload = {
        "chat_id": chat_id,
        "text": "Welcome! Choose an option:",
        "reply_markup": json.dumps(BOT_KEYBOARD)
    }
    response = send_message("sendMessage", payload)
    print(response.text)


def send_message(method, data):
    """Sends a message to Telegram API."""
    url = f"{TELEGRAM_API_URL}{method}"
    return requests.post(url, data)
