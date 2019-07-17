'''
**This is for telegram version 11.1.0

This annotated tutorial is to give a basic example of how easy
it is to create a bot for telegram using the telegram-python-bot
package

You can first begin by installing the following

$ pip install python-telegram-bot --upgrade

'''

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger()
'''
Logging is useful because it gives us an idea of where the program
goes wrongly and how to rectify the issue.

It is good practise to use logging, however some people may prefer
to just print the statements to debug.
'''

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
'''
Importing the functions from telegram.ext to be able to access the
Handler modules.

What the handler does is to set up a webhook that listens for incoming
requests from the get method and updates information once it receives 
the latest updates.

Handlers are extremely useful because it sets a channel for information
to be able to stream in.

Some common types of handlers includes CommandHandler and MessageHandler
'''

def msghandler(bot,update):
	bot.send_message(chat_id= update.message.chat_id, text = "Your text here")

'''
msghandler is the function of what we want to achieve. So in this case
we are replying to the specific group/chat with the text you want it to send

`update.message.chat_id` basically uses the Updater class to look for
that specific chat id when invoked. Next we will see how to invoke it.
'''

def main():
	updater = Updater(token = "Your token here")
	dispatcher = updater.dispatcher
	msghandler = MessageHandler(Filters.text, msghandler)
	dispatcher.add_handler(msghandler)
	updater.start_polling()
	updater.idle()

'''
We are using the Updater to constantly listen to updates on the
bot with the token assigned to it.

Filters.text basically filters only text inputs by the user.
Other advanced filters can be employed using regex with specific
string finding. You can look into the documentations for the
list of filters available.

dispatcher is being used to deploy the msghandler, which can also
handle multiple handlers at once using threading.
'''

if __name__ == "__main__":
	main()

'''
__name__ == "__main__" ensures that this is the package we
are using and it is not being called from external sources
as a package.

With just a few lines of code, we have simply wrote our first bot!
'''