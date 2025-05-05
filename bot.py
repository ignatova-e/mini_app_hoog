# TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
# CHANNEL_ID = "@testtestt23e" 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
CHANNEL_ID = "testtestt23e"  # Убедитесь, что канал указан корректно и бот является администратором канала

# Функция для отправки и закрепления сообщения с кнопкой на канале
async def send_and_pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /start command")  # Логирование для диагностики
    try:
        # Создаем клавиатуру с кнопкой, ведущей на мини-приложение
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📚 База знаний", 
                web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")  # Убедитесь, что URL правильный
            )
        ]])

        # Отправляем сообщение в канал и закрепляем его
        sent_msg = await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="📌 Нажми на кнопку, чтобы открыть базу знаний:",
            reply_markup=keyboard
        )

        # Закрепляем сообщение
        await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=sent_msg.message_id)
        print("Сообщение отправлено и закреплено в канале")

    except Exception as e:
        # Добавим более подробную информацию об ошибке для диагностики
        print(f"Ошибка при отправке сообщения: {e}")
        await update.message.reply_text(f"Что-то пошло не так при попытке отправить сообщение в канал. Ошибка: {e}")

# Основная функция для запуска бота
def main():
    # Создаем приложение с токеном
    app = Application.builder().token(TOKEN).build()

    # Подключаем команду /start
    app.add_handler(CommandHandler("start", send_and_pin))

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()
