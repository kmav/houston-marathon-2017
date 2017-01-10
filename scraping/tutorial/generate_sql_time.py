
import numpy as np
import random
import time
import sys

def getAgeGroup(ageGroup):

	if ageGroup=='16-19':
		return 0
	if ageGroup=='20-24':
		return 1
	if ageGroup=='25-29':
		return 2
	if ageGroup=='30-34':
		return 3
	if ageGroup=='35-39':
		return 4
	if ageGroup=='40-44':
		return 5
	if ageGroup=='45-49':
		return 6
	if ageGroup=='50-54':
		return 7
	if ageGroup=='55-59':
		return 8
	if ageGroup=='60-64':
		return 9
	if ageGroup=='65-69':
		return 10
	if ageGroup=='70-74':
		return 11
	if ageGroup=='75-80':
		return 12
	if ageGroup=='80+':
		return 13
	if ageGroup=='99':
		return 14
	else:
		return 15


year = int(sys.argv[1])
#gender = str(sys.argv[2])

file1 = open('attempt1.csv','r')
file2 = open('archiveTIMES.sql','w')


lines_array = []
for line in file1:
	lines_array.append((line.strip()).split(','))

#get rid of first line
titles = lines_array[0]
for i in range(len(titles)):
	print titles[i],
	title=titles[i]
	if title=='speed_05k':
		title='speed_01k'
	if title=='speed_10k':
		title='speed_02k'
	if title=='speed_15k':
		title='speed_03k'
	if title=='speed_20k':
		title='speed_04k'
	if title=='speed_52k':
		title='speed_05k'
	if title=='speed_25k':
		title='speed_06k'
	if title=='speed_30k':
		title='speed_07k'
	if title=='speed_35k':
		title='speed_08k'
	if title=='speed_40k':
		title='speed_09k'
	if title=='time_05k':
		title='time_01k'
	if title=='time_10k':
		title='time_02k'
	if title=='time_15k':
		title='time_03k'
	if title=='time_20k':
		title='time_04k'
	if title=='time_52k':
		title='time_05k'
	if title=='time_25k':
		title='time_06k'
	if title=='time_30k':
		title='time_07k'
	if title=='time_35k':
		title='time_08k'
	if title=='time_40k':
		title='time_09k'

	print title
	titles[i]=title
print titles
lines_array = lines_array[1:]


#format of lines is: bibNumber,speed_25k,
					# speed_20k,speed_30k,
					# startTime,year,
					# place_overall,speed_35k,
					# speed_05k,speed_10k,
					# #name,speed_15k,
					# speed_09k,speed_08k,
					# ageGroup,place_gender


#append an avgSpeed to each of the numbers
speeds = {}
avgSpeed = {}

j=0
for competitor in lines_array:
	j+=1
	print j
	if 'M-15' in competitor:
		continue
	if '-' in competitor:
		continue
	else:

		# sqlTxt = "INSERT INTO MarathonTimes(year,bibNumber,timeMeasured,speed) VALUES ( 2014,"
		times = {}
		speeds = {}

		i=-1
		#print competitor
		#print titles
		for title in titles:
			i+=1
			#print title
			#print competitor[i]
			if title=='name':
				i+=1
				continue
			if title=="bibNumber":
				bibNumber = competitor[i]
			elif title[0:5]=='speed':
				if title=="speed_05k":
					continue
				speeds[title[6:8]]=float(competitor[i])
			elif title[0:4]=='time':
				if title=='time_05k':
					continue
				timeString = (competitor[i])
				t_hour = int(competitor[i][:2])
				t_minute = int(competitor[i][3:5])
				#ignore seconds
				t_amPM = competitor[i][8:10]
				if (t_hour<7):
					t_hour=t_hour+12

				times[title[5:7]] = float(t_hour-7)*60 + float(t_minute) -30

		for key in times:
			#reduce by half the distance at the speed we got (2.5km / (mph*1.609) )
			times[key] = times[key] - 2.5/(speeds[key]*1.609)

		for key in speeds:
			sqlTxt = "INSERT INTO MarathonTimes (year,bibNumber,timeMeasured,speed,distance) VALUES (2013,"+str(bibNumber)+','
			sqlTxt += str(times[key])+','+str(speeds[key])+','+str(key)+');\n'

			file2.write(sqlTxt)
		#print sqlTxt








