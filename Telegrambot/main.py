from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from weather import *
#import emoji

app = ApplicationBuilder().token("Token").build()
print("Server start")

app.add_handler(CommandHandler('start', start))

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("NY", New_Year))
app.add_handler(CommandHandler("W_City", weather_command))

#print(emoji.emojize(f'Привет :thumbs_up:'))
app.run_polling()
print("Server stop")