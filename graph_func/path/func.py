from math import cos, sin, asin, acos
from graph_func.path.instructions import *
instr()

i = int(input("Enter func number here: "))
x_list = list(map(float, input("Enter x: ").split()))
y_list = list()


def linear_function():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    for j in x_list:
        y = a * j + b
        y_list.append(y)
    return {"x": x_list, "y": y_list }


def quadratic_function():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    for j in x_list:
        y = (a * (j ** 2)) + (b * j) + c
        y_list.append(y)
    return {"x": x_list, "y": y_list}


def cubic_function():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    for j in x_list:
        y = (a * (j ** 3)) + (b * (j ** 2)) + (c * j) + d
        y_list.append(y)
    return {"x": x_list, "y": y_list}


def sin_function():
    for j in x_list:
        y = sin(j)
        y_list.append(y)
    return {"x": x_list, "y": y_list}


def cos_function():
    for j in x_list:
        y = cos(j)
        y_list.append(y)
    return {"x": x_list, "y": y_list}


def arc_cos_function():
    for j in x_list:
        if -1 <= j <= 1:
            y = acos(j)
            y_list.append(y)
        else:
            print("Error! x only [-1:1]")
    return {"x": x_list, "y": y_list}


def arc_sin_function():
    for j in x_list:
        if -1 <= j <= 1:
            y = asin(j)
            y_list.append(y)
        else:
            print("Error! x only [-1:1]")
    return {"x": x_list, "y": y_list}