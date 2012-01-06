from math import sqrt
from itertools import islice


def bezierApproximation(path, maxDeviation):
    result = list()
    subPath = list()
    for node in path:
        subPath.append(node)
        if(len(subPath) < 3):
            continue
        
        bezier = getApproximateBezier(subPath)
        deviation = getMaxDeviation(bezier, subPath)
        
        if deviation < maxDeviation:
            bezier0 = bezier
            continue

        if len(subPath) <= 3:
            result.append(("polyline", subPath))
        else:
            result.append(("bezier", bezier))
        
        subPath = list(node)
        
    if len(subPath) > 0:
        result.append(("polyline", subPath))
    return result
    
def getBezier(b, t):
    x = b[0][0] * (1 - t) ** 3 + 3 * b[1][0] * t * (1 - t) ** 2 + 3 * b[2][0] * (t ** 2) * (1 - t) + b[3][0] *t **3
    y = b[0][1] * (1 - t) ** 3 + 3 * b[1][1] * t * (1 - t) ** 2 + 3 * b[2][1] * (t ** 2) * (1 - t) + b[3][1] *t **3
    return (x, y)
    
def getMaxDeviation(bezier, path):
    length = getLength(path);
    x0, y0 = bezier[0]
    deviation = 0
    t = 0
    for x, y in islice(path, 1, None):
        t = t + sqrt((x - x0) ** 2 + (y - y0) ** 2) / length
        bx, by = getBezier(bezier, t)
        deviation = max(deviation, sqrt((bx - x) ** 2 + (by - y) ** 2))
        x0, y0 = x, y
    return deviation
    
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
    cx0, cx1, cx2, cx3 = 0.0, 0.0, 0.0, 0.0
    cy0, cy1, cy2, cy3 = 0.0, 0.0, 0.0, 0.0
    
    t0 = 0.0
    for x1, y1 in islice(path, 1, None):
        partialLength = partialLength + sqrt((x1 - x0) ** 2.0 + (y1 - y0) ** 2.0)
        t1 = partialLength / length
        cx0 = cx0 + bezier0(t0, t1, x0, x1);   cy0 = cy0 + bezier0(t0, t1, y0, y1)
        cx1 = cx1 + bezier1(t0, t1, x0, x1);     cy1 = cy1 + bezier1(t0, t1, y0, y1)
        cx2 = cx2 + bezier2(t0, t1, x0, x1);   cy2 = cy2 + bezier2(t0, t1, y0, y1)
        cx3 = cx3 + bezier3(t0, t1, x0, x1);   cy3 = cy3 + bezier3(t0, t1, y0, y1)
        x0, y0, t0 = x1, y1, t1
    
    bx0, bx1, bx2, bx3  = convert(cx0, cx1, cx2, cx3)
    by0, by1, by2, by3  = convert(cy0, cy1, cy2, cy3)
    
    bx0, by0 = path[0]
    bx3, by3 = path[len(path) - 1]
    return [(bx0, by0), (bx1, by1), (bx2, by2), (bx3, by3)]
    
def convert(u0, u1, u2, u3):
    v0  = 16.0  * u0 - 24.0      * u1  + 16.0       * u2 -4.0    * u3
    v1  = -24.0 * u0 + 208.0/3.0 * u1  - 172.0/3.0   * u2 + 16.0  * u3
    v2 =  16.0  * u0 - 172.0/3.0  * u1  + 208.0/3.0  * u2 - 24.0  * u3
    v3 =  -4.0  * u0 + 16.0      * u1  - 24.0       * u2  + 16.0 * u3
    return v0, v1, v2, v3
    
def getIntegral(t0, t1, y0, y1, a3, a2, a1, a0):
    if(t0 == t1):
        return 0.0
    b1 = (y1 - y0) / (t1 - t0)
    b0 = y0 - b1 * t0
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
    for x, y in islice(path, 1, None):
        length = length + sqrt((x - x0) ** 2.0 + (y - y0) ** 2.0)
        x0, y0 = x, y
    return length
    
