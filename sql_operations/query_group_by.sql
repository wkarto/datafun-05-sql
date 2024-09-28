-- Count the number of books per author
SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS book_count
FROM authors
INNER JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id;

-- Average year_published per author
SELECT authors.first_name, authors.last_name, AVG(books.year_published) AS average_year
FROM authors
INNER JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id;

-- Sum of books published per decade
SELECT 
    (books.year_published / 10) * 10 AS decade,
    COUNT(books.book_id) AS books_count
FROM books
GROUP BY decade
ORDER BY decade ASC;
