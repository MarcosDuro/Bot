from pyrogram import Client
from pyrogram import filters
import time
import random
from mongoDB import *



@Client.on_message(filters.command('gkey',prefixes=['.','!','/',',','-','$','%','#']))
async def gkey(_,message):
	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>You are not currently registered in my database. /register</b>',quote=True)
		
	if buscar_permisos["role"] == "Owner" or buscar_permisos["role"] == "Co-Owner": pass	
	else: return await message.reply(text='<b>Only administrators can use this command.</b>',quote=True)
		
	ccs = message.text[len('/gkey'):]
	espacios = ccs.split()
	if len(espacios)==0: return await message.reply('<b>/gkey days</b>',quote=True)
		
	days = espacios[0]

	key = f'Key-{str(random.randint(1000, 9999))}-AkameChk-{str(random.randint(1000, 9999))}-{str(random.randint(1000, 9999))}'
	my_dict = {
	"key" : key,
	"days" : int(days)
	}
	collection_dos.insert_one(my_dict)
	texto = f'''
<b>[<a href="https://t.me/Sinalgunrol">シ</a>] Key: <code>{key}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Days: <code>{days}</code>
[<a href="https://t.me/Sinalgunrol">シ</a>] Type: <code>All gates</code>
━━━━━━━━━━━━━━
[<a href="https://t.me/Sinalgunrol">シ</a>] Key generated by: @{message.from_user.username}[{buscar_permisos["plan"]}]</b>
'''
	await message.reply(texto,quote=True)