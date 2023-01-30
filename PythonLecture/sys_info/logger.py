from datetime import datetime as dt

def temperature_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, date))
                    
def pressure_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, date))
                    
def wind_speed_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, date))