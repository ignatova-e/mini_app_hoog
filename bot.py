# 7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA

from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Вставь сюда свой токен от BotFather
BOT_TOKEN = "7257113754:AAEH7m3Fu0eOOMzmNB3Kgz4mtk6j7a33sGA"

# 🌐 URL мини-приложения (из GitHub Pages или Vercel)
WEBAPP_URL = "https://ignatova-e.github.io/mini_app_hoog/"

# 📲 Команда /start — показать кнопку запуска мини-приложения
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть базу знаний", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать! Нажмите кнопку ниже, чтобы открыть базу знаний:",
        reply_markup=reply_markup
    )

# 🚀 Запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
