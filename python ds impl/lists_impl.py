'''
builds a list of words. 
For each word on each line check to see if the word is already in the list 
and if not append it to the list.
sorts and prints the resulting words in alphabetical order.
'''
file_handle = open("romeo.txt")
uniq_words = []
for line in file_handle:
	words = line.split()
	for word in words:
		if word in uniq_words: continue
		uniq_words.append(word)

uniq_words.sort()
print(uniq_words)