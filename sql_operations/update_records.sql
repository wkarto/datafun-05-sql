-- Update the year_born for author 'Jane Doe'
UPDATE authors
SET year_born = 1965
WHERE author_id = 'i9j0k1l2-3456-7hij-4567-90abcdef0123';

-- Correct update for book title
UPDATE books
SET title = 'Harry Potter and the Sorcerer''s Stone'
WHERE book_id = 'ca8e64c3-1e67-47f5-82cc-3e4e30f63b75';
