import math


def quadratic(a, b, c):
    y1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    y2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return y1, y2


def trim(a):
    if a[0]==' ':
        a = a[1:]
    elseif a[-1]==' ':
        a=
