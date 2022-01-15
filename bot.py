from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5009722252:AAFla1n_v5_zD_DgVOTkQinv8QtUCUAMTIY',use_context = True )

def start(updater,context):
 updater.message.reply_text("👋🏻 Salom botga hush kelibsiz!\nBotdan foydalanish uchun\n@foydali_link_1 kanaliga a'zo bo'lib \nqayta /start bosing!  ")
 updater.message.reply_start(" Endi botdan be'malol foydalanishingiz mumkin! ")
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='uz') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
