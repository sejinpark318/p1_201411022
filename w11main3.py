
import turtle
wn=turtle.Screen()
wn.bgpic("myMaze.gif")
t1=turtle.Turtle()


def keyup():
	t1.fd(50)
def keydown():
	t1.back(50)
def keyright():
	t1.right(90)
def keyleft():
	t1.left(90)



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

turtle.mainloop()

def lab11():



def main():
	lab11()


if__name__=="__main__":
	main()
