


from graphics import*


def examGraphic():

    win = GraphWin()
    win.setCoords(0,0,10, 10)
    rect = Rectangle(Point(0,0),Point(3,3)) 
    rect.draw(win)
    rect.setFill('blue')
    rect.setOutline('red')
examGraphic()
