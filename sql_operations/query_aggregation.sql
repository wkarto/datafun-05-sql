-- Count the number of authors
SELECT COUNT(*) AS total_authors FROM authors;

-- Average year_published of books
SELECT AVG(year_published) AS average_year_published FROM books;

-- Sum of all years_born (just for demonstration)
SELECT SUM(year_born) AS sum_year_born FROM authors;
