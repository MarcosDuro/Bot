from pyrogram import Client
from pyrogram import filters
import re
from mongoDB import *
from datetime import date , datetime
from datetime import timedelta




@Client.on_message(filters.command('addgp',prefixes=['.','!','/',',','-','$','%','#']))
async def addgp(_,message):

	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>Currently you are already registered in my database</b>',quote=True)	
	if buscar_permisos["role"] == "Owner" or buscar_permisos["role"] == "Co-Owner": pass		
	else: return await message.reply(text='<b>Only administrators can use this command.</b>',quote=True)
	ccs = message.text[len('/addgp'):]
	espacios = ccs.split()
	if len(espacios)==0:
		return await message.reply('<b>/addgp days</b>',quote=True)

	days = espacios[0]

	x = datetime.now() + timedelta(days=int(days))

	encontrar_key = collection_tres.find_one({"group": str(message.chat.id)})
	if encontrar_key is None:
		my_dict = {
		"group" : str(message.chat.id),
		"days" : int(days),
		"key" : x,
		}
		collection_tres.insert_one(my_dict)
		texto = f'''
<b>Id: <code>{message.chat.id}</code>
Days: <code>{days}</code>
Key: <code>{x.strftime('%d %B %X')}</code>ㅤㅤ
━━━━━━━━━━━━━━
group promoted by: @{message.from_user.username}[{buscar_permisos["plan"]}]</b>ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
'''
		await message.reply(texto,quote=True)
	else:
		texto = f'<b>This group already has a premium membership.</b>'
		await message.reply(texto,quote=True)