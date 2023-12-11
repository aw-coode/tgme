import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 29515967))

    API_HASH = os.environ.get("API_HASH", "2d82195bf121962008d599998947ae71")

    