TOKEN = "6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U"
from telegram.ext import CallbackContext
from keyboards import keyboard,inline_keyboard
from telegram import Update
from flask import Flask,request
import telegram
from db import inc_dislike,inc_like,get_user,clear,add_user,inc_inline_dislike,inc_inline_like,inline_clear,is_user
app = Flask(__name__)

bot = telegram.Bot(TOKEN)
def start(update: Update, context: CallbackContext):
    user = update.effective_user
    if not is_user(chat_id=str(user.id)):
        add_user(chat_id=str(user.id))
        update.message.reply_html(
            text=f'Hello, {user.full_name}! Press one of the buttons.',
            reply_markup=keyboard
        )
        update.message.reply_html(
            text=f'Hello, {user.full_name}! Press one of the buttons.',
            reply_markup=inline_keyboard
        )
    else:
        user_data = get_user(chat_id=str(user.id))
        update.message.reply_html(
            text=f'<b>inline likes:</b> {user_data["inline_likes"]}\n<b>inline dislikes:</b> {user_data["inline_dislikes"]}',
            reply_markup=keyboard
        )
        update.message.reply_html(
            text=f'<b>inline likes:</b> {user_data["inline_likes"]}\n<b>inline dislikes:</b> {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )

@app.route('/',methods = ['POST'])
def index():  
    data = request.get_json()
    chat_ids = data['message']['from']['id']
    print(data)

    if data['message']['text']=='/start':
        if not is_user(chat_id=str(chat_ids)):
            start(user=data['message']['chat'])

        add_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id=chat_ids,
            text=f'Hello, {data["message"]["from"]["first_name"]}! Press one of the buttons.',
            reply_markup=keyboard
        )
    elif data['message']['text']=='👍':
        if not is_user(str(chat_ids)):
            start(user = data['message']['chat'])

        inc_like(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id=chat_ids,
            text=f'😅likes:{user_data["likes"]}\n🥲dislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    elif data['message']['text']=='👎':
        if not is_user(str(chat_ids)):
            start(user = data['message']['chat'])

        inc_dislike(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id = chat_ids,
            text=f'😅likes:{user_data["likes"]}\n🥲dislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        ) 
    elif data['message']['text']=='🆑':
        clear(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.send_message(
            chat_id = chat_ids,
            text=f'😅likes:{user_data["likes"]}\n🥲dislikes: {user_data["dislikes"]}',
            reply_markup=keyboard
        )
    elif data['message']['photo'][0]['file_id']!=None:
        if not is_user(str(chat_ids)):
            start(user = data['message']['chat'])

        inc_inline_like(chat_id=str(chat_ids))
        user_data =get_user(chat_id=str(chat_ids))
        bot.edit_message_text(
            chat_id = chat_ids,
            message = Update.callback_query.message.message_id,
            text=f'likes:{user_data["inline_likes"]}\ndislikes: {user_data["dislikes"]}',
            reply_markup=inline_keyboard
        )
    elif data['message']['photo'][0]['file_id']!=None:        
        if not is_user(str(chat_ids)):
            start(user = data['message']['chat'])

        inc_inline_dislike(chat_id=str(chat_ids))
        user_data = get_user(chat_id=str(chat_ids))
        bot.edit_message_text(
            chat_id=chat_ids,
            message = Update.callback_query.message.message_id,
            text = f'inline_likes:{user_data["inline_likes"]}\ninline_dislikes: {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )
    elif data['message']['photo'][0]['file_id']!=None:        
        if not is_user(str(chat_ids)):
            start(user = data['message']['chat'])

        inline_clear(chat_id=str(chat_ids))
        user_data = get_user(chat_id=chat_ids)
        bot.edit_message_text(
            chat_id = chat_ids,
            message = Update.callback_query.message.message_id,
            text = f'inline_likes:{user_data["inline_likes"]}\ninline_dislikes: {user_data["inline_dislikes"]}',
            reply_markup=inline_keyboard
        )
    else:
        bot.send_message(chat_id=chat_ids,text=f'{data}')
    
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)