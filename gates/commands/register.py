from pyrogram import (
    Client,
    filters
)
from pymongo.errors import *
from mongoDB import *
import os
from datetime import datetime
import locale
from datetime import timedelta
import time


@Client.on_message(filters.command('register',prefixes=['/',',','.','!','$','-']))
async def register(_,message):
    try:
        find = collection.find_one({"_id": message.from_user.id})
        if find is None:
                            
            mydict = {
            "_id": message.from_user.id,
            "id": message.from_user.id,
            "username": message.from_user.username,
            "plan": "FreeUser",
            "role": "User",
            "status": "F",
            "credits": 0,
            "antispam": 50,
            "time_user": 0,
            "alerts": 0,
            "since": datetime.now(),
            "key" : 'None',


            }
            collection.insert_one(mydict)
            text = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Your Id: <code>{message.from_user.id}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Your Username: @{message.from_user.username}
[<a href="https://t.me/Sinalgunrol">シ</a>] Your Plan: <code>FreeUser</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Your Credits: <code>0</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Your Key: <code>You currently do not have a key</code></b>ㅤ
'''
            await message.reply(text=text,quote=True)
        else:
            await message.reply(text='<b>Currently you are already registered in my database</b>',quote=True)
    except Exception as e:
        print(e)
        
    
       
@Client.on_message(filters.command('my',prefixes=['/',',','.','!','$','-']))
async def myacc(_,message):
    tiempo = time.time()

    try:
        if message.reply_to_message.from_user.id:
            encontrar_usuario = collection.find_one({"_id": message.reply_to_message.from_user.id})
    except: encontrar_usuario = collection.find_one({"_id": message.from_user.id})
        
   
    if encontrar_usuario is None: return await message.reply(text='<b>You are not currently registered in my database. /register</b>')
        
    creditos = encontrar_usuario["credits"]
    id_usuario = encontrar_usuario["id"]
    user_name = encontrar_usuario["username"]
    plan = encontrar_usuario["plan"]
    role = encontrar_usuario["role"]
    key_ = encontrar_usuario["key"]
    if key_ != 'None':
        #key_ = key_.strftime('%Y|%m|%d')
        key_ = key_.strftime('%d %B %X')
    else:
        key_ = 'The user does not have an active key.'

    


    texto_xd = f"""
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] User Id: <code>{id_usuario}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Username: @{user_name}
[<a href="https://t.me/Sinalgunrol">シ</a>] Plan: <code>{plan}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Credits: <code>{creditos}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Key: <code>{key_}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.from_user.username}[{plan}]</b>
        """
    await message.reply(text=texto_xd,quote=True)




@Client.on_message(filters.command(['mygp','infogp'],prefixes=['/',',','.','!','$','-']))
async def mygp(_,message):
    tiempo = time.time()

    encontrar_usuario = collection.find_one({"_id": message.from_user.id})   
    
    if encontrar_usuario is None: return await message.reply(text='<b>You are not currently registered in my database. /register</b>',quote=True)

    encontrar_grupo = collection_tres.find_one({"group": str(message.chat.id)})

    if encontrar_grupo is None: grupo = 'This group currently does not have a premium membership.'
        
    else: 
        a = encontrar_grupo['key']  
        grupo = a.strftime('%d %B %X')
        
    


    texto_xd = f"""
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Id: <code>{message.chat.id}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Key: <code>{grupo}</code></b>
        """

    await message.reply(text=texto_xd,quote=True)






