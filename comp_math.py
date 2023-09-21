import math

def fun(x):
    return math.exp(2*x) + 3*x - 4

def quadro_fun(x):
    return x * x - 2 * x + 1

def diff_fun(x):
    return 2*math.exp(2 * x) + 3

def dichotomy_method(a, b, e):

    x = (a + b)/2

    while abs(fun(x)) > e:
        if fun(a) * fun(x) < 0:
            b = x
            x = (a + b)/2
        elif fun(x) * fun(b) < 0:
            a = x
            x = (a + b)/2
    return(x)

def secant_method(a, b, e):

    x = a + (fun(a) * (a - b))/(fun(b) - fun(a))

    while abs(fun(x)) > e:
        if fun(a) * fun(x) < 0:
            b = x
            x = a + (fun(a) * (a - b))/(fun(b) - fun(a))
        elif fun(b) * fun(x) < 0:
            a = x
            x = a + (fun(a) * (a - b))/(fun(b) - fun(a))
    return(x)

def tangent_method(e, x_0):
    #conditions for a point from the localization segment: f(x)f'(x) > 0
    if diff_fun(x_0) * fun(x_0) > 0:
        while abs(fun(x_0)) > e:
            x_0 = x_0 - (fun(x_0))/(diff_fun(x_0))
        return(x_0)
    else:
        return("Initial point does not require conditions, try to enter another one")

def modified_tangent_method(e, x_0):
#conditions for a point from the localization segment: f(x)f'(x) > 0
    if diff_fun(x_0) * fun(x_0) > 0:
        initial_x_0 = x_0
        diff_fun_init_x_0 = diff_fun(initial_x_0)
        while abs(fun(x_0)) > e:
            x_0 = x_0 - (fun(x_0)) / (diff_fun_init_x_0)
        return(x_0)
    else:
        return("Initial point does not require conditions, try to enter another one")

def phi_fun(x):
    if (4 - 3 * x) > 0:
        return 0.5*math.log(4 - 3 * x,math.e)
    else:
        print("This point does not require the scope of definition")


def diff_phi_fun(x):
    return (-3/2)/(4 - 3 * x)

def simple_iteration_method(e, x_0):
#conditions for a point from the localization segment: |phi'(x_0)| < 1
    if abs(diff_phi_fun(x_0)) < 1:
        while abs(fun(x_0)) > e:
            x_0 = phi_fun(x_0)
        return(x_0)
    else:
        return("Initial point does not require conditions, try to enter another one")





print(secant_method(0.4, 0.6, 0.00001), dichotomy_method(0.4, 0.6, 0.00001),
      tangent_method(0.000001,0.5), modified_tangent_method(0.000001,0.5), simple_iteration_method(0.00001, 2))





































