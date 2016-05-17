import math

def isInCircle(circle,pos):
    radius=circle[1]-circle[0]
    return math.sqrt(math.pow(circle[0]-pos[0],2) + math.pow(circle[1]-pos[1],2))<=radius
isInCircle((0,50),(60,60))