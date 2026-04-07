import logging
import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_USERNAME = "sobr667"
PRODUCTS = {
"mcdo": {
"name": "McDonald’s Discount",
"description": "Get -50% off your McDonald’s order!\nValid on any order\nEasy to use\nInstant delivery”,
“price”: “-50% off”
},
“retatrutide”: {
“name”: “Retatrutide (Weight Loss)”,
“description”: “Retatrutide injection - premium weight loss solution.\nFast results\nMedical grade\nDiscreet shipping”,
“price”: “250EUR”
},
“cinema”: {
“name”: “Cinema (FR)”,
“description”: “Get -50% off cinema tickets in France!\nAll movies\nAll cinemas\nAny day”,
“price”: “-50% off”
},
“abonnements”: {
“name”: “Cheap Subscriptions”,
“description”: “Netflix, Spotify, Disney+, and more at -50%!\nFull access\nAll regions\nInstant activation”,
“price”: “-50% off”
},
“iptv”: {
“name”: “IPTV Premium”,
“description”: “10,000+ channels | Movies | Series | Sports\nHD/4K quality\nAll devices\nInstant activation”,
“price”: “60EUR/year”
}
}

def get_main_keyboard():
return InlineKeyboardMarkup([
[InlineKeyboardButton(“McDonald’s Discount”, callback_data=“mcdo”)],
[InlineKeyboardButton(“Retatrutide (Weight Loss)”, callback_data=“retatrutide”)],
[InlineKeyboardButton(“Cinema (FR)”, callback_data=“cinema”)],
[InlineKeyboardButton(“Cheap Subscriptions”, callback_data=“abonnements”)],
[InlineKeyboardButton(“IPTV Premium”, callback_data=“iptv”)],
])

def start(update: Update, context: CallbackContext):
update.message.reply_text(
“Welcome! What are you looking for today?\n\nChoose a category below:”,
reply_markup=get_main_keyboard()
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
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Order Now", url="https://t.me/" + OWNER_USERNAME + "?start=ORDER-" + str(order_number))],
        [InlineKeyboardButton("Back", callback_data="back")]
    ])
    query.edit_message_text(
        product["name"] + "\n\n" +
        product["description"] + "\n\n" +
        "Price: " + product["price"] + "\n\n" +
        "Your order number: #ORD" + str(order_number) + "\n\n" +
        "Click below to place your order. Send your order number to the seller!",
        reply_markup=keyboard
    )

elif data == "back":
    query.edit_message_text(
        "Welcome! What are you looking for today?\n\nChoose a category below:",
        reply_markup=get_main_keyboard()
    )
```

def handle_message(update: Update, context: CallbackContext):
update.message.reply_text(
“Choose a category below:”,
reply_markup=get_main_keyboard()
)

if **name** == “**main**”:
updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler(“start”, start))
dp.add_handler(CallbackQueryHandler(button))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
print(“Bot started…”)
updater.start_polling()
updater.idle()
