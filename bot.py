import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден!")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🦈 Бот работает!")

def main():
    print("🦈 Бот запускается...")
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
    print("🦈 Бот успешно завершил работу.")

if __name__ == "__main__":
    main()
