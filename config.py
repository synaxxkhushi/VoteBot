from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("20515794"))
API_HASH = getenv("da128bd223a333f5bde8dc1359db4609")

TOKEN = getenv("6510303912:AAE2k8DFC7Ot_ifKayMeXoTtcrWerTwPs8w")
MONGO_DB_URL = getenv("mongodb+srv://synaxxkhushi:synaxherebaby@cluster0.vqzfrg0.mongodb.net/?retryWrites=true&w=majority", None)

OWNER_ID = int(getenv("OWNER_ID", 6231550362))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/synaxchatgroup")

LOGGER_ID = getenv("LOGGER_ID", "-1002132398644")
DEV_USERS = set(int(x) for x in getenv("DEV_USERS", "").split())
