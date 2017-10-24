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

def findTrekantOmskrevneCirkelsRadius(a,b,c): #Lead: Gwion, team: Frederik L, Frederik H
    s = (a + b + c) / 2
    aAT = math.sqrt(s * (s - a) * (s - b) * (s - c))
    rAC1 = (a * b * c) / (aAT * 4)

    print('---')
    print('Radius Af Din Cirkel Er: ', rAC1)
    print('---')

def findTrekantOmskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3): #Lead: Magnus, team: Christoffer, Liam
    return [x,y]

def findTrekantIndskrevneCirkelsRadius(areal,omkreds): #Lead: Michael, team: Alexander
    return r

def findTrekantIndskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3): #Lead: Gabriel, team: Allan, Daniel
    return [x,y]

def skrivResultater(): #Lead: Gwion, team: Frederik L, Frederik H
    return

def tegnBaggrund(): #Lead: Bjørn, team: Elo, Nick
    return

def flytTrekant(x1,x2,x3,y1,y2,y3,xflyt,yflyt): #Lead: Michael, team: Alexander
    return [x1,x2,x3,y1,y2,y3]