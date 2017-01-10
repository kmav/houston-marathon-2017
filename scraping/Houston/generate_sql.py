

year = int(sys.argv[1])
gender = str(sys.argv[2])
file1 = open('out'+str(year)+'.csv','r')
file2 = open('out'+str(year)+'.sql','w')

lines_array = []
for line in file1:
	lines_array.append((line.strip()).split(','))
titles = lines_array[0]
print titles

lines_array = lines_array[1:]

speeds = {}
avgSpeed = {}

for competitor in lines_array:
	j+=1
	print j
	if '-' in competitor:
		continue
	if -1 in competitor:
		continue
	if 'DSQ' in competitor:
		continue
	else:
		sqlTxt = "INSERT INTO MarathonData(gender,"
		for title in titles:
			sqlTxt+=title+','
		sqlTxt+='avgSpeed,stdDev,year,country) VALUES("'+str(gender)+'"'


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
				#starttime = float((int(strtTime[0:2])-7)*60.0)+float(int(strtTime[3:5]))+float(float(strtTime[6:8])/60.0)-30.00
				sqlTxt += ','+str(starttime)
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
		sqlTxt += ',"'+str(year)
		sqlTxt += ',"'+str(country)
		sqlTxt += '"); \n '
		file2.write(sqlTxt)
		#print sqlTxt
