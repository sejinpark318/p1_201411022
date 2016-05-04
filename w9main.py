
def charCount(word):
    for c in word:
        if c not in mydict:
            mydict[c]=1
        else:
            mydict[c]=mydict[c]+1
    print mydict



def charcountBar():
    plt.bar(range(len(mydict)),mydict.values(),align='center')
    plt.xticks(range(len(mydict)),list(mydict.keys()))
    plt.show()
    



def charcountAddress(school):
    address=({'su':0,'mun':0})
    for c in school:
        if c.isdigit()==True:
            address['su']+=1
        else:
            address['mun']+=1
    print address

    plt.bar(range(len(address)),address.values(),align='center')
    plt.xticks(range(len(address)),list(address.keys()))
    plt.show()





def homeSet(myhome,urhome):
    print myhome.union(urhome)
    print myhome.intersection(urhome)
    print myhome-urhome
    print urhome-myhome
    



 
def lab7():  
    word='sangmyung university'
    mydict=dict()
    charCount(word)

    import matplotlib
    import matplotlib.pyplot as plt
    charcountBar()

    school='20, Hongjimun 2-gil, Jongno-gu, Seoul, Korea'
    charcountAddress(school)

    myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    urhome={'coffee machine', 'raido', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    homeSet(myhome,urhome)
 
def main(): 
    lab7() 

 
if __name__=="__main__": 
    main() 
