'''
This code is a basic version of the message_handler method used in
telegram-python-bot.

This uses basic threading to run the updategetter + messagesender
function in the background. 

Please note that this only works for raw text and will throw an error
if other things such as stickers are posted.
'''

import requests
import threading

TOKEN = ""
print("Running in background...")
'''
We use the same updategetter function with some minor changes to catch
catch null responses when there are no pending updates.
'''
def updategetter(token = TOKEN):
	
	get_updates = "https://api.telegram.org/bot{}/getUpdates".format(token)
	response = requests.get(get_updates)
	try:
		response = response.json()['result']
		latest_msg = (response[0]['message']['text'])
		latest_id = (response[0]['message']['chat']['id'])
		latest_user = (response[0]['message']['from']['username'])
		update_id = (response[0]['update_id'])
		return latest_msg, latest_id, latest_user , update_id
	except:
		print("Caution! array is empty, doing nothing...")
		return None, None, None ,0

'''
This is our main function that connects to the telegram API which
is placed in a while True loop to keep it running in the background.
'''
def messagesender(token = TOKEN, msg = "you message text"):
	while True:
		latest_msg, latest_id, latest_user, update_id = updategetter(token)
		send_text = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token, latest_id, msg)
		response = requests.get(send_text)
		offset = "https://api.telegram.org/bot{}/getUpdates?offset={}".format(token, update_id+1)
		response = requests.get(offset)
'''
We then start the thread with the input arguments.

'''
thread = threading.Thread(target = messagesender, kwargs = {"msg": "walang pingpong"})
thread.start()
