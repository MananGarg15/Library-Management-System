import sqlite3 as sql
import pandas as pd


conn = sql.connect('Tables.db')
cursor = conn.cursor()

create_table_members = """
CREATE TABLE IF NOT EXISTS members(
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    membership_type TEXT NOT NULL,
    join_date DATE
)
"""

create_table_authors = """
CREATE TABLE IF NOT EXISTS authors(
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL,
    country TEXT
)
"""

create_table_categories = """
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL
)
"""

create_table_books = """
CREATE TABLE IF NOT EXISTS books(
    book_id TEXT PRIMARY KEY,
    author_id INTEGER,
    category_id INTEGER,
    title TEXT NOT NULL,
    published_year INTEGER,
    total_copies INTEGER,
    available_copies INTEGER,
    average_rating FLOAT    
)
"""

create_table_borrow_records = """
CREATE TABLE IF NOT EXISTS borrow_records(
    borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id TEXT NOT NULL,
    member_id INTEGER NOT NULL,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    fine_amount FLOAT    
)
"""

cursor.execute(create_table_members)
cursor.execute(create_table_authors)
cursor.execute(create_table_categories)
cursor.execute(create_table_books)
cursor.execute(create_table_borrow_records)

df= pd.read_csv('datasets/books_data/books.csv',
                delimiter=';', encoding='latin1',
                on_bad_lines='skip')
df.drop(columns=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], inplace=True)
print(df.head())
print(df.columns)
print(df['Year-Of-Publication'].dtype)