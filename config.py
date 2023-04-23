import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "21049434")) #optional
API_HASH = getenv("API_HASH", "62e99a639d86cd09d93be558f5772f5e") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1345594412").split()))
OWNER_ID = int(getenv("OWNER_ID", "1345594412"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5967781911:AAF1FbUP2Bov3GFesw7QoVFZwICCRWWVW4w")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN", "SHA256:azvkVegsZyKoLxKq30eyBdPZ1+iURKf/rurx70H/nZ4") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilabdat04/zaiduser")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQApjm_qzQxiSqdw41WKad8laziy5s89ovgj-ydpCW_B3EQAo80UDcqfSJJUv6ZP4D_RJHjbW40HMWGlE96G2Fkpiz9fqm8RV6mRjHJM-2F5js09asSdeOSmv7TY6Ux3tm08U9n3tIxSq9iqfFjVOpxCUvN-IBQpoQlhLFXQS1kwCRfDfWsGjcILWcXgBeB3a3_UO44Igr4aLlR2EgKyjATkBoVH1pvOkzfqgAr_f06aSMEF8jFKvouKe2nasx4BwQg-DDEkVWF3RS7OBejGIANsRZqjdfVCRiBdLkfSBpdosPyDjTUNl_-hhQ2S5G3RHWvf0fMjBSwQLK1_xOxZP6gAAAABqjCuWAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
