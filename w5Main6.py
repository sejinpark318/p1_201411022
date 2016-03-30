inmarks=raw_input("input your score(0~100): ")
marks=float(inmarks)
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
    
    print "Your grade is " +grade
    
computeGrade(marks)