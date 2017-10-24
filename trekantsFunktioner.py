import math

import pygame

def tegnTrekant(x1, x2, x3, y1, y2, y3,window): #Closed. Lead: Yusuf, team: Hadi
    pygame.draw.polygon(window, (0, 0, 0), ((x1, y1),(x2,y2),(x3,y3)), 0)
    return window

def findTrekantOmkreds(a,b,c): #Closed. Lead: Yusuf, team: Hadi
    TrekantOmkreds = a + b + c
    return TrekantOmkreds

def trekantSider(x1, x2, x3, y1, y2, y3): #Closed. Lead: Bjørn, Rasmus E, Nick
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    return [a, b, c]

def findTrekantAreal(a,b,C): #Closed. Lead: Rasmus W, team: Jakob
    areal = (1 / 2) * a * b * math.sin(math.radians(C))
    return areal

def findTrekantVinkler(a,b,c): #Closed. Lead: Said, team: Omar
    vinkelSum = 180
    taellerA = (b ** 2 + c ** 2 - a ** 2)
    naevnerA = (2 * b * c)
    Av = math.acos(taellerA / naevnerA)
    A = math.degrees(Av)

    taellerB = (a ** 2 + c ** 2 - b ** 2)
    naevnerB = (2 * a * c)
    Bv = math.acos(taellerB / naevnerB)
    B = math.degrees(Bv)

    C = vinkelSum - A - B

    return [A, B, C]

def findTrekantIndskrevneCirkelsRadius(areal,omkreds): #Closed. Lead: Michael, team: Alexander
    r = areal / (omkreds * 2)
    return r

def findTrekantOmskrevneCirkelsRadius(a,b,c): #Closed. Lead: Gwion, team: Frederik L, Frederik H
    s = (a + b + c) / 2
    aAT = math.sqrt(s * (s - a) * (s - b) * (s - c))
    rAC1 = (a * b * c) / (aAT * 4)

    return rAC1

def flytTrekant(x1,x2,x3,y1,y2,y3,xflyt,yflyt): #Closed. Lead: Michael, team: Alexander
    x1 = x1 + xflyt
    x2 = x2 + xflyt
    x3 = x3 + xflyt
    y1 = y1 + yflyt
    y2 = y2 + yflyt
    y3 = y3 + yflyt
    return [x1,x2,x3,y1,y2,y3]

def findTrekantOmskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3): #Closed. Lead: Magnus, team: Christoffer, Liam
    ## Linjen mellem x/y 1 og x/y 2

    linje12a = (y2 - y1) / (x2 - x1)
    a12 = -1 / linje12a

    x12 = (x1 + x2) / 2
    y12 = (y1 + y2) / 2

    b12 = y12 - a12 * x12

    ## Linjen mellem x/y 1 og x/y 3

    linje13a = (y3 - y1) / (x3 - x1)
    a13 = -1 / linje13a

    x13 = (x1 + x3) / 2
    y13 = (y1 + y3) / 2

    b13 = y13 - a13 * x13

    x = (b13 - b12) / (a12 - a13)
    y = a12 * x + b12
    return [x,y]

def findTrekantIndskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3): #Lead: Gabriel, team: Allan, Daniel
    return [x,y]

def skrivResultater(): #Lead: Gwion, team: Frederik L, Frederik H
    return

def tegnBaggrund(): #Lead: Bjørn, team: Elo, Nick
    return