import json
import requests

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from .handler import handle_update


@csrf_exempt
def telegram_bot_handler(request):
    """Handles incoming messages from Telegram."""
    if request.method == 'POST':
        try:
            update = json.loads(request.body.decode('utf-8'))
            handle_update(update)
            return HttpResponse('ok')
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON')
    return HttpResponseBadRequest('Bad Request')
