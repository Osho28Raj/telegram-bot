import telegram
import sys
import random
from os import execl
from telegram import *
from telegram.ext import *
import random
import reply

token = "1874572677:AAEk3KyuFXeis7gFUEzPRIIBRuRmLkJbJls"
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher=updater.dispatcher

#==================/restart=====================
def restart(update:Update,context:CallbackContext):
    user = update.message.from_user
    if user.id == 1210937719:
        bot.send_message(
            "**Restarted.**\n /ping me  to check if I am online, actually it takes 10 to seconds for restarting",
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
        bot.disconnect()
        execl(sys.executable, sys.executable, *sys.argv)
    else:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text="Only my owner can use this command."
            )
start_value = CommandHandler("restart", restart)
dispatcher.add_handler(start_value)
#===============================================

#===================/gandu======================
def gandu(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"`{random.choice(reply.ABUSES)}`",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("gandu", gandu)
dispatcher.add_handler(start_value)
#================================================

#===================/insult======================
def insult(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"`{random.choice(reply.INSULTS)}`",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("insult", insult)
dispatcher.add_handler(start_value)
#================================================

#=====================/beta======================
def beta(update: Update, context:CallbackContext):
    user = update.message.from_user
    if user.id == 1210937719:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hi! Master {mention}.\nThanks for making me.",
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
    elif user.id == 1173082794:
        mention = f"[Gandu Jeet](tg://user?id={user.id})"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hi beta {mention}\nGali gali me shor h jeet gandu chor h.",
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
    else:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hi! {mention}",
            parse_mode=telegram.ParseMode.MARKDOWN,
        )
start_value=CommandHandler("beta", beta)
dispatcher.add_handler(start_value)
#================================================



updater.start_polling()
updater.idle()

