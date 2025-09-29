from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):

	update.message.reply_text("KOREYS botga hush kelibsiz yordam uchun /help deb yozing")