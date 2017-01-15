#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math
import calcDrops

dropoutPerHalfHour = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
droputDone = [0]*len(dropoutPerHalfHour)


class Runner(object):
    def __init__(self,number,corral,deviation):
        self.id=number
        self.corral = corral
        self.deviation = deviation 
        self.position = -1
        self.started = False
        self.finished = False
        self.dropout = 0
        
    # change this to def __str__(self):
    def printMe(self):
        print "Runner: ",self.id," Corral: ",self.corral," Pos: ",self.position
        
        
def getSpeed(runner):
    
    
    TEMP = float(currentTemp)
    DISTANCE = float(runner.position)
    corral = runner.corral 
    speed = 0.0

    # speed = ax + b
    # speed = (slope)*distance_travelled + initial_speed
    
    #CORRAL A
    if corral == 0:
        speed = 7.410739129 + (-0.02280316304)*DISTANCE
    #CORRAL B
    if corral == 1:
        speed = 6.720575488 + (-0.02714138849)*DISTANCE
    #CORRAL C
    if corral == 2:
        speed = 6.05103729 + (-0.02377687221)*DISTANCE
    #CORRAL D
    if corral == 3 or corral == 4:
        speed = 5.53263038 + (-0.02222242746)*DISTANCE
    i
    # add on the individual runner speed deviation
    return speed+runner.deviation




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
        while (float(percentage[corralNum]) < float(randNum) and corralNum<6):
            #decide which one to put by looping on increasing number of corrals
            corralNum+=1
            print corralNum,
        # keeps track of how many runners are in each corral
        corralCum[corralNum]+=1
        
        # set the wave (if they have one)
        if corralNum>7:
            wave=2
        else:
            wave=1
        
        runnerStdDev = random.gauss(0,stdDev[corralNum])
        # you could also do runnerSpeed = random.gauss(speed_avg(distance)[corral],stdDev[corral])
        runner = Runner(i,corralNum,runnerStdDev)
        
        Runners[i]=(runner)
    
    
    # corral numbers
    print corralCum
    #now give them start times
    for j in range(len(startTime)):
        # the time between each runner to start = the total time for the corral to start  / number of runners in the corral
        startDelay[j] = float(startInterval[j])/float(corralCum[j])
    
    #here, we would assign starting times to the fastest first and then the slow people
    #now assign to each of the runners a time
    corralNumDone = [0]*5
    for i in range(number_runners):
        runner = Runners[i]
        corral = runner.corral
        Runners[i].startTime = startTime[corral] + startDelay[corral]*corralNumDone[corral]
        #print Runners[i].startTime
        # keep track of how many you assigned for each corral
        corralNumDone[corral]+=1

    return Runners
    
