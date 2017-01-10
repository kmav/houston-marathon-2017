#get the split at every single mile (how many marathon runners out of total runners)

import MySQLdb as mdb
import random
import math
import sys
### mysql connection

#con = mdb.connect(host='localhost',user='bpeynetti',db='c9')
con = mdb.connect(host='localhost', user='rachellin23', db='houston2016')
cur = con.cursor(mdb.cursors.DictCursor)

groupedNumber = 10

class Runner(object):
    def __init__(self,number,corral,stdDev,half):
        self.id=number
        self.corral = corral
        self.stdDev = stdDev 
        self.position = -1
        self.started = False
        self.finished = False
        self.half = half
        


splits = {}
for minute in range(0,500,2):
    
    mileNumbers = [0]*10
    for i in range(9):
    
        sql = "SELECT minute, count(*) ct FROM MarathonRunners where dropout=0 and half=0 and minute="+str(minute)+" and position between "+str(float(i*5.00))+" and "+str(float((i+1)*5.00)) 
        # print sql
        cur.execute(sql)
        rows = cur.fetchall()
        row = rows[0]
        # for row in rows:
        #     print row['ct']
        
        mileNumbers[i] = int(row['ct'])
    print "Minute: ",minute," - ",mileNumbers
        
    
    