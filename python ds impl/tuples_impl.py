''' 
determines the distribution by hour of the day for each of the messages. 
'From ' line by finds the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
prints out the counts, sorted by hour.
'''

file_handle = open("mbox-short.txt")
hours = {}
for line in file_handle:
	if not line.startswith("From ") : continue
	hour = line[-14:-6].split(":")[0]
	if hour in hours.keys():
		hours[hour] =  hours[hour] + 1
	else:
		hours[hour] = 1

keys = list(hours.keys())
keys.sort()
for key in keys:
	print(key, hours[key])