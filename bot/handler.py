from bot.commands import start
from .clients import send_message

COMMANDS_LIST = {
    "/start": start.start_command
}

def handle_update(update):
    """Processes the incoming update and responds to the message."""
    message = update.get('message')
    if not message:
        return

    chat_id = message['chat']['id']
    text = message.get('text')

    if text in COMMANDS_LIST.keys():
        COMMANDS_LIST[text](chat_id)
    else:
        send_message(
            "sendMessage",
            {'chat_id': chat_id, 'text': "Unknown command"}
        )
