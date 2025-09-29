from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):
    update.message.reply_text("QUYIDAGI KOMMANDALARNDAN FOYDALANING\n/lugat Lug'atlar/so'zlar\n/uz2ko uzbekcha so'zni koreyscha qiladi\n/ko2uz koreyscha so'zni uzbekcha qiladi\nHozircha shu boshqa tugmalar ustida endi ishlamoqdamiz!!")