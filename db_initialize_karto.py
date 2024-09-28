"""
Database Initialization Script
This script initializes the SQLite database by creating tables and inserting initial data from CSV files.

"""

# Import from Python Standard Library first
import sqlite3
import pathlib
import logging

# Import from external packages
import pandas as pd

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define paths using pathlib
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            logging.info(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            logging.debug(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        logging.exception(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.exception(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        # Read CSV files
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        
        # Rename columns to match the SQL table schema
        authors_df.rename(columns={'first': 'first_name', 'last': 'last_name'}, inplace=True)
        
        # Add the 'year_born' column with NaN values (or you can provide default values if known)
        authors_df['year_born'] = pd.NA
        
        # Insert data into the database
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="append", index=False)
            books_df.to_sql("books", conn, if_exists="append", index=False)
            logging.info("Data inserted successfully from CSV files.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception(f"Error inserting data: {e}")

def main():
    logging.info("Database initialization started.")
    
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)   
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)
    
    logging.info("Database initialization completed successfully.")

if __name__ == "__main__":
    main()
