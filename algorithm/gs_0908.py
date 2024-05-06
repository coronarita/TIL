import math


def solution(w,h):
    if math.gcd(w,h) == 1 :
        return w*h -(w+h-1)
    else :
        return w*h - (w+h-math.gcd(w,h))