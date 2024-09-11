from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуй {update.effective_user.first_name}')#cообщение с именем


app = ApplicationBuilder().token("Your bot TOKEN").build()#Токен бота. Д

app.add_handler(CommandHandler("start", start)) #декларация команды /start

app.run_polling() # Чтобы был активен до того пока не выключишь
