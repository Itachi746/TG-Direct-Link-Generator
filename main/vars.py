# This file is a part of TG-Direct-Link-Generator

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "10993668"))
    API_HASH = str(environ.get("API_HASH", "3d113cba2bc4351d4f5cf189b5961759"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "5374915395:AAG7XQ679Y27VGBbty2mBsHfSJstjBBAULw"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minute
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1001408434519")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 4022))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "12.229.61.118"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", "12.229.61.118"))
        if not ON_HEROKU or environ.get("FQDN")
        else APP_NAME + ".herokuapp.com"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    UPDATES_CHANNEL = "Moviezpure"
    OWNER_ID = int(environ.get('OWNER_ID', '5469155535'))

    BANNED_CHANNELS = list(set(int(x) for x in str(environ.get("BANNED_CHANNELS", "-1001296894100")).split()))
    BANNED_USERS = list(set(int(x) for x in str(environ.get("BANNED_USERS","5275470552 5287015877")).split()))
