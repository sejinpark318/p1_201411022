import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t1.home()
t1.clear()
def drawLine(line1):
    x1=line1[0][0]-1
    y1=line1[0][1]-1
    x2=line1[1][0]+1
    y2=line1[1][1]+1
    t1.penup()
    t1.goto(x1,y1)
    t1.pendown()
    t1.fd(x2-x1)
    t1.left(90)
    t1.fd(y2-y1)
    t1.left(90)
    t1.fd(x2-x1)
    t1.left(90)
    t1.fd(y2-y1)



def isInRectangle(pos,coord):
    #drawRectangle(coord)
    t1.goto(pos)
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    (x,y)=pos
    return xs<=x<=xe and ys<=y<=ye


def isInOnLine(pos,coord):
    drawLine(coord)
    t1.goto(pos)
    x1=coord[0][0]-1
    y1=coord[0][1]-1
    x2=coord[1][0]+1
    y2=coord[1][1]+1
    (x,y)=pos
    return isInRectangle(pos,[(x1,y1),(x2,y2)])


def keyup():
	t1.fd(50)
	if isInOnLine(t1.pos(),coord)==true:
		print "t1 passed Line!"
def keydown():
	t1.back(50)
	if isInOnLine(t1.pos(),coord)==true:
		print "t1 passed Line!"
def keyright():
	t1.right(90)
	t1.fd(50)
	if isInOnLine(t1.pos(),coord)==true:
		print "t1 passed Line!"
def keyleft():
	t1.left(90)
	t1.fd(50)
	if isInOnLine(t1.pos(),coord)==true:
		print "t1 passed Line!"



wn.onkey(keyup, "Up")
wn.onkey(keydown, "Down")
wn.onkey(keyright, "Right")
wn.onkey(keyleft, "Left")

def mousetogo(x,y):
	t1.setpos(x,y)
	(x,y)=t1.pos()
def addMouse():
	wn.onclick(mousetogo)
addMouse()
wn.listen()

coord=[(100,100),(200,100)]