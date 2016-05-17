import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

t1.home()
t1.clear()
def drawRectangle(coord):
    t1.penup()
    t1.goto(coord[0])
    t1.pendown()
    t1.fd(int(coord[1][0])-int(coord[0][0]))
    t1.left(90)
    t1.fd(int(coord[1][1])-int(coord[0][1]))
    t1.left(90)
    t1.fd(int(coord[1][1])-int(coord[0][1]))
    t1.left(90)
    t1.fd(int(coord[1][0])-int(coord[0][0]))

def isInRectangle(pos,coord):
    drawRectangle(coord)
    t1.goto(pos)
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    (x,y)=pos
    return xs<=x<=xe and ys<=y<=ye


print isInRectangle((0,0),[(100,100),(200,200)])
print isInRectangle((150,100),[(100,100),(200,200)])