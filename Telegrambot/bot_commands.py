from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime, date, time
from weather import *
from spy import *


async def start(update, context):
    # ожидание отправки сообщения по сети - нужен `await`
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='''Здравствуйте! Я чат-бот. Вот что я могу: 
- /hi я очень вежливый и умею здороваться.
- /time я пунктуальный и умею показывать текущее время.
- /sun я очень умный и умею складывать два числа "Например введите /sum 2 2".
- /NY я знаю сколько дней осталось до Нового Года"
- /W_City я знаю какая погода в любом городе. Например введите /W_City "Название города"
- ...
Напоминаю, что при запуске чат-бота Вы передаёте
персональные данные, даете согласие на их обработку
и получение коммуникаций через чат-бот.''')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Добрый день, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.today().strftime("%H:%M:%S")}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    mess = update.message.text
    items = mess.split()
    print(items)
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(f'{a} + {b} = {a+b}')

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    mess = update.message.text
    city = mess.split()
    print(city)
    await update.message.reply_text(f'{current_weather(city[1])}')


def days2NY():
    now = datetime.today()
    NY = datetime(now.year + 1, 1, 1)
    d = NY - now
    print(datetime.today().strftime('%d.%m.%Y'))
    print(NY)
    print(d)
    return ('Сегодня {}, до Нового Года осталось {} дней' .format(datetime.today().strftime('%d.%m.%Y'), d.days))

async def New_Year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{days2NY()}')

#print(days2NY())
