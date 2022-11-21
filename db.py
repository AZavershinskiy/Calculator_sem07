from datetime import datetime as dt
from time import time

def saving_numbers(a, b, operation, result):
    time = dt.now().strftime()
    path = 'Logs.txt'
    with open(path, 'a') as file:
        file.write(f'{a}{operation}{b}={result}\n')


def reading_number():
    path = 'Logs.txt'
    with open(path, 'r') as file:
        return file.readlines()[-1]
