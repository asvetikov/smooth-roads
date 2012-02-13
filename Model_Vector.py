from Model_Bezier import *
from math import sqrt, acos, pi
from itertools import islice

def length(a):
    xa, ya = a
    return sqrt(xa ** 2 + ya ** 2)
    
def streighten(a, b):
    xa, ya = a
    xb, yb = b

    a2b = length(a) / length(b)
    a1 = (0.5 * (xa - xb * a2b), 0.5 * (ya - yb * a2b))
    
    b2a = length(b) / length(a)
    b1 = (0.5 * (xb - xa * b2a), 0.5 * (yb - ya * b2a))
    
    return a1, b1

