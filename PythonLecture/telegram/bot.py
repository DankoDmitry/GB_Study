# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = ApplicationBuilder().token("5594652921:AAForhu_ZRG4Eivede5El6j0Eyx-7CynyO4").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_now))
app.add_handler(CommandHandler("lesson", lesson_today))
app.add_handler(CommandHandler("lesson_tomorrow", lesson_tomorrow))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", Start))
app.add_handler(CommandHandler("group", group))



app.run_polling()