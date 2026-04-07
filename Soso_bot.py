import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8705907084:AAG7pGg6waUlihOSRuTJuxBs97qejsUZTUk"
OWNER_USERNAME = "sobr667"

BUTTON = [[InlineKeyboardButton("🛒 For Order", url=f"https://t.me/{OWNER_USERNAME}")]]
MARKUP = InlineKeyboardMarkup(BUTTON)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Pour commander, appuie ci-dessous 👇", reply_markup=MARKUP)

def post(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Usage : /post Ton message ici")
        return
    texte = " ".join(context.args)
    update.message.reply_text(texte, reply_markup=MARKUP)

def handle_message(update: Update, context: CallbackContext):
    update.message.reply_text("👇 Pour commander :", reply_markup=MARKUP)

if __name__ == "__main__":
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("post", post))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    print("✅ Bot démarré...")
    updater.start_polling()
    updater.idle()
