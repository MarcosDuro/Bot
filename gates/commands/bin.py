import time
from pyrogram import Client
from pyrogram import filters
import re
from gates.functions.func_bin import get_bin_info
from mongoDB import *
from gates.textos import *
from datetime import datetime

@Client.on_message(filters.command('bin',prefixes=['.','/','!','?'], case_sensitive=False) & filters.text)
async def bin(_,message):

	tiempo = time.time()

	if message.reply_to_message:
		search_bin = re.findall(r'[0-9]+',str(message.reply_to_message.text))
	else:
		search_bin = re.findall(r'[0-9]+',str(message.text))

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

	try: BIN = search_bin[0][0:6]
	except IndexError: return await message.reply(text='<b>Enter a valid bin ⚠️</b>',quote=True)

	x = get_bin_info(BIN)

	if not x: return await message.reply(text='<b>Enter a valid bin ⚠️</b>',quote=True)

	texto = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Bin: <code>{BIN}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Information: <code>{x.get("vendor")} / {x.get("type")} / {x.get("level")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Bank: <code>{x.get("bank_name")}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Country: <code>{x.get("country")} {x.get("flag")}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked By: @{message.from_user.username}[{encontrar_usuario["plan"]}]</b>               
'''
	return await message.reply(text=texto,quote=True)



