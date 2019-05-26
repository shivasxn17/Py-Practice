1. books_db_tsv_updated.txt (tab separated values)
2. books_db_to_sql.py (Python Script)
3. output.sql (Generated SQL Script)

Guidelines:

1. Make sure these files are in same directory:
	- books_db_tsv_updated.txt
	- books_db_to_sql.py

2. Make sure command prompt directory is same as files.
	change using cd command if not

3. Run the Python Script with follwing command:

python books_db_to_sql.py

To Generate SQL Script "output.sql" containing:
	- create database command to create db statement
		named: 'output' and 
	- populating it with all the books data of excel file.
		insert statements for title and 
		multi value insert statements for author, themes and qualities