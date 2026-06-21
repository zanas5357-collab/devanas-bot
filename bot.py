import telebot
import sqlite3
from telebot import types

API_TOKEN = '8916470014:AAFvf6L0b4XEyDM0w5smQFKbk6ZqMfj8DQc'
bot = telebot.TeleBot(API_TOKEN)

# Database setup
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    cursor.execute('INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)', (user_id, user_name))
    conn.commit()

    welcome_text = (
        f"Greetings, {user_name}.\n\n"
        "I am DevAnas, your intelligent assistant powered by high-level engineering. "
        "Choose an option from the menu below to get started."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_about = types.InlineKeyboardButton("About Me", callback_data='about')
    btn_social = types.InlineKeyboardButton("TikTok", url='https://tiktok.com/@yourprofile')
    btn_help = types.InlineKeyboardButton("Help", callback_data='help')
    
    markup.add(btn_about, btn_social, btn_help)
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'about':
        bot.edit_message_text("I am DevAnas. An automated bot designed to showcase expertise in Software Engineering and technical operations.", 
                              call.message.chat.id, call.message.message_id)
    elif call.data == 'help':
        bot.edit_message_text("I am here to assist you with technical inquiries. Use /start to return to the main menu.", 
                              call.message.chat.id, call.message.message_id)

bot.infinity_polling()
