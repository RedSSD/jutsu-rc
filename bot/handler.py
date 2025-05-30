from bot.commands import start
from .clients import send_message

from core_app.models import User

from .websocket_client import send_to_websocket

COMMANDS_LIST = {
    "/start": start.start_command,
}

ACTIONS_LIST = [
    "pause/play",
    "V+",
    "V-",
    "back",
    "forward",
    "Next EP",
    "Skip OP"
]

def handle_update(update):
    """Processes the incoming update and responds to the message."""
    message = update.get('message')
    if not message:
        return

    chat_id = message['chat']['id']
    user_token = None
    try:
        user_token = User.objects.get(telegram_id=chat_id).token
    except:
        pass

    text = message.get('text')

    if text in COMMANDS_LIST.keys():
        COMMANDS_LIST[text](chat_id)
    elif text in ACTIONS_LIST:
        send_to_websocket(user_token, message)
    else:
        send_message(
            "sendMessage",
            {'chat_id': chat_id, 'text': "Unknown command"}
        )
