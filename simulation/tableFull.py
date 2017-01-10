#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math

# dropoutPerHalfHour = [0,0,0,1,5,4,3,5,3,2,4,2,1,0,0,0,0]
# droputDone = [0]*len(dropoutPerHalfHour)


class Runner(object):
    def __init__(self,number,corral,stdDev):
        self.id=number
        # self.wave=wave
        self.corral = corral
        self.stdDev = stdDev 
        self.position = -1
        self.started = False
        self.finished = False
        # self.dropout = 0
        
        
def getSpeed(runner):
    
    
    TEMP = float(currentTemp)
    DISTANCE = float(runner.position)
    corral = runner.corral 
    speed = 0.0

    if corral==0:
        speedpct = 1.03796 - 0.00214642*DISTANCE



    #first to go, awd
    if corral == 0:
        speed = 5.33
    #american development
    if corral == 2:
        #corral = 1
        speed = 9.55

    #elites
    if corral== 1 : 
        if DISTANCE<10: 
                speed = (9.64419873876+(-0.000931700630522)*TEMP) + (0.0249328163757 + (-0.000256469719805)* TEMP ) * DISTANCE 
        if DISTANCE>=10: 
                speed =  (9.83017994657+(0.00489768256501)*TEMP) + (0.00444863374136 + (-0.000604232629418)* TEMP ) * DISTANCE 
    #a
    if corral== 3 : 
            if DISTANCE<10: 
                    speed = (8.63220503083+(-0.00382457306738)*TEMP) + (0.0193243058485 + (-6.82844351124e-05)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (8.68436001534+(0.00660202442628)*TEMP) + (0.00916185756893 + (-0.000766755226609)* TEMP ) * DISTANCE 

    if corral== 4 : 
            if DISTANCE<10: 
                    speed = (7.98493369699+(-0.00453265898854)*TEMP) + (0.0267840268359 + (-0.000131032547266)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (8.19300906124+(0.00444016642186)*TEMP) + (0.00491892840694 + (-0.000745671376061)* TEMP ) * DISTANCE 
    if corral== 5 : 
            if DISTANCE<10: 
                    speed = (7.52058024011+(-0.00480665269828)*TEMP) + (0.0279470019205 + (-0.000158780053557)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (7.76181966951+(0.00412169288934)*TEMP) + (0.00337916243936 + (-0.000764865156778)* TEMP ) * DISTANCE 
    if corral== 6 : 
            if DISTANCE<10: 
                    speed = (7.17481729795+(-0.00438339369739)*TEMP) + (0.0254197458153 + (-0.000107657154661)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (7.37919414097+(0.00544428219455)*TEMP) + (0.00640028541955 + (-0.000838846452681)* TEMP ) * DISTANCE 
    if corral== 7 : 
            if DISTANCE<10: 
                    speed = (6.93550624774+(-0.00374942346129)*TEMP) + (0.0308542405954 + (-0.000210439989279)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (7.11186613731+(0.00695459217648)*TEMP) + (0.0109394824862 + (-0.000946642791164)* TEMP ) * DISTANCE 
    if corral== 8 : 
            if DISTANCE<10: 
                    speed = (6.73753769292+(-0.00393604373944)*TEMP) + (0.0354416751432 + (-0.00032493723748)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (7.14188096529+(0.00326161798086)*TEMP) + (-0.00028552029072 + (-0.000809021936703)* TEMP ) * DISTANCE 
    if corral== 9 : 
            if DISTANCE<10: 
                    speed = (6.33105080709+(-0.00338678012864)*TEMP) + (0.0257720634635 + (-0.000372695303258)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (6.91431918238+(-0.00108374220717)*TEMP) + (-0.0131216390398 + (-0.000597959197359)* TEMP ) * DISTANCE 
    if corral== 10 : 
            if DISTANCE<10: 
                    speed = (6.00623980025+(-0.00283603398457)*TEMP) + (0.0128652191841 + (-0.000425523726021)* TEMP ) * DISTANCE 
            if DISTANCE>=10: 
                    speed =  (6.5386297425+(-0.00233551710924)*TEMP) + (-0.0176116607083 + (-0.000520283204613)* TEMP ) * DISTANCE 
    if corral== 11 : 
            if DISTANCE<10: 
                    speed = (5.93291719084+(-0.00322367137615)*TEMP) + (0.000500343064203 + (-0.000389975526887)* TEMP ) * DISTANCE 
            if DISTANCE>=10:
                    speed =  (6.5121368141+(-0.00486876666938)*TEMP) + (-0.0226966469797 + (-0.000444260057232)* TEMP ) * DISTANCE 
    if corral== 12 : 
            if DISTANCE<10: 
                    speed = (5.73527217176+(-0.00461414224181)*TEMP) + (-0.0130848767638 + (-0.000499228830686)* TEMP ) * DISTANCE 
            if DISTANCE>=10:
                    speed =  (6.25493721077+(-0.00977631228215)*TEMP) + (-0.0301529659912 + (-0.000266797577107)* TEMP ) * DISTANCE 
    
    return 0.85*speed+runner.stdDev




def GenerateRunners(number_runners):

    #generate runners
    Runners = {}
    # we need to extract data from file 
    corralData = open('percentages.txt','r')
    
    line_array = []
    percentage = {}
    stdDev = {}
    startTime = {}
    startInterval = {}
    corral = {}
    startDelay = {}
    i=0
    for line in corralData:
        lines = line.strip()
        lines = lines.split(',')
        line_array.append(lines)
    data = line_array[1:]
    
    for each in data:
        corral[i] = each[0]
        percentage[i] = float(each[1])
        stdDev[i] = float(each[2])
        startTime[i] = float(each[3])
        startInterval[i] = float(each[4])
        i+=1
    
    corralCum = [0]*5
    corralCum[0]=1
    corralCum[1]=1
    print "Number:",number_runners
    for i in range(number_runners):
        randNum = random.random()
        #print randNum
        corralNum = 0
        pct = 0
        #print percentage[corralNum]
        while (float(percentage[corralNum]) < float(randNum) and corralNum<5):
            #decide which one to put by looping on increasing number of corrals
            corralNum+=1
            #print corralNum,
        corralCum[corralNum]+=1

        
        runnerStdDev = random.gauss(0,stdDev[corralNum])
        runner = Runner(i,corralNum,runnerStdDev)
        
        Runners[i]=(runner)
    
    
    # corral numbers
    print corralCum
        #now give them start times
    for j in range(len(startTime)):
        startDelay[j] = float(startInterval[j])/float(corralCum[j])
    
    #here, we would assign starting times to the fastest first and then the slow people
    
    #now assign to each of the runners a time
    corralNumDone = [0]*5
    for i in range(number_runners):
        runner = Runners[i]
        corral = runner.corral
        Runners[i].startTime = startTime[corral] + startDelay[corral]*corralNumDone[corral]
        #print Runners[i].startTime
        corralNumDone[corral]+=1

    return Runners
    
def main():

    # con = mdb.connect(host='bpeynetti-chicagomarathon2015-1689696',user='bpeynetti',db='c9')
    # cur = con.cursor()

    # with con:

    #     sql = "Delete from MarathonRunners;"
    #     print "Deleting current table"
    #     cur.execute(sql);
    #     number_runners = int(input("How many runners do we have?"))/ratio_grouped
    #     currentTemp = int(input("What's the predicted temperature? use integers"))
    if (1==1):
        print number_runners

        Runners = GenerateRunners(number_runners)
        
        print len(Runners)
        
        runnersSegment = {}
        startedMin = {}
        finishedMin = {}
        
        #### now let them run the entire marathon
        operations = 0
        minute = -24
        onCourse=0
        totalDropped = 0
        while (minute<500):
            print "total dropped:",totalDropped
            drop=0
            Halfhour = int(minute/30)
            print "hfhour:",Halfhour
            if droputDone[Halfhour]<dropoutPerHalfHour[Halfhour]:
                if (random.random()>0.5):
                    drop = 1
                    selectedDropout = int(float(random.random())*float(number_runners))
            
            if drop==1:
                totalDropped+=1
                droputDone[Halfhour]+=1
                Runners[selectedDropout].dropout = 1
            
            
            minute +=minuteInterval
            print minute,'\t',"On course",onCourse

            started = 0
            for key in Runners:
                runner = Runners[key]
                if (runner.started==False):
                    if runner.startTime < minute:
                        Runners[key].started=True
                        Runners[key].position = 0.00
                        started+=1
            print "started:",started
            
          
            onCourse = 0
            positions = []
            for key in Runners:
                runner = Runners[key]
                if (runner.started==True and runner.finished==False):
                    position = runner.position
                    speedKmPerMin = float(getSpeed(runner)) * 1.609 / 60.0
                    position = runner.position + speedKmPerMin*float(minuteInterval)
                    if position>42.2:
                        position = 42.2
                        Runners[key].finished = True
                   
                    Runners[key].position = position
                    runner.position = position
                    positions.append(position)
                    onCourse+=1

                #now put the sql code for that runner
                if runner.started==True:
                    start=1
                else:
                    start=0
                if runner.finished==True:
                    finish=1
                else:
                    finish=0
                # sql = "INSERT into MarathonRunners (runnerId,minute,started,finished,corral,startTime,position,deviation,dropout) VALUES ("+str(runner.id)+','+str(minute)+','+str(start)+','+str(finish)+','+str(runner.corral)+','+str(runner.startTime)+','+str(runner.position)+','+str(runner.stdDev)+','+str(runner.dropout)+");"
                # print sql
                # cur.execute(sql)
                operations+=1
            # con.commit()
            
            
            #now store the number of runners at each mile for the entire 500 minutes
            mileData = [0]*27
            started = 0
            finished = 0
            
            for key in Runners:
                runner = Runners[key]
                if runner.finished==True:
                    mileData[-1] += ratio_grouped
                    finished +=1
                if runner.started==True:
                    started +=1
                    if runner.position>42.2 and runner.finished==False:
                        runner.finished = True
                        mileData[-1] += ratio_grouped
                    pos = float(runner.position)
                    # file.write(str(pos)+'\n')
                    for i in range(27):
                        if float(pos)>float(1.609*float(i)):
                            mileData[i]+=ratio_grouped
            
            inMile = [0]*27
            for i in range(26):
                inMile[i] = mileData[i] - mileData[i+1]
                
            print inMile
                    
            runnersSegment[minute] = inMile
            startedMin[minute] = started
            finishedMin[minute] = finished

        print "operations: ",operations
    
    # file = open('../data/Densities.csv','w')

    # file.write("raceMinute,started,atMile0,atMile1,atMile2,atMile3,atMile4,atMile5,atMile6,atMile7,atMile8,atMile9,atMile10,atMile11,atMile12,atMile13,atMile14,atMile15,atMile16,atMile17,atMile18,atMile19,atMile20,atMile21,atMile22,atMile23,atMile24,atMile25,atMile26,finished\n")
    # for minute in range(0,500,minuteInterval):
        # txt = str(minute)+","+str(startedMin[minute])
        # for mile in range(27):
        #     txt += ","+str(runnersSegment[minute][mile])
        # txt += ","+str(finishedMin[minute])+'\n'
        # file.write(txt)

    # print totalDropped
        

ratio_grouped = 40
minuteInterval = 2
currentTemp = 60
if __name__=='__main__':
    main();
    
#groups of 20, 1 minute interval: 1:36.74 (1,084,680 operations)