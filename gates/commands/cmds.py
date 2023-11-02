from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import (
    Client,
    filters
)

BOTONES = [
        [
            InlineKeyboardButton(
                "Gateways",callback_data='gates'),
            InlineKeyboardButton(
                "Tools",callback_data='tools'),
        ],
        [
            
            InlineKeyboardButton('Perfil',callback_data='user_perfil'),

        ],
        [

            InlineKeyboardButton('Finish',callback_data='close'),
                
        ]
    ]
REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)
 





@Client.on_message(filters.command('cmds',prefixes=['/',',','.','!','$','-'],case_sensitive=False) & filters.text)
async def cmds_(_,message):

    mensaje = f"""
<b>Hi, to learn about my commands, press any of the buttons!"</b>  
    """    
    await Client.send_message(_,chat_id=message.chat.id,text=mensaje,reply_to_message_id=message.id,reply_markup=REPLY_MARKUP,)