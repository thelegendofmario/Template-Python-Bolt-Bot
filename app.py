import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("BOT_TOKEN"))

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["APP_TOKEN"]).start()