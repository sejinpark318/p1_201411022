
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


def milkPercent(data):
    sWater=0
    sMilk=0
    for i in data:
        if(i[2]=="Yes"):
            sMilk+=1

    fsMilk= float(sMilk)
    percent=fsMilk/len(data)*100
    return "{0}%".format(percent)


def scoreAve():
    English=0
    Math=0
    for i in Score:
        English+=i[0]
        Math+=i[1]

    fEnglish=float(English)
    fMath=float(Math)
    return (fEnglish/len(Score),fMath/len(Score))

def Letitbe():
    for i in range(len(Letitbe)):
        for c in Letitbe[i].split():
            if c not in count:
                count[c]=1
            else:
                count[c]+=1
    return count


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


	allData=list()
	allData=(("coffee","Water","Milk","Icecream"),
	        ("Espresso","No","No","No"),
	        ("Long Black","Yes","No","No"),
	        ("Flat White","No","Yes","No"),
	        ("Cappuccino","No","Yes","No"),
	        ("Affogato","No","No","Yes"))
	data=allData[1:6]
	milkPercent(data)


	allScore=list()
	allScore=[("English","Math"),	
	       (100,200),
	       (200,200),
	       (100,300)]

	Score=allScore[1:]
	scoreAve(Score)

	Letitbe=list()
	Letitbe=("When I find myself in times of trouble",
	"Mother Mary comes to me",
	"Speaking words of wisdom let it be",
	"And in my hour of darkness",
	"She is standing right in front of me",
	"Speaking words of wisdom let it be",
	
	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",
	
	"And when the broken-hearted people",
	"Living in the world agree",
	"There will be an answer let it be",
	"For though they may be parted",
	"There is still a chance that they will see",
	"There will be an answer let it be",
	
	"Let it be let it be",
	"Let it be let it be",
	"Yeah there will be an answer let it be",
	"Let it be let it be",
	"Let it be let it be",
	"Whisper words of wisdom let it be",
	
	"Let it be let it be",
	"Ah let it be yeah let it be",
	"Whisper words of wisdom let it be",
	
	"And when the night is cloudy",
	"There is still a light that shines on me",
	"Shine on until tomorrow let it be",
	"I wake up to the sound of music",
	"Mother Mary comes to me",
	"Speaking words of wisdom let it be",
	
	"Let it be let it be",
	"Let it be yeah let it be",
	"Oh there will be an answer let it be",
	"Let it be let it be",
	"Let it be yeah let it be",
	"Whisper words of wisdom let it be")

	count=dict()
	Letitbe()

		
def main(): 
    lab10() 

 
if __name__=="__main__": 
    main() 
