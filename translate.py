from telegram import Update
from telegram.ext import CallbackContext
from googletrans import Translator

tarjimon = Translator()

def uz2ko(update: Update, context: CallbackContext):
    if context.args:
        matn = " ".join(context.args)
        tarjima = tarjimon.translate(matn, src='uz', dest='ko')
        update.message.reply_text(f"Koreyscha: {tarjima.text}")
    else:
        update.message.reply_text("Iltimos, o‘zbekcha so‘z yozing. Masalan: /uz2ko Salom")

def ko2uz(update: Update, context: CallbackContext):
    if context.args:
        matn = " ".join(context.args)
        tarjima = tarjimon.translate(matn, src='ko', dest='uz')
        update.message.reply_text(f"O‘zbekcha: {tarjima.text}")
    else:
        update.message.reply_text("Iltimos, koreyscha so‘z yozing. Masalan: /ko2uz 안녕하세요")