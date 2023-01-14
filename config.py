from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 22681384))
API_HASH = getenv("API_HASH", "14ae45755537c723aab0564a80d723a9")
BOT_TOKEN = getenv("BOT_TOKEN", "5833103468:AAF3bnqY-y8Ld44KGskBO43SocsjUR-DDNE")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://autoani:autoani@autoanime.x7uprzw.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("INDEX_ID", -1001240432549))
UPLOADS_ID = int(getenv("UPLOADS_ID", -1001876066812))

STATUS_ID = int(getenv("STATUS_ID", 3))
SCHEDULE_ID = int(getenv("SCHEDULE_ID", 4))

CHANNEL_TITLE = getenv("CHANNEL_TITLE", "aeiou")
INDEX_USERNAME = getenv("INDEX_USERNAME", "mainanimechan")
UPLOADS_USERNAME = getenv("UPLOADS_USERNAME", "uploadanimechan")
