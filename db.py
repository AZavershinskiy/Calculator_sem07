import datetime


def saving_numbers(a, b, operation, result):
    path = 'Logs.txt'
    with open(path, 'a') as file:
        file.write(f'{now_log}   {a}{operation}{b}={result}\n')


def reading_number():
    path = 'Logs.txt'
    with open(path, 'r') as file:
        return file.readlines()[-1]


now = datetime.datetime.now()
now_log = now.strftime('%y-%m-%d %H:%M:%S')
