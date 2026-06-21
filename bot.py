import telebot
from telebot import types

API_TOKEN = '8916470014:AAFvf6L0b4XEyDM0w5smQFKbk6ZqMfj8DQc'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Salon magana na DevAnas
    welcome_text = (
        f"Gaisuwa gare ka, {message.from_user.first_name}.\n\n"
        "Ni ne DevAnas, bot ɗin da aka kera domin ƙwarewa da fasaha. "
        "Kada ka bata lokaci, ka zaɓi abin da kake buƙata a ƙasa."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_about = types.InlineKeyboardButton("Game da Ni", callback_data='about')
    btn_social = types.InlineKeyboardButton("TikTok", url='https://tiktok.com/@yourprofile')
    btn_help = types.InlineKeyboardButton("Taimako", callback_data='help')
    
    markup.add(btn_about, btn_social, btn_help)
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'about':
        bot.edit_message_text("Sunana DevAnas. Ni bot ne da aka kera don nuna ƙwarewa a fannin Software Engineering da fasaha.", 
                              call.message.chat.id, call.message.message_id)
    elif call.data == 'help':
        bot.edit_message_text("Ina nan don taimaka maka da tambayoyin fasaha. Kuna iya amfani da /start don sake ganin menu.", 
                              call.message.chat.id, call.message.message_id)

bot.infinity_polling()

