"""
Database Operations Script
This script performs various operations on the SQLite database, including inserting, updating, deleting records, and executing queries.

"""

# Import from Python Standard Library first
import sqlite3
import pathlib
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define paths using pathlib
db_file_path = pathlib.Path("project.db")
sql_folder_path = pathlib.Path("sql_operations")

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL statements from a given file."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing SQL from {sql_file}: {e}")

def insert_records(db_filepath, sql_file):
    """Insert additional records into the database."""
    logging.info("Inserting additional records.")
    execute_sql_from_file(db_filepath, sql_file)

def update_records(db_filepath, sql_file):
    """Update existing records in the database."""
    logging.info("Updating records.")
    execute_sql_from_file(db_filepath, sql_file)

def delete_records(db_filepath, sql_file):
    """Delete records from the database."""
    logging.info("Deleting records.")
    execute_sql_from_file(db_filepath, sql_file)

def perform_queries(db_filepath, query_file):
    """Perform queries and display results."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(query_file, 'r') as file:
                query = file.read()
            
            # Check if the query contains multiple statements
            if ";" in query.strip():
                results = conn.executescript(query)
            else:
                cursor = conn.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
            
            logging.info(f"Executed query from {query_file}")
            print(f"Results from {query_file}:")
            for row in results:
                print(row)
    except sqlite3.Error as e:
        logging.exception(f"Error performing query from {query_file}: {e}")


def main():
    logging.info("Database operations started.")

    # Insert additional records
    insert_records(db_file_path, sql_folder_path.joinpath("insert_records.sql"))
    
    # Update records
    update_records(db_file_path, sql_folder_path.joinpath("update_records.sql"))
    
    # Delete records
    delete_records(db_file_path, sql_folder_path.joinpath("delete_records.sql"))
    
    # Perform Aggregation Queries
    perform_queries(db_file_path, sql_folder_path.joinpath("query_aggregation.sql"))
    
    # Perform Filter Queries
    perform_queries(db_file_path, sql_folder_path.joinpath("query_filter.sql"))
    
    # Perform Sorting Queries
    perform_queries(db_file_path, sql_folder_path.joinpath("query_sorting.sql"))
    
    # Perform Group By Queries
    perform_queries(db_file_path, sql_folder_path.joinpath("query_group_by.sql"))
    
    # Perform Join Queries
    perform_queries(db_file_path, sql_folder_path.joinpath("query_join.sql"))
    
    logging.info("Database operations completed successfully.")

if __name__ == "__main__":
    main()
