#!/usr/bin/env python
"""
 This Script will read tabbed separated txt file converted 
 from books data excel file and generated DDL(create DB and create Tables) 
 and DML(insert) sqls in output as SQL file.

 Script Functions:
 	- createDatabase(db_name)
 	- createTables(db_name)
	- createMultiValuesInsertSQL(base_query,values)
"""
__author__ = "Shivam Saxena"

input_filename = 'books_db_tsv_updated.txt' 
output_sql_filename = 'output.sql'


def createDatabase(db_name):
	"""
		this function will create the database for give db name 
	"""
	db_exists_check_query = "drop database if exists {};\n".format(db_name)
	create_db_str = "create database {} ;\n".format(db_name)
	return db_exists_check_query + create_db_str

def createTables(db_name):
	"""
		this function will create tables in given db name
	"""	
	title_table_str = "create table {}.title(\
	isbn VARCHAR(13) NOT NULL PRIMARY KEY,\
	title VARCHAR(500) NOT NULL\
	);\n".format(db_name)

	author_table_str = "create table {}.author(\
	isbn VARCHAR(13) NOT NULL,\
	author_rank INT NOT NULL,\
	author VARCHAR(100) NOT NULL,\
	PRIMARY KEY ( isbn,author_rank )\
	);\n".format(db_name)

	theme_table_str = "create table {}.theme(\
	isbn VARCHAR(13) NOT NULL,\
	theme_id INT NOT NULL,\
	theme VARCHAR(100) NOT NULL,\
	PRIMARY KEY ( isbn,theme_id )\
	);\n".format(db_name)

	qualities_table_str = "create table {}.qualities(\
	isbn VARCHAR(13) NOT NULL,\
	quality_id INT NOT NULL,\
	qualities VARCHAR(100) NOT NULL,\
	PRIMARY KEY ( isbn,quality_id )\
	);\n".format(db_name)

	all_tables_sqls = title_table_str + author_table_str + theme_table_str + qualities_table_str

	return all_tables_sqls

def createMultiValuesInsertSQL(base_query,values):
	values = values.strip(" \"\'\t\r\n")
	if ' and ' in values:
		values = values.split(" and ")
	else:
		values = values.split(",")

	values = list(filter(None, values))

	for rank,value in enumerate(values,1):
		base_query += '("{0}", {1},"{2}")'.format(isbn,rank,value.strip(" \"\'\t\r\n"))	
		if rank != len(values):	base_query += ","
		else: base_query += ";"

	return base_query

if __name__ == '__main__':

	try:
		db_name = "" # enter the db_name need to be populated 

		with open(input_filename) as books_file:
			with open(output_sql_filename, "w") as sql_file:
					
				# DDLs
				sql_file.write(createDatabase(db_name))
				sql_file.write(createTables(db_name))

				# DMLs
				for line in books_file:
					if 'ISBN' in line: continue				
					book = line.strip().split("\t")
					isbn = book[0]
				
					# to insert into title table
					title_insert_str = "insert into {0}.title values"\
					'("{1}", "{2}");'.format(db_name,isbn,book[1].strip(" \"\'\t\r\n"))
					sql_file.write(title_insert_str)
					sql_file.write("\n")

					# to insert into author table
					author_insert_str = "insert into {}.author values".format(db_name)
					author_insert_str	= createMultiValuesInsertSQL(author_insert_str, book[2])
					sql_file.write(author_insert_str)
					sql_file.write("\n")

					# to insert into theme table
					theme_insert_str = "insert into {}.theme values".format(db_name)
					theme_insert_str	= createMultiValuesInsertSQL(theme_insert_str, book[3])
					sql_file.write(theme_insert_str)
					sql_file.write("\n")

					# to insert into qualities table
					qualities_insert_str = "insert into {}.qualities values".format(db_name)
					qualities_insert_str	= createMultiValuesInsertSQL(qualities_insert_str, book[4])
					sql_file.write(qualities_insert_str)
					sql_file.write("\n")

				print("SQL script {} generated successfully".format(output_sql_filename))
	except Exception as e:
		print(e)
		print("Error Occurred: Please recheck Input tsv file")