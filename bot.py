import telebot
import sqlite3
import os
from flask import Flask
from telebot import types
from threading import Thread

API_TOKEN = '8916470014:AAFvf6L0b4XEyDM0w5smQFKbk6ZqMfj8DQc'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

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
        "Choose an option from the menu below."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("About Me", callback_data='about'),
        types.InlineKeyboardButton("TikTok", url='https://tiktok.com/@yourprofile'),
        types.InlineKeyboardButton("Help", callback_data='help')
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'about':
        bot.edit_message_text("I am DevAnas. An automated bot designed to showcase expertise in Software Engineering.", 
                              call.message.chat.id, call.message.message_id)
    elif call.data == 'help':
        bot.edit_message_text("I am here to assist you. Use /start to return to the main menu.", 
                              call.message.chat.id, call.message.message_id)

@app.route('/')
def home():
    return "DevAnas Bot is running!"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    Thread(target=run_bot).start()
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

