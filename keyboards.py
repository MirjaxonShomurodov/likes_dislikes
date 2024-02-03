from telegram import ReplyKeyboardMarkup,KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👍'), KeyboardButton(text='👎')
        ],
        [
            KeyboardButton(text='🆑')
        ]
    ],
    resize_keyboard=True
)
