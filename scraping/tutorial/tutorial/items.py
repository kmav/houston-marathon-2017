# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class TrackRunner(scrapy.Item):



	k5 = scrapy.Field()
	k10 = scrapy.Field()
	k15 = scrapy.Field()
	k20 = scrapy.Field()
	k25 = scrapy.Field()
	k30 = scrapy.Field()
	k35 = scrapy.Field()
	k40 = scrapy.Field()

	pass
	

class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    pass

# class MarathonItem(scrapy.Item):
# 	cell = scrapy.Field()
# 	pass
# class MarathonDetails1(scrapy.Item):

	# bibNumber = scrapy.Field()
	# startTime = scrapy.Field()
	# name = scrapy.Field()
	# ageGroup = scrapy.Field()
	# year = scrapy.Field()
	# speed_05k = scrapy.Field()
	# speed_10k = scrapy.Field()
	# speed_15k = scrapy.Field()
	# speed_20k = scrapy.Field()
	# speed_25k = scrapy.Field()
	# speed_30k = scrapy.Field()
	# speed_35k = scrapy.Field()
	# speed_40k = scrapy.Field()
	# speed_42k = scrapy.Field()

	# pass
	
class MarathonDetails1(scrapy.Item):

	bibNumber = scrapy.Field()
	startTime = scrapy.Field()
	name = scrapy.Field()
	ageGroup = scrapy.Field()
	year = scrapy.Field()
	place_overall = scrapy.Field()
	place_gender = scrapy.Field()

	speed_05k = scrapy.Field()
	speed_10k = scrapy.Field()
	speed_15k = scrapy.Field()
	speed_20k = scrapy.Field()
	speed_25k = scrapy.Field()
	speed_30k = scrapy.Field()
	speed_35k = scrapy.Field()
	speed_40k = scrapy.Field()
	speed_52k = scrapy.Field()

	# time_05k = scrapy.Field()
	# time_10k = scrapy.Field()
	# time_15k = scrapy.Field()
	# time_20k = scrapy.Field()
	# time_25k = scrapy.Field()
	# time_30k = scrapy.Field()
	# time_35k = scrapy.Field()
	# time_40k = scrapy.Field()

	pass

class Tracking(scrapy.Item):

	textjson = scrapy.Field()
	pass
	