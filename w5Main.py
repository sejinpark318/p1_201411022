"""
20160330
"""

def computeGrade(marks):
    if (marks>=90 and marks<=100):
        grade='A'
    elif (marks>=80 and marks<90):
        grade='B'
    elif (marks>=70 and marks<80):
        grade='C'
    elif (marks>=60 and markse<70):
        grade='D'
    else:
        grade='F'
    return grade


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

"""
20160404
"""
def computeBMI():
	"""
	coumpute bmi
	height:float
	weight:float
	"""    
    bmi=w/(h*h)

    if bmi<=18.5:
        res="underweight"
    elif bmi>=18.5 and bmi<25:
        res="Normalweight"
    elif bmi>=25 and bmi<30:
        res="Overweight"
    else:
        res="Obesity"
    return res


def lab3():
	inmarks=raw_input("input your score(0~100): ")
	marks=float(inmarks)
	computeGrade(marks)

def lab4():
	n1type=raw_input("player a : rock:1, sissor:2, paper:3 ")
	n2type=raw_input("player b : rock:1, sissor:2, paper:3 ")

	a=n1type
	b=n2type
	playRsp(a,b)

def lab5():
	weight=raw_input("Enter your weight: ")
	height=raw_input("Enter your height: ")
	w=float(weight)
	h=float(height)
	computeBMI()
	
	for i in range(1,6):
   		print "*"*i
 	for i in range(1,6):
    		print " "*(6-i)+"*"*i
	for i in range(1,6):
  		print " "*(6-i)+"*"*(i*2-1)

def main():
	lab4()
	lab5()

if__name__=="__main__":
	main()
