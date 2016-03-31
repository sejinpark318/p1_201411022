n1type=raw_input("player a : rock:1, sissor:2, paper:3 ")
n2type=raw_input("player b : rock:1, sissor:2, paper:3 ")

a=n1type
b=n2type

def playRsp(a,b):
    if(a=='1'):
        if(b=='1'):
            print "draws"
        elif(b=='2'):
            print "a wins"
        elif(b=='3'):
            print "b wins"

    elif(a=='2'):
        if(b=='1'):
            print "b winsd"
        elif(b=='2'):
            print "draws"
        elif(b=='3'):
            print "a wins"

    else:
        if(b=='1'):
            print "a winsd"
        elif(b=='2'):
            print "b wins"
        elif(b=='3'):
            print "draw"

playRsp(a,b)