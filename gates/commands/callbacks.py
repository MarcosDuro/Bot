import os
from pyrogram import filters, Client
from pyrogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton)
import re
import time
from mongoDB import *
import pyrogram.errors
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest, Forbidden
from gates.functions.func_bin import get_bin_info
from gates.functions.func_gen import cc_gen
from gates.functions.func_imp import make_order,get_sms

async def perfil(Client, message, update): ######PERFIL
    buttons = [[InlineKeyboardButton('Back',callback_data='start')]]


    reply_markup = InlineKeyboardMarkup(buttons)

    encontrar_usuario = collection.find_one({"_id": message.reply_to_message.from_user.id})

    if encontrar_usuario is None:
        texto_xd = "<b>You are not currently registered in my database. /register</b>"
    else:      
        creditos = encontrar_usuario["credits"]
        id_usuario = encontrar_usuario["id"]
        user_name = encontrar_usuario["username"]
        plan = encontrar_usuario["plan"]
        role = encontrar_usuario["role"]
        key_ = encontrar_usuario["key"]
        if key_ != 'None':
            key_ = key_.strftime('%d %B %X')
        else:
            key_ = 'You currently do not have a key'


        texto_xd = f"""
<b>User Id: <code>{id_usuario}</code>
Username: @{user_name}
Plan: <code>{plan}</code>
Credits: <code>{creditos}</code>
Key: <code>{key_}</code></b>
            """

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=texto_xd,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True
    )



async def gates(Client, message , update):   ####GATESSSSSS
    buttons = [
    [
        InlineKeyboardButton('Auth', callback_data='authgate'),
        InlineKeyboardButton('Charged', callback_data='chargedgate'),
        InlineKeyboardButton('Special',callback_data='specialgate')
    ],
    [
        InlineKeyboardButton('Back', callback_data='start')
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    text = f"""   
<b>Hi, to learn about my commands, press any of the buttons!"</b> 
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def gates2(Client, message , update):   ### RETURN A EL INICIO
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
    text=f"""
<b>>Hi, to learn about my commands, press any of the buttons!</b>       
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def authgatecomand(Client, message,update):
    BOTONES = [
        [
            InlineKeyboardButton('🔙',callback_data='gates'),
        ]
    ]
    REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)
    text=f"""
<b>Section Charge Nº0

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code></b>
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True)
    
async def chargedgatecomand(Client, message,update):
    BOTONES = [
        [
            InlineKeyboardButton('🔙',callback_data='gates'),
            InlineKeyboardButton('🔜', callback_data='page2')
        ]
    ]
    REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)
    text=f"""
<b>Section Charge Nº1

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code></b>ㅤㅤ
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True)

async def chargedgatecomand_2(Client,message,update):
    BOTONES = [
        [
            InlineKeyboardButton('🔙',callback_data='chargedgatecomand'),
            InlineKeyboardButton('🔜',callback_data='page3')

        ]
    ]
    REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)

    text=f"""
<b>Section Charge Nº2

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code></b>
    """

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True)



async def chargedgatecomand_3(Client,message,update):
    BOTONES = [
        [
            InlineKeyboardButton('🔙',callback_data='page2'),
            InlineKeyboardButton('Home',callback_data='start')

        ]
    ]
    REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)

    text=f"""
<b>Section Charge Nº3

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code>

[<a href="https://t.me/Sinalgunrol">シ</a>] Name: <code>Akame</code> [PREMIUM] ✅
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>/ak card|month|year|cvv</code> 
[<a href="https://t.me/Sinalgunrol">シ</a>] Gateway: <code>Shopify</code></b>
    """

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True)


async def specialgatecomand(Client, message,update):
    BOTONES = [
        [
            InlineKeyboardButton('Back',callback_data='gates'),
        ]
    ]
    REPLY_MARKUP = InlineKeyboardMarkup(BOTONES)
    text=f"""
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
<b>Coming soon...</b>

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=REPLY_MARKUP,
        message_id=message.id,
        disable_web_page_preview=True)





async def tools(Client, message , update):  ##TOOLS 1
    buttons = [
        [
            InlineKeyboardButton('Back',callback_data='start'),
            InlineKeyboardButton('Next',callback_data='sexo'),
        ]
    ]
   
    reply_markup = InlineKeyboardMarkup(buttons)
    text_tools_1 = f""" 
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
<b>≭ ┌ Section - >  <code>Tools</code> 
≭ └ Page - > <code>1/2</code>
━━━━━━━━━━━━━━

≭ ┌ Name - > <code>Generator Ccs 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/gen cc|month|year|cvv</code>
≭ └ Status - > <code>[ONLINE ✅]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>Bin info 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/bin 444444</code>
≭ └ Status - > <code>[ONLINE ✅]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>Fake Address 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/rand</code>
≭ └ Status - > <code>[ONLINE ✅]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>My info 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/my</code>
≭ └ Status - > <code>[ONLINE ✅]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>Extrapolation 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/extrap</code>
≭ └ Status - > <code>[ONLINE ✅]</code></b>

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 
    """
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_tools_1,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def tools_2(Client, message , update):   ##TOOLS 2
    buttons = [
        [
            InlineKeyboardButton('Back',callback_data='tools'),
            InlineKeyboardButton('Home',callback_data='start'),
        ]
    ]
    text_tools_2 = f"""
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
<b>≭ ┌ Section - >  <code>Tools</code> 
≭ └ Page - > <code>2/2</code>
━━━━━━━━━━━━━━

