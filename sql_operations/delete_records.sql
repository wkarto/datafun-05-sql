-- Delete an author who has no books
DELETE FROM authors
WHERE author_id = 'j0k1l2m3-4567-8ijk-5678-0abcdef01234';

-- Delete a book by title
DELETE FROM books
WHERE title = 'Custom Book Title';
