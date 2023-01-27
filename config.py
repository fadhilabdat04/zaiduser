import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "26446294")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2144429590").split()))
OWNER_ID = int(getenv("OWNER_ID", "2144429590"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5819453709:AAFp_LJZ3hxsReVmLi-UuvvbBDPIqiLbaPc")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAJ5ZK5T0ge4GFpOopRtwDFSGioOuEnf5SOcLJyy4xXj0aY-m0q5GE3nHF2gkQJP5Yb6TwRwJrSL4UF_92scfoaDM8OgXTKxO_TUCNwwHKcNOrJVBR2qTYQuDnhXvrGgu-2Nz-gNnEckbU-Ut5SotsNv06tBiW9FTv0nEQOgT6zZoaNTj_edxmrDYH_1ObAAWbsHshZfFFXntWRC0Me7T8NMY-o5kbcSASFVbOzhT3bYxvrZxtb5n4Fhcx_dSdD-dp5dyjty9laQHfiqBP7_8dTz_mwKdp1c9sW-n2Lr93dxGb2LTU_AlLqXOqoJYOpo9EpsoKuYsU2F4VMe9w-j34WAAAAAB_0WYWAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
