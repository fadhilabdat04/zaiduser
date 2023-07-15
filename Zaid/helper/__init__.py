import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zaid"])

async def join(client):
    try:
        await client.join_chat("SiArab_Store")
        await client.join_chat("SiArabSupport")
        await client.join_chat("cehasiarab")
    except BaseException:
        pass
