"""
20160418
"""

def drawSquareAtSave(size,oldpos):
    t1.clear()
    for i in range(4):
        t1.fd(size)
        t1.left(90)

        tracks.append(t1.pos())
    return tracks
       


def drawSquareFromList(tracks):
    for i in range(4):
        t1.goto(tracks[i])


"""
20160420
"""
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def saveTracks():
    t1.speed(1)
    t1.penup()
    tracks=list()
    t1.goto(-400,300)
    tracks.append(t1.pos())
    t1.pendown()
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    tracks.append(t1.pos())
    t1.backward(150)
    t1.left(90)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(150)
    tracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    tracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    tracks.append(t1.pos())
    t1.fd(300)
    tracks.append(t1.pos())
    t1.back(100)
    tracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    tracks.append(t1.pos())

    return tracks

def replayTracks(tracks):
    print 'hello'
    for t in mytracks:
        print t

def lab7():
    size=100
    pos=(0,0)
    tracks=list()
    mytracks=drawSquareAtSave(size, pos)
    print mytracks 


    tracks=list()
    tracks=[(0,0),(50,0),(100,100),(0,10)]
    drawSquareFromList(tracks)

    mytracks=saveTracks():
    replayTracks(tracks)
def main():
    lab7()

if __name__=="__main__": 
 	main() 