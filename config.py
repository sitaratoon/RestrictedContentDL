# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "BQG7FU4AgmWdkVg42HT-rEsamEp-8OtRFosG-C0ikuPVolG1ygDInw9F7FI9O3YxbkwWNViM5kiw6Zy0bIwtOZtBVR9UzRIqYguhR_zIotABWNjqf6VldWKfrFhvtC9zlAWP5jr7hb386Unj0R0HfKQ5xY_Nt1rQCdgAQ8E-1eL6IrjiAMC-3gvQoWT0o-G-stBvZAUGGyXKzRgKD6-_QqMydVOdmZPspJ7h63WNs8yHDBOoz5-3zGLnhAGSnBMcJ4MV8wiqftuP3o1HwOFnIx7OkeRiU3mDOuhl72j5DI33dUo3gy_lnqPAoaFL8bWmqPtk7loWfF60jk5VXuE8R581E4ISUAAAAAHDxaOpAA"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("API_ID", "29037902"))
    API_HASH = getenv("API_HASH", "8f963da8e2040053cf0ad8932244890e")
    BOT_TOKEN = getenv("BOT_TOKEN")
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()
