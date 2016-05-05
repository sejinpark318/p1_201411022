
def closestSta():
    for i in range(1,4):
        x.append(math.sqrt((loc[0][0]-loc[i][0])**2 + (loc[0][1]-loc[i][1])**2))
    print x

    res=min(x)
    return res



def sumaveofJumin():
    bsum=0
    gsum=0
    gusum=list()
    guname=list()
    res=dict()
    for i in range(0,len(stat)):
        bsum+=stat[i][1]
    res['boyssum']=bsum
    res['boysave']=bsum/len(stat)
    
    for i in range(0,len(stat)):
        gsum+=stat[i][2]
    res['girlssum']=gsum
    res['girlsave']=gsum/len(stat)

    for i in range(0,len(stat)):
        gusum.append(stat[i][1]+stat[i][2])
        guname.append(stat[i][0])
        res[guname[i]]=gusum[i]
    print gusum
    print guname
    
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(gusum)),gusum,align='center')
    plt.xticks(range(len(gusum)),list(guname))
    plt.show()

    return res


def lab10():  
	import math
	x=list()

	closestSta()


	stat=list()
	stat=(
	('jongno',80531,83291),
	('jung',66755,67574),
	('yongsan',121027,126882),
	('sungdong',151459,153606),
	('kwangjin',183436,191744),
	('dongdaemun',185827,187997),
	('junglang',208393,210227),
	('sungbuk',229183,240377),
	('gangbuk',164337,170089),
	('dobong',173804,179437),
	('nowon',281538,296683),
	('eunpyeong',244964,257614),
	('seodaemun',156130,166975),
	('mapo',190957,207394),
	('yangchun',242074,246936),
	('kangseo',291216,304475),
	('kuro',228201,226403),
	('keumchun',131346,124821),
	('youngdeungpo',210388,207423),
	('dongjak',202165,210609),
	('kwanak',266773,262258),
	('seocho',217036,234222),
	('kangnam',279209,302551),
	('songpa',325950,341530),
	('kangdong',230851,232470))
	
	
	sumaveofJumin()

def main(): 
    lab10() 

 
if __name__=="__main__": 
    main() 
