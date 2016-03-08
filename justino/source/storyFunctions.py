from datetime import datetime
from math import pi, sqrt, factorial
from decimal import getcontext, Decimal
import numbers
import getpass
from time import sleep

# List of Functions for use in story checker.as


# ********************
#        fib
# ********************
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# ********************
#         Pi
# ********************
def npi(n):
    if n == 0:
        return 'Invalid index for pi'
    else:
        myPi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        return int(myPi[int(n-1)])




# ********************
#    rebuke_user
# ********************
def rebuke_user():
    user = getpass.getuser()
    sorry = 'I\'m afraid I can\'t do that <' + user + '>'
    return sorry


# Enum convert everything to 1 then multiply by 10^n power based on enum.

# ********************
#    metricDisplay
# ********************
def metric_display():
    return 'tera = 6, giga = 5, mega = 4, kilo = 3, deca = 1, no_unit = 0, deci = -1, centi = -2, ' \
           '\n milli = -3, micro = -4, nano = -5, pico = -6; ' \
           '\n Format = "Convert <value> <unit> to <unit to convert to>"'


# ********************
#      metric
# ********************
def metricConversion(value, unit, convert_unit):

    metric = {
        'tera': 6,
        'giga': 5,
        'mega': 4,
        'kilo': 3,
        'hecto': 2,
        'deca': 1,
        'no_unit': 0,
        'deci': -1,
        'centi': -2,
        'milli': -3,
        'micro': -4,
        'nano': -5,
        'pico': -6,
    }

    param = 0
    param2 = 0

    for key in metric:
        if key == unit:
            param = metric[key]

    for key in metric:
        if key == convert_unit:
            param2 = metric[key]

    step = param - param2
    value *= 10**step

    return str(value) + ' ' + str(convert_unit)


# ********************
#    FavoriteNumber
# ********************
def fav_num(num):
    return 'The number ' + str(int(num)) + ' is a dumb number.'


# ********************
#   colorWheelPrint
# ********************
def colorPrint():
    return 'yellow, red, and blue are the primary colors available for mixing'


# ********************
#   colorWheel
# ********************
def colorWheel( colorA, colorB ):

    if colorA == 'blue':
        if colorB == 'red':
            return 'violet'
        if colorB == 'yellow':
            return 'green'
        if colorB == 'blue':
            return 'blue'
    elif colorA == 'red':
        if colorB == 'red':
            return 'red'
        if colorB == 'yellow':
            return 'orange'
        if colorB == 'blue':
            return 'violet'
    elif colorA == 'yellow':
        if colorB == 'red':
            return 'orange'
        if colorB == 'yellow':
            return 'yellow'
        if colorB == 'blue':
            return 'green'


# ********************
#   factorial
# ********************
def nFactorial(n):
    return factorial(n)


# ********************
#   SquareRoot
# ********************
def square_root(n):
    return sqrt(n)


# ********************
#   absoluteVal
# ********************
def abs_value(n):
    if n < 0:
        return n*(-1)
    else:
        return n

# ********************
#   hypotenuse
# ********************
def hypotenuse(x, y):
    z = x**2 + y**2
    c = sqrt(z)
    return c

# ********************
#   WannaHear a joke
# ********************
def joke():

    print "Wanna hear a joke?...\n "
    sleep(1)
    return "To whoever took my Microsoft Office: I will find you. You have my Word."


# ********************
#         numE
# ********************
def numE(n):
    if n == 0:
        return 'Invalid index for e'
    else:
        myE = "271828182845904523536028747135266249775724709369995"
        return int(myE[int(n-1)])

# ********************
#      pokemon
# ********************
def pokemon():
    return 'Snorlax, and hes too tired to program anymore today'