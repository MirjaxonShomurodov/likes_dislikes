TOKEN = "6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U"
from telegram import Update
from keyboards import keyboard,inline_keyboard
from flask import Flask,request
import telegram
from db import inc_dislike,inc_like,get_user,clear,add_user,inc_inline_dislike,inc_inline_like,inline_clear
app = Flask(__name__)

bot = telegram.Bot(TOKEN)

@app.route('/',methods = ['POST'])
def index():
    data = request.get_json()
    chat_ids = data['message']['from']['id']
    print(data)
    if data['message']['text']=='/start':
        add_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id=chat_ids,
            text=f'Hello, {data["message"]["from"]["first_name"]}! Press one of the buttons.',
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
    elif data['message'].get('photo')==data['message'].get('photo'):
        inc_inline_like(chat_id=str(chat_ids))
        user_data =get_user(chat_id=str(chat_ids))
        bot.send_photo(
            chat_id = chat_ids,
            file_id = data['message']['photo'][0]['file_id'],
            capiton = f'inline_likes:{user_data["inline_like"]}\ninline_dislikes:{user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )
    elif data['message'].get('photo')==data['message'].get('photo'):
        inc_inline_dislike(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_photo(
            chat_id=chat_ids,
            file_id=data['message']['photo'][0]['file_id'],
            capiton=f'inline_likes:{user_data["inline_like"]}\ninline_dislikes:{user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )
    elif data['message'].get('photo')==data['message'].get('photo'):
        inline_clear(chat_id=str(chat_ids))
        user_data = get_user(chat_id=chat_ids)
        bot.send_message(
            chat_id = chat_ids,
            file_id = data['message']['photo'][0]['file_id'],
            capiton=f'inline_likes:{user_data["inline_like"]}\ninline_dislikes:{user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )
    else:
        bot.send_message(chat_id=chat_ids,text=f'{data}')
    
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)