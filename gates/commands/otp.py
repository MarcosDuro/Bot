from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pyrogram import (
    Client,
    filters
)
from mongoDB import *
from datetime import datetime
import time

BOTONES = [
        [
            InlineKeyboardButton(
                "Telegram",callback_data='otp_telegram'),
            InlineKeyboardButton(
                "#",callback_data='#'),
            InlineKeyboardButton("#",callback_data='#')
        ],
        [
            
            InlineKeyboardButton(
                "#",callback_data='#'),
            InlineKeyboardButton(
                "#",callback_data='#'),
            InlineKeyboardButton("#",callback_data='#')

        ],
        [

            InlineKeyboardButton(
                "#",callback_data='#'),
            InlineKeyboardButton(
                "#",callback_data='#'),
            InlineKeyboardButton("#",callback_data='#')
                
        ]
    ]
REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)
 





@Client.on_message(filters.command('otp',prefixes=['/',',','.','!','$','-'],case_sensitive=False) & filters.text)
async def otp_(_,message):

    encontrar_usuario = collection.find_one({"_id": message.from_user.id})

    #
    if encontrar_usuario is None: return await message.reply(text='<b>You are not currently registered in my database. /register</b>',quote=True)
        


    encontrar_grupo = collection_tres.find_one({"group": str(message.chat.id)})

    if encontrar_usuario['key'] != 'None' or encontrar_grupo != None:
        if encontrar_usuario['key'] != 'None':
            if encontrar_usuario["key"] < datetime.now():            
                collection.update_one({"_id": message.from_user.id},{"$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"antispam": 50}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"plan": 'Free'}})
                return await message.reply(text='<b>your key has expired.</b>',quote=True)
        elif encontrar_grupo["key"] < datetime.now():
            collection_tres.delete_one({"group": str(message.chat.id)})

    else: return await message.reply(text='<b>Contact an administrator to get a key.</b>',quote=True)

    tiempo_usuario = int(encontrar_usuario["time_user"])
    spam_time = int(time.time()) - tiempo_usuario
    if spam_time < encontrar_usuario['antispam']:
        tiempo_restante = encontrar_usuario['antispam'] - spam_time
        texto_spam = f"""
<b>[ANTI_SPAM_DETECTED] Try again after <code>{tiempo_restante}</code>'s</b> 
    """
        return await Client.send_message(_,chat_id=message.chat.id,text=texto_spam,reply_to_message_id=message.id)

    collection.update_one({"_id": message.from_user.id},{"$set": {"time_user": int(time.time())}})


    mensaje = f"""
<b>Bienvenido al menu OTP! estos son los servicios disponibles."</b>  
    """    
    await Client.send_message(_,chat_id=message.chat.id,text=mensaje,reply_to_message_id=message.id,reply_markup=REPLY_MARKUP,)