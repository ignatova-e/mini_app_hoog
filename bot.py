# TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
# CHANNEL_ID = "@testtestt23e" 

from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
CHANNEL_ID = "@testtestt23e"  # Подставьте правильное имя канала

# Функция для отправки и закрепления сообщения в канале
async def send_and_pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📚 База знаний", url="https://ignatova-e.github.io/mini_app_hoog/")
    ]])
    sent_msg = await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="📌 Нажми на кнопку, чтобы открыть базу знаний:",
        reply_markup=keyboard
    )
    await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=sent_msg.message_id)

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        KeyboardButton("База знаний", web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/"))
    ]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Салют, мой дорогой Незнайка! 🤗\nСпециально для тебя мы подготовили базу знаний по приложению, чекай кнопку ниже ⬇️",
        reply_markup=reply_markup
    )

# Основная функция для запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("start", start))  # Команда /start
    app.add_handler(CommandHandler("pin", send_and_pin))  # Команда /pin

    app.run_polling()

if __name__ == '__main__':
    main()
