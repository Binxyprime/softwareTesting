"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""


# ----------------------------------------------------------------- #
#                          get_triangle_type                        #
# ----------------------------------------------------------------- #
def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    elif a == b and b == c:
        return "equilateral"
    elif (a + b) <= c or (b + c) <= a or (a + c) <= b:
        return "invalid"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


# ----------------------------------------------------------------- #
#                          get_quad_type                            #
# ----------------------------------------------------------------- #
def get_quad_type(a=0, b=0, c=0, d=0, e=90, f=90, g=90, h=90):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :param e: line a
    :type e: float or int or tuple or list or dict

    :param f: line b
    :type f: float

    :param g: line c
    :type g: float

    :param h: line d
    :type h: float

    :return:
    :rtype: str
    """

    if isinstance(a, (tuple, list)) and len(a) == 8:
        h = a[7]
        g = a[6]
        f = a[5]
        e = a[4]
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 8:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]
        e = values[4]
        f = values[5]
        g = values[6]
        h = values[7]

    # inputs must be integers or floating point numbers.
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"
    if not (isinstance(e, (int, float)) and isinstance(f, (int, float)) and isinstance(g, (int, float)) and isinstance(h, (int, float))):
        return "invalid"

    # cannot have negative length, if length = 0 on any input then it will be a line not a quadrilateral or a triangle
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    # convert angles above or below 360 to degrees between 0 and 360
    while e > 360:
        e -= 360
    while e < (-360):
        e += 360

    while f > 360:
        f -= 360
    while f < (-360):
        f += 360

    while g > 360:
        g -= 360
    while g < (-360):
        g += 360

    while h > 360:
        h -= 360
    while h < (-360):
        h += 360

    # Convert negative angles into their positive counter parts.
    if e < 0:
        e += 360
    if f < 0:
        f += 360
    if g < 0:
        g += 360
    if h < 0:
        h += 360

    # for a 4 sided shape to be connected the angles must add to 360
    if (e + f + g + h) != 360:
        return "disconnected"
    elif a == b and a == c and a == d and e == 90 and f == 90 and g == 90 and h == 90:
        return "Square"
    elif a == c and b == d and e == 90 and f == 90 and g == 90 and h == 90:
        return "rectangle"
    # Opposing sides and angles must match.
    elif a == c and b == d and e == g and f == h:
        return "rhombus"
    else:
        return "invalid"
