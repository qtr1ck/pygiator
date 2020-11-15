################################################################################
##                                                                            ##
##      Title:      Pygiator Logo                                             ##
##      Author:     Patrick Schaefler                                         ##   
##      Date:       15.11.2020                                                ##
##      Version:    0.1                                                       ## 
##                                                                            ##
################################################################################

import turtle as t

def plotDiamond(n, size, degree):
    t.left(degree)
    t.left(45)

    for i in range(0, n):
        endPos = t.Vec2D(0,0)
        for j in range(0,4):
            t.fd(size)
            t.left(90)
            if j == 1:
                endPos = t.pos()
        t.goto(endPos)
    t.left(-45)

def plotP(size):
    plotDiamond(10, size, 0)
    for i in range(0,3):
        plotDiamond(5, size, -90)
        
def plotY(size):
    plotDiamond(5, size, 0)
    tmpPos = t.pos()

    plotDiamond(6, size, 35)
    t.up()
    t.goto(tmpPos)
    t.down()
    plotDiamond(6, size, -70)

def plotG(size):
    plotDiamond(3, size, 90)

    for i in range(0, 2):
        plotDiamond(2, size, -45)
        plotDiamond(3, size, -45)

    plotDiamond(2, size, -45)
    plotDiamond(2, size, 135)
    plotDiamond(5, size, -180)
    plotDiamond(2, size, -45)
    plotDiamond(2, size, 180)
    plotDiamond(5, size, -135)
    plotDiamond(2, size, -45)
    plotDiamond(3, size, -45)
    plotDiamond(1, size, -45)

def plotI(size):
    plotDiamond(5, size, 0)

    t.up()
    t.goto(t.pos() + t.Vec2D(0, size * 2))
    t.down()

    plotDiamond(1, size, 0)

def plotA(size):
    plotDiamond(3, size, 90)

    for i in range(0, 2):
        plotDiamond(2, size, -45)
        plotDiamond(3, size, -45)

    plotDiamond(2, size, -45)
    plotDiamond(2, size, 135)
    plotDiamond(7, size, -180)
    plotDiamond(2, size, 180)
    plotDiamond(2, size, 135)

def plotT(size):
    plotDiamond(1, size, 90)
    plotDiamond(1, size, -45)
    plotDiamond(9, size, -45)
    plotDiamond(3, size, 180)
    plotDiamond(2, size, 90)
    plotDiamond(4, size, 180)

def plotO(size):
    plotDiamond(3, size, 90)

    for i in range(0, 3):
        plotDiamond(2, size, -45)
        plotDiamond(3, size, -45)
    plotDiamond(2, size, -45)

def plotR(size):
    plotDiamond(6, size, 0)
    plotDiamond(1, size, 180)
    plotDiamond(1, size, 135)
    plotDiamond(2, size, -45)
    plotDiamond(1, size, -45)

def nextChar(pos):
    t.up()
    t.goto(pos) 
    t.seth(0)
    t.down()

def plotLogo(size):
    t.pensize(2)
    t.speed(speed=0)
    t.pencolor('#e3c729')
    
    t.right(90)
    t.up()
    t.fd(375)
    t.down()
    t.left(90)
    t.color('#e3c729')
    t.begin_fill()
    t.circle(375)
    t.end_fill()

    # logo
    t.pencolor('#e62727')
    t.up()
    t.goto(-360, -50)
    t.down()
    addPos = t.Vec2D(size * 14, 0)
    posPrev = t.pos()

    plotP(size)
    posPrev = posPrev + addPos
    nextChar(posPrev)

    plotY(size) 
    posPrev = posPrev + addPos * 0.8
    nextChar(posPrev)

    plotG(size)
    posPrev = posPrev + addPos * 0.4
    nextChar(posPrev)

    plotI(size)
    posPrev = posPrev + addPos * 0.7
    nextChar(posPrev)

    plotA(size)
    posPrev = posPrev + addPos * 0.7
    nextChar(posPrev)

    plotT(size)
    posPrev = posPrev + addPos * 0.6
    nextChar(posPrev)

    plotO(size)
    posPrev = posPrev + addPos * 0.5
    nextChar(posPrev)

    plotR(size)
    t.ht()

plotLogo(10)
t.Screen().exitonclick()