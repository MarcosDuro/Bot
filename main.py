from pyrogram import Client
import logging
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest



logging.basicConfig(level=logging.INFO)


bot = Client(
    'SinRol',
    api_id= 20312658
    api_hash= "08be37f8bfeba7e29b2f76082a82ecd6"
    bot_token= "6731916194:AAFhoR2dqo1T6RwG50m6JOvNP0eCOhVJTrw"
    plugins=dict(root="gates")   
    )        




bot.run()