'''
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines 
and computes the mean of those values.
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
file_handle = open(fname)
count = 0
total = 0

for line in file_handle:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count = count + 1
	index= line.find('0')
	total = total + float(line[index:])

print("Average spam confidence:",total/count)