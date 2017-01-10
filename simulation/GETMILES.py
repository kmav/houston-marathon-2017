#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math
import sys
### mysql connection

groupedNumber = 10
minuteInterval=2
con = mdb.connect(host='localhost',user='rachellin23',db='houston2016')
cur = con.cursor(mdb.cursors.DictCursor)



class Runner(object):
    def __init__(self,number,wave,corral,stdDev):
        self.id=number
        self.corral = corral
        self.stdDev = stdDev 
        self.position = -1
        self.started = False
        self.finished = False

txt = "raceMinute,started,atMile0,atMile1,atMile2,atMile3,atMile4,atMile5,atMile6,atMile7,atMile8,atMile9,atMile10,atMile11,atMile12,atMile13,atMile14,atMile15,atMile16,atMile17,atMile18,atMile19,atMile20,atMile21,atMile22,atMile23,atMile24,atMile25,atMile26,atMile28,atMile29,atMile30,finished\n"
altTxt = "Mile,Minute,Runners,Half\n"
altTxtH = "Mile,Minute,Runners\n"

for minute in range(0,501,minuteInterval):
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
		runner['half'] = int(row["half"])
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
	##now we need to calculate who's where
	
	# Segment[i] = realData[i] - realData[i+1]

	##now simulation data
	simData = [0]*30
	started = 0
	finished = 0
	
	# file = open('outPositions.csv','w')
	halfData = [0]*27
	for r in RunnersArray:
		if r['finished']==1:
			finished += groupedNumber
			started += groupedNumber
		elif r['started']==1:
			started += groupedNumber
			#simData[0]+=4
			pos = float(r['position'])
			# file.write(str(pos)+'\n')
			mile = int(float(pos) / 1.609)
			# if (r['half']==1) and mile>8:
				# print "I'm half, position is ",float(pos)/1.609,"th mile (floored) -> " ,
				
			if (r['half']==1):
				#put in halfData array
				if mile<8:
					halfData[mile] += groupedNumber;
				if mile>10:
					halfData[mile + 13] += groupedNumber;
			
			if (r['half'])==1 and (mile>7 and mile<11):
				simData[mile+19] += groupedNumber
				# print mile,"h, (atMile",mile+19,")"
			elif (r['half'])==1 and (mile>10):
				# print "my position is ",float(pos)/1.609,"so I go to mile ",mile+13
				simData[mile+13] += groupedNumber
				# print "atMile",mile+13
				if (mile==13):
					print "*****************************************************************************************************************************************"
			else:
				simData[mile] += groupedNumber
	print simData
	txt +=  str(minute)+','+str(started)
	for each in simData:
		txt+= ','+str(each)
	txt += ','+str(finished)
	txt+='\n'
	
	for i in range(26):
		altTxt += str(i)+','+str(minute)+','+str(simData[i])+','+str(halfData[i])+'\n'
		
	for j in range(27,30):
		altTxtH += str(j-19)+'H,'+str(minute)+','+str(simData[j])+'\n'
	
		
file = open("../data/Densities.csv",'w')
file2 = open("../data/RunnerData.csv",'w')	
file3 = open("../data/RunnerDataHalf.csv","w")
file.write(txt)
file2.write(altTxt)
file3.write(altTxtH)
