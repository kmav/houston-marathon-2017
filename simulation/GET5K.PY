#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import random
import math
import sys
### mysql connection

groupedNumber = 40
minuteInterval = 2
con = mdb.connect(host='localhost',user='rachellin23',db='houston2016')
cur = con.cursor(mdb.cursors.DictCursor)

file = open("simulation_results.csv",'w');


class Runner(object):
    def __init__(self,number,wave,corral,stdDev):
        self.id=number
        self.wave=wave
        self.corral = corral
        self.stdDev = stdDev 
        self.position = -1
        self.started = False
        self.finished = False

txt = "MIN,K0,K5,K10,K15,K20,K25,K30,K35,K40,FINISHED\n"

for minute in range(0,500,10):
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
	
		RunnersArray.append(runner)
		# print RunnersArray[-1]

	print "done"
	##now we need to calculate how's where
	
	# Segment[i] = realData[i] - realData[i+1]

	##now simulation data
	simData = [0]*10
	
	# file = open('outPositions.csv','w')
	
	for r in RunnersArray:
		if r['finished']==1:
			simData[-1] += groupedNumber
		if r['started']==1:
			#simData[0]+=4
			pos = float(r['position'])
			# file.write(str(pos)+'\n')
			for i in range(9):
				if float(pos)>float(5.00*float(i)):
					simData[i]+=groupedNumber

	txt +=  str(minute)
	for each in simData:
		txt+= ','+str(each)
	
	txt+='\n'
	

file.write(txt)