TOKEN = "6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U"
from telegram import Update
from keyboards import keyboard
from flask import Flask,request
import telegram
from db import inc_dislike,inc_like,get_user,clear
app = Flask(__name__)

bot = telegram.Bot(TOKEN)

@app.route('/',methods = ['POST'])
def index():
    data = request.get_json()
    chat_ids = data['message']['chat']['id']

    if data['message']['text']=='/start':
        bot.send_message(chat_id=chat_ids,text = data['message']['text'])
        user = Update.effective_user
        bot.send_message(
            chat_id=chat_ids,
            text=f'Hello, {user.full_name}! Press one of the buttons.',
            reply_markup=keyboard
        )
    elif data['message']['text']=='👍':
        inc_like(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id=chat_ids,
            text=f'likes:{user_data["likes"]}\ndislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    elif data['message']['text']=='👎':
        inc_dislike(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id = chat_ids,
            text=f'likes:{user_data["likes"]}\ndislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    elif data['message']['text']=='🆑':
        clear(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id = chat_ids,
            text=f'likes:{user_data["likes"]}\ndislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    else:
        bot.send_message(chat_id=chat_ids,text=f'{data}')
    
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)