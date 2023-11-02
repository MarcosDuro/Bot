from pyrogram import Client
from pyrogram import filters
import time
import asyncio
import random
import re
from mongoDB import *
from gates.textos import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from datetime import datetime
from gates.functions.func_bin import get_bin_info
from gates.functions.func_imp import get_time_taken
from gates.functions.func_rias import auto_sho_async


@Client.on_message(filters.command('ri',prefixes=['.','!','/',',','-','$','%','#']))
async def ri_(_,message):

    tiempo = time.time()

    if message.reply_to_message:
      input = re.findall(r'[0-9]+',str(message.reply_to_message.text))
    else:
      input = re.findall(r'[0-9]+',str(message.text))

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

    alaa = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Command: <code>Rias</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ri cc|month|year|cvv.</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify + Moneris $16.17 USD</code></b>
'''
    if len(input) < 4: return await message.reply(text=alaa,quote=True)      

    tiempo_usuario = int(encontrar_usuario["time_user"])
    spam_time = int(time.time()) - tiempo_usuario
    if spam_time < encontrar_usuario['antispam']:
        tiempo_restante = encontrar_usuario['antispam'] - spam_time
        texto_spam = f"""
<b>[ANTI_SPAM_DETECTED] Try again after <code>{tiempo_restante}</code>'s</b> 
    """
        return await Client.send_message(_,chat_id=message.chat.id,text=texto_spam,reply_to_message_id=message.id)

    collection.update_one({"_id": message.from_user.id},{"$set": {"time_user": int(time.time())}})
  

    cc = input[0]
    mes = input[1]
    ano = input[2]
    cvv = input[3]


    if cc[0] in bin_prohibido:
          return await message.reply('<b>The bot only supports VISA, MASTERCARD, DISCOVER Y AMEX.</b>',quote=True)

    boton_ = [[InlineKeyboardButton(text='Channel',url='https://t.me/SinalgunrolGroup')]]

    #


    x = get_bin_info(cc[0:6])


    texto_1 = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Card: <code>{cc}:{mes}:{ano}:{cvv}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Information: <code>{x.get("vendor")} / {x.get("type")} / {x.get("level")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Bank: <code>{x.get("bank_name")} {x.get("flag")}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.from_user.username}[{encontrar_usuario["plan"]}]</b>
'''
    
    
    ñ = await message.reply(text=texto_1,quote=True)
    resultado = await auto_sho_async(cc,mes,ano,cvv)
    if resultado == 'Charged':
        mensaje = 'Charged $8.92 USD'
        status = 'Approved'
        logo = '✅'
    elif resultado == 'CVD ERROR                       99048':
        mensaje = 'CVD ERROR                       99048'
        status = 'Approved'
        logo = '✅'
    elif resultado == 'AUTH DECLINED                   09001':
        mensaje = 'AUTH DECLINED                   09001'
        status = 'Declined'
        logo = '❌'
    elif resultado == 'AUTH DECLINED                   99001':
        mensaje = 'AUTH DECLINED                   99001'
        status = 'Declined'
        logo = '❌'
    elif resultado == 'Declined refer call to issue':
        mensaje = 'Declined refer call to issue'
        status = 'Declined'
        logo = '❌'
    else:
        mensaje = resultado
        status = 'Declined'
        logo = '❌'        
      

    texto_final = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Card: <code>{cc}:{mes}:{ano}:{cvv}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Status: <code>{status} {logo}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Message: <code>{mensaje}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Bin: <code>{cc[0:6]}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Information: <code>{x.get("vendor")} / {x.get("type")} / {x.get("level")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Bank: <code>{x.get("bank_name")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Country: <code>{x.get("country")} {x.get("flag")}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Time: <code>{get_time_taken(tiempo)}'s</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.from_user.username}[{encontrar_usuario["plan"]}]</b>
''' 

    await ñ.edit(texto_final)

