"""
20160406
"""

def sumof35Mul():
    isum=0
    for i in range(1,1000):
        if i%3==0 and i%5==0:
            print i,
            isum=isum+i
        elif i%3==0 or i%5==0:
            print i,
            isum=isum+i

    print isum
    return isum



def leapYear():
    year=raw_input("insert the year: ")
    year=int(year)
    
    if(year%4==0)and (year%100!=0) or (year%400==0):
        res="It's leap year"
    else:
        res="not leap year"
    print res
    return res
    


def upDown():
    range1=raw_input("1st number of range: ")
    range2=raw_input("last number of range: ")
    range1=int(range1)
    range2=int(range2)
    print "Player 1 insert number between",
    print "range1 and range2: ",
    num1=raw_input(": ")
    num1=int(num1)
    
    for i in range(100):
        num2=raw_input("Player2 Try to guess what the number is")
        num2=int(num2)
        if(num1==num2):
            res="Player2 win!!"
            break
        elif(num1<num2):
            print "down!"
        elif(num1>num2):
            print "up!"

    print res
    return res
        

def lab3():
	sumof35Mul()
	leapYear()

	upDown()

def main():
	lab3()

if __name__=="__main__":
	main()