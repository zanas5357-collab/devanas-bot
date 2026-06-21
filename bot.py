import telebot
import os
from flask import Flask

API_TOKEN = '8916470014:AAFvf6L0b4XEyDM0w5smQFKbk6ZqMfj8DQc'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Greetings! I am DevAnas, your intelligent assistant.")

@app.route('/')
def home():
    return "DevAnas Bot is running!"

if __name__ == "__main__":
    # Wannan shi ne yake ba Render damar gane Port din
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
