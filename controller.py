import view
import math_f
import db


def сalculator():
    number_1 = view.number_request()
    number_2 = view.number_request()
    operator = view.operation_request()
    result = math_f.equation(operator, number_1, number_2)
    db.saving_numbers(number_1, number_2, operator, result)
    view.output(number_1, number_2, operator, result)
    
