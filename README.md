# Datafun-05-sql
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

## Overview

Project 5 integrates Python and SQL using SQLite. This project introduces logging for debugging and monitoring, and involves the following tasks:
   - Creating and managing a database
   - Building a schema
   - Performing SQL operations like joins, filters, and aggregations

## Installation and Setup

### Create a GitHub Repository

Create a new repository on GitHub, including a README file.
Clone the repository to your local machine

bash
git clone https://github.com/yourusername/datafun-05-sql


### Add a .gitignore File

Ensure the following entries are added to your .gitignore file to exclude unnecessary files from being committed:

bash
# Python virtual environment
.venv/

# Visual Studio Code settings and workspace
.vscode/

# Compiled Python files
__pycache__/


### Create and Activate a Virtual Environment

Create a virtual environment:

bash
python -m venv .venv


Activate the virtual environment:

bash
.\.venv\Scripts\activate


### Install Dependencies

Add requirements.txt file, it will be used to install with the necessary libraries.

Add the following libraries to your requirements.txt file:

bash
pandas
pyarrow


Install into your active project virtual environment with this command:

bash
py -m pip install -r requirements.txt

### Add Database with Two Related Tables

I created a simple SQLite database (book_db) with two related tables: books and authors. The books table includes book_id, title, year_published, and author_id (a foreign key). The authors table includes author_id, first, and last. I populated these tables using CSV files under the data folder. 


### Database Creation and Data Insertion

I updated the project to include automatic database creation and population from CSV files. The following changes were made:

Added db_initialize_karto.py script to:
   - Create an SQLite database (project.db) if it doesn't already exist.
   - Execute SQL commands from create_tables.sql to set up authors and books tables.
   - Insert data from authors.csv and books.csv into the respective tables, handling potential mismatches between the CSV headers and table schema.
   - Implement logging for debugging, with log messages output to log.txt.
Created a create_tables.sql file in the sql/ folder to define the schema for both tables.
Verified that the database was successfully created, and the data was inserted without errors.

bash
python db_initialize_karto.py

### SQL Operations and Database Manipulation

Added scripts to perform SQL operations such as inserting, updating, deleting records, and executing queries with joins, filters, and aggregations:

Created db_operations_karto.py to perform:
   - Inserting additional records (insert_records.sql)
   - Updating records (update_records.sql)
   - Deleting records (delete_records.sql)
   - Executing queries (query_aggregation.sql, query_filter.sql, query_sorting.sql, query_group_by.sql, query_join.sql)

Run the operations script to execute all database actions:
bash
python db_operations_karto.py



### Stage and Push Files to GitHub

Use the following Git commands to stage and commit changes:

bash
git add .
git commit -m "message: commit message"
git push origin main
