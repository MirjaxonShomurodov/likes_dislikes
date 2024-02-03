from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext
TOKEN = "6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U"
from telegram import Update,ReplyKeyboardMarkup, KeyboardButton
import json
from flask import Flask,request
import telegram
app = Flask(__name__)
TOKEN = '6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U'
bot = telegram.Bot(TOKEN)


keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='👍'), KeyboardButton(text='👎')],[KeyboardButton(text='🆑')]],resize_keyboard=True)
def read_db() -> dict:
    with open('db.json') as f:
        data = f.read()
        try:
            return json.loads(data)
        except json.decoder.JSONDecodeError: 
            return {}
def save_db(data: dict) -> dict:
    with open('db.json', 'w') as f:
        str_data = json.dumps(data, indent=4)
        f.write(str_data)
def is_user(chat_id: str) -> bool:
    data = read_db()
    return chat_id in data.keys()
def get_user(chat_id: str) -> bool:
    data = read_db()
    if not is_user(chat_id):
        return False
    return data[chat_id]
def add_user(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        data[chat_id] = {
            "likes": 0,
            "dislikes": 0
        }
    save_db(data)
def inc_like(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False 
    data[chat_id]['likes'] += 1
    save_db(data)
def inc_dislike(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['dislikes'] += 1
    save_db(data)
def clear(chat_id: str):
    data = read_db()
    if not is_user(chat_id):
        return False
    data[chat_id]['likes'] = 0
    data[chat_id]['dislikes'] = 0
    save_db(data)
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    if not is_user(chat_id=str(user.id)):
        add_user(chat_id=str(user.id))      
    else:
        update.message.reply_html(
            text=f'Hello, {user.full_name}! Press one of the buttons.',
            reply_markup=keyboard
        )
def like(update: Update, context: CallbackContext):
    user = update.effective_user
    if not is_user(str(user.id)):
        start(update, context)
        return
    inc_like(chat_id=str(user.id))
    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f'<b>likes:</b> {user_data["likes"]}\n<b>dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
def dislike(update: Update, context: CallbackContext):
    user = update.effective_user
    if not is_user(str(user.id)):
        start(update, context)
        return
    inc_dislike(chat_id=str(user.id))
    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f'<b>likes:</b> {user_data["likes"]}\n<b>dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
def db_clear(update:Update,context:CallbackContext):
    user =update.effective_user
    if not is_user(str(user.id)):
        start(update,context)
        return
    clear(chat_id=str(user.id))
    user_data = get_user(chat_id=str(user.id))
    update.message.reply_html(
        text=f'<b>likes:</b> {user_data["likes"]}\n<b>dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
@app.route('/',methods = ['POST'])
def index():
    # data = request.get_json()
    # chat_id = data['message']['chat']['id']
    # bot.send_message(chat_id=chat_id,text = data['message']['text'])
    def main():
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
        dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👍'), callback=like))
        dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👎'), callback=dislike))
        dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('🆑'),   callback=db_clear))
        updater.start_polling()
        updater.idle()
    if __name__ == '__main__':
        main()
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)