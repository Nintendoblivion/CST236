"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or isosceles
"""


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

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"

    else:
        return "scalene"


def get_quad_type(a=0, b=0, c=0, d=0):

    """
    Determine if the given Quadrilateral is square or rectangle

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

     :param d: line d
    :type d: float

    :return: "square", "rectangle" or "invalid"
    :rtype: str
    """

    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    elif (a == b and c == d) or (a == c and b == d) or (a == d and c == b):
        return "rectangle"

    else:
        return "invalid"


def get_quad_type_with_angle(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):

    """
    Determine if the given Quadrilateral is square or rectangle

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

     :param d: line d
    :type d: float

    :param e: angle e
    :type e: float

    :param f: angle f
    :type f: float

    :param g: line g
    :type g: float

     :param h: line h
    :type h: float

    :return: "square", "rectangle", "rhombus", "parallelogram or "invalid"
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

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or e <= 0 or f <= 0 or g <= 0 or h <= 0:
        return "invalid"

    if (e + f + g + h) != 360:
        return "invalid"

    if a == b and b == c and c == d:
        if e == f and f == g and g == h:
            return "square"
        elif (e == f and g == h) or (e == g and f == h) or (e == h and g == f):
            return "rhombus"
        else:
            return "invalid"

    elif (a == b and c == d) or (a == c and b == d) or (a == d and c == b):
        if e == f and f == g and g == h:
            return "rectangle"
        elif (e == f and g == h) or (e == g and f == h) or (e == h and g == f):
            return "parallelogram"
        else:
            return "invalid"

    else:
        return "invalid"

