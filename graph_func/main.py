import matplotlib.pyplot as plt
from graph_func.path.func import *


if i == 1:
    linear_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=ax+b',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 2:
    quadratic_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=ax**2+bx+c',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 3:
    cubic_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=(a*x**3)+(b*x**2)+(c*x)+d',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 4:
    sin_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=sin(x)',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 5:
    cos_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=cos(x)',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 6:
    arc_sin_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.set(title='y=arccos(x)',
           xlabel='X axis',
           ylabel='Y axis')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()

elif i == 7:
    arc_cos_function()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("center")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set(title='y=arccos(x)',
           xlabel='X',
           ylabel='Y')
    ax.scatter(x_list, y_list, marker="o")
    plt.show()
