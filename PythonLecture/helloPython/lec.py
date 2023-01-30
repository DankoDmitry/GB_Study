# # import datetime as DT
# # now = DT.datetime.now(DT.timezone.utc).astimezone()
# # time_format = "%Y-%m-%d %H:%M:%S"
# # print(f"{now:{time_format}}")


# mas = [['*'] * 2] * 8
# print(mas)

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import pandas as pd
# from pprint import pprint

# excel_data = pd.read_excel('C:/Users/ddigo/OneDrive/Документы/timetable.xlsx')
# data_base = pd.DataFrame(excel_data, dtype="str", columns=["День", "Пары", "Время", "НМТбд-01-21", "НМТбд-02-21", "НПМбд-01-21", "НПМбд-02-21", "НКНбд-01-21",	"НКНбд-02-21", "НФИбд-01-21", "НФИбд-02-21", "НПИбд-01-21",	"НПИбд-02-21", "НБИбд-01-21", "НБИбд-02-21", "НФЗбд-01-21", "НФЗбд-02-21", "НХМбд-01-21", "НХМбд-02-21"])
# # print("The content of the file is:\n", data)

# def Lesson(day: int, group: int, data = data_base):

#     weekday = [range(0, 8), range(8, 16), range(16, 24), range(24, 32), range(32, 40), range(40, 48)]
#     timeline = [" 9.00-10.20", "10.30-11.50", "12.00-13.20", "13.30-14.50", "15.00-16.20", "16.30-17.50", "18.00-19.20", "19.30-20.50"]

#     mas = ''

#     for i in weekday[day]:
#             j = i - 8*day
#             if str(data.values[i, group]) != "nan":
#                 mas += timeline[j] + ': ' + data.values[i, group] + '\n'
#             else: 
#                 mas += timeline[j] + ': ' + "-" + '\n'

#     print(mas)

    # strok = ''
    # for i in range(8):
    #     strok += str(mas[i][0]) + ': ' + str(mas[i][1]) + '\n'
    
    # print(strok)

    # await update.message.reply_text(f'{srok}')

# Lesson(1, 3)







# def log_group_write(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     f = open('log_group_base.txt', 'r')
#     for line in f.readlines():
#         if update.effective_user.id in line:
#             return False
#     f.close()
#     f = open('log_group_base.txt', 'a')
#     f.write(f'{update.message.text[7:]};{update.effective_user.id};\n')
#     f.close()
#     return True




from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pandas as pd
from pprint import pprint
import datetime as DT

# # Load the xlsx file
# excel_data = pd.read_excel('C:/Users/ddigo/OneDrive/Документы/timetable.xlsx')
# # Read the values of the file in the dataframe
# columns_b=["День", "Пары", "Время", "НМТбд-01-21", "НМТбд-02-21", "НПМбд-01-21", "НПМбд-02-21", "НКНбд-01-21",	"НКНбд-02-21", "НФИбд-01-21", "НФИбд-02-21", "НПИбд-01-21",	"НПИбд-02-21", "НБИбд-01-21", "НБИбд-02-21", "НФЗбд-01-21", "НФЗбд-02-21", "НХМбд-01-21", "НХМбд-02-21"]
# data = pd.DataFrame(excel_data, dtype="str", columns=columns_b)
# # Print the content
# # print("The content of the file is:\n", data)

# # print(type(data))
# # timetable = list(data)
# # print(timetable)

# weekday = [range(0, 8), range(8, 16), range(16, 24), range(24, 32), range(32, 40), range(40, 48)]

print(DT.datetime.today().weekday())