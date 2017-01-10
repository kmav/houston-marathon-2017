#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math
import sys
### mysql connection

#con = mdb.connect(host='localhost',user='bpeynetti',db='c9')
con = mdb.connect(host='bpeynetti-chicagomarathon2015-1689696', user='bpeynetti', db='c9')
cur = con.cursor(mdb.cursors.DictCursor)

#connections
currentTemp = 0

class Runner(object):
    def __init__(self,number,wave,corral,stdDev):
        self.id=number
        self.wave=wave
        self.corral = corral
        self.stdDev = stdDev 
        self.position = -1
        self.started = False
        self.finished = False

def getSpeed(runner):
    TEMP = float(currentTemp)
    DISTANCE = float(runner['position'])
    corral = runner['corral']
    speed = 0.0

    #first to go, awd
    if corral == 0:
        speed = 5.33
    #american development
    if corral == 2:
        corral = 1
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
    return 0.93*speed+runner['deviation']


    pass

def retrieveRunners(minute):

	pass

def getCorrectness(movement):
	
	x = 0
	for each in movement:
		x += math.fabs(each)
	
	return x
	pass

def GetDifferences(simulation,real):
	
	#we know, in simulation, what we have for each segment
	#we know, in real, how many people passed each 5k mark at any time
	
	# thus, we can simply 'pull back' or 'push forward' as needed 
	
	differences = [0]*len(simulation)
	for i in range(len(simulation)):
		differences[i] = real[i] - simulation[i]
		
	# now we know how many we have to change
	# if number is positive, then more people have passed this point than in the simulation
	# which means we're going slow, meaning we have to pull people from behind
	# if number is negative, then the simulation has more people ahead (going faster)
	# so we have to move the runners back (before they passed)
	
	return differences
	
	pass

