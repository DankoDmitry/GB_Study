from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pandas as pd
from pprint import pprint


# excel_data = pd.read_excel('C:/Users/ddigo/OneDrive/Документы/timetable.xlsx')

# data_frame = pd.DataFrame(excel_data, dtype="str", columns=columns_b)



# # print(data.values[weekday[3], columns_b.index(f'{"НМТбд-01-21"}')])

# async def Lesson(update: Update, context: ContextTypes.DEFAULT_TYPE, group: str, day: int, data=data_frame):
#     weekday = [range(0, 8), range(8, 16), range(16, 24), range(24, 32), range(32, 40), range(40, 48)]
#     timles = list(data.values[weekday[day], columns_b.index(f'{group}')])
#     mas = ''

#     for i in timles:
#         mas += str(i) + '\n'

#     await update.message.reply_text(f'{mas}')



columns_b=["День", "Пары", "Время", "НМТбд-01-21", "НМТбд-02-21", "НПМбд-01-21", "НПМбд-02-21", "НКНбд-01-21",	"НКНбд-02-21", "НФИбд-01-21", "НФИбд-02-21", "НПИбд-01-21",	"НПИбд-02-21", "НБИбд-01-21", "НБИбд-02-21", "НФЗбд-01-21", "НФЗбд-02-21", "НХМбд-01-21", "НХМбд-02-21"]
excel_data = pd.read_excel('C:/Users/ddigo/OneDrive/Документы/timetable.xlsx')
data_base = pd.DataFrame(excel_data, dtype="str", columns=columns_b)
# print("The content of the file is:\n", data)

async def Lessons_in_day(update: Update, context: ContextTypes.DEFAULT_TYPE, group: str, day: int, data = data_base):

    if day != 6:
        weekday = [range(0, 8), range(8, 16), range(16, 24), range(24, 32), range(32, 40), range(40, 48)]
        timeline = ["9.00-10.20", "10.30-11.50", "12.00-13.20", "13.30-14.50", "15.00-16.20", "16.30-17.50", "18.00-19.20", "19.30-20.50"]
        gr = columns_b.index(group)

        mas = ''

        for i in weekday[day]:
                j = i - 8*day
                if str(data.values[i, gr]) != 'nan':
                    mas += timeline[j] + ': ' + data.values[i, gr] + '\n'
                else: 
                    mas += timeline[j] + ': ' + "-" + '\n'
        
        await update.message.reply_text(f'{mas}')
    else:
        await update.message.reply_text(f'Sunday: has not lesson!\nYou free...')

# Lesson(data, 1, 3)
