# TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
# CHANNEL_ID = "@testtestt23e" 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔐 Токен и канал
TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"
CHANNEL_ID = "@testtestt23e"  # Бот должен быть админом канала

# 📦 Команда /start — кнопка для открытия мини-приложения в личке
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ Получена команда /start")

    try:
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📚 База знаний",
                web_app=WebAppInfo(url="https://ignatova-e.github.io/mini_app_hoog/")
            )
        ]])

        await update.message.reply_text(
            text="📌 Нажми на кнопку, чтобы открыть базу знаний:",
            reply_markup=keyboard
        )
        print("➡️ Кнопка отправлена пользователю")

    except Exception as e:
        print(f"❌ Ошибка при отправке кнопки: {e}")
        await update.message.reply_text("Произошла ошибка при отправке кнопки.")

# 📌 Команда /pin — отправка кнопки в канал
async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📌 Получена команда /pin")

    try:
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📚 База знаний",
                url="https://ignatova-e.github.io/mini_app_hoog/?start_param=1"
  # 👈 Эта ссылка должна вести в вашего бота
            )
        ]])

        sent_msg = await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text="Нажми на кнопку ниже, чтобы открыть базу знаний:",
            reply_markup=keyboard
        )

        await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=sent_msg.message_id)
        print("✅ Сообщение отправлено и закреплено в канале")

    except Exception as e:
        print(f"❌ Ошибка при закреплении: {e}")
        await update.message.reply_text("Не удалось отправить сообщение в канал.")

# 🚀 Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pin", pin))
    app.run_polling()

if __name__ == '__main__':
    main()