def main():

	simulation = 0
	if simulation==0:
		#ask for temperature and minute of the race
		minute = int(sys.argv[1])
		# add = minute%4;
		# minute = minute + (4-add)
		# if minute%2==1:
		# 	minute +=1
			
		temperature = int(sys.argv[2])
		currentTemp = temperature
		
		realData = [0]*10
	
		print "----- starting -----"
		print "MINUTE: "+str(minute)
		print "TEMPERATURE: "+str(temperature)+" F"
		print "\n"
		print "---- input data ----"
	
		pp = raw_input("EXIT, PRESS 'q', CONTINUE, PRESS 'c' ")
		if (pp=='q'):
			return
	
		print "\n"
	
	
		realData = [0]*11
		realData[0] = int(input("Input number of runners started"))
		for i in range(1,9):
			realData[i] = int(input("Input cumulative number of runners (FULL MARATHON) at "+str(i*5)+"k"))
		realData[9] = int(input("input cumulative number of runners at 15K Half Marathon split"))
		realData[10] = int(input("Input number of runners finished"))
	
		#now verify information
		i=0
		print "\nINFORMATION VERIFICATION:"
		for number in realData:
			if (i==9):
				print "HALF! ",
			print "\t "+str(i)+"k - "+str(number)
			i+=1
	
	
		decision = raw_input("Correct? y/n")
		if (decision=="n"):
			return
		
		

	## now we need to know how many people are at each spot
	## and we also neeed to figure out the moving of people

	# we could load all the runners
	# create a 2d multidimenstional array of n runners
	# each array element has
		# runner id
		# runner position
		# runner corral
		# runner started
		# runner finished
		# runner startTime
		# runner deviation

	# that way we can sort a lot of things easily
		# get only the ones we need given on positions
		# get corral data
		# get other things

	sql = "SELECT * FROM MarathonRunners where dropout=0 and minute="+str(minute)
	print sql
	cur.execute(sql)

	rows = cur.fetchall()

	print "fetching from database ...   ",
	#now go row by row 
	RunnersArray = []
	
	j=0
	for row in rows:
		j+=1
		# print j,
		runner = {}
		runner['runnerId']	= int(row["runnerId"])
		runner['minute']	= int(row["minute"])
		runner['started'] 	= int(row["started"])
		runner['finished'] 	= int(row["finished"])
		runner['corral'] 	= int(row["corral"])
		runner['startTime'] = float(row["startTime"])
		runner['position']	= float(row["position"])
		#print runner['position']
		runner['deviation']	= float(row["deviation"])
		runner['half'] = float(row['half'])

		RunnersArray.append(runner)
		# print RunnersArray[-1]
	
	

	print "done"
	##now we need to calculate how's where

	realSegment = [0]*11
	#calculate the differences 
	for i in range(len(realSegment)-2):
		realSegment[i] = realData[i] - realData[i+1]
		realSegment[9] = ######################

	##now simulation data
	simData = [0]*11
	
	for r in RunnersArray:
		if r['finished']==1:
			simData[-1] += groupedNumber
		if r['started']==1:
			#simData[0]+=4
			pos = float(r['position'])
			if (r['half']==0):
				for i in range(9):
					if float(pos)>float(5.00*float(i)):
						simData[i]+=groupedNumber
			else:
				if float(pos)>0:
					simData[0]+=groupedNumber
				if float(pos)>5.00:
					simData[1]+=groupedNumber
				if float(pos)>10.00:
					simData[1]+=groupedNumber
				if float(pos)>15.00:
					simData[9]+=groupedNumber
				if float(pos)>20.00:
					simData[8]+=groupedNumber
					

	for i in range(len(realSegment)-2):
		print str(i*5)+"k :\t"+str(simData[i])+'\t'+str(realData[i])
	print "Half split: \t"+str(simData[9])+'\t'+str(realData[9])

	print "finished \t"+str(simData[-1])+'\t'+str(realData[-1])
	

	movements = GetDifferences(simData,realData)

	print movements

	# now, we need to re-order the data and move some front and back
	#sort by position
	# >>> sorted(student_objects, key=lambda student: student.age)   # sort by age

	RunnersSorted = sorted(RunnersArray, key=lambda runner: runner['position'], reverse=True) # sort by position
	
	
	########################################## MODIFIED ALGORITHM
	
	##modify speeds based on offset
	attempt = 0
	objective = getCorrectness(movements) 
	newobjective = objective-1
	while (newobjective < objective and attempt<7):
		print "Attempt: ",attempt
		attempt+=1
		
		#GET DATA FROM 10 MINUTES AGO
		sql = "SELECT * FROM MarathonRunners where dropout=0 and minute="+str(minute-10)
		print sql
		cur.execute(sql)
		rows = cur.fetchall()
		print "fetching from database ...   ",
		#now go row by row 
		RunnersArrayPast = []
		
		j=0
		for row in rows:
			j+=1
			# print j,
			runner = {}
			runner['runnerId']	= int(row["runnerId"])
			runner['minute']	= int(row["minute"])
			runner['started'] 	= int(row["started"])
			runner['finished'] 	= int(row["finished"])
			runner['corral'] 	= int(row["corral"])
			runner['startTime'] = float(row["startTime"])
			runner['position']	= float(row["position"])
			#print runner['position']
			runner['deviation']	= float(row["deviation"])
			runner['half'] = float(row['half'])
	
			RunnersArrayPast.append(runner)
		
		movementsSign = []
		for m in movements:
			if m>0:
				movementsSign.append(.1+attempt*.04)
			elif m==0:
				movementsSign.append(0)
			else:
				movementsSign.append(-.1-attempt*.04)
				
		print movementsSign;
		#increase/decrease the speed by 1%
		for r in RunnersArrayPast:
			runner = r
			if runner['started']==1 and runner['finished']==0:
				speed = getSpeed(runner)-runner['deviation']
				segment = int(runner['position']/5.00)
				#if it's on the second half of any but the last segment, modify as how it should be in the next segment
				if runner['position']%5.00>2.5:
					if runner['position']<35.00:
						speedChange = speed*movementsSign[segment+1]
				else:
					#if it's on the first half of the segment, move within the segment
					speedChange = speed*movementsSign[segment]
				runner['deviation'] += speedChange
		
		#and now we run it for 10 minutes
		for t in range(2,11,minuteInterval):
			#perform the 'moving of people'
			t2 = minute-10+t
			for i in range(len(RunnersArrayPast)):
				runner = RunnersArrayPast[i]
				if runner['started']==0:
					if runner['startTime'] < t2:
						RunnersArrayPast[i]['started'] = 1
						RunnersArrayPast[i]['position'] = 0.00
			print "changing positions"
			for i in range(len(RunnersArrayPast)):
				#print i,
				runner = RunnersArrayPast[i]
				if (runner['started']==1 and runner['finished']==0):
					position = runner['position']
					speedKmPerMin = float(getSpeed(runner)) * 1.609/60
					position = position + speedKmPerMin*(float(minuteInterval))
					if position>42.2:
						position = 42.2
						RunnersSorted[i]['finished'] = 1
					RunnersArrayPast[i]['position'] = position
				
			
		simData2 = [0]*10
		
		for r in RunnersArrayPast:
			if r['finished']==1:
				simData2[-1] += groupedNumber
			if r['started']==1:
				#simData[0]+=4
				pos = float(r['position'])
				for i in range(9):
					if float(pos)>float(5.00*float(i)):
						simData2[i]+=groupedNumber

		
		movements2 = GetDifferences(simData2,realData)
		print movements2;
		newobjective = getCorrectness(movements2) 

	
	
	
	
	
	###################################################################
	
	# minute=60 --> 41418	17809	8857	552	14	0	0	0	0	0	60
	# minue=90  --> 41418	37593	18648	10563	2118	147	11	0	0	0	90
	# minute=130 --> 41418	41303	38184	31601	14161	6121	1466	160	25	6	130
	#minute = 170-> 41418	41303	41232	38515	27109	16529	9894	3745	1034	453	170
	
	
	#now we have to move them to a given point, or change their speed

	# if number is positive, then more people have passed this point than in the simulation
	# which means we're going slow, meaning we have to pull people from behind
	# if number is negative, then the simulation has more people ahead (going faster)
	# so we have to move the runners back (before they passed)
	simData1 = simData
	
	for s in range(9):
		#movements = GetDifferences(simData2,realData)
		print movements
		print "Changing segment",s
		# if s=0, number of people past km 0 (started)
		difference = movements[s]/groupedNumber
		moved = []
		if difference>0:
			# push people to go faster (fwd) so pull from behind
			behind = [x for x in RunnersSorted if (x['position']<5.00*s)]
			
			# we can only move those we still have
			moving = min(difference,len(behind))
			
			#already sorted decreasing in theory
			for i in range(moving):
				behind[i]['position'] = (s+1)*5.00
				moved.append(behind[i])
				
		if difference<0:
			print "Pushing"+str(difference)+" people back"
			#push people back (slower) so push back from this segment to start of segment
			ahead = [x for x in RunnersSorted if (x['position']>(s*5.00)) ]
			
			#we can only move those that we have
			moving = min(difference,len(ahead))
			print "Can move: ",moving
			moving = -1*moving
			
			ahead_sorted = sorted(ahead, key=lambda runner: runner['position']) #sort increasing
			
			for i in range(moving):
				#move those to the beginning
				ahead_sorted[i]['position'] = s*5.00-.001
				moved.append(ahead_sorted[i])
				#print moved[-1]['position']
		
		#now we need to replace them in the real RunnersSorted array
		k=-1
		print "\t\t Input into real array"
		for each in RunnersSorted:
			k+=1
			for m in moved:
				if each['runnerId']==m['runnerId']:
					RunnersSorted[k]['position'] = m['position']
					if float(RunnersSorted[k]['position'])>0.00:
						RunnersSorted[k]['started']=1
					else:
						RunnersSorted[k]['started']=0
					
		simData2 = [0]*10
		
		for r in RunnersSorted:
			if r['finished']==1:
				simData2[-1] += groupedNumber
			if r['started']==1:
				if r['position']>42.2 and r['finished']==0:
					r['finished'] = 1
					simData2[-1] += groupedNumber
				pos = float(r['position'])
				# file.write(str(pos)+'\n')
				for i in range(9):
					if float(pos)>float(5.00*float(i)):
						simData2[i]+=groupedNumber

	for i in range(len(realSegment)-1):
		print str(i*5)+"k :\t"+str(simData2[i])+'\t'+str(realData[i])

	print "finished \t"+str(simData2[-1])+'\t'+str(realData[-1])

