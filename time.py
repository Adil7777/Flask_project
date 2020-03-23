import datetime


def time():
    today = datetime.datetime.today()
    time = "на время " + str(today.time())[0:5]
    day = "на " + str(today)[0:10].split('-')[0] + ' год ' + str(today)[0:10].split('-')[1] + ' месяц ' + \
          str(today)[0:10].split('-')[1] + ' день '
    return ''.join([day, time])


print(time())
