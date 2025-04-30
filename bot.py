from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"


# Функция для обработки команды /start
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


# Основная функция
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == '__main__':
    main()
