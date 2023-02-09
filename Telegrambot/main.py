from telegram import *
from telegram.ext import *
from bot_commands import *
from weather import *
from tic_tac_toe import *
#import emoji

app = ApplicationBuilder().token("5983506085:AAH51vZUMQG5vJA3tUEhjvb_yAB9-rW4a7E").build()


print("Server start")

app.add_handler(CommandHandler('start', start))

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("NY", New_Year))
app.add_handler(CommandHandler("W_City", weather_command))
app.add_handler(CommandHandler("Game", game_command))
app.add_handler(MessageHandler(filters.TEXT, message_response))

#print(emoji.emojize(f'Привет :thumbs_up:'))
app.run_polling()
print("Server stop")