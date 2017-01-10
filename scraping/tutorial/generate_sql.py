
import numpy as np
import random
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

file1 = open('archive'+str(year)+'.csv','r')
file2 = open('archive'+str(year)+'.sql','w')


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
	if 'DSQ' in competitor:
		continue
	else:
		sqlTxt = "INSERT INTO MarathonData(gender,"
		for title in titles:
			sqlTxt+=title+','
		sqlTxt+='avgSpeed,stdDev,country) VALUES ("G"'

		i=-1
		speeds = []
		print competitor
		for title in titles:
			i+=1
			print title,i,competitor[i]

			if title=='ageGroup':
				ageGrp = getAgeGroup(competitor[i])
				sqlTxt += ','+str(ageGrp)
			elif title=='startTime':
				strtTime = competitor[i]
				starttime = float((int(strtTime[0:2])-7)*60.0)+float(int(strtTime[3:5]))+float(float(strtTime[6:8])/60.0)-30.00
				sqlTxt += ','+str(starttime)
			elif title=='year':
				sqlTxt += ','+str(year)
			elif title=='name':
				country = competitor[i+1][-5:-2]
				sqlTxt += ','+competitor[i]+competitor[i+1]
				i+=1
			elif title=='bibNumber':
				bib = competitor[i]
				sqlTxt += ","+str(competitor[i])
			else:
				if title[0:5]=='speed':
					speeds.append(1.00)
				sqlTxt += ','+str(1.00)
		sqlTxt += ','+str(np.mean(speeds))
		sqlTxt += ','+str(np.std(speeds))
		sqlTxt += ',"'+str(country)
		sqlTxt += '"); \n '
		file2.write(sqlTxt)
		#print sqlTxt








