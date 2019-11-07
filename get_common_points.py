from sympy import *
x = Symbol("x")
a = Symbol("a")
b = Symbol("b")


def f_x(x, p_function):
    return eval(p_function)


def get_common_points(p_function):
    function_a = p_function
    function_b = p_function.replace("a", "b")
    common_x_values = solve(eval(function_a) - eval(function_b), x)
    results = []
    for value in common_x_values:
        results.append((value, f_x(value, p_function)))
    return results


if __name__ == '__main__':
    f_function = input("Function:\n")
    print("common points:", get_common_points(f_function))
