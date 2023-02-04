# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "1923471"))
API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6106738725:AAFYvWc_Lf57lwN0x8abmQMCSJqqayo5NPQ")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "asuvarisubot")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://asuvarisubot:asuvarisubot@asuvarisubot.6fqoto1.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "880087645")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(880087645)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "False") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
