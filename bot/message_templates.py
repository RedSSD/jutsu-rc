WELCOME_TEXT = """
Welcome to JutsuRC! 🎌

🔥 Control your anime playback on jut.su directly from Telegram!

✅ How to get started:

1️⃣ Install the JutsuRC Chrome extension
2️⃣ Open jut.su and input your token
3️⃣ Use this bot to pause, play, skip, or adjust volume remotely

Enjoy your anime! 🍿🎥
"""

BOT_KEYBOARD = {
    "keyboard": [
        [
            {"text": "back"},
            {"text": "pause/play"},
            {"text": "forward"}
        ],
        [
            {"text": "V+"},
            {"text": "V-"},
        ],
        [
            {"text": "Skip OP"},
            {"text": "Next EP"},
        ]
      ],
    "resize_keyboard": True,
    "one_time_keyboard": False
    }