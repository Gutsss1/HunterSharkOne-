import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise ValueError("Токен не найден!")

# Простой HTTP-сервер для Render (чтобы он видел открытый порт)
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_health_server():
    server = HTTPServer(('0.0.0.0', 10000), HealthHandler)
    server.serve_forever()

# Запускаем HTTP-сервер в отдельном потоке
threading.Thread(target=run_health_server, daemon=True).start()

# Основной код бота
def start(update: Update, context: CallbackContext):
    update.message.reply_text("🦈 Бот работает! Поздравляю!")

def main():
    print("🦈 Бот запускается...")
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
