#
# Copyright (c) 2012 pinocchio964
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.
#


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

