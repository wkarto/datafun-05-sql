-- Insert additional authors
INSERT INTO authors (author_id, first_name, last_name, year_born) VALUES
('a1b2c3d4-5678-90ab-cdef-1234567890ab', 'Ernest', 'Hemingway', 1899),
('b2c3d4e5-6789-0abc-def1-234567890abc', 'Mark', 'Twain', 1835),
('c3d4e5f6-7890-1bcd-ef12-34567890abcd', 'Virginia', 'Woolf', 1882),
('d4e5f6g7-8901-2cde-f123-4567890abcde', 'Leo', 'Tolstoy', 1828),
('e5f6g7h8-9012-3def-0123-567890abcdef', 'Gabriel', 'Garcia Marquez', 1927),
('f6g7h8i9-0123-4efg-1234-67890abcdef0', 'James', 'Joyce', 1882),
('g7h8i9j0-1234-5fgh-2345-7890abcdef01', 'Toni', 'Morrison', 1931),
('h8i9j0k1-2345-6ghi-3456-890abcdef012', 'Friedrich', 'Nietzsche', 1844),
('i9j0k1l2-3456-7hij-4567-90abcdef0123', 'Jane', 'Doe', 1970),
('j0k1l2m3-4567-8ijk-5678-0abcdef01234', 'John', 'Smith', 1980);

-- Insert additional books
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('e1f2g3h4-5678-90ab-cdef-1234567890ab', 'The Old Man and the Sea', 1952, 'a1b2c3d4-5678-90ab-cdef-1234567890ab'),
('f2g3h4i5-6789-0abc-def1-234567890abc', 'Adventures of Huckleberry Finn', 1884, 'b2c3d4e5-6789-0abc-def1-234567890abc'),
('g3h4i5j6-7890-1bcd-ef12-34567890abcd', 'Mrs Dalloway', 1925, 'c3d4e5f6-7890-1bcd-ef12-34567890abcd'),
('h4i5j6k7-8901-2cde-f123-4567890abcde', 'War and Peace', 1869, 'd4e5f6g7-8901-2cde-f123-4567890abcde'),
('i5j6k7l8-9012-3def-0123-567890abcdef', 'One Hundred Years of Solitude', 1967, 'e5f6g7h8-9012-3def-0123-567890abcdef'),
('j6k7l8m9-0123-4efg-1234-67890abcdef0', 'Ulysses', 1922, 'f6g7h8i9-0123-4efg-1234-67890abcdef0'),
('k7l8m9n0-1234-5fgh-2345-7890abcdef01', 'Beloved', 1987, 'g7h8i9j0-1234-5fgh-2345-7890abcdef01'),
('l8m9n0o1-2345-6ghi-3456-890abcdef012', 'Thus Spoke Zarathustra', 1883, 'h8i9j0k1-2345-6ghi-3456-890abcdef012'),
('m9n0o1p2-3456-7hij-4567-90abcdef0123', 'Custom Book Title', 2020, 'i9j0k1l2-3456-7hij-4567-90abcdef0123'),
('n0o1p2q3-4567-8ijk-5678-0abcdef01234', 'Another Custom Book', 2021, 'j0k1l2m3-4567-8ijk-5678-0abcdef01234');
