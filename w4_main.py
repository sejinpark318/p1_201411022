import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

turns=raw_input("set how many turns: ")
grow=raw_input("set how much to grow bigger: ")
stsize=raw_input("set start size: ")

in_turn=int(turns)
in_grow=int(grow)
in_size=int(stsize)

def makeSwirlSquare(in_turn,in_grow,in_size):
    for i in range (in_turn):
        t1.fd(in_size)
        t1.right(90)
	if(i%2==1): 
        in_size=in_size+in_grow  
      

makeSwirlSquare(in_turn,in_grow,in_size)

