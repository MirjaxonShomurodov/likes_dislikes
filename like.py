from flask import Flask,request
import telegram
app = Flask(__name__)
TOKEN = '6839845710:AAE41G3cQslmBNL8FYMXwDFtqgUnoG_Uy3U'

bot = telegram.Bot(TOKEN)

@app.route('/')
def index():
    return "Har doimgdek, 'Hello world'"

if __name__=="__main__":
    app.run(debug=True,port=9000)