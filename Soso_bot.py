from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8705907084:AAG7pGg6waUlihOSRuTJuxBs97qejsUZTUk"
OWNER_USERNAME = "sobr667"

BUTTON = [[InlineKeyboardButton("🛒 For Order", url=f"https://t.me/{OWNER_USERNAME}")]]
MARKUP = InlineKeyboardMarkup(BUTTON)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Pour commander, appuie ci-dessous 👇", reply_markup=MARKUP)

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage : /post Ton message ici")
        return
    texte = " ".join(context.args)
    await update.message.reply_text(texte, reply_markup=MARKUP)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👇 Pour commander :", reply_markup=MARKUP)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot démarré...")
    app.run_polling(drop_pending_updates=True)


