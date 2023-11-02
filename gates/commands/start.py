from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import (
    Client,
    filters
)



@Client.on_message(filters.command('start',prefixes=['/',',','.','!','$','-'],case_sensitive=False) & filters.text)
async def start(_,message):

    caption = f"""
<b>Hello! Welcome to my bot, type /cmds to know my commands.</b>  
    """    
    await Client.send_video(_,video='https://i.pinimg.com/originals/f4/69/b6/f469b66e2b819384c232b62f86a801a9.gif',chat_id=message.chat.id,caption=caption,reply_to_message_id=message.id)
