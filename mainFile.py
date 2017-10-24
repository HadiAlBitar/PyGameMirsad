import pygame.locals, trekantsFunktioner


pygame.init()

w = 1000
h = 800
isRunning = True
hasPainted = False
corners = [];

window = pygame.display.set_mode([w,h])
window.fill([255,255,255])
pygame.key.set_repeat(500,50)

while isRunning:
    xflyt = yflyt = 0
    for event in pygame.event.get():
        if event.type == pygame.locals.MOUSEBUTTONUP:
            if len(corners) == 3:
                corners.clear()
                window.fill([255, 255, 255])
            else:
                corners.append(pygame.mouse.get_pos())
        elif event.type == pygame.locals.QUIT:
            exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_RIGHT:
                xflyt = 1
            elif event.key == pygame.locals.K_RIGHT:
                xflyt = -1
            elif event.key == pygame.locals.K_DOWN:
                yflyt = 1
            elif event.key == pygame.locals.K_UP:
                yflyt = -1

    for i in range(0,len(corners)):
        #corners[i][0] = corners[i][0] + xflyt
        #corners[i][1] = corners[i][1] + yflyt
        x,y = corners[i]
        pygame.draw.circle(window,[255,0,0],[x,y],2)

    if len(corners) == 3 and not hasPainted:
        x1,y1 = corners[0]
        x2, y2 = corners[1]
        x3, y3 = corners[2]
        x1, x2, x3, y1, y2, y3 = trekantsFunktioner.flytTrekant(x1, x2, x3, y1, y2, y3, xflyt, yflyt)
        a,b,c = trekantsFunktioner.trekantSider(x1, x2, x3, y1, y2, y3)
        A,B,C = trekantsFunktioner.findTrekantVinkler(a,b,c)
        areal = trekantsFunktioner.findTrekantAreal(a, b, C)
        omkreds = trekantsFunktioner.findTrekantOmkreds(a,b,c)
        indskrevneCirkelR = trekantsFunktioner.findTrekantIndskrevneCirkelsRadius(areal,omkreds)
        omskrevneCirkelR = trekantsFunktioner.findTrekantOmskrevneCirkelsRadius(a,b,c)
        omskrevneCirkelX,omskrevneCirkelY = trekantsFunktioner.findTrekantOmskrevneCirkelsKordinater(x1, x2, x3, y1, y2, y3)
        print(areal,omkreds,indskrevneCirkelR)
        trekantsFunktioner.tegnTrekant(x1,x2,x3,y1,y2,y3,window)
        pygame.draw.circle(window, [255, 0, 0], [int(omskrevneCirkelX), int(omskrevneCirkelY)], 2)
        pygame.draw.circle(window,[0,255,0],[int(omskrevneCirkelX), int(omskrevneCirkelY)], int(omskrevneCirkelR),2)
        hasPainted = True

    if len(corners) != 3:
        hasPainted = False

    pygame.display.update()
