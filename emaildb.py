import sqlite3 as sqlite

conn = sqlite.connect('emaildb.sqlite')
dbh = conn.cursor()

dbh.execute('DROP TABLE IF EXISTS Counts')
dbh.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input("Enter File Name:")

if (len(file_name) < 1) : file_name = 'mbox-short.txt'

fh = open(file_name)

for line in fh:
	if not line.startswith('From: '): continue
	words = line.split('@')
	org = words[1]
	dbh.execute('SELECT count FROM Counts WHERE org= ?', (org,))
	row = dbh.fetchone()
	if row is None:
		dbh.execute('INSERT INTO Counts (org,count) VALUES (? , 1)', (org,));
	else:
		dbh.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,));

conn.commit()