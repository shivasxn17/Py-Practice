'''
program to read through the mbox-short.txt and figure out
who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
creates a Python dictionary that maps 
the sender's mail address to a count of the number of times they appear in the file. 
reads through the dictionary using a max to find the most prolific committer.
'''

# fname = input("Enter file name: ")
file_handle = open("mbox-short.txt")
contacts = {}

for line in file_handle:
	if not line.startswith("From ") : continue
	if line.split()[1] in contacts:
		contacts[line.split()[1]] = contacts[line.split()[1]] + 1 
	else:
		contacts[line.split()[1]] = 1
	
print(list(contacts.keys())[list(contacts.values()).index(max(contacts.values()))],max(contacts.values()))