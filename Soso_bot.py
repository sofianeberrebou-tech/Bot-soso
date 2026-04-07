import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = “8705907084:AAG7pGg6waUlihOSRuTJuxBs97qejsUZTUk”
OWNER_USERNAME = “sobr667”

PRODUCTS = {
“mcdo”: {
“name”: “🍔 McDonald’s Discount”,
“description”: “Get -50% off your McDonald’s order!\n✅ Valid on any order\n✅ Easy to use\n✅ Instant delivery”,
“price”: “-50% off”
},
“retatrutide”: {
“name”: “💊 Retatrutide (Weight Loss)”,
“description”: “Retatrutide injection — premium weight loss solution.\n✅ Fast results\n✅ Medical grade\n✅ Discreet shipping”,
“price”: “250€”
},
“cinema”: {
“name”: “🎬 Cinema (FR)”,
“description”: “Get -50% off cinema tickets in France!\n✅ All movies\n✅ All cinemas\n✅ Any day”,
“price”: “-50% off”
},
“abonnements”: {
“name”: “📱 Cheap Subscriptions”,
“description”: “Netflix, Spotify, Disney+, and more at -50%!\n✅ Full access\n✅ All regions\n✅ Instant activation”,
“price”: “-50% off”
},
“iptv”: {
“name”: “📺 IPTV Premium”,
“description”: “10,000+ channels | Movies | Series | Sports\n✅ HD/4K quality\n✅ All devices\n✅ Instant activation”,
“price”: “60€/year”
}
}

def start(update: Update, context: CallbackContext):
keyboard = [
[InlineKeyboardButton(“🍔 McDonald’s Discount”, callback_data=“mcdo”)],
[InlineKeyboardButton(“💊 Retatrutide (Weight Loss)”, callback_data=“retatrutide”)],
[InlineKeyboardButton(“🎬 Cinema (FR)”, callback_data=“cinema”)],
[InlineKeyboardButton(“📱 Cheap Subscriptions”, callback_data=“abonnements”)],
[InlineKeyboardButton(“📺 IPTV Premium”, callback_data=“iptv”)],
]
reply_markup = InlineKeyboardMarkup(keyboard)
update.message.reply_text(
“👋 Welcome! What are you looking for today?\n\nChoose a category below 👇”,
reply_markup=reply_markup
)

def button(update: Update, context: CallbackContext):
query = update.callback_query
query.answer()
data = query.data

```
if data in PRODUCTS:
    product = PRODUCTS[data]
    order_number = random.randint(10000, 99999)
    context.user_data["order"] = {
        "number": order_number,
        "product": product["name"],
        "price": product["price"]
    }
    keyboard = [
        [InlineKeyboardButton("🛒 Order Now", url=f"https://t.me/{OWNER_USERNAME}?start=ORDER-{order_number}")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        f"{product['name']}\n\n"
        f"{product['description']}\n\n"
        f"💰 Price: {product['price']}\n\n"
        f"🔖 Your order number: #ORD{order_number}\n\n"
        f"👇 Click below to place your order. Send your order number to the seller!",
        reply_markup=reply_markup
    )

elif data == "back":
    keyboard = [
        [InlineKeyboardButton("🍔 McDonald's Discount", callback_data="mcdo")],
        [InlineKeyboardButton("💊 Retatrutide (Weight Loss)", callback_data="retatrutide")],
        [InlineKeyboardButton("🎬 Cinema (FR)", callback_data="cinema")],
        [InlineKeyboardButton("📱 Cheap Subscriptions", callback_data="abonnements")],
        [InlineKeyboardButton("📺 IPTV Premium", callback_data="iptv")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        "👋 Welcome! What are you looking for today?\n\nChoose a category below 👇",
        reply_markup=reply_markup
    )
```

def handle_message(update: Update, context: CallbackContext):
keyboard = [
[InlineKeyboardButton(“🍔 McDonald’s Discount”, callback_data=“mcdo”)],
[InlineKeyboardButton(“💊 Retatrutide (Weight Loss)”, callback_data=“retatrutide”)],
[InlineKeyboardButton(“🎬 Cinema (FR)”, callback_data=“cinema”)],
[InlineKeyboardButton(“📱 Cheap Subscriptions”, callback_data=“abonnements”)],
[InlineKeyboardButton(“📺 IPTV Premium”, callback_data=“iptv”)],
]
reply_markup = InlineKeyboardMarkup(keyboard)
update.message.reply_text(
“Choose a category below 👇”,
reply_markup=reply_markup
)

if **name** == “**main**”:
updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler(“start”, start))
dp.add_handler(CallbackQueryHandler(button))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
print(“✅ Bot started…”)
updater.start_polling()
updater.idle()
