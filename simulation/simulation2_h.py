#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math
import sys
### mysql connection

#con = mdb.connect(host='localhost',user='bpeynetti',db='c9')
con = mdb.connect(host='localhost', user='rachellin23', db='houston2016')
cur = con.cursor(mdb.cursors.DictCursor)

#connections
currentTemp = 0

class Runner(object):
    def __init__(self,number,corral,stdDev):
        self.id=number
        # self.wave=wave
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
    if corral == 3:
        speed = 5.53263038 + (-0.02222242746)*DISTANCE
    

    return speed+runner['deviation']



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
	
	
		realData = [0]*10
		realData[0] = int(input("Input number of runners started"))
		for i in range(1,9):
			realData[i] = int(input("Input cumulative number of runners at "+str(i*5)+"k"))
		realData[9] = int(input("Input number of runners finished"))
	
		#now verify information
		i=0
		print "\nINFORMATION VERIFICATION:"
		for number in realData:
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

	sql = "SELECT * FROM MarathonRunners where dropout=0 and half=1 and minute="+str(minute)
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

		RunnersArray.append(runner)
		# print RunnersArray[-1]
	
	

	print "done"
	##now we need to calculate how's where

	realSegment = [0]*10
	#calculate the differences 
	for i in range(len(realSegment)-1):
		realSegment[i] = realData[i] - realData[i+1]

	##now simulation data
	simData = [0]*10
	
	for r in RunnersArray:
		if r['finished']==1:
			simData[-1] += groupedNumber
		if r['started']==1:
			#simData[0]+=4
			pos = float(r['position'])
			for i in range(9):
				if float(pos)>float(5.00*float(i)):
					simData[i]+=groupedNumber

	for i in range(len(realSegment)-1):
		print str(i*5)+"k :\t"+str(simData[i])+'\t'+str(realData[i])

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
		sql = "SELECT * FROM MarathonRunners where dropout=0 and half=1 and minute="+str(minute-10)
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
					if position>21.1:
						position = 21.1
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
				if r['position']>21.1 and r['finished']==0:
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
				if r['position']>21.1 and r['finished']==0:
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
				if position>21.1:
					position = 21.1
					RunnersSorted[i]['finished'] = 1
				RunnersSorted[i]['position'] = position
				
				started = RunnersSorted[i]['started']
				finished = RunnersSorted[i]['finished']
				position = RunnersSorted[i]['position']
				runnerId = RunnersSorted[i]['runnerId']
				sql = "UPDATE MarathonRunners SET started="+str(started)+", finished="+str(finished)+", position="+str(position)+" where half=1 and runnerId="+str(runnerId)+" and minute="+str(currentTime)+" ; \n"
				#print sql
				cur.execute(sql)
				con.commit()
			
		
	# file = open("sqlUpdate.sql",'q)
	# file.write(sql)
	pass

groupedNumber = 10
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