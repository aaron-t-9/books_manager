# Books Manager

A book database management program. Written in Python 3.8.

The program accepts a text file containing books with 6 attributes in the order of: Title, Author, Publisher,
Shelf, Category, and Subject. Each attribute for a given book is separated by a tabbed space, and 
each book is separated by a new line. The program is intended to read a spreadsheet file exported as
a tab delimited text file and saves & writes any user changes to the provided text file. The text file
should be encoded in UTF-16 to minimize errors.

Features a search function that allows the user to search for books of their desired attribute, 
allows them to move books to different shelf locations, and contains unit-tests
and doc-tests to ensure the program works as intended.