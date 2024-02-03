from flask import Flask,request
import telegram
app = Flask(__name__)
TOKEN = '6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U'

bot = telegram.Bot(TOKEN)

@app.route('/',methods = ['POST'])
def index():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    bot.send_message(chat_id=chat_id,text = data['message']['text'])
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)