from threading import Thread

from django.core.management.base import BaseCommand

from core_app.bot import start_telegram_bot


class Command(BaseCommand):
    help = "A command to start a bot"

    def handle(self, *args, **kwargs):
        Thread(target=lambda: self.start_bot()).start()

    def start_bot(self):
        start_telegram_bot()
