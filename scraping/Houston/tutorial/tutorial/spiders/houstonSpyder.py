import scrapy 
from tutorial.items import Runner
from tutorial.items import RunnerHalf
import urlparse


class HoustonSpyder(scrapy.Spider):
	name = "houston1"
	allowed_domains = ["results.houstonmarathon.com"]

	gender = "M"
# http://results.chicagomarathon.com/2015/?page=2&event=MAR&lang=EN_CAP&pid=list&search%5Bsex%5D=M
#	start_urls=["http://results.chicagomarathon.com/2014/?content=detail&fpid=search&pid=search&idp=999999107FA30900001373D9&lang=EN_CAP&event=MAR&lang=EN_CAP&page=5&search%5Bname%5D=%2A&search%5Bfirstname%5D=%2A&search_sort=name&search_event=MAR"]
 	start_urls = []
 	for i in range(1,5):
 		start_urls.append("http://results.houstonmarathon.com/2015/?page="+str(i)+"&event=MARA&num_results=1000&pid=list&search%5Bsex%5D="+str(gender))
 		#start_urls.append("http://results.chicagomarathon.com/2015/?page="+str(i)+"&event=MAR&lang=EN_CAP&pid=search&search%5Bname%5D=%2A&search_sort=name")
 		print start_urls[-1]

	def parse(self, response):
		for i in range(1,1000):
			for href in response.css("#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(4) > a::attr('href')"):
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(2) > td:nth-child(4) > a
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(25) > td:nth-child(4)
				urlextend = href.extract()
				#print href.extract()
				#print 'a'
				#print 'a'
				#print 'a'
				#print 'a'
				url = urlparse.urljoin('http://results.houstonmarathon.com/2015/',urlextend)
				print url
				yield scrapy.Request(url, callback=self.parse_dir_contents)



	def parse_dir_contents(self,response):

		newRunner = Runner()

		print "HI IM HERE!!!! \n\n\n\n "
		Prestring = '/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr['
		Poststring = ']/td[6]/text()'
		Poststring_time = ']/td[2]'

		speeds = [-1]*9

		for i in range(1,9):
			newRunner['speed_'+str(i*5)+'k'] = float(response.xpath(str(Prestring+str(i)+Poststring)).extract()[0])
			#speeds[i-1] = float(response.xpath(str(Prestring+str(i)+Poststring)).extract()[0])


		finish_clock  = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/text()').extract()[0]
			
		#now parse through the finish_clock to figure out what minute after 7am they finished
		print finish_clock
		hour = int(finish_clock[0:2])
		minute = int(finish_clock[3:5])
		second = int(finish_clock[6:8])
		dayTime = finish_clock[8:10]
		if (dayTime=='PM'):
			hour = hour+12

		print hour,minute,second,dayTime
		finish_clock = float((hour-7)*60) + float(minute) + float(second/60)
		newRunner['finish_clock'] = finish_clock
		finish_time = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr[9]/td[3]/text()').extract()[0]
		
		
		hour = int(finish_time[0:2])
		minute = int(finish_time[3:5])
		second = int(finish_time[6:8])
		finish_time =  float((hour)*60) + float(minute) + float(second/60)
		newRunner['finish_time'] = finish_time

		newRunner['start_time'] = float(finish_clock - finish_time)


		newRunner['finish_speed'] = float(response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr[9]/td[6]/text()').extract()[0])

		newRunner['name'] = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/text()').extract()[0]
		newRunner['bibNumber'] = int(response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[4]/td[2]/text()').extract()[0])

		newRunner['age'] = int(response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[5]/td[2]/text()').extract()[0])

		newRunner['place_overall'] = int(response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/text()').extract()[0])




		yield newRunner



class HoustonSpyder(scrapy.Spider):
	name = "houston2"
	allowed_domains = ["results.houstonmarathon.com"]

	gender = "M"
# http://results.chicagomarathon.com/2015/?page=2&event=MAR&lang=EN_CAP&pid=list&search%5Bsex%5D=M
#	start_urls=["http://results.chicagomarathon.com/2014/?content=detail&fpid=search&pid=search&idp=999999107FA30900001373D9&lang=EN_CAP&event=MAR&lang=EN_CAP&page=5&search%5Bname%5D=%2A&search%5Bfirstname%5D=%2A&search_sort=name&search_event=MAR"]
 	start_urls = []
 	for i in range(1,5):
 		start_urls.append("http://results.houstonmarathon.com/2013/?page="+str(i)+"&event=MARA&num_results=1000&pid=list&search%5Bsex%5D="+str(gender))
 		#start_urls.append("http://results.chicagomarathon.com/2015/?page="+str(i)+"&event=MAR&lang=EN_CAP&pid=search&search%5Bname%5D=%2A&search_sort=name")
 		print start_urls[-1]

	def parse(self, response):
		for i in range(1,1000):
			for href in response.css("#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(4) > a::attr('href')"):
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(2) > td:nth-child(4) > a
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(25) > td:nth-child(4)
				urlextend = href.extract()
				#print href.extract()
				#print 'a'
				#print 'a'
				#print 'a'
				#print 'a'
				url = urlparse.urljoin('http://results.houstonmarathon.com/2013/',urlextend)
				print url
				yield scrapy.Request(url, callback=self.parse_dir_contents)



	def parse_dir_contents(self,response):

		newRunner = Runner()

		print "HI IM HERE!!!! \n\n\n\n "
		Prestring = '//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div/div/table/tbody/tr['#1]/td[5]'
		#Prestring = '/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr['
		Poststring = ']/td[5]/text()'
		Poststring_time = ']/td[2]'

		speeds = [-1]*9

		for i in range(1,9):
			k=i
			if (i>=5):
				k=k+1
			speed = response.xpath(str(Prestring+str(k)+Poststring)).extract()[0]
			if (speed=='-'):
				continue
			newRunner['speed_'+str(i*5)+'k'] = float(response.xpath(str(Prestring+str(k)+Poststring)).extract()[0])
			#speeds[i-1] = float(response.xpath(str(Prestring+str(i)+Poststring)).extract()[0])


		#finish_clock  = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/text()').extract()[0]
		finish_clock = response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[5]/td[2]/text()').extract()[0]
		#now parse through the finish_clock to figure out what minute after 7am they finished
		print finish_clock
		hour = int(finish_clock[0:2])
		minute = int(finish_clock[3:5])
		second = int(finish_clock[6:8])


		print hour,minute,second
		finish_clock = float((hour)*60) + float(minute) + float(second/60)
		newRunner['finish_clock'] = finish_clock
		finish_time = response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/text()').extract()[0]
		
		
		hour = int(finish_time[0:2])
		minute = int(finish_time[3:5])
		second = int(finish_time[6:8])
		finish_time =  float((hour)*60) + float(minute) + float(second/60)
		newRunner['finish_time'] = finish_time

		newRunner['start_time'] = float(finish_clock - finish_time)


		newRunner['finish_speed'] = float(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div/div/table/tbody/tr[10]/td[5]/text()').extract()[0])

		newRunner['name'] = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/text()').extract()[0]
		newRunner['bibNumber'] = int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]/text()').extract()[0])

		newRunner['age'] = int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[4]/td[2]/text()').extract()[0])

		newRunner['place_overall'] = int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/text()').extract()[0])




		yield newRunner



class HoustonSpyder(scrapy.Spider):
	name = "houstonhalf"
	allowed_domains = ["results.houstonmarathon.com"]

	gender = "M"
# http://results.chicagomarathon.com/2015/?page=2&event=MAR&lang=EN_CAP&pid=list&search%5Bsex%5D=M
#	start_urls=["http://results.chicagomarathon.com/2014/?content=detail&fpid=search&pid=search&idp=999999107FA30900001373D9&lang=EN_CAP&event=MAR&lang=EN_CAP&page=5&search%5Bname%5D=%2A&search%5Bfirstname%5D=%2A&search_sort=name&search_event=MAR"]
 	start_urls = []
 	for i in range(1,5):
 		start_urls.append("http://results.houstonmarathon.com/2014/?page="+str(i)+"&event=HALF&num_results=1000&pid=list&search%5Bsex%5D="+str(gender))
 		#start_urls.append("http://results.chicagomarathon.com/2015/?page="+str(i)+"&event=MAR&lang=EN_CAP&pid=search&search%5Bname%5D=%2A&search_sort=name")
 		print start_urls[-1]

	def parse(self, response):
		for i in range(1,1000):
			for href in response.css("#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(4) > a::attr('href')"):
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(2) > td:nth-child(4) > a
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(25) > td:nth-child(4)
				urlextend = href.extract()
				#print href.extract()
				#print 'a'
				#print 'a'
				#print 'a'
				#print 'a'
				url = urlparse.urljoin('http://results.houstonmarathon.com/2014/',urlextend)
				print url
				yield scrapy.Request(url, callback=self.parse_dir_contents)



	def parse_dir_contents(self,response):

		newRunner = RunnerHalf()

		print "HI IM HERE!!!! \n\n\n\n "
		Prestring = '//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div/div/table/tbody/tr['#1]/td[5]'
		Prestring = '//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div/div/table/tbody/tr['#1]/td[5]'
		#Prestring = '/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr['
		Poststring = ']/td[6]/text()'
		Poststring_time = ']/td[2]'

		speeds = [-1]*9

		for i in range(1,5):
			print i
			k=i
			if (i>=5):
				k=k+1
			speed = response.xpath(str(Prestring+str(k)+Poststring)).extract()[0]
			if (speed=='-'):
				continue
			newRunner['speed_'+str(i*5)+'k'] = float(response.xpath(str(Prestring+str(k)+Poststring)).extract()[0])
			#speeds[i-1] = float(response.xpath(str(Prestring+str(i)+Poststring)).extract()[0])


		#finish_clock  = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/text()').extract()[0]
		finish_clock = response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[5]/td[2]/text()').extract()[0]
		#now parse through the finish_clock to figure out what minute after 7am they finished
		print finish_clock
		hour = int(finish_clock[0:2])
		minute = int(finish_clock[3:5])
		second = int(finish_clock[6:8])


		print hour,minute,second
		finish_clock = float((hour)*60) + float(minute) + float(second/60)
		newRunner['finish_clock'] = finish_clock
		#finish_time = response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/text()').extract()
		finish_time = response.xpath("//*[@class='f-time_finish_netto last']/text()").extract()[0]
		print finish_time
		
		hour = int(finish_time[0:2])
		minute = int(finish_time[3:5])
		second = int(finish_time[6:8])
		finish_time =  float((hour)*60) + float(minute) + float(second/60)
		newRunner['finish_time'] = finish_time

		newRunner['start_time'] = float(finish_clock - finish_time)


		#newRunner['finish_speed'] = float(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div/div/table/tbody/tr[10]/td[5]/text()').extract()[0])
		newRunner['finish_speed'] = float(response.xpath(str(Prestring+str(k)+Poststring)).extract()[0])

		newRunner['name'] = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/text()').extract()[0]
		#newRunner['bibNumber'] = int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]/text()').extract()[0])
		newRunner['bibNumber'] = int(response.xpath('//*[@class="f-start_no_text last"]/text()').extract()[0])
		#newRunner['age'] = int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[1]/div/table/tbody/tr[4]/td[2]/text()').extract()[0])
		newRunner['age'] = int(response.xpath('//*[@class="f-age last"]/text()').extract()[0])
		newRunner['place_overall'] = int(response.xpath('//*[@class="f-place_nosex last"]/text()').extract()[0])
		#int(response.xpath('//*[@id="cbox-left"]/div[5]/div[1]/div[3]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/text()').extract()[0])




		yield newRunner












