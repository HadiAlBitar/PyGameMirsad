import pygame.locals, trekantsFunktioner


pygame.init()

w = 1000
h = 800
isRunning = True
hasPainted = False
corners = [];

window = pygame.display.set_mode([w,h])
window.fill([255,255,255])

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.locals.MOUSEBUTTONUP:
            if len(corners) == 3:
                corners.clear()
                window.fill([255, 255, 255])
            corners.append(pygame.mouse.get_pos())
        elif event.type == pygame.locals.QUIT:
            exit()

    for corner in corners:
        x,y = corner
        pygame.draw.circle(window,[255,0,0],[x,y],5)

    if len(corners) == 3 and not hasPainted:
        x1,y1 = corners[0]
        x2, y2 = corners[1]
        x3, y3 = corners[2]
        a,b,c = trekantsFunktioner.trekantSider(x1, x2, x3, y1, y2, y3)
        A,B,C = trekantsFunktioner.findTrekantVinkler(a,b,c)
        areal = trekantsFunktioner.findTrekantAreal(a, b, C)
        omkreds = trekantsFunktioner.findTrekantOmkreds(a,b,c)
        trekantsFunktioner.tegnTrekant(x1,x2,x3,y1,y2,y3,window)
        hasPainted = True

    if len(corners) != 3:
        hasPainted = False

    pygame.display.update()
