-- Inner Join: Get all books with their authors' names
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Left Join: Get all authors and their books (including authors with no books)
SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id;

-- Right Join: SQLite does not support RIGHT JOIN, but you can simulate it using LEFT JOIN
-- Example: Get all books and their authors, ensuring all books are included
SELECT books.title, authors.first_name, authors.last_name
FROM books
LEFT JOIN authors ON books.author_id = authors.author_id;
