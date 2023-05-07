import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "12857763")) #optional
API_HASH = getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1345594412").split()))
OWNER_ID = int(getenv("OWNER_ID", "1345594412")
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5845010844:AAGgPbvnHKToIxOxzIyHbiJHGghgtWz2yt4")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph//file/8fffe9f061a0bd1fe1c3f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "UDAH AKTIF TOD")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP", "-1001946186040")
GIT_TOKEN = getenv("GIT_TOKEN", "SHA256:azvkVegsZyKoLxKq30eyBdPZ1+iURKf/rurx70H/nZ4") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilabdat04/zaiduser")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAAZrtaBAfiFgS9-VIIqqbZZ9XubuAKiKK4J1_eDjdtGSbTIkXTb7i_aQ0UAHJ66KOmGM7g9UAE_BYhfb6Pk0wM8hhPTnXio1cYxyOlVySPJOTPlgOoRSqaWuUY6-5NKgPTKzBKl3oHNLhMjjLGGztXYs_OWKAQyosNN_03PC_5-ScAdXQq2khro2dVtQeBeYBWJLxZj36oMpFBYK7Yx2KabSl6D-IUVoKviGiNN_y87ZGGUenm5vTX2nHGcmpwODkB3Ll2QRdBGU5CFb6HfBpUjJXHmZWtifm6D9xj-BCNvp7I6IkSlRXKNmeFF5wP_p2-YS8fDtjzjDk-XwRCv0V8gAAAABQNCQsAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
