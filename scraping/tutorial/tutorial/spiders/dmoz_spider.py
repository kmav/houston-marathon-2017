import scrapy

from tutorial.items import MarathonDetails1
from tutorial.items import DmozItem
import urlparse


# class Tracking(scrapy.Spider):
# 	name = "location"
# 	allowed_domains = ["gateway.landairsea.com"]
# 	start_urls = [
# 		"https://gateway.landairsea.com/tmmgw/tmmgw.asmx/Poll?cmd={%22usr%22:%22cemevent%22,%22pwd%22:%22raceday%22,%22posidx%22:%22[MaxPosIdx]%22}"
# 	]

# 	def parse(self,response):

# 		for sel in response.xpath("//div[@class='collapsible-content']"):
# 			print "\n\n\n\n --- ",sel," \n\n\n"
# 			item = Tracking()
# 			item['textjson'] = sel.xpath('/span').extract()
# 			yield item



class DmozSpider(scrapy.Spider):
	name = "dmoz"
	#so you don't click on a wrong link
	allowed_domains = ["dmoz.org"]
	start_urls = [
	"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
	
	#this function extracts information
	def parse(self,response):
		#filename = response.url.split("/")[-2]+'.html'
		#with open(filename,'wb') as f:
		#	f.write(response.body)
		# http://doc.scrapy.org/en/latest/topics/selectors.html
		
		#xpath allows you to get the specific item you are looking for
		# //ul = all <ul> elements  (ul is ordered list)
		# 	all <li> elements inside the <ul> elements (li is linked item)
		
		for sel in response.xpath('//ul/li'):
			#item = DmozItem()
			#in that selection of this path we are looking for link a and get the text in that space
			item['title']= sel.xpath('a/text()').extract()
			#actually gets the link in that location
			item['link'] = sel.xpath('a/@href').extract()
			#item['desc'] = sel.xpath('text()').extract()
			yield item


#failed runner tracking
# class RunnerTracking(scrapy.Spider):
# 	name = "runners"
# 	allowed_domains = ["stats.chicagomarathon.com"]
# 	start_urls = [
# 	"http://stats.chicagomarathon.com/2015/?lang=EN_CAP&pid=statistics"]

# 	def parse(self,response):
# 		#filename = response.url.split("/")[-2]+'.html'
# 		#with open(filename,'wb') as f:
# 		#	f.write(response.body)
# 		item = TrackRunner()
# 		item['k5'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[1]/td[2]').extract()
# 		item['k10'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[2]/td[2]').extract()
# 		item['k15'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[4]/td[2]').extract()
# 		item['k20'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[5]/td[2]').extract()
# 		item['k25'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[8]/td[2]').extract()
# 		item['k30'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[9]/td[2]').extract()
# 		item['k35'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[10]/td[2]').extract()
# 		item['k40'] = response.xpath('//div[@id="cbox-left"]/div[5]/div[1]/div[3]/div/div[1]/table[1]/tbody/tr[12]/td[2]').extract()

# 		yield item


class MarathonSpider(scrapy.Spider):
		name = "marathon"
		allowed_domains = ["results.houstonmarathon.com/2015"]

		start_urls = []
		for i in range(1,1626):
			start_urls.append("http://results.houstonmarathon.com/2014/?page="+str(i)+"&event=MAR&lang=EN_CAP&pid=search&search%5Bname%5D=%2A&search%5Bfirstname%5D=%2A&search_sort=name")
			print start_urls[-1]

		def parse(self,response):
			#select all the tr's in the field
			times = 1
			for sel in response.xpath('//tr'):
				item = MarathonItem()
				item['cell']=sel.xpath('td/text()').extract()
				if times==1:
					y=item['cell']
					print item['cell']
					times+=1
				else:
					yield item


class MarathonDetailsSpider(scrapy.Spider):
	name = "marathonDetails"
	allowed_domains = ["results.houstonmarathon.com"]
	gender = "M"
# http://results.chicagomarathon.com/2015/?page=2&event=MAR&lang=EN_CAP&pid=list&search%5Bsex%5D=M
#	start_urls=["http://results.chicagomarathon.com/2014/?content=detail&fpid=search&pid=search&idp=999999107FA30900001373D9&lang=EN_CAP&event=MAR&lang=EN_CAP&page=5&search%5Bname%5D=%2A&search%5Bfirstname%5D=%2A&search_sort=name&search_event=MAR"]
 	
 	start_urls = []
 	#collect all urls you need (1000 per page and 4 pages)
 	for i in range(1,5):
 		#looping through each page number
 		start_urls.append("http://results.houstonmarathon.com/2015/?page="+str(i)+"&event=MARA&num_results=1000&pid=list&search%5Bsex%5D="+str(gender))
 		#start_urls.append("http://results.chicagomarathon.com/2015/?page="+str(i)+"&event=MAR&lang=EN_CAP&pid=search&search%5Bname%5D=%2A&search_sort=name")
 		print start_urls[-1]
	#build two spiders, one that clicks, and one that uses the result of the click to get the information
	
	def parse(self, response):
		# this is the spider that 'clicks' 
		for i in range(1,1000):
			#css: # for id for example (go to page and look at how it is built by doing inspect element. Identify what changes between each link for each row)
			for href in response.css("#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(4) > a::attr('href')"):
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(2) > td:nth-child(4) > a
			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(25) > td:nth-child(4)
				#href is the element, extract is the string in that element
				urlextend = href.extract()
				#print href.extract()

				#we got the part of the link past the ? in the url, and now we are adding the beginning part
				url = urlparse.urljoin('http://results.houstonmarathon.com/2015/',urlextend)
				print url
				#look into that url and parse the information about the individual runner
				#yield allows you to use the value, like without return, but without destroying the stack
				yield scrapy.Request(url, callback=self.parse_dir_contents)



	def parse_dir_contents(self,response):

		item = MarathonDetails1()

		#print response.xpath("//body")
		#print response.xpath("//td[@class='f-start_no last']")
		for sel in response.xpath("//body"):
			#print sel
			item['bibNumber']=sel.xpath("//td[@class='f-start_no_text last']/text()").extract()
			item['startTime']=sel.xpath("//td[@class='f-starttime_net last']/text()").extract()
			item['name']=sel.xpath("//td[@class='f-__fullname last']/text()").extract()
			item['ageGroup']=sel.xpath("//td[@class='f-age_class last']/text()").extract()
			#item['speed_42k']=sel.xpath("//td[@class='list-highlight f-time_finish_netto']/td[@class='kmh last']/text()").extract()


			#trying to get the 5k information (ignoring start and finish)
			for i in ['05','10','15','20','25','30','35','40']:
				if i in ['10','20','25','35']:
					#identify which color the row is highlighted
					#tr is table row
					mypath = "//tr[@class='list-highlight f-time_"+i+" split']"
				else:
					mypath = "//tr[@class=' f-time_"+i+" split']"
				#print mypath
				
				# this is the entire row
				sl = response.xpath(mypath)

				#we only need speed because we can figure out the rest given the start time
				#we are already inside the row so we don't need to do the whole path again (just the additional class modifier)
				#/ means go into next one
				#// is everything
			 	item['speed_'+str(i)+'k'] = sl.xpath("td[@class='kmh last']/text()").extract()
			 	#item['time_'+str(i)+'k'] = sl.xpath("td[@class='time_day']/text()").extract()
			 	# item['time'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[3]/text()').extract()
			 	# item['diff'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[4]/text()').extract()
			 	# item['min_per_mile'+str(i)+'k'] = sel.xpath('//[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[5]/text()').extract()
			 	# item['speed'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[6]/text()').extract()

			yield item


	# class AllChicagoMarathon(scrapy.Spider):
	# 	name = "allMarathon"
	# 	allowed_domains = ["results.chicagomarathon.com",'']


	# 	#for marathon, change year, gender and run 
	# 	# need to do M,W for years: 2008,2009,2010,2011,2012
	# 	start_urls = []
	# 	for gender in ['M']:
	# 		for year in range(2012,2013):
	# 			for page in range(25):
	# 				start_urls.append("http://results.chicagomarathon.com/2014/?page="+str(page)+"&event=MAR&lang=EN_CAP&num_results=1000&pid=list&search%5Bsex%5D="+gender)

	# 	# start_urls = ["http://chicago-history.r.mikatiming.de/2012/?page=1&event=MAR_999999107FA3090000000051&event_main_group=2010&lang=EN_CAP&num_results=1000&pid=list&search%5Bage_class%5D=%25&search%5Bsex%5D=M"]

	# 	print start_urls

	# 	def parse(self, response):
	# 		for i in range(1001):
	# 			for href in response.css("#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child("+str(i)+") > td:nth-child(4) > a::attr('href')"):
	# 			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(2) > td:nth-child(4) > a
	# 			#cbox-left > div.cbox-content > div.list > table > tbody > tr:nth-child(25) > td:nth-child(4)
	# 				urlextend = href.extract()
	# 				#print href.extract()
	# 				#print 'a'
	# 				#print 'a'
	# 				#print 'a'
	# 				#print 'a'
	# 				url = urlparse.urljoin('http://results.chicagomarathon.com/2014/',urlextend)
	# 				#print url
	# 				yield scrapy.Request(url, callback=self.parse_dir_contents)



	# 	def parse_dir_contents(self,response):

	# 		#print "Hi I'm here!!!!"
	# 		item = MarathonDetails()
	# 		#print 'xxxxxxxxxqwerqweruioqweruiqoweruiqoweruiqworuiqworuqiwoeruqiweo'

	# 		#print response.xpath("//body")
	# 		#print response.xpath("//td[@class='f-start_no last']")
	# 		#myUrl = response.url()
	# 		#print myUrl


	# 		for sel in response.xpath("//body"):
	# 			#print sel
	# 			#print 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
	# 			item['bibNumber']=sel.xpath("//td[@class='f-start_no last']/text()").extract()
	# 			item['startTime']=sel.xpath("//td[@class='f-starttime_net last']/text()").extract()
	# 			item['name']=sel.xpath("//td[@class='f-__fullname last']/text()").extract()
	# 			item['ageGroup']=sel.xpath("//td[@class='f-age_class last']/text()").extract()
	# 			#item['speed_42k']=sel.xpath("//td[@class='list-highlight f-time_finish_netto']/td[@class='kmh last']/text()").extract()
	# 			item['place_overall']=sel.xpath("//td[@class='f-place_nosex last']/text()").extract()
	# 			item['place_gender']=sel.xpath("//td[@class='f-place_all last']/text()").extract()
	# 			#item['year']=myUrl[171:175]

	# 			numbers = ['05','10',3,4,6,7,8,9]
	# 			for i in ['05','10','15','20','52','25','30','35','40']:
	# 				if i in ['10','20','25','35']:
	# 					mypath = "//tr[@class='list-highlight f-time_"+i+" split']"
	# 				else:
	# 					mypath = "//tr[@class=' f-time_"+i+" split']"
	# 				#print mypath
	# 				sl = response.xpath(mypath)
	# 				#print 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

	# 				#print sl
	# 			 	item['speed_'+str(i)+'k'] = sl.xpath("td[@class='kmh last']/text()").extract()
	# 			 	# item['time'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[3]/text()').extract()
	# 			 	# item['diff'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[4]/text()').extract()
	# 			 	# item['min_per_mile'+str(i)+'k'] = sel.xpath('//[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[5]/text()').extract()
	# 			 	# item['speed'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[6]/text()').extract()

	# 			yield item



		# def parse_dir_contents(self,response):

		# 	print "Hi I'm here!!!!"
		# 	item = MarathonDetails()
		# 	#print 'xxxxxxxxxqwerqweruioqweruiqoweruiqoweruiqworuiqworuqiwoeruqiweo'

		# 	#print response.xpath("//body")
		# 	#print response.xpath("//td[@class='f-start_no last']")
		# 	myUrl = response.url()
		# 	print myUrl


		# 	for sel in response.xpath("//body"):
		# 		#print sel
		# 		#print 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
		# 		item['bibNumber']=sel.xpath("//td[@class='f-start_no last']/text()").extract()
		# 		item['startTime']=sel.xpath("//td[@class='f-starttime_net last']/text()").extract()
		# 		item['name']=sel.xpath("//td[@class='f-__fullname last']/text()").extract()
		# 		item['ageGroup']=sel.xpath("//td[@class='f-age_class last']/text()").extract()
		# 		item['speed_42k']=sel.xpath("//td[@class='list-highlight f-time_finish_netto']/td[@class='kmh last']/text()").extract()
		# 		item['year']=myUrl[171:175]

		# 		numbers = ['05','10',3,4,6,7,8,9]
		# 		for i in ['05','10','15','20','25','30','35','40']:
		# 			if i in ['10','20','25','35']:
		# 				mypath = "//tr[@class='list-highlight f-time_"+i+" split']"
		# 			else:
		# 				mypath = "//tr[@class=' f-time_"+i+" split']"
		# 			#print mypath
		# 			sl = response.xpath(mypath)
		# 			#print 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

		# 			#print sl
		# 		 	item['speed_'+str(i)+'k'] = sl.xpath("td[@class='kmh last']/text()").extract()
		# 		 	# item['time'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[3]/text()').extract()
		# 		 	# item['diff'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[4]/text()').extract()
		# 		 	# item['min_per_mile'+str(i)+'k'] = sel.xpath('//[@id="cbox-left"]/div[5]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[5]/text()').extract()
		# 		 	# item['speed'+str(i)+'k'] = sel.xpath('div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr['+str(numbers[i])+'/td[6]/text()').extract()

	# 		yield item



