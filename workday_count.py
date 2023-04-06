from datetime import datetime
from datetime import timedelta
import holidays


#  get a holiday list
holidayList = []
for holiday in holidays.Australia(years=2023):
    holidayList.append(holiday)


try:
    #  input start date and numbers of working day to increment
    startInput = input('Please input your start date (ex:2023-03-31):  ')
    startDay = datetime.strptime(startInput, '%Y-%m-%d')

    workDays = input('How many working day you are checking? ' )
    count = int(workDays)

    i = 1
    while(i <= int(workDays)):
        startDay = startDay + timedelta(days=1)
        #  not weekends and holiday
        if (startDay.isoweekday() != 6 and startDay.isoweekday() != 7 and startDay.date() not in holidayList):
            i += 1
            
    print(startDay.date())

except ValueError:
    print('Input format incorrect')