def main():

    # establish connection to database
    con = mdb.connect(host='localhost',user='rachellin23',db='houston2016')
    # set a cursor (what you execute)
    cur = con.cursor()

    # with con:
    if (1==1):
        sql = "Delete from MarathonRunners where half=0;"
        print "Deleting current Full Marathon table"
        # this actually executes the command in the database 
        cur.execute(sql);
        # number of runners = real # of runners / ratio_grouped 
        number_runners = int(input("How many FULL MARATHON runners do we have?"))/ratio_grouped
        currentTemp = int(input("What's the predicted temperature? use integers"))
         
        print number_runners

        # returns an array of all the runner objects 
        Runners = GenerateRunners(number_runners)
        
        # check 
        print len(Runners)
        
        # dictionaries to store information as the race goes on 
        runnersSegment = {}
        startedMin = {}
        finishedMin = {}
        runnersDrops = {}
        
        # ====== 2017 Drops Pred - start ====== 
        # load in drop ratios
        dropPct_table = calcDrops.load_drops()
            
        # load starting numbers for each corral
        start_table = calcDrops.load_starts()
            
        # load in average time by corral and event
        times_table = calcDrops.load_times()
        
        # calculate number of drops from ratios and starting numbers
        dropCt_table = calcDrops.calc_drops(dropPct_table, start_table)
        # ====== 2017 Drops Pred - end ====== 
        
        #### now let them run the entire marathon
        # operations keeps track of total operations in database (debugging)
        operations = 0
        # start before anyone begins (WHEELCHAIR STARTS AT -10)
        minute = -24
        # variables to keep track of race 
        onCourse=0
        totalDropped = 0
        
        # loop through the race until you get to 500 minutes after start time  (8.3 hours)
        while (minute<500):
            # print "total dropped:",totalDropped
            drop=0
            # figure out what half hour we're in 
            Halfhour = int(minute/30)
            # print "hfhour:",Halfhour
            
            # sets dropouts - NOT USED 
            # if droputDone[Halfhour]<dropoutPerHalfHour[Halfhour]:
            #     if (random.random()>0.5):
            #         drop = 1
            #         selectedDropout = int(float(random.random())*float(number_runners))
            
            # if drop==1:
            #     totalDropped+=1
            #     droputDone[Halfhour]+=1
            #     Runners[selectedDropout].dropout = 1
            
            # ====== 2017 Drops Pred - start ====== 

            # calculate current drops based upon current minute and average corral pace
            totalDrops = calcDrops.sumDrops(times_table, dropCt_table, minute)

            # ====== 2017 Drops Pred - end ====== 

            
            # step through the race 
            minute +=minuteInterval
            
            # initialize to keep track of how many new runners started at this time interval
            started = 0
            # Runners is a dictionary, step through all of them
            for key in Runners:
                # get the runner object
                runner = Runners[key]
                # if it hasn't started, and it should start, make it start 
                print runner.started
                if (runner.started==False):
                    if runner.startTime < minute:
                        Runners[key].started=True
                        Runners[key].position = 0.00
                        started+=ratio_grouped
            
            # debugging 
            print "Time: ",minute/60,':',minute%60,'\t',"On course",onCourse,
            print "started:",started
            
            # drops debugging
            print "Drops: ",totalDrops,'\n'
          
            onCourse = 0
            positions = []
            # loop through the runners again 
            for key in Runners:
                runner = Runners[key]
                # if runner is still running, then move the runner forward by <minuteInterval> minutes
                if (runner.started==True and runner.finished==False):
                    position = runner.position
                    # get the runner speed and convert to km per minute
                    speedKmPerMin = float(getSpeed(runner)) * 1.609 / 60.0
                    # move it forward 
                    position = runner.position + speedKmPerMin*float(minuteInterval)
                    
                    # check if they finished and set finished to True if they did 
                    if position>42.2:
                        position = 42.2
                        Runners[key].finished = True
                    
                    # store it back in the Runner dictionary
                    Runners[key].position = position
                    # you actually don't need ( I think)
                    runner.position = position
                    # keep track of all the positions in the race 
                    positions.append(position)
                    onCourse+=ratio_grouped

                #now put the sql code for that runner
                if runner.started==True:
                    start=1
                else:
                    start=0
                if runner.finished==True:
                    finish=1
                else:
                    finish=0
                # insert a new row into the runner table 
                sql = "INSERT into MarathonRunners (runnerId,minute,started,finished,corral,startTime,position,deviation,dropout,half) VALUES ("+str(runner.id)+','+str(minute)+','+str(start)+','+str(finish)+','+str(runner.corral)+','+str(runner.startTime)+','+str(runner.position)+','+str(runner.deviation)+','+str(runner.dropout)+",0);"
                # print sql
                cur.execute(sql)
                # just to keep track, not needed 
                operations+=1
            
            # commit the operations 
            con.commit()
            
            # NOW FIGURE OUT DENSITY 
            
            #now store the number of runners at each mile for the entire 500 minutes
            # array MileData will have the runner density for the given minute 
            mileData = [0]*27
            started = 0
            finished = 0
            
            # loop through the runners 
            for key in Runners:
                runner = Runners[key]
                # if runner finished 
                if runner.finished==True:
                    # add it to the end of the array 
                    mileData[-1] += ratio_grouped
                    finished +=1
                if runner.started==True:
                    # add one to cumulative number of runners that started by that minute 
                    started +=1
                    # extra check for finishers  (PROBABLY NEVER GETS EXECUTED )
                    if runner.position>42.2 and runner.finished==False:
                        runner.finished = True
                        mileData[-1] += ratio_grouped
                        
                    # otherwise, put them in the corresponding 
                    pos = float(runner.position)
                    # file.write(str(pos)+'\n')
                    # for each mile 
                    for i in range(27):
                        # if they have passed that mile 
                        if float(pos)>float(1.609*float(i)):
                            # add one 
                            mileData[i]+=ratio_grouped
            
            # get the number of people inside a mile, put it in inMile array 
            inMile = [0]*27
            for i in range(26):
                inMile[i] = mileData[i] - mileData[i+1]
                
            print inMile
                    
            # runnersSegment is a dictionary (or an array) of arrays
            # it holds as many elements as time intervals, and each element holds the list 
            # of people in each mile at that time 
            runnersSegment[minute] = inMile
            startedMin[minute] = started
            finishedMin[minute] = finished
            runnersDrops[minute] = totalDrops

        print "operations: ",operations
    
    file = open('DensitiesFull.csv','w')

    file.write("raceMinute,started,atMile0,atMile1,atMile2,atMile3,atMile4,atMile5,atMile6,atMile7,atMile8,atMile9,atMile10,atMile11,atMile12,atMile13,atMile14,atMile15,atMile16,atMile17,atMile18,atMile19,atMile20,atMile21,atMile22,atMile23,atMile24,atMile25,atMile26,finished,drops\n")
    for minute in range(0,500,minuteInterval):
        txt = str(minute)+","+str(startedMin[minute])
        for mile in range(27):
            txt += ","+str(runnersSegment[minute][mile])
        txt += ","+str(finishedMin[minute])
        txt += ","+str(runnersDrops[minute])+'\n'
        file.write(txt)

    print totalDropped
        

ratio_grouped = 10
minuteInterval = 2
currentTemp = 60
if __name__=='__main__':
    main();
    
#groups of 20, 1 minute interval: 1:36.74 (1,084,680 operations)