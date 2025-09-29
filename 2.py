from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from handlers.start import start
from handlers.lugat import lugat
from handlers.help import help
from handlers.translate import uz2ko, ko2uz

BOT_TOKEN = "8117184210:AAFEWJM4YXtvuBA___cRU7TnPoCr3lSEmEw"

updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('lugat', lugat))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('uz2ko', uz2ko))
dispatcher.add_handler(CommandHandler('ko2uz', ko2uz))


updater.start_polling()
updater.idle()

