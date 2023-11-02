from pyrogram import Client
from pyrogram import filters
import time
import asyncio
import aiohttp
from mongoDB import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from datetime import datetime
from gates.functions.func_imp import get_time_taken
from gates.functions.func_imp import auto_ext
from gates.functions.func_imp import find_between


@Client.on_message(filters.command('exc',prefixes=['.','!','/',',','-','$','%','#']))
async def exc_(_,message):

    tiempo = time.time()

    encontrar_usuario = collection.find_one({"_id": message.from_user.id})

    #
    if encontrar_usuario is None:
        return await Client.send_message(_,chat_id=message.chat.id,text="<b>REGISTRATE PARA USARME</b>. /register",reply_to_message_id=message.id)

    alertas = int(encontrar_usuario["alerts"])
    if alertas >= 3:
        return
    encontrar_grupo = collection_tres.find_one({"group": str(message.chat.id)})

    if encontrar_usuario['key'] != 'None' or encontrar_grupo != None:
        if encontrar_usuario['key'] != 'None':
            if encontrar_usuario["key"] < datetime.now():            
                collection.update_one({"_id": message.from_user.id},{"$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"antispam": 50}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"plan": 'Free'}})
                return await Client.send_message(_,chat_id=message.chat.id,text="<b>LO SIENTO TU KEY HA EXPIRADO.</b>",reply_to_message_id=message.id)
        elif encontrar_grupo["key"] < datetime.now():
            collection_tres.delete_one({"group": str(message.chat.id)})

    else:
        return await Client.send_message(_,chat_id=message.chat.id,text="<b>CONTACTA A UN ADMINISTRADOR PARA OBTENER UNA KEY.</b>",reply_to_message_id=message.id)

    tiempo_usuario = int(encontrar_usuario["time_user"])
    spam_time = int(time.time()) - tiempo_usuario
    if spam_time < encontrar_usuario['antispam']:
        tiempo_restante = encontrar_usuario['antispam'] - spam_time
        texto_spam = f"""
<b>ALERTA DE SPAM INTENTALO NUEVAMENTE EN <code>{tiempo_restante}</code>'s</b> 
    """
        collection.update_one({"_id": message.from_user.id},{"$set": {"alerts": alertas+1}})
        return await Client.send_message(_,chat_id=message.chat.id,text=texto_spam,reply_to_message_id=message.id)
    else:
        pass
    collection.update_one({"_id": message.from_user.id},{"$set": {"time_user": int(time.time())}})

    boton_ = [[InlineKeyboardButton(text='Channel',url='https://t.me/SinalgunrolGroup')]]


    x = message.text[len('/exc '):]
    a = x.split(' ')
    url = a[0]

    try:

        checkout = auto_ext(checkout=url)
        api_key,cs = checkout

        async with aiohttp.ClientSession() as session:
            headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
            xd = f'key={api_key}&eid=NA&browser_locale=es-419&redirect_type=stripe_js'
            peticion = await session.post(url=f'https://api.stripe.com/v1/payment_pages/{cs}/init',data=xd,headers=headers)
            texto = await peticion.text()
            display_name = find_between(texto,'"display_name": "','",')
            customer_email = find_between(texto,'"customer_email": "','",')
            currency = find_between(texto,'"currency": "','",')
            total_price = find_between(texto,'"total": ',',')
            mensaje = f'''
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
<b>≭ ┌ Website - > <code>{display_name}</code>
≭ ├ Amount - >  <code>{total_price} {currency}</code>
≭ └ Email - >  <code>{customer_email}</code>
━━━━━━━━━━━━━━
≭ ┌ cs_live - > <code>{cs}</code>
≭ └ pk_live - >  <code>{api_key}</code>
━━━━━━━━━━━━━━
≭ ┌ Time - > <code>{get_time_taken(tiempo)}'s</code>
≭ ├ Checked by - > @{message.from_user.username}[{encontrar_usuario["plan"]}]
≭ └ Bot by - > <code>@Jey</code></b>
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
'''
            return await message.reply(mensaje,quote=True,reply_markup=InlineKeyboardMarkup(boton_))

    except:

        return await message.reply('<b>There was an error please try again.</b>',quote=True)





























            



















