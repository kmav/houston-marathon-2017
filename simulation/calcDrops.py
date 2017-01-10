import pandas as pd
import os

def load_drops():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	drops = pd.read_csv(dir_path + '/runner_dropPcts.csv')

	events = ["Start", "5K", "10K", "15K", "20K","Half", "25K", "30K", "35K", "40K", "Finish"]
	drops["Event"] = drops["Event"].astype('category', categories = events, ordered = True)

	corrals = ["A", "B","C","D","E"]
	drops["Corral"] = drops["Corral"].astype('category', categories = corrals, ordered = True)

	return drops

def load_starts():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	starts = pd.read_csv(dir_path + '/runner_starts.csv')
	return starts
	
def load_times():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	times = pd.read_csv(dir_path + '/runner_times.csv')
	return times

def calc_drops(data, start):
	for index, row in data.iterrows():
		if row['Event'] == "Start":
			corral = row['Corral']

			# update starting drops to 0
			data.loc[index,'Drops']=0
			data.loc[index, 'Runners'] =  start[start.Corral == corral]["Start"].values[0]

		else:
			tmp_drop = - round(data.loc[index - 1, 'Runners'] * row['DropPct'],0)
			data.loc[index, 'Drops'] = tmp_drop
			data.loc[index, 'Runners'] = data.loc[index - 1, 'Runners'] - tmp_drop

	return data

def sumDrops(times, drops, curMinute):
	# for each row in times, if avg pacer time <= current minute in race, then add those drops to total
	totalDrops = 0

	for index, row in times.iterrows():
		if row['Min'] <= curMinute:
			totalDrops += drops.loc[index,"Drops"]
		else:
			totalDrops += 0

	return totalDrops