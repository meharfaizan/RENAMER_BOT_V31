import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "1815909310:AAF8XTGTAhpyd053l8Rl-956pvHZCLFcybM")

API_ID = int(os.environ.get("API_ID", "6534707"))

API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
