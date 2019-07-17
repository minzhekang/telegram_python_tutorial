import telegram

def messagesender(latest_id ='123456789', token = "your token here"):
	bot = telegram.Bot(token)
	bot.send_message(chat_id = latest_id, text="Your reply here")

def updategetter(token):
	bot = telegram.Bot(token)
	latest_msg = bot.get_updates()[-1].message.text
	latest_id = bot.get_updates()[-1].message.chat_id
	latest_user = bot.get_updates()[-1].message.from_user.username
	
	return latest_msg, latest_id, latest_user

'''
This prints the latest message's text, chat id and username in order.
'''
latest_msg, latest_id, latest_user = updategetter("your token here")
messagesender(latest_id, "your token here")
'''
Using the telegram api we are able to receive and send the latest message.

Please note that this does not use webhook and will only send the
message once. If you want to actively listen and send to client, please
use handlers instead.

Using handlers will override the get_updates function which will return
an empty list if the get_updates method is called.
'''

'''
Let us try and recreate this short snippet of code using requests
and not the telegram-python-bot wrapper.
'''

import requests

def messagesender(latest_id ='123456789', 
					token = "your token here", 
					msg ="you message text"):
	send_text = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token, latest_id, msg)
	response = requests.get(send_text)
	return response.json()

def updategetter(token = "your token here"):
	get_updates = "https://api.telegram.org/bot{}/getUpdates".format(token)
	response = requests.get(get_updates)
	response = response.json()['result']
	latest_msg = (response[-1]['message']['text'])
	latest_id = (response[-1]['message']['chat']['id'])
	latest_user = (response[-1]['message']['from']['username'])

	return latest_msg, latest_id, latest_user

'''
Hence we have successfully created the same function as the 
telegram-python-bot using requests only.

Hope this helps
'''