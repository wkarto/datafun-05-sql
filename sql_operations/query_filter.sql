-- Select books published after 1950
SELECT * FROM books
WHERE year_published > 1950;

-- Select authors born before 1900
SELECT * FROM authors
WHERE year_born < 1900;

-- Select books by a specific author
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id
WHERE authors.last_name = 'Tolkien';
