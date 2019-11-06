from sympy import *

f_function = ""
g_function = ""
x = Symbol("x")
a = Symbol("a")


def get_first_derivative(p_function):
    x = Symbol("x")
    return diff(p_function, x)


def get_second_derivative(p_function):
    x = Symbol("x")
    return diff(p_function, x, x)


def get_third_derivative(p_function):
    x = Symbol("x")
    return diff(p_function, x, x, x)


def f_x(x):
    return eval(f_function)


def g_x(x):
    return eval(g_function)


def g_a(a):
    return eval(g_function)


def get_bend_points(p_function):
    first_derivative = get_first_derivative(p_function)
    x_value = solve(first_derivative, x)
    y_value = []
    for value in x_value:
        y_value.append(f_x(value))
    results = []
    for value in x_value:
        results.append((value, y_value[x_value.index(value)]))
    return results


def get_turning_points(p_function):
    second_derivative = get_second_derivative(p_function)
    x_value = solve(second_derivative, x)
    y_value = []
    for value in x_value:
        y_value.append(f_x(value))
    results = []
    for value in x_value:
        results.append((value, y_value[x_value.index(value)]))
    return results


def get_x_param(x_value):
    return solve(x_value-x, a)[0]


def insert_into_y_value(x_param, y_value):
    global g_function
    g_function = str(y_value)
    return g_a(x_param)


if __name__ == '__main__':
    f_function = input("Function:\n")
    if int(input("1=bend points (Extrempunkte), 2=turning points (Wendepunkte)\n")) == 1:
        bend_points = get_bend_points(f_function)
        print("bend_points:", bend_points)
        x_p = get_x_param(bend_points[0][0])
        print("x_param:", x_p)
        print("g(x)=" + str(insert_into_y_value(x_p, bend_points[0][1])))
    else:
        turning_points = get_turning_points(f_function)
        print("turning_points:", turning_points)
        x_p = get_x_param(turning_points[0][0])
        print("x_param:", x_p)
        print("g(x)=" + str(insert_into_y_value(x_p, turning_points[0][1])))
