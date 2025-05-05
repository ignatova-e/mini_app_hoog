# TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
# CHANNEL_ID = "@testtestt23e" 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import logging

# Включаем подробное логирование
logging.basicConfig(level=logging.DEBUG)

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
CHANNEL_ID = "@testtestt23e"  # Ваш канал

# Функция для отправки и закрепления сообщения с кнопкой на канале
async def send_and_pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Создаем клавиатуру с кнопкой, ведущей на мини-приложение
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "📚 База знаний", 
                web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")
            )
        ]])

        # Отправляем сообщение в канал и закрепляем его
        sent_msg = await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="📌 Нажми на кнопку, чтобы открыть базу знаний:",
            reply_markup=keyboard
        )

        await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=sent_msg.message_id)
        print("Сообщение отправлено и закреплено в канале")

    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")
        logging.error("Ответ Telegram API: ", exc_info=True)
        await update.message.reply_text("Что-то пошло не так при попытке отправить сообщение в канал.")

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Создаем клавиатуру с кнопкой, ведущей на мини-приложение
        keyboard = [[
            InlineKeyboardButton(
                "📚 База знаний", 
                web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")
            )
        ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Отправляем сообщение с кнопкой в личку
        await update.message.reply_text(
            "Салют, мой дорогой Незнайка! 🤗\nСпециально для тебя мы подготовили базу знаний по приложению, чекай кнопку ниже ⬇️",
            reply_markup=reply_markup
        )
        print("Команда /start выполнена успешно")
    except Exception as e:
        logging.error(f"Ошибка при выполнении команды /start: {e}")
        logging.error("Ответ Telegram API: ", exc_info=True)

# Основная функция для запуска бота
def main():
    # Создаем приложение с токеном
    app = Application.builder().token(TOKEN).build()

    # Подключаем команду /start
    app.add_handler(CommandHandler("start", start)) 

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()
