# TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
# CHANNEL_ID = "@testtestt23e" 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
CHANNEL_ID = "@testtestt23e"  # Убедитесь, что канал указан корректно и бот является администратором канала

# Функция для отправки кнопки для лички (команда /start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /start command")  # Логирование для диагностики
    try:
        # Создаем клавиатуру с кнопкой, ведущей на мини-приложение
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📚 База знаний", 
                web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")  # Убедитесь, что URL правильный
            )
        ]])

        # Отправляем сообщение с кнопкой в личку
        await update.message.reply_text(
            text="📌 Нажми на кнопку, чтобы открыть базу знаний:",
            reply_markup=keyboard
        )
        print("Сообщение отправлено в личку")

    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
        await update.message.reply_text("Что-то пошло не так при попытке отправить сообщение.")

# Функция для отправки и закрепления сообщения в канале (команда /pin)
async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received /pin command")  # Логирование для диагностики
    try:
        # Создаем клавиатуру с кнопкой, ведущей на мини-приложение
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📚 База знаний", 
                url="https://t.me/KBHoogBot?startapp=/start"
                # url="https://ignatova-e.github.io/mini_app_hoog/"
                # web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")  # Убедитесь, что URL правильный
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
        print(f"Ошибка при отправке сообщения: {e}")
        await update.message.reply_text("Что-то пошло не так при попытке отправить сообщение в канал.")

# Основная функция для запуска бота
def main():
    # Создаем приложение с токеном
    app = Application.builder().token(TOKEN).build()

    # Подключаем команды /start и /pin
    app.add_handler(CommandHandler("start", start))  # Убедитесь, что эта строка правильная
    app.add_handler(CommandHandler("pin", pin))      # Убедитесь, что эта строка правильная

    # Запуск бота
    app.run_polling()

if __name__ == '__main__':
    main()