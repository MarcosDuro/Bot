import time
from random import *
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup
)
import re
from gates.textos import *
from gates.functions.func_bin import get_bin_info
from gates.functions.func_gen import cc_gen
from datetime import datetime
from mongoDB import *



@Client.on_message(filters.command('gen', prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
async def gen(_, message):

    tiempo = time.time()

    if message.reply_to_message:
        input = re.findall(r'[0-9x]+',message.reply_to_message.text)
    else:
        input = re.findall(r'[0-9x]+',message.text)

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

    if not input: return await message.reply('<b>Invalid Bin ⚠️</b>',quote=True)

    if len(input)==1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input)==2:
        cc = input[0]
        mes = input[1][0:2]
        ano = 'x'
        cvv = 'x'
    elif len(input)==3:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = 'x'
    elif len(input)==4:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1][0:2]
        ano = input[2]
        cvv = input[3]                

    if len(input[0]) < 6: return await message.reply('<b>Invalid Bin ⚠️</b>',quote=True)
        
    if cc[0] in bin_prohibido: return await message.reply('<b>Invalid Bin ⚠️</b>',quote=True)    
    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10 = cc_gen(cc,mes,ano,cvv)

    extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
    if mes == 'x':
        mes_2 = 'rnd'
    else:
        mes_2 = mes
    if ano == 'x':
        ano_2 = 'rnd'
    else:
        ano_2 = ano
    if cvv == 'x':
        cvv_2 = 'rnd'
    else:
        cvv_2 = cvv

    x = get_bin_info(cc[0:6])

    buttons = [
                [InlineKeyboardButton(text='Regenerate! 🔄',callback_data='gen_pro')
                    ]
                ]


    text = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Bin: <code>{cc[0:6]}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Information: <code>{x.get("vendor")} / {x.get("type")} / {x.get("level")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Bank: <code>{x.get("bank_name")} {x.get("flag")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>{extra[0:16]}|{mes_2}|{ano_2}|{cvv_2}</code>.
━━━━━━━━━━━━━━
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.from_user.username}[{encontrar_usuario["plan"]}]</b>ㅤㅤㅤㅤㅤㅤㅤㅤㅤ
'''     
    return await Client.send_message(_,chat_id=message.chat.id,text=text,reply_to_message_id=message.id,reply_markup=InlineKeyboardMarkup(buttons))
        
