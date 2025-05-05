from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"


# /start — кнопка в личку
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        KeyboardButton("База знаний",
                       web_app=WebAppInfo(
                           url="https://ignatova-e.github.io/mini_app_hoog/"))
    ]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Салют, мой дорогой Незнайка! 🤗\nСпециально для тебя мы подготовили базу знаний по приложению, чекай кнопку ниже ⬇️",
        reply_markup=reply_markup)


# /pin — отправка сообщения с кнопкой в канал и закрепление
async def send_and_pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = '@название_твоего_канала'  # Замени на свой username канала или chat_id (например: -1001234567890)

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("База знаний", url="https://ignatova-e.github.io/mini_app_hoog/")
    ]])

    sent_msg = await context.bot.send_message(
        chat_id=chat_id,
        text="📚 Открой базу знаний здесь:",
        reply_markup=keyboard
    )

    await context.bot.pin_chat_message(chat_id=chat_id, message_id=sent_msg.message_id)


# Основная функция запуска
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pin", send_and_pin))  # Подключаем /pin

    app.run_polling()


if __name__ == '__main__':
    main()
