from Model_Bezier import *
from math import sqrt, acos, pi
from itertools import islice

def getEgLength(a, b):
    ax, ay = a
    bx, by = b
    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)
    
def getAngle(points):
    a = points[0]
    b = points[1]
    c = points[2]
    ab = getEgLength(a, b)
    bc = getEgLength(b, c)
    ac = getEgLength(a, c)
    return acos((ab**2 + bc ** 2 - ac**2) / (2.0 * ab * bc))

def bezierApproximation(path, relMaxDeviation):
    result = list()
    subPath = list()
    maxDeviation = 10
    for node in path:
        subPath.append(node)
        
        if(len(subPath) < 3):
            continue
        
        bezier = getApproximateBezier(subPath)
        deviation = getMaxDeviation(bezier, subPath)
        
        if deviation < maxDeviation:
            continue
        
        subPath.pop()
        
        if len(subPath) > 2:
            bezier = getApproximateBezier(subPath)
            result.append(("bezier", bezier))
        else:
            result.append(("polyline", subPath))
        
        subPath = [subPath.pop(), node]
        
    if len(subPath) > 2:
       bezier = getApproximateBezier(subPath)
       result.append(("bezier", bezier))
       return result
    
    result.append(("polyline", subPath))
    return result

def smoothAngles(curves):
    curve0 = curves[0]
    result = list()
    for curve in islice(curves, 1, None):
        curve0, curve = smoothBezierCurves(curve0, curve)
        result.append(curve0)
        curve = curve0

def smooth(curve0, curve1):
    tag0, nodes0 = curve0
    tag1, nodes1 = curve1
    
    if tag0 != 'bezier' and tag1 != 'bezier':
        return curve0, curve1
    
    len0 = len(nodes0)
    ax, ay = getVector(nodes0[len0 - 1], nodes0[len0 - 2])
    bx, by = getVector(nodes1[0], nodes1[1])
    cx, cy = ax - bx, ay - by
    a2 = ax * ax + ay * ay
    b2 = bx * bx + by * by
    
    if a2 == 0 or b2 == 0:
        return curve0, curve1
    
    c2 = cx * cx + cy * cy
    # c2 = a2 + b2 - 2 * a * b * cos(alpha)
    alpha = acos((a2 + b2 - c2) / (2.0 * a * b))
    
    
def getVector(begin, end):
    x0, y0 = begin
    x1, y1 = end
    return x1 - x0, y1 - y0
    
def alignVectors(a, b):
    xa, ya = a
    xb, yb = b
    a2 = xa * xa + ya * ya
    b2 = xb * xb + yb * yb
    ax1 = 0.5 * (ax - bx * sqrt(a) / sqrt(b))
    ay1 = 0.5 * (ay - by * sqrt(a) / sqrt(b))
    bx1 = 0.5 * (bx - ax * sqrt(b) / sqrt(a))
    by1 = 0.5 * (by - ay * sqrt(b) / sqrt(a))
    a1 = (ax1, ay1)
    b1 = (by1, by1)
    return a1, b1

