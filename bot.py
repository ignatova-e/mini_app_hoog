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

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Открыть приложение",
            url="https://t.me/KBHoogBot?startapp=1"  # Параметр startapp
        )
    ]])

    await update.message.reply_text(
        text="Нажми кнопку, чтобы открыть приложение:",
        reply_markup=keyboard
    )

# 📌 Команда /pin — отправка кнопки в канал
async def pin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📌 Получена команда /pin")

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Открыть приложение",
            url="https://t.me/KBHoogBot?startapp=1"  # Параметр startapp
        )
    ]])

    sent_msg = await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="Нажми кнопку, чтобы открыть приложение:",
        reply_markup=keyboard
    )
    await context.bot.pin_chat_message(chat_id=CHANNEL_ID, message_id=sent_msg.message_id)


# 🚀 Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pin", pin))

    app.run_polling()

if __name__ == '__main__':
    main()