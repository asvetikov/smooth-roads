import math
from itertools import islice

def bezierApproximation(path):
    return list()

# inverse matrix of gram
# [ 16.0,    -24.0,      16.0,        -4.0    ]
# [ -24.0,   208.0/3.0,  -172.0/3.0,   16.0    ]
# [ 16.0,    -172.0/3.0,  208.0/3.0,   -24.0   ]
# [ -4.0,    16.0,       -24.0,       16.0    ]

def getApproximateBezier(path):
    if(len(path) < 2):
        return None
    
    bezier0 = lambda t0, t1, y0, y1: getIntegral(t0, t1, y0, y1, -1.0, 3.0, -3.0, 1.0)
    bezier1 = lambda t0, t1, y0, y1: getIntegral(t0, t1, y0, y1, 3.0, -6.0, 3.0, 0.0)
    bezier2 = lambda t0, t1, y0, y1: getIntegral(t0, t1, y0, y1, -3.0, 3.0, 0.0, 0.0)
    bezier3 = lambda t0, t1, y0, y1: getIntegral(t0, t1, y0, y1, 1.0,  0.0, 0.0, 0.0)
    
    length = getLength(path)
    x0, y0 = path[0]
    partialLength = 0.0
    cx0, cx1, cx2, cx3 = 0.0, 0.0, 0.0, 0.0;
    cy0, cy1, cy2, cy3 = 0.0, 0.0, 0.0, 0.0;
    
    for x1, y1 in islice(path, 1, None):
        dx, dy = x1 - x0, y1 - y0
        t0 = partialLength / length
        partialLength = partialLength + math.sqrt(dx * dx + dy * dy)
        t1 = partialLength / length
        cx0 = cx0 + bezier0(t0, t1, x0, x1);   cy0 = cy0 + bezier0(t0, t1, y0, y1)
        cx1 = cx1 + bezier1(t0, t1, x0, x1);     cy1 = cy1 + bezier1(t0, t1, y0, y1)
        cx2 = cx2 + bezier2(t0, t1, x0, x1);   cy2 = cy2 + bezier2(t0, t1, y0, y1)
        cx3 = cx3 + bezier3(t0, t1, x0, x1);   cy3 = cy3 + bezier3(t0, t1, y0, y1)
        x0, y0 = x1, y1
    
    bx0  = 16.0  * cx0 - 24.0      * cx1  + 16.0       * cx2 -4.0    * cx3
    bx1  = -24.0 * cx0 + 208.0/3.0 * cx1  - 172.0/3.0   * cx2 + 16.0  * cx3
    bx2 =  16.0  * cx0 - 172.0/3.0  * cx1  + 208.0/3.0  * cx2 - 24.0  * cx3
    bx3 =  -4.0  * cx0 + 16.0      * cx1  - 24.0       * cx2  + 16.0 * cx3
    
    by0  = 16.0  * cy0 - 24.0      * cy1  + 16.0       * cy2 -4.0    * cy3
    by1  = -24.0 * cy0 + 208.0/3.0 * cy1  - 172.0/3.0   * cy2 + 16.0  * cy3
    by2 =  16.0  * cy0 - 172.0/3.0  * cy1  + 208.0/3.0  * cy2 - 24.0  * cy3
    by3 =  -4.0  * cy0 + 16.0      * cy1  - 24.0       * cy2  + 16.0 * cy3

    return [(bx0, by0), (bx1, by1), (bx2, by2), (bx3, by3)]
    
            
def getIntegral(t0, t1, y0, y1, a3, a2, a1, a0):
    if(t0 == t1):
        return 0.0
    b1 = (y1 - y0) / (t1 - t0)
    b0 = y0 
    p1 = getPrimitive(t1, b1, b0, a3, a2, a1, a0)
    p0 = getPrimitive(t0, b1, b0, a3, a2, a1, a0)
    return p1 - p0
     
# return primitive of product
# (b1 * t + b0) * (a3 * t^3 + a2 * t^2 + a1 * t^1 + a0)
def getPrimitive(t, b1, b0, a3, a2, a1, a0):
    result = b1 * a3 / 5.0
    result = (b1 * a2 + b0 * a3) / 4.0 + result * t
    result = (b1 * a1 + b0 * a2) / 3.0 + result * t
    result = (b1 * a0 + b0 * a1) / 2.0 + result * t
    result = b0 * a0 + result * t
    return result * t

def getLength(path):
    if (len(path) < 2):
        return 0.0
    
    length = 0.0
    x0, y0 = path[0]
    for x, y in path:
        dx, dy = x - x0, y - y0 
        length = length + math.sqrt(dx * dx + dy * dy)
        x0, y0 = x, y
    return length
    
