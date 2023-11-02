from pyrogram import Client
from pyrogram import filters
import time
from mongoDB import *
from gates.textos import *
from datetime import date , datetime
from datetime import timedelta




@Client.on_message(filters.command('claim',prefixes=['.','!','/',',','-','$','%','#']))
async def claim(_,message):
	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>You are not currently registered in my database. /register</b>',quote=True)

	ccs = message.text[len('/claim'):]
	espacios = ccs.split()
	if len(espacios)==0: return await message.reply('<b>/claim key</b>',quote=True)
	key = espacios[0]

	encontrar_key = collection_dos.find_one({"key": key})
	if encontrar_key is None: return await message.reply(text='<b>This key has already been used or is invalid.</b>',quote=True)
		
	dias = encontrar_key['days']
	x = datetime.now() + timedelta(days=dias)

	collection.update_one({"_id": message.from_user.id},{"$set": {"key": x}})
	collection.update_one({"_id": message.from_user.id},{"$set": {"antispam": 30}})
	collection.update_one({"_id": message.from_user.id},{"$set": {"plan": 'Premium'}})
	collection_dos.delete_one({"key": key})

	texto = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Days: <code>{dias}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Type: <code>All gates</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Key: <code>{x.strftime("%d %B %X")}</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Checked by: @{message.from_user.username}[{buscar_permisos["plan"]}]</b>
'''

	await message.reply(texto,quote=True)
