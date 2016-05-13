def aveofSchoolsat(verygood, good, bad, verybad):
    sum1=0
    avg1=0
    for i in verygood + good:  
        sum1=sum1+i  

    avg1=sum1/len(verygood+good)

    sum2=0
    avg2=0
    for i in verybad + bad:  
        sum2=sum2+i  

    avg2=sum2/len(verybad+bad)
    return avg1, avg2

def count10words(listname,morethan):
    split = dict()
    for sentence in listname:
        words=sentence.split()
        for c in words:
            if c in split:
                split[c]+=1
            else:
                split[c]=1

    
    manyw=set()
    for i in split:
        if split[i]>morethan:
            manyw.add(i)
    return manyw



def compare2list(list1,list2):
    print goerge10.difference(Will10)
    print goerge10.intersection(Will10)
    print goerge10.union(Will10)


def lab11():

    aveofSchoolsat(verygood, good, bad, verybad)

	George_bush=list()
	George_bush=["Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens: ",
	
	"On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country. I am grateful 	for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed. ",
	
	"At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by 	standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire. ",
	
	"We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed 	hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat. There is only one force of 	history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human 	freedom. ",
	
	"We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands. The best hope for 	peace in our world is the expansion of freedom in all the world. ",
	
	"America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, 	and matchless value, because they bear the image of the Maker of Heaven and earth. Across the generations we have proclaimed the imperative of self-government, because no one is 	fit to be a master, and no one deserves to be a slave. Advancing these ideals is the missionthat created our Nation. It is the honorable achievement of our fathers. Now it is the 	urgent requirement of our nation's security, and the calling of our time. ",
	
	"So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture, with the ultimate goal of ending 	tyranny in our world. ",
	
	"This is not primarily the task of arms, though we will defend ourselves and our friends by force of arms when necessary. Freedom, by its nature, must be chosen, and defended by 	citizens, and sustained by the rule of law and the protection of minorities. And when the soul of a nation finally speaks, the institutions that arise may reflect customs and 	traditions very different from our own. America will not impose our own style of government on the unwilling. Our goal instead isto help others find their own voice, attain their 	own freedom, and make their own way. ",
	
	"The great objective of ending tyranny is the concentrated work of generations. The difficulty of the task is no excuse for avoiding it. America'sinfluence is not unlimited, but 	fortunately for the oppressed, America's influence is considerable, and we will use it confidently in freedom's cause. ",
	
	"My most solemn duty is to protect this nation and its people against further attacks and emerging threats. Some have unwisely chosen to test America's resolve, and have found it 	firm. ",
	
	"We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression, which is always wrong, and freedom,which is eternally right. 	America will not pretend that jailed dissidents prefer their chains, or that women welcome humiliation and servitude, or that any human being aspires to live at the mercy of 	bullies. ",
	
	"We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people.America's belief in human 	dignity will guide our policies, yet rights must be more than the grudging concessions of dictators; they are securedby free dissent and the participation of the governed. In the 	long run, there is no justice without freedom, and there can be no human rights without human liberty. ",
	
	"Some, I know, have questioned the global appeal of liberty —though this time in history, four decades defined by the swiftest advance of freedom ever seen, is an odd time for 	doubt. Americans, of all people, should never be surprised by the power of our ideals. Eventually, the call of freedom comes to every mind and every soul. We do not accept the 	existence of permanent tyranny because we do not accept the possibility of permanent slavery. Liberty will come to those who love it. ",
	
	"Today, America speaks anew to the peoples of the world: ",
	
	"All who live in tyranny and hopelessness can know: the United States will not ignore your oppression, or excuse your oppressors. When you stand for your liberty, we will stand 	with you. ",
	
	"Democratic reformers facing repression, prison, or exile can know: America sees you for who you are: the future leaders of your free country. ",
	
	"The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did: 'hose who deny freedom to others deserve it not for themselves; and, under the rule of a just 	God, cannot long retain it.' ",
	
	"The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them. Start on this journey of progress and justice, and America 	will walk at your side. ",
	
	"And all the allies of the United States can know: we honor your friendship, we rely on your counsel, and we depend on your help. Division among free nations is a primary goal of 	freedoms enemies. The concerted effort of free nations to promote democracy is a prelude to our enemies defeat. ",
	
	"Today, I also speak anew to my fellow citizens: ",
	
	"From all of you, I have asked patience in the hard task of securing America, which you have granted in good measure. Our country has accepted obligations that are difficult to 	fulfill, and would be dishonorable to abandon. Yet because we have acted in the great liberating tradition of this nation, tens of millions have achieved their freedom. And as 	hope kindles hope, millions more will find it. By our efforts, we have lit a fire as well —a fire in the minds of men. It warms those who feel its power, it burns those who fight 	its progress, and one day this untamed fire of freedom will reach the darkest corners of our world. ",
	
	"A few Americans have accepted the hardest duties in this cause —in the quiet work of intelligence and diplomacy ... the idealistic work of helping raise up free governments ... 	the dangerous and necessary work of fighting our enemies. Some have shown their devotion to our country in deaths that honored their whole lives —and we will always honor their 	names and their sacrifice.", 
	
	"All Americans have witnessed this idealism, and some for the first time. I ask our youngest citizens to believe the evidence of your eyes. You have seen duty and allegiance in 	the determined faces of our soldiers. You have seen that life is fragile, and evil is real, and courage triumphs. Make the choiceto serve in a cause larger than your wants, larger 	than yourself —and in your days you will add not just to the wealth of our country, but to its character. ",
	
	"America has need of idealism and courage, because we have essential work at home —the unfinished work of American freedom. In a world moving toward liberty, we are determined to 	show the meaning and promise of liberty. ",
	
	"In America's ideal of freedom, citizens find the dignity and security of economic independence, instead of laboring on the edge of subsistence. This is the broaderdefinition of 	liberty that motivated the Homestead Act, the Social Security Act, and the G.I. Bill of Rights. And now we will extend this vision by reforming great institutions to serve the 	needs of our time. To give every American a stake in the promise and future of our country, we will bring the highest standards to our schools, and build an ownership society. We 	will widen the ownership of homes and businesses, retirement savings and health insurance —preparing our people for the challenges of life in a free society. By making every 	citizen an agent of his or her own destiny, we will give our fellow Americans greater freedom from want and fear, and make our society more prosperous and just and equal. ",
	
	"In America's ideal of freedom, the public interest depends on private character —on integrity, and tolerance toward others, and the rule of conscience in our own lives.Self-	government relies, in the end, on the governing of the self. That edifice of character is built in families, supported by communities with standards, and sustained in our national 	life by the truths of Sinai, the Sermon on the Mount, the words of the Koran, and the varied faiths of our people. Americans move forward in every generationby reaffirming all 	that is good and true that came before —ideals of justice and conduct that are the same yesterday, today, and forever. ",
	
	"In America's ideal of freedom, the exercise of rights is ennobled by service, and mercy, and a heart for the weak. Liberty for all does not mean independence from one another. 	Our nation relies on men and women who look after a neighbor and surround the lost with love. Americans, at our best, value the life we see in one another, and mustalways remember 	that even the unwanted have worth. And our country must abandon all the habits of racism, because we cannot carry the message of freedom and the baggage of bigotry at the same 	time. ",
	
	"From the perspective of a single day, including this day of dedication, the issues and questions before our country are many. From the viewpoint of centuries,the questions that 	come to us are narrowed and few. Did our generation advance the cause of freedom? And did our character bring credit to that cause? ",
	
	"These questions that judge us also unite us, because Americans of every party and background, Americans by choice and by birth, are bound to one another in thecause of freedom. 	We have known divisions, which must be healed to move forward in great purposes —and I will strive in good faith to heal them.Yet those divisions do not define America. We felt 	the unity and fellowship of our nation when freedom came under attack, and our response camelike a single hand over a single heart. And we can feel that same unity and pride 	whenever America acts for good, and the victims of disaster are given hope, and the unjust encounter justice, and the captives are set free. ",
	
	"We go forward with complete confidence in the eventual triumph of freedom. Not because history runs on the wheels of inevitability; it is human choices that move events. Not 		because we consider ourselves a chosen nation; God moves and chooses as He wills. We have confidence because freedom is the permanenthope of mankind, the hunger in dark places, 	the longing of the soul. When our Founders declared a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful 	outrage under the banner Freedom Now they were acting on an ancient hope that is meant to be fulfilled. History has an ebb and flow of justice, but history also has a visible 	direction, set by liberty and the Author of Liberty. ",
	
	"When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration, a witness said, It rang as if it meant something.In our time it 	means something still. America, in this young century, proclaims liberty throughout all the world, and to all the inhabitants thereof. Renewed in our strength — tested, but not 	weary — we are ready for the greatest achievements in the history of freedom. ",
	
	"May God bless you, and may He watch over the United States of America. "]
	
	William_Mck=list()
	William_Mck=["WHEN we assembled here on the 4th of March, 1897, there was great anxiety with regard to our currency and credit. ",
	"None exists now. Then our Treasury receipts were inadequate to meet the current obligations of the Government. ",
        "Now they are sufficient for all public needs, and we have a surplus instead of a deficit. ",
	"Then I felt constrained to convene the Congress in extraordinary session to devise revenues to pay the ordinary expenses of the Government. ",
	"Now I have the satisfaction to announce that the Congress just closed has reduced taxation in the sum of $41,000,000. ",
        "Then there was deep solicitude because of the long depression in our manufacturing, mining, agricultural, and mercantile industries ",
        "and the consequent distress of our laboring population. ",
        "Now every avenue of production is crowded with activity, labor is well employed, and American products find good markets at home and abroad.",
        "Our diversified productions, however, are increasing in such unprecedented volume as to admonish us of the necessity ",
        "of still further enlarging our foreign markets by broader commercial relations. ",
        "For this purpose reciprocal trade arrangements with other nations should in liberal spirit be carefully cultivated and promoted. ",
        "The national verdict of 1896 has for the most part been executed. ",
        "Whatever remains unfulfilled is a continuing obligation resting with undiminished force upon the Executive and the Congress. ",
        "But fortunate as our condition is, its permanence can only be assured by sound business methods and strict economy in national administration and legislation. ",
        "We should not permit our great prosperity to lead us to reckless ventures in business or profligacy in public expenditures. ",
        "While the Congress determines the objects and the sum of appropriations, the officials of the executive departments are responsible ",
        "for honest and faithful disbursement, and it should be their constant care to avoid waste and extravagance. ",
        "Honesty, capacity, and industry are nowhere more indispensable than in public employment. ",
        "These should be fundamental requisites to original appointment and the surest guaranties against removal.", 

        "Four years ago we stood on the brink of war without the people knowing it and without any preparation or effort at preparation for the impending peril. ",
        "I did all that in honor could be done to avert the war, but without avail. ",
        "It became inevitable; and the Congress at its first regular session, without party division, provided money in anticipation of the crisis ",
        "and in preparation to meet it. It came. The result was signally favorable to American arms and in the highest degree honorable to the Government. ",
        "It imposed upon us obligations from which we cannot escape and from which it would be dishonorable to seek escape. ",
        "We are now at peace with the world, and it is my fervent prayer that if differences arise between us and other powers they may be settled by peaceful arbitration ",
        "and that hereafter we may be spared the horrors of war. ",
        "Intrusted by the people for a second time with the office of President, ",
        "I enter upon its administration appreciating the great responsibilities which attach to this renewed honor and commission, ",
        "promising unreserved devotion on my part to their faithful discharge and reverently invoking for my guidance the direction and favor of Almighty God.",
        "I should shrink from the duties this day assumed if I did not feel that in their performance I should have the co-operation of the wise ",
        "and patriotic men of all parties. ",
        "It encourages me for the great task which I now undertake to believe that those who voluntarily committed to me the trust imposed ",
        "upon the Chief Executive of the Republic will give to me generous support in my duties to preserve, protect, and defend, the Constitution of the United States" ,
        "and to care that the laws be faithfully executed. The national purpose is indicated through a national election. It is the constitutional method of ascertaining ",
        "the public will. When once it is registered it is a law to us all, and faithful observance should follow its decrees. ",

             
	"Strong hearts and helpful hands are needed, and, fortunately, we have them in every part of our beloved country. ",
        "We are reunited. Sectionalism has disappeared. Division on public questions can no longer be traced by the war maps of 1861. ",
        "These old differences less and less disturb the judgment. Existing problems demand the thought and quicken the conscience of the country, ",
        "and the responsibility for their presence, as well as for their righteous settlement, rests upon us all - no more upon me than upon you. ",
        "There are some national questions in the solution of which patriotism should exclude partisanship. ",
        "Magnifying their difficulties will not take them off our hands nor facilitate their adjustment. ",
        "Distrust of the capacity, integrity, and high purposes of the American people will not be an inspiring theme for future political contests. ",
        "Dark pictures and gloomy forebodings are worse than useless. These only becloud, they do not help to point the way of safety and honor. ",
        "Hope maketh not ashamed. The prophets of evil were not the builders of the Republic, nor in its crises since have they saved or served it. ",
        "The faith of the fathers was a mighty force in its creation, and the faith of their descendants has wrought its progress and furnished its defenders. ",
        "They are obstructionists who despair, and who would destroy confidence in the ability of our people to solve wisely and for civilization ",
        "the mighty problems resting upon them. The American people, intrenched in freedom at home, take their love for it with them wherever they go,",
        "and they reject as mistaken and unworthy the doctrine that we lose our own liberties by securing the enduring foundations of liberty to others.", 
        "Our institutions will not deteriorate by extension, and our sense of justice will not abate under tropic suns in distant seas. ",
        "As heretofore, so hereafter will the nation demonstrate its fitness to administer any new estate which events devolve upon it, ",
        "and in the fear of God will take occasion by the hand and make the bounds of freedom wider yet. If there are those among us who would make our way more difficult, ",
        "we must not be disheartened, but the more earnestly dedicate ourselves to the task upon which we have rightly entered. The path of progress is seldom smooth. ",
        "New things are often found hard to do. Our fathers found them so. We find them so. They are inconvenient. They cost us something.",
        "But are we not made better for the effort and sacrifice, and are not those we serve lifted up and blessed? ",
             
	"We will be consoled, too, with the fact that opposition has confronted every onward movement of the Republic from its opening hour until now,",
	"but without success. The Republic has marched on and on, and its step has exalted freedom and humanity. ",
	"We are undergoing the same ordeal as did our predecessors nearly a century ago",
	"We are following the course they blazed. They triumphed. ",
	"Will their successors falter and plead organic impotency in the nation? ",
	"Surely after 125 years of achievement for mankind we will not now surrender our equality with other powers on matters fundamental and essential to nationality. ",
	"With no such purpose was the nation created. In no such spirit has it developed its full and independent sovereignty. ",
	"We adhere to the principle of equality among ourselves, and by no act of ours will we assign to ourselves a subordinate rank in the family of nations. ",
	"My fellow-citizens, the public events of the past four years have gone into history. They are too near to justify recital. Some of them were unforeseen; ",
	"many of them momentous and far-reaching in their consequences to ourselves and our relations with the rest of the world. ",
	"The part which the United States bore so honorably in the thrilling scenes in China, while new to American life, ",
	"has been in harmony with its true spirit and best traditions, and in dealing with the results its policy will be that of moderation and fairness. ",
	
	"We face at this moment a most important question that of the future relations of the United States and Cuba. ",
	"With our near neighbors we must remain close friends. The declaration of the purposes of this Government in the resolution of April 20, 1898, ",
	"must be made good. Ever since the evacuation of the island by the army of Spain, the Executive, with all practicable speed, has been assisting ",
	"its people in the successive steps necessary to the establishment of a free and independent government prepared to assume and perform the obligations of ",
	"international law which now rest upon the United States under ",
	"the treaty of Paris. The convention elected by the people to frame a constitution is approaching the completion of its labors. ",
	"The transfer of American control to the new government is of such great importance, involving an obligation resulting from our intervention and the treaty of peace, ",
	"that I am glad to be advised by the recent act of Congress of the policy which the legislative branch of the Government deems essential ",
	"which the new government rests should be adapted to secure a government capable of performing the duties and discharging t",
	"he functions of a separate nation, of observing its international obligations of protecting life and property, insuring order, safety, and liberty,",
	"and conforming to the established and historical policy of the United States in its relation to Cuba. ",
	"The peace which we are pledged to leave to the Cuban people must carry with it the guaranties of permanence. ",
	"We became sponsors for the pacification of the island, and we remain accountable to the Cubans, no less than to our own country and people, ",
	"for the reconstruction of Cuba as a free commonwealth on abiding foundations of right, justice, liberty, and assured order. ",
	"Our enfranchisement of the people will not be completed until free Cuba shall be a reality, not a name; a perfect entity, ",
	"not a hasty experiment bearing within itself the elements of failure." ,
	
	"While the treaty of peace with Spain was ratified on the 6th of February, 1899, and ratifications were exchanged nearly two years ago, ",
	"the Congress has indicated no form of government for the Philippine Islands. It has, however, provided an army to enable the ",
	"Executive to suppress insurrection, restore peace, give security to the inhabitants, and establish the authority of the United States throughout the archipelago. ",
	"It has authorized the organization of native troops as auxiliary to the regular force. It has been advised from time to time of ",
	"the acts of the military and naval officers in the islands, of my action in appointing civil commissions, of the instructions ",
	"with which they were charged, of their duties and powers, of their recommendations, and of their several acts under executive commission, ",
	"together with the very complete general information they have submitted. These reports fully set forth the conditions, past and present, ",
	"in the islands, and the instructions clearly show the principles which will guide the Executive until the Congress shall, as it is required to do by the treaty, ",
	"determine the civil rights and political status of the native inhabitants.The Congress having added the sanction of ",
	"its authority to the powers already possessed and exercised by the Executive under the Constitution, thereby leaving with the ",
	"Executive the responsibility for the government of the Philippines, I shall continue the efforts already begun until order shall be restored throughout the islands, ",
	"and as fast as conditions permit will establish local governments, in the formation of which the full co-operation of the people has been already invited, ",
	"and when established will encourage the people to administer them. The settled purpose, long ago proclaimed, ",
	"to afford the inhabitants of the islands self-government as fast as they were ready for it will be pursued with earnestness and fidelity. ",
	"Already something has been accomplished in this direction. The Government's representatives, civil and military, ",
	"are doing faithful and noble work in their mission of emancipation and merit the approval and support of their countrymen. ",
	"The most liberal terms of amnesty have already been communicated to the insurgents, and the way is still open for those ",
	"who have raised their arms against the Government for honorable submission to its authority. Our countrymen should not be deceived. ",
	"We are not waging war against the inhabitants of the Philippine Islands. A portion of them are making war against the United States. ",
	"By far the greater part of the inhabitants recognize American sovereignty and welcome it as a guaranty of order and of security for life, property, ",
	"liberty, freedom of conscience, and the pursuit of happiness. To them full protection will be given. They shall not be abandoned. ",
	"We will not leave the destiny of the loyal millions the islands to the disloyal thousands who are in rebellion against the United States. ",
	"Order under civil institutions will come as soon as those who now break the peace shall keep it. ",
	"Force will not be needed or used when those who make war against us shall make it no more. May it end without further bloodshed, ",
	"and there be ushered in the reign of peace to be made permanent by a government of liberty under law! "]
	
	
	george10=set()
	Will10=set()
	goerge10=count10words(George_bush,23)
	Will10=count10words(William_Mck,20)
	print goerge10, Will10 

	compare2list(goerge10,Will10)

def main():
    lab11()

if __name__=="__main__": 
    main()    
