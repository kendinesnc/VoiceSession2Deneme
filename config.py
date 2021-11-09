from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME1 = getenv("SESSION_NAME1", "session1")
SESSION_NAME2 = getenv("SESSION_NAME2", "session2")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME") 
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME") 
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Mehmetbaba55")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split())) 

