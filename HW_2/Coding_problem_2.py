#Ashton Chiang
#1869119
#CIS 2348
#Professor Ratner

import datetime

dates = []
with open('inputDates.txt') as file:
    for line in file.readlines():
        line = line.strip()
        if line == '-1':
            break
        dates.append(line.strip())



for date in dates[:2]:
    date = date.replace(',', '')
    if '/' not in date:
        temp = datetime.datetime.strptime(date, '%B %d %Y')
        print('{d.month}/{d.day}/{d.year}'.format(d=temp))
    else:
        print(date)







