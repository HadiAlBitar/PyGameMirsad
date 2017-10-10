import math

import pygame


def findTrekantOmkreds(): #Made by Yusuf, Hadi
    a + b + c
    return [a,b,c]

def trekantSider(x1, x2, x3, y1, y2, y3): #Made by Bjørn, Rasmus E, Nick
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    return [a, b, c]

def findTrekantAreal(sider, vinkler): #Made by Jakob, Rasmus W
    # sider = findTrekantSidelængde, vinkler = findTrekantVinkler
    areal = (1 / 2) * sider[0] * sider[1] * math.sin(math.radians(vinkler[2]))
    return areal

def findTrekantVinkler(a,b,c): #Made by Said, Omar
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

    return (A, B, C)

def findTrekantOmskrevneCirkelsRadius(a,b,c): #Made by Gwion, Frederik L
    s = (a + b + c) / 2
    aAT = math.sqrt(s * (s - a) * (s - b) * (s - c))
    rAC1 = (a * b * c) / (aAT * 4)

    print('---')
    print('Radius Af Din Cirkel Er: ', rAC1)
    print('---')

def findTrekantOmskrevneCirkelsKordinater(): #Made by Oliver, Mads, Liam
    return 0

def findTrekantIndskrevneCirkelsRadius(): #Made by Michael, Alexander
    return 0

def findTrekantIndskrevneCirkelsKordinater(): #Made by Allan, Gabriel, Daniel
    return 0

def findTrekantVinkelHalveringsLinjer(): #Made by
    return 0

def tegnTrekant(): #Made by Yusuf, Hadi
    while True:
        mitVindue = pygame.display.set_mode((1000, 1000))
        mitVindue.fill((255, 255, 255))
        pygame.display.update()
        return [pygame.draw.polygon(mitVindue, (0, 0, 0), ((x_1, y_1),(x_2,y_2),(x_3,y_3)), 0)]

def skrivResultater(): #Made by Gwion, Frederik L
    return 0