####### now to plot mile segment data

	mileData = [0]*27
	for r in RunnersArray:
			if r['finished']==1:
				mileData[-1] += groupedNumber
			if r['started']==1:
				if r['position']>42.2 and r['finished']==0:
					r['finished'] = 1
					mileData[-1] += groupedNumber
				pos = float(r['position'])
				# file.write(str(pos)+'\n')
				for i in range(27):
					if float(pos)>float(1.609*float(i)):
						mileData[i]+=groupedNumber
	
	inMile = [0]*27
	for i in range(26):
		inMile[i] = mileData[i] - mileData[i+1]
		
	print inMile
	
	## NOW WE NEED TO CHANGE THESE PEOPLE'S POSITIONS FOR THE NEXT 30 MINUTES
	for t in range(2,21,minuteInterval):
		#perform the 'moving of people'
		currentTime = minute+t
		sql = ""
		print "Updating minute"+str(currentTime)

		
		for i in range(len(RunnersSorted)):
			runner = RunnersSorted[i]
			if runner['started']==0:
				if runner['startTime'] < currentTime:
					RunnersSorted[i]['started'] = 1
					RunnersSorted[i]['position'] = 0.00
		print "changing positions"
		for i in range(len(RunnersSorted)):
			#print i,
			runner = RunnersSorted[i]
			if (runner['started']==1 and runner['finished']==0):
				position = runner['position']
				speedKmPerMin = float(getSpeed(runner)) * 1.609/60
				position = position + speedKmPerMin*(float(minuteInterval))
				if position>42.2:
					position = 42.2
					RunnersSorted[i]['finished'] = 1
				RunnersSorted[i]['position'] = position
				
				started = RunnersSorted[i]['started']
				finished = RunnersSorted[i]['finished']
				position = RunnersSorted[i]['position']
				runnerId = RunnersSorted[i]['runnerId']
				sql = "UPDATE MarathonRunners SET started="+str(started)+", finished="+str(finished)+", position="+str(position)+" where runnerId="+str(runnerId)+" and minute="+str(currentTime)+" ; \n"
				#print sql
				cur.execute(sql)
				con.commit()
			
		
	# file = open("sqlUpdate.sql",'q)
	# file.write(sql)
	pass

groupedNumber = 40
minuteInterval = 2

if __name__=='__main__':
	main()
	
	
# minute=50
# INFORMATION VERIFICATION:
#          0k - 34396
#          1k - 15580
#          2k - 3728
#          3k - 60
#          4k - 0
#          5k - 0
#          6k - 0
#          7k - 0
#          8k - 0
#          9k - 0