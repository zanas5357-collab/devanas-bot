import telebot
from telebot import types
import time
from flask import Flask
from threading import Thread

API_TOKEN = '8916470014:AAFvf6L0b4XEyDM0w5smQFKbk6ZqMfj8DQc'
ADMIN_ID = 6578383502

bot = telebot.TeleBot(API_TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "DevAnas Bot yana aiki lafiya a kan Cloud!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, "🔒 Yi haƙuri! Wannan bot ɗin na sirri ne na uban gidana DevAnas. Ba ka da ikon amfani da shi.")
        return

    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_meeting = types.InlineKeyboardButton("📅 Taron Rabitatul Kiram", callback_data="meeting_rem")
    btn_study = types.InlineKeyboardButton("📚 Bitar Karatun ATBU", callback_data="study_rem")
    btn_income = types.InlineKeyboardButton("💰 Duba Micro-Tasks (Income)", callback_data="income_rem")
    
    markup.add(btn_meeting, btn_study, btn_income)
    
    welcome_text = "Sannu da zuwa Uban gidana, Anas! 🤖\n\nKomai yana karkashin ikonka. Wanne aiki kake son na tunatar da kai ko na duba maka yanzu?"
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message.chat.id != ADMIN_ID:
        bot.answer_callback_query(call.id, "Ba ka da iko!")
        return

    if call.data == "meeting_rem":
        bot.send_message(call.message.chat.id, "📢 **Tunatarwa Kan Rabitatul Kiram:**\n\nUban gida Anas, kar ka manta da lura da tsara taro na gaba na ƙungiyar Rabitatul Kiram da kuma duba ayyukan tafiyar da group ɗin a matsayinka na Admin! 📋")
    elif call.data == "study_rem":
        bot.send_message(call.message.chat.id, "📖 **Tsarin Karatu (ATBU B.Tech SE):**\n\nLokaci ya yi na yin bitar darussan Software Engineering ko duba ayyukan coding na gaba domin kiyaye darajar Alpha Man mai babban buri! 🚀")
    elif call.data == "income_rem":
        bot.send_message(call.message.chat.id, "💸 **Harkar Digital Income:**\n\nLokaci ya yi na duba shafukan micro-tasking (kamar SproutGigs) ko walat ɗinka na crypto domin tabbatar da cewa komai yana tafiya daidai! 💵")
    
    bot.answer_callback_query(call.id)

def start_bot():
    print("Alhamdulillah, Bot din Automation yana gudu a kan Cloud...")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"An samu matsala, ana sake jarawa: {e}")
            time.sleep(5)

if __name__ == '__main__':
    t = Thread(target=run_flask)
    t.start()
    start_bot()

