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

def lab7():
    size=100
    pos=(0,0)
    tracks=list()
    mytracks=drawSquareAtSave(size, pos)
    print mytracks 

    tracks=list()
    tracks=[(0,0),(50,0),(100,100),(0,10)]
    drawSquareFromList(tracks)

def main():
    lab7()

if __name__=="__main__": 
 	main() 