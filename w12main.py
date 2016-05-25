%%writefile python.txt
Python is a widely used high-level, general-purpose, interpreted, 
dynamic programming language.[23][24] 
Its design philosophy emphasizes code readability, and 
its syntax allows programmers to express concepts in fewer lines of code 
than would be possible in languages such as C++ or Java.[25][26] 
The language provides constructs intended to enable clear programs on 
both a small and large scale.[27]

import os
mydir = os.getcwd()
print mydir

mydir=os.getcwd()
filename='python.txt'
myfilename=os.path.join(mydir, filename)

def findWord(word):
    myfile=open(myfilename,'r')
    for line in myfile:
        if line.find(word)>=0:
            return line
        else:
            return "Not found"
    myfile.close()


myfile=open('output.txt','w')
line1='first line\n'
myfile.write(line1)
line2='\tsecond line!!\n'
myfile.write(line2)
line3='\t\tthird line!!'
myfile.write(line3)
myfile.close()

def wordUp(Location,findword):
    myfile=open(Location,'r') 
    for line in myfile: 
        if line.find(findword)>=0:
            print line.upper()
        else:
            return "Not found"
    myfile.close() 

def lab12():
	findWord('Python')
	wordUp(outputLoc,'line')

def main():
	lab12()


if__name__=="__main__":
	main()
