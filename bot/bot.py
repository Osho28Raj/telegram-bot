import os
import telegram
import random
from telegram import *
from telegram.ext import *
import random
import reply as reply
token = os.environ.get("TOKEN")
bot = Bot(token)
pic = "https://telegra.ph/file/dab7aa0e02fe075f35dff.jpg"
updater = Updater(token, use_context=True)
dispatcher=updater.dispatcher
bot.set_my_commands(cmd.botcmds)
#===================/start======================
def start(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    bot.sendPhoto(
        chat_id,
        pic,
        caption=f"Hi! My name is PyBot: A Python based bot.\nI was created by an accident by my master.",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("start", start)
dispatcher.add_handler(start_value)
#===============================================

#===================/owner======================
def owner(update: Update, context: CallbackContext):
    owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"I was made by my master **{owner_id}**",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("owner", owner)
dispatcher.add_handler(start_value)
#================================================

#===================/gandu=======================
def gandu(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"`{random.choice(reply.ABUSES)}`",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("gandu", gandu)
dispatcher.add_handler(start_value)
#================================================

#===================/slap========================
def slap(update: Update, context: CallbackContext):
    def slapping(user_id, owner_id):
        owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
        user = update.message.from_user
        user_id = user.id
        first_name = user.first_name
        slapped = f"[{first_name}](tg://user?id={user_id})"
        temp = random.choice(reply.SLAP)
        item = random.choice(reply.ITEMS)
        hit = random.choice(reply.HIT)
        throw = random.choice(reply.THROW)
        where = random.choice(reply.WHERE)
        return temp.format(
            user1=owner_id,
            victim=slapped,
            item=item,
            hits=hit,
            throws=throw,
            where=where,
        )
    owner_id = "[Ø𝖘𝖍Ø](tg://user?id=1210937719)"
    user = update.message.from_user
    user_id = user.id
    caption = slapping(user_id, owner_id)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{caption}",
        parse_mode=telegram.ParseMode.MARKDOWN,
    )
start_value = CommandHandler("slap", slap)
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

