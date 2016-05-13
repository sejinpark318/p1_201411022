
import turtle
wn=turtle.Screen()
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

wn.listen()

turtle.mainloop()

def lab11():



def main():
	lab11()


if__name__=="__main__":
	main()
