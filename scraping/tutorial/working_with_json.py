import json

from pprint import pprint

with open('items1.json') as data_file:
	data = json.load(data_file)

print data[1]["bibNumber"]