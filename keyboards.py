from telegram import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

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

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👍"),InlineKeyboardButton(text="👎")
        ],
        [
            InlineKeyboardButton(text="🆑")
        ]
    ]
)