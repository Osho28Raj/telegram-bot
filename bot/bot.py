import telegram
import os
from sys import executable
import random
from os import execl
from telegram import *
from telegram.ext import *
import random
import reply
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
token = "1874572677:AAEk3KyuFXeis7gFUEzPRIIBRuRmLkJbJls"
bot = Bot(token)
updater = Updater(token, use_context=True)
dispatcher=updater.dispatcher

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
"""
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
"""
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

