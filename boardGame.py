import turtle
import random
wn=turtle.Screen()
wn.bgpic("C:\Users\park\Desktop\sejin.gif")
p1=turtle.Turtle()
p2=turtle.Turtle()
p1.pencolor("RED")
p2.pencolor("blue")

x1=(-190,-100,0,100,190)
y1=(-180,-100,0,100,180)
x2=(-230,-100,0,100,230)
y2=(-220,-100,0,100,220)

score=(50,100,70,150,30,100,50,200,70,100,30,150,70,20,170)

ss1={(x1[0],y1[1]):score[0],(x1[0],y1[2]):score[1],(x1[0],y1[3]):score[2],(x1[0],y1[4]):score[3],
    (x1[1],y1[4]):score[4],(x1[2],y1[4]):score[5],(x1[3],y1[4]):score[6],(x1[4],y1[4]):score[7],
    (x1[4],y1[3]):score[8],(x1[4],y1[2]):score[9],(x1[4],y1[1]):score[10],(x1[4],y1[0]):score[11],
    (x1[3],y1[0]):score[12],(x1[2],y1[0]):score[13],(x1[1],y1[0]):score[14]}
ss2={(x2[0],y2[1]):score[0],(x2[0],y2[2]):score[1],(x2[0],y2[3]):score[2],(x2[0],y2[4]):score[3],
    (x2[1],y2[4]):score[4],(x2[2],y2[4]):score[5],(x2[3],y2[4]):score[6],(x2[4],y2[4]):score[7],
    (x2[4],y2[3]):score[8],(x2[4],y2[2]):score[9],(x2[4],y2[1]):score[10],(x2[4],y2[0]):score[11],
    (x2[3],y2[0]):score[12],(x2[2],y2[0]):score[13],(x2[1],y2[0]):score[14]}


def sejinMarble():
    i=0
    j=0
    k=0
    l=0
    point1=0
    point2=0
    p1.goto(x1[0],y1[0])
    p2.goto(x2[0],y2[0])
    p1.clear()
    p2.clear()

    for m in range(0,10):
        
        res1=random.randrange(1,4)
        print "player1 dice roled",res1
        if (res1==1):
            if (i==0 and j!=4):
                i=i
                j=j+1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i!=4 and j==4):
                i=i+1
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i==4 and j!=0):
                i=i
                j=j-1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
               
            elif (i!=0 and i!=1 and j==0):
                i=i-1
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            else:
                p1.goto(0,0)
                print "player1's point:" ,point1
                print "player1's position:" ,p1.pos
                
        

        elif (res1==2):
            if (i==0 and j!=4 and j!=3):
                i=i
                j=j+2
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i==0 and j==3):
                i=i+1
                j=j+1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i!=3 and i!=4 and j==4):
                i=i+2
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i==3 and j==4):
                i=i+1
                j=j-1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i==4 and j!=1 and j!=0):
                i=i
                j=j-2
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif (i==4 and j==1):
                i=i-1
                j=j-1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                

            elif ((i==4 or i==3) and j==0):
                i=i-2
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            else:
                p1.goto(0,0)
                print "player1's point:" ,point1
                print "player1's position:" ,p1.pos
                
        

        else:
            if(i==0 and (j==0 or j==1)):
                i=i
                j=j+3
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif((i==0 or i==1) and j==4):
                i=i+3
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
               
            elif(i==4 and (j==4 or j==3)):
                i=i
                j=j-3
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif(i==4 and j==0):
                i=i-3
                j=j
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
               
            elif(i==0 and j==2):
                i=i+1
                j=j+2
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
               
            elif(i==0 and j==3):
                i=i+2
                j=j+1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif(i==2 and j==4):
                i=i+2
                j=j-1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif(i==3 and j==4):
                i=i+1
                j=j-2
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif(i==4 and j==2):
                i=i-1
                j=j-2
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            elif(i==4 and j==1):
                i=i-2
                j=j-1
                p1.goto(x1[i],y1[j])
                p1.pos=(x1[i],y1[j])
                point1+=ss1[(x1[i],y1[j])]
                print "player1's position:" ,p1.pos
                
            else:
                print "player1's point:" ,point1
                p1.goto(0,0)
                
        res2=random.randrange(1,4)
        print "player2 dice roled",res2
        if (res2==1):
            if (k==0 and l!=4):
                k=k
                l=l+1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k!=4 and l==4):
                k=k+1
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k==4 and l!=0):
                k=k
                l=l-1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k!=0 and k!=1 and l==0):
                k=k-1
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            else:
                p2.goto(0,0)
                print "player2's point:" ,point2
                print "player2's position:" ,p2.pos


        elif (res2==2):
            if (k==0 and l!=4 and l!=3):
                k=k
                l=l+2
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k==0 and l==3):
                k=k+1
                l=l+1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k!=3 and k!=4 and l==4):
                k=k+2
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k==3 and l==4):
                k=k+1
                l=l-1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k==4 and l!=1 and l!=0):
                k=k
                l=l-2
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif (k==4 and l==1):
                k=k-1
                l=l-1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos


            elif ((k==4 or k==3) and l==0):
                k=k-2
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            else:
                p2.goto(0,0)
                print "player2's point:" ,point2
                print "player2's position:" ,p2.pos



        else:
            if(k==0 and (l==0 or l==1)):
                k=k
                l=l+3
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif((k==0 or k==1) and l==4):
                k=k+3
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==4 and (l==4 or l==3)):
                k=k
                l=l-3
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==4 and l==0):
                k=k-3
                l=l
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==0 and l==2):
                k=k+1
                l=l+2
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==0 and l==3):
                k=k+2
                l=l+1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==2 and l==4):
                k=k+2
                l=l-1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==3 and l==4):
                k=k+1
                l=l-2
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==4 and l==2):
                k=k-1
                l=l-2
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            elif(k==4 and l==1):
                k=k-2
                l=l-1
                p2.goto(x2[k],y2[l])
                p2.pos=(x2[k],y2[l])
                point2+=ss2[(x2[k],y2[l])]
                print "player2's position:" ,p2.pos

            else:
                print "player2's point:" ,point2
                p2.goto(0,0)
                
    
    if point1>point2:
        res="player1 win!"
    elif point1<point2:
        res="player2 win!"
    else:
        res="draw!"
    
    return res

def lab7():
    sejinMarble()
def main():
    lab7()

if __name__=="__main__": 
 	main() 
