# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Runner(scrapy.Item):
	#define fields
	name = scrapy.Field()
	bibNumber = scrapy.Field()
	age = scrapy.Field()
	place_overall = scrapy.Field()

	speed_5k= scrapy.Field()
	speed_10k = scrapy.Field()
	speed_15k = scrapy.Field()
	speed_20k = scrapy.Field()
	speed_25k = scrapy.Field()
	speed_30k = scrapy.Field()
	speed_35k = scrapy.Field()
	speed_40k = scrapy.Field()

	start_time = scrapy.Field()

	finish_time = scrapy.Field()
	finish_clock = scrapy.Field()
	finish_speed = scrapy.Field()

class RunnerHalf(scrapy.Item):
	#define fields
	name = scrapy.Field()
	bibNumber = scrapy.Field()
	age = scrapy.Field()
	place_overall = scrapy.Field()

	speed_5k= scrapy.Field()
	speed_10k = scrapy.Field()
	speed_15k = scrapy.Field()
	speed_20k = scrapy.Field()

	start_time = scrapy.Field()

	finish_time = scrapy.Field()
	finish_clock = scrapy.Field()
	finish_speed = scrapy.Field()
