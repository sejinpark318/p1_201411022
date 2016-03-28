import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawblade():
    t1.home()
    t1.clear()
    turns=raw_input("set how many turns: ")
    grow=raw_input("set how much to grow bigger: ")
    angle=raw_input("set angles: ")
    stsize=raw_input("set start size: ")
    i=0
    in_turn=int(turns)
    in_grow=int(grow)
    in_angle=int(angle)
    in_size=int(stsize)
    
    for i in range (in_turn):
        t1.fd(in_size)
        t1.right(in_angle)
        if(i%2==1):
            in_size=in_size+in_grow    
    
drawblade()