≭ ┌ Name - > <code>Sk live 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/sk sk_</code>
≭ └ Status - > <code>[OFFLINE ❌]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>Extras 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/extra 444444</code>
≭ └ Status - > <code>[ONLINE ✅]</code>
━━━━━━━━━━━━━━
≭ ┌ Name - > <code>Fake address Mass 🪐</code> [PREMIUM]
≭ ├ Format - > <code>/rndmass</code>
≭ └ Status - > <code>[ONLINE ✅]</code></b>
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ 
    """
   
    reply_markup = InlineKeyboardMarkup(buttons)

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_tools_2,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def gen_pro(Client,message,update): 
    encontrar_usuario = collection.find_one({"_id": message.reply_to_message.from_user.id})
    msg = re.search(r'Format: (.*).\n', update.message.text).group(1)
    input = re.findall(r"[0-9x]+", msg)
    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    if len(input) == 2:
        cc = input[0]
        mes = input[1]
        ano = 'x'
        cvv = 'x'
    if len(input) == 3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = 'x'
    if len(input) == 4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
                        # lista = cc + "|" + mes + "|" + ano + "|" + cvv
    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10 = cc_gen(cc,mes,ano,cvv)
    #jose = cc_gen(cc,mes,ano,cvv)
    #cards = ''.join(jose)
    
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


    text = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Bin: <code>{cc[0:6]}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Information: <code>{x.get("vendor")} / {x.get("type")} / {x.get("level")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Bank: <code>{x.get("bank_name")} {x.get("flag")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Format: <code>{extra[0:16]}|{mes_2}|{ano_2}|{cvv_2}</code>.
━━━━━━━━━━━━━━
<code>{cc1}</code><code>{cc2}</code><code>{cc3}</code><code>{cc4}</code><code>{cc5}</code><code>{cc6}</code><code>{cc7}</code><code>{cc8}</code><code>{cc9}</code><code>{cc10}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.reply_to_message.from_user.username}[{encontrar_usuario["plan"]}]</b>ㅤㅤㅤㅤㅤㅤㅤㅤㅤ
'''  
   
    buttons = [[InlineKeyboardButton(text='Regenerate! 🔄',callback_data='gen_pro')]]
                        


    reply_markup = InlineKeyboardMarkup(buttons)
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True)


async def otp_telegram(Client,message,update):

    buttons = [
        [
            InlineKeyboardButton('Cancel Order',callback_data='#'),
            InlineKeyboardButton('Skip Number',callback_data='#'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    x = await make_order()

    if not x:
        text = f'''
PAPI HA SUCEDIDO UN ERROR... LO SIENTO
'''
        return await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True)

    orderid, numero = x

    texto_1 = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Numero: <code>+44 {numero}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Order Id: <code>{orderid}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Service: <code>Telegram</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Message: <code>please wait for the code...</code></b>
'''

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=texto_1,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True)

    a = await get_sms(orderid)

    if not a:
        return await Client.edit_message_text(
        chat_id=message.chat.id,
        text=f'Algo ha fallado',
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True)

    texto_2 = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Numero: <code>{numero}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Order Id: <code>{orderid}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Service: <code>Telegram</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Message: <code>{a}</code></b>
'''

    return await Client.edit_message_text(
        chat_id=message.chat.id,
        text=texto_2,
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True)


















@Client.on_callback_query()
async def button(Client, update):
      cb_data = update.data
      text = 'Este menú es de otro usuario ⚠️'
      try:
            if update.message.reply_to_message.from_user.id == update.from_user.id:
                if "gates" in cb_data:
                    await gates(Client, update.message,update)
                elif "close" in cb_data:
                    await update.message.delete()
                elif "start" in cb_data:
                    await gates2(Client, update.message,update)
                elif "authgate" in cb_data:
                    await authgatecomand(Client, update.message,update)
                elif "chargedgate" in cb_data:
                    await chargedgatecomand(Client, update.message,update)
                elif "specialgate" in cb_data:
                    await specialgatecomand(Client, update.message,update)
                elif "tools" in cb_data:
                    await tools(Client, update.message,update)
                elif "gen" in cb_data:
                    await gen_pro(Client,update.message,update)
                elif "page2" in cb_data:
                    await chargedgatecomand_2(Client,update.message,update)
                elif "page3" in cb_data:
                    await chargedgatecomand_3(Client,update.message,update)
                elif "sexo" in cb_data:
                    await tools_2(Client, update.message, update)
                elif "user_perfil" in cb_data:
                    await perfil(Client, update.message, update)
                elif "otp_telegram" in cb_data:
                    await otp_telegram(Client, update.message, update)
            else:
                await Client.answer_callback_query(
            callback_query_id=update.id,
            text=text,
            show_alert="true"
          )
      except RPCError as e:
          print(e)
      except BadRequest as e:
          print(e)
      except Forbidden as e:
          print(e)
            

     
            
 
