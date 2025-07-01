# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20373203"))
API_HASH = getenv("API_HASH", "8962717c7c708e210f66ea658db58d85")
BOT_TOKEN = getenv("BOT_TOKEN", "7906843564:AAH0mKvjm9oWFIBJal76jmdNQ3AvYnUuwAU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7968732891").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://koxiher824:uhWjdKAzmfAHcagy@cluster0.lg66r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002596328286")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002413032052"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
