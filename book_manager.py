"""
Books Manager

Aaron T.

Written for an Assignment for a Python programming class.
"""


def valid_location_printer():
    """
    Simply prints a list of available locations.

    :param: None, no parameters accepted.
    :return: None, nothing is returned.
    """
    print("\nAvailable shelf locations are 1 - 38, and available locations are: 'Gaby', 'Island', "
          "'Lego', 'Noguchi', 'Reading', and 'Students'.")


def search_results_formatter(search_results: list, key: str, search_query: str):
    """
    Prints a series of strings.

    Formats the search results from a user search in an easy-to-read format and prints the user's
    search results in this format.

    :param search_results: A list.
    :param key: A string.
    :param search_query: A string.
    :precondition: Search_results must be a list containing dictionaries representing books with
                   their respective key, value, pairs.
    :precondition: Key must be a string of one of the six keys representing the attributes
                   of a book.
    :precondition: Search_query should be a string containing the query the user wants to search.
    :postcondition: A series of strings formatted for readability displaying all of the results from
                    the user's search query.
    :return: Nothing is return, various strings are printed.

    >>> test_search_results_author = [{'author': 'Motohiko', 'title': 'Phantom Limb', \
'publisher': 'Mori Art Museum', 'shelf': '12', 'category': 'Art', 'subject': 'Japanese'}]
    >>> test_key = "author"
    >>> test_search_query = "hik"
    >>> search_results_formatter(test_search_results_author, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 1 result(s) for books with Author: 'hik'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Motohiko
    Title: Phantom Limb
    Publisher: Mori Art Museum
    Shelf: 12
    Category: Art
    Subject: Japanese
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 1 result(s) for books with Author: 'hik'.\033[0m
    <BLANKLINE>

    >>> test_search_results_title = [{'author': 'Townsend', \
'title': 'The Growing Pains of Adrian Mole', 'publisher': 'Metheun', 'shelf': '2', 'category': \
'Fiction', 'subject': 'Children'}, {'author': 'Townsend', \
'title': 'The Secret Diary of Adrian Mole aged 13 3/4', 'publisher': 'Metheun', 'shelf': '2', \
'category': 'Fiction', 'subject': 'Children'}]
    >>> test_key = "title"
    >>> test_search_query = "mol"
    >>> search_results_formatter(test_search_results_title, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 2 result(s) for books with Title: 'mol'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Townsend
    Title: The Growing Pains of Adrian Mole
    Publisher: Metheun
    Shelf: 2
    Category: Fiction
    Subject: Children
    <BLANKLINE>
    v----------Result: #2----------v
    Author: Townsend
    Title: The Secret Diary of Adrian Mole aged 13 3/4
    Publisher: Metheun
    Shelf: 2
    Category: Fiction
    Subject: Children
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 2 result(s) for books with Title: 'mol'.\033[0m
    <BLANKLINE>

    >>> test_search_results_publisher = [{'author': 'Wrede', \
'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
'category': 'Fiction', 'subject': 'Fantasy'}, {'author': 'Dozois (ed)', 'title': 'One Million AD', \
'publisher': 'SFBC', 'shelf': '24', 'category': 'Fiction', 'subject': 'SF'}, {'author': 'Wolfe', \
'title': 'The Book of the New Sun', 'publisher': 'SFBC', 'shelf': '9', \
'category': 'Fiction', 'subject': 'SF'}]
    >>> test_key = "publisher"
    >>> test_search_query = "sfbc"
    >>> search_results_formatter(test_search_results_publisher, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 3 result(s) for books with Publisher: 'sfbc'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Wrede
    Title: The Enchanted Forest Chronicles
    Publisher: SFBC
    Shelf: 30
    Category: Fiction
    Subject: Fantasy
    <BLANKLINE>
    v----------Result: #2----------v
    Author: Dozois (ed)
    Title: One Million AD
    Publisher: SFBC
    Shelf: 24
    Category: Fiction
    Subject: SF
    <BLANKLINE>
    v----------Result: #3----------v
    Author: Wolfe
    Title: The Book of the New Sun
    Publisher: SFBC
    Shelf: 9
    Category: Fiction
    Subject: SF
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 3 result(s) for books with Publisher: 'sfbc'.\033[0m
    <BLANKLINE>

    >>> test_search_results_shelf = [{'author': 'Larson and Pridmore', \
'title': 'Chicago Architecture and Design', 'publisher': 'Abrams', 'shelf': 'Noguchi', \
'category': 'Architecture', 'subject': 'American Architecture'}, {'author': 'Wiseman', \
'title': 'I. M. Pei A Profile in American Architecture', 'publisher': 'Abrams', \
'shelf': 'Noguchi', 'category': 'Architecture', 'subject': 'American Architecture'}, \
{'author': 'Polkonen (ed) et al', 'title': 'Eero Saarinen Shaping the Future', \
'publisher': 'Yale University Press', 'shelf': 'Noguchi', 'category': 'Architecture', \
'subject': 'Architecture'}, {'author': 'Crow', 'title': 'Nancy Crow', \
'publisher': 'Breckling Press', 'shelf': 'Noguchi', 'category': 'Art', 'subject': 'Quilting'}]
    >>> test_key = "shelf"
    >>> test_search_query = "no"
    >>> search_results_formatter(test_search_results_shelf, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 4 result(s) for books with Shelf: 'no'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Larson and Pridmore
    Title: Chicago Architecture and Design
    Publisher: Abrams
    Shelf: Noguchi
    Category: Architecture
    Subject: American Architecture
    <BLANKLINE>
    v----------Result: #2----------v
    Author: Wiseman
    Title: I. M. Pei A Profile in American Architecture
    Publisher: Abrams
    Shelf: Noguchi
    Category: Architecture
    Subject: American Architecture
    <BLANKLINE>
    v----------Result: #3----------v
    Author: Polkonen (ed) et al
    Title: Eero Saarinen Shaping the Future
    Publisher: Yale University Press
    Shelf: Noguchi
    Category: Architecture
    Subject: Architecture
    <BLANKLINE>
    v----------Result: #4----------v
    Author: Crow
    Title: Nancy Crow
    Publisher: Breckling Press
    Shelf: Noguchi
    Category: Art
    Subject: Quilting
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 4 result(s) for books with Shelf: 'no'.\033[0m
    <BLANKLINE>

    >>> test_search_results_category = [{'author': 'Time', 'title': 'Lighting and Electricity', \
'publisher': 'Time-Life Books', 'shelf': '5', 'category': 'Home', 'subject': 'Electricity'}, \
{'author': 'Gore', 'title': '2001 Household Hints & Dollar Stretchers', \
'publisher': 'Hanover House', 'shelf': '9', 'category': 'Home economics', 'subject': 'History'}]
    >>> test_key = "category"
    >>> test_search_query = "hom"
    >>> search_results_formatter(test_search_results_category, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 2 result(s) for books with Category: 'hom'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Time
    Title: Lighting and Electricity
    Publisher: Time-Life Books
    Shelf: 5
    Category: Home
    Subject: Electricity
    <BLANKLINE>
    v----------Result: #2----------v
    Author: Gore
    Title: 2001 Household Hints & Dollar Stretchers
    Publisher: Hanover House
    Shelf: 9
    Category: Home economics
    Subject: History
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 2 result(s) for books with Category: 'hom'.\033[0m
    <BLANKLINE>

    >>> test_search_results_subject = [{'author': 'Gorey', 'title': 'The Gashleycrumb Tinies', \
'publisher': 'Harcourt Brace & Co', 'shelf': '18', 'category': 'Fiction', 'subject': 'Cartoon'}, \
{'author': 'K', 'title': 'Caribbean Cuisine', 'publisher': 'Centax Books', 'shelf': '9', \
'category': 'Food', 'subject': 'Caribbean'}]
    >>> test_key = "subject"
    >>> test_search_query = "car"
    >>> search_results_formatter(test_search_results_subject, test_key, test_search_query)
    <BLANKLINE>
    \033[1mThere are a total of 2 result(s) for books with Subject: 'car'.\033[0m
    <BLANKLINE>
    v----------Result: #1----------v
    Author: Gorey
    Title: The Gashleycrumb Tinies
    Publisher: Harcourt Brace & Co
    Shelf: 18
    Category: Fiction
    Subject: Cartoon
    <BLANKLINE>
    v----------Result: #2----------v
    Author: K
    Title: Caribbean Cuisine
    Publisher: Centax Books
    Shelf: 9
    Category: Food
    Subject: Caribbean
    <BLANKLINE>
    ---------------------------------
    \033[1mThere are a total of 2 result(s) for books with Subject: 'car'.\033[0m
    <BLANKLINE>
    """
    num_of_results = len(search_results)
    print("\n\033[1m" f"There are a total of {num_of_results} result(s)"
          f" for books with {key.capitalize()}: '{search_query}'." "\033[0m\n")
    for list_num, search_results in enumerate(search_results, 1):
        print(f"v----------Result: #{list_num}----------v")
        print(f"Author: {search_results['author']}")
        print(f"Title: {search_results['title']}")
        print(f"Publisher: {search_results['publisher']}")
        print(f"Shelf: {search_results['shelf']}")
        print(f"Category: {search_results['category']}")
        print(f"Subject: {search_results['subject']}\n")

    print("---------------------------------")
    print("\033[1m" f"There are a total of {num_of_results} result(s)"
          f" for books with {key.capitalize()}: '{search_query}'." "\033[0m\n")


def user_search_handler(book_collection: tuple, search_menu_user_choice: str) -> list:
    """
    Returns a list of the user's search results.

    Based on the user's choice of searching, conditional statements call on appropriate helper
    search functions. The list returned contains numerous dictionaries of books.

    :param book_collection: A tuple of dictionaries.
    :param search_menu_user_choice: A string.
    :precondition: Book_collection is a tuple of dictionaries of books with their attributes stored
                   as key, value, pairs.
    :precondition: Search_menu_user_choice is a string containing an integer from 1-6
                   with each number representing the key the user would like to search for.
    :postcondition: A list representing the search_results is returned, and the correct search
                    helper function is called.
    :return: A list containing dictionaries of books.
    """

    if search_menu_user_choice == "1":
        search_results = search_by_author(book_collection)

    elif search_menu_user_choice == "2":
        search_results = search_by_title(book_collection)

    elif search_menu_user_choice == "3":
        search_results = search_by_publisher(book_collection)

    elif search_menu_user_choice == "4":
        search_results = search_by_shelf(book_collection)

    elif search_menu_user_choice == "5":
        search_results = search_by_category(book_collection)

    elif search_menu_user_choice == "6":
        search_results = search_by_subject(book_collection)

    # search_results is producing a format Pycharm error,
    # But the variable is always assigned before reference.
    return search_results


def search_engine(book_collection: tuple, key: str, search_query: str) -> list:
    """
    Returns a list of dictionaries containing the books the user has searched for.

    Loops through the entire tuple of dictionaries of books and appends the dictionary's of books
    that match the user's search query to a list. This list of dictionaries is then returned.

    :param book_collection: A tuple of dictionaries.
    :param key: A string.
    :param search_query: A string.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :precondition: Key must be a string of one of the six keys representing the attributes
                   of a book.
    :precondition: Search_query should be a string containing the value the user wants to search.
    :postcondition: A list of dictionaries containing the matching books are returned within a list.
    :return: A list of dictionaries of books.

    >>> book_collection_empty_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles',   'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "title"
    >>> test_search_query = ""
    >>> search_engine(book_collection_empty_query, test_key, test_search_query)
    [{'author': 'Wrede', \
'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> book_collection_search_author_full_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '2', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "author"
    >>> test_search_query = "wrede"
    >>> search_engine(book_collection_search_author_full_query, test_key, test_search_query)
    [{'author': 'Wrede', 'title': 'The Enchanted Forest Chronicles', \
'publisher': 'SFBC', 'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}]

    >>> book_collection_search_author_partial_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '2', \
'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "author"
    >>> test_search_query = "en"
    >>> search_engine(book_collection_search_author_partial_query, test_key, test_search_query)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '2', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> book_collection_search_shelf_full_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "shelf"
    >>> test_search_query = "lego"
    >>> search_engine(book_collection_search_shelf_full_query, test_key, test_search_query)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}]

    >>> book_collection_search_shelf_partial_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "shelf"
    >>> test_search_query = "no"
    >>> search_engine(book_collection_search_shelf_partial_query, test_key, test_search_query)
    [{'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> book_collection_search_publisher_full_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "publisher"
    >>> test_search_query = "california"
    >>> search_engine(book_collection_search_publisher_full_query, test_key, test_search_query)
    [{'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> book_collection_search_publisher_partial_query = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> test_key = "publisher"
    >>> test_search_query = "i"
    >>> search_engine(book_collection_search_publisher_partial_query, test_key, test_search_query)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]
    """
    search_results = []
    for item in book_collection:
        if search_query in item[key].lower():
            search_results.append(item)

    return search_results


def search_by_author(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the user's search query for the name, or
    partial name, of the author of a book.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books matching the search results for
                    the name of the author inputted by the user.
    :return: A list of dictionaries.
    """
    search_query = input("Please enter the name of the author of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "author", search_query)
    search_results_formatter(search_results, "author", search_query)

    return search_results


def search_by_title(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the user's search query for the title, or
    partial title, of a book.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books matching the search results for
                    the title of the book inputted by the user.
    :return: A list of dictionaries.
    """
    search_query = input("Please enter the title of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "title", search_query)
    search_results_formatter(search_results, "title", search_query)

    return search_results


def search_by_publisher(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the user's search query for the publisher,
    or partial name of the publisher, for a book.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books matching the search results for
                    the publisher of the book inputted by the user.
    :return: A list of dictionaries.
    """
    search_query = input("Please enter the publisher of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "publisher", search_query)
    search_results_formatter(search_results, "publisher", search_query)

    return search_results


def search_by_shelf(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the shelf, or location, that a book is
    currently located at.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books matching the search results for
                    the shelf, or location, selected by the user.
    :return: A list of dictionaries.

    """
    search_query = input("Please enter the location/shelf of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "shelf", search_query)
    search_results_formatter(search_results, "shelf", search_query)

    return search_results


def search_by_category(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the category, or partially matches the
    category, of a book.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books matching the search results for
                    the category of a book inputted by the user.
    :return: A list of dictionaries.

    """
    search_query = input("Please enter the category of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "category", search_query)
    search_results_formatter(search_results, "category", search_query)

    return search_results


def search_by_subject(book_collection: tuple) -> list:
    """
    Returns a list of dictionaries containing the user's search results.

    Returns a list of dictionaries of books that matches the subject, or partially matches the
    subject, of a book.

    :param book_collection: A tuple of dictionaries.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :postcondition: A list of dictionaries containing the books that match the user inputted subject
                    for a book.
    :return: A list of dictionaries.

    """
    search_query = input("Please enter the subject of the"
                         " book you would like to search for: ").strip().lower()
    search_results = search_engine(book_collection, "subject", search_query)
    search_results_formatter(search_results, "subject", search_query)

    return search_results


def get_valid_location(book_collection: tuple) -> list:
    """
    Returns a set containing valid locations.

    Iterates through the tuple of dictionaries of books and creates a set of all of the values
    associated with the "shelf" key. The set is then casted as a list and is sorted.

    :param book_collection: A tuple of dictionaries.
    :precondition: A tuple of dictionaries containing a list of all of the books along with their
                   attributes stored as key, value, pairs.
    :postcondition: A list containing all unique locations.
    :return: A list.

    >>> book_collection_empty = ()
    >>> get_valid_location(book_collection_empty)
    []

    >>> book_collection_no_overlap = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
    'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '2', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> get_valid_location(book_collection_no_overlap)
    ['2', '30', 'Lego']

    >>> book_collection_overlap = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
    'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '30', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> get_valid_location(book_collection_overlap)
    ['30', 'Lego']

    >>> book_collection_strings_no_overlap = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': 'Gaby', \
    'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> get_valid_location(book_collection_strings_no_overlap)
    ['Gaby', 'Lego', 'Noguchi']

    >>> book_collection_strings_overlap = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': 'Noguchi', \
    'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'})
    >>> get_valid_location(book_collection_strings_overlap)
    ['Lego', 'Noguchi']
    """
    valid_locations = set()
    for item in book_collection:
        valid_locations.add(item["shelf"].capitalize())

    return sorted(list(valid_locations))


def is_valid_location(valid_locations: list) -> str:
    """
    Returns a string representing the validated new location for a book.

    Checks to ensure that the new location specified by the user is a valid location that a book
    can be moved to.

    :param valid_locations: A list.
    :precondition: A set that contains all of the valid locations that a book can be moved to.
    :postcondition: The user specified location is validated and returned.
    :return: A string representing a valid location.
    """
    new_location = input("Please enter the number associated with the shelf/location you would "
                         "like to move the book to: ").strip().lower().capitalize()
    if new_location in valid_locations:
        return new_location
    else:
        new_location = "invalid"
        return new_location


def move_book(book_collection: tuple, search_results: list, book_to_move: int, new_location: str):
    """
    Prints a string.

    Moves the selected book specified by the user to a new location specified by the user. A
    string is printed containing helpful information, including the old and new location of the
    book.

    :param book_collection: A tuple of dictionaries.
    :param search_results: A list.
    :param book_to_move: A string.
    :param new_location: A string.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :precondition: Search_results must be a list containing dictionaries representing books with
                   their respective key, value, pairs.
    :precondition: Book_to_move must be an integer in a string representing the index of the book
                   from the list search_results.
    ;precondition: New_location must be a string that represents a valid location that a book can
                   be moved too.
    :postcondition: Moves the specified book to the specified location. Prints a string containing
                    helpful information including the new and old location of the book.
    :return: Nothing is returned, a string is printed displaying helpful information.

    >>> book_collection_num_location_books = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
    'category': 'Fiction', 'subject': 'Fantasy'} ,\
    {'author': 'Steven Jobs', 'title': 'Apple and Oranges', 'publisher': 'California', \
    'shelf': '2', 'category': 'Technology', 'subject': 'Biography'})
    >>> test_search_results = [{'author': 'Steven Jobs', 'title': 'Apple and Oranges', \
    'publisher': 'California', 'shelf': '2', 'category': 'Technology', 'subject': 'Biography'}]
    >>> test_book_to_move = 1
    >>> test_new_location = "1"
    >>> move_book(book_collection_num_location_books, test_search_results, test_book_to_move, \
    test_new_location)
    <BLANKLINE>
    \033[1mThe book 'Apple and Oranges' by Steven Jobs has been moved from \
the shelf/location: 2, to the shelf/location: 1.\033[0m
    <BLANKLINE>

    >>> book_collection_num_location_books = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
    'category': 'Fiction', 'subject': 'Fantasy'} ,\
    {'author': 'Steven Jobs', 'title': 'Apple and Oranges', 'publisher': 'California', \
    'shelf': '2', 'category': 'Technology', 'subject': 'Biography'})
    >>> test_search_results = [{'author': 'Wrede', 'title': 'The Enchanted Forest Chronicles', \
'publisher': 'SFBC', 'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}]
    >>> test_book_to_move = 1
    >>> test_new_location = "38"
    >>> move_book(book_collection_num_location_books, test_search_results, \
    test_book_to_move, test_new_location)
    <BLANKLINE>
    \033[1mThe book 'The Enchanted Forest Chronicles' by Wrede has been moved from \
the shelf/location: 30, to the shelf/location: 38.\033[0m
    <BLANKLINE>

    >>> book_collection_invalid = ({'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', 'shelf': '30', \
    'category': 'Fiction', 'subject': 'Fantasy'} ,\
    {'author': 'Steven Jobs', 'title': 'Apple and Oranges', 'publisher': 'California', \
    'shelf': '2', 'category': 'Technology', 'subject': 'Biography'})
    >>> test_search_results = [{'author': 'Wrede', 'title': 'The Enchanted Forest Chronicles', \
'publisher': 'SFBC', 'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}]
    >>> test_book_to_move = 1
    >>> test_new_location = "invalid"
    >>> move_book(book_collection_invalid, test_search_results, \
    test_book_to_move, test_new_location)
    <BLANKLINE>
    Invalid location selected.
    <BLANKLINE>
    """
    if new_location == "invalid":
        print("\nInvalid location selected.\n")
        return
    else:
        book_index = book_collection.index(search_results[book_to_move - 1])
        moved_book = book_collection[book_index]
        old_location = search_results[book_to_move - 1]['shelf']
        book_collection[book_index]["shelf"] = new_location

        print("\n\033[1m" f"The book '{moved_book['title']}' by {moved_book['author']} "
              f"has been moved from the shelf/location: {old_location}, "
              f"to the shelf/location: {book_collection[book_index]['shelf']}." "\033[0m\n")


def move_book_handler(book_collection: tuple, valid_locations: list):
    """
    Returns nothing. Accepts user input.

    Handles, and drives, the book moving system. Calls on a series of helper functions.

    :param book_collection: A tuple of dictionaries.
    :param valid_locations: A list.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :precondition: A set that contains all of the valid locations that a book can be moved to.
    :postcondition: Calls helper functions and runs the system to a books to new a location.
    :return: Nothing is returned, strings are printed.
    """
    search_menu_user_choice = menu_generator("search_menu")
    search_menu_user_choice = valid_user_input("search_menu", search_menu_user_choice)

    if search_menu_user_choice == "invalid":
        print("\nInvalid menu option selected.\n")
        return

    search_results = user_search_handler(book_collection, search_menu_user_choice)
    if len(search_results) == 0:
        print("No results found!\n")
        return

    book_to_move = input("Which book would you like to move (enter the result number): ").strip()
    if not book_to_move.isdigit():
        print("\nPlease enter a valid number!\n")
        return

    book_to_move = int(valid_user_input("move_menu", book_to_move, search_results))
    if book_to_move == -1:
        print("\nPlease enter a valid number!\n")
        return

    valid_location_printer()
    new_location = is_valid_location(valid_locations)
    move_book(book_collection, search_results, book_to_move, new_location)


def menu_generator(menu_type: str) -> str:
    """
    Prints a series of strings containing menu options.

    Handles the printing of the different menus that the user can choose from. Returns the menu
    selection that the user has inputted.

    :param menu_type: A string.
    :precondition: A string that is either "main_menu" or "search_menu" that prints different menus
                   based on the user's choice of what they would like the program to do.
    :postcondition: A series of strings are printed displaying the different options the user can
                    select from. The user's input is returned as a string.
    :results: A string representing the user's input is returned.
    """
    if menu_type == "main_menu":
        print("What would you like to do?")
        print("1: Find book(s).")
        print("2: Move a book.")
        print("3: Exit the program.")
        return input("Please enter a number between 1 and 3: ")

    elif menu_type == "search_menu":
        print("1: Author")
        print("2: Title")
        print("3: Publisher")
        print("4: Shelf")
        print("5: Category")
        print("6: Subject")
        return input("I would like to search by (enter number): ")


def valid_user_input(menu_type: str, user_selection: str, *args: list) -> str:
    """
    Returns a string containing the validated user's choice.

    Handles checking the user's input for any errors, prints a helpful error message, and prompts
    the user for input until valid input is provided. Returns the validated user input as a string.

    :param menu_type: A string.
    :param user_selection: A string
    :param args: A list.
    :precondition: Menu_type must be a string containing the type of menu that the user has
                   selected. it must be either "main_menu", "search_menu", or "move_menu".
    :precondition: User_selection must be a string representing the user's input.
    :precondition: *args must be a list containing the search results from the user's query. This
                    parameter is only used for "move_menu" and is not always required or available.
    :postcondition: The user's input is validated based on the menu that they are in, and their
                    validated input is returned.
    :return: A string containing validated user input.

    >>> test_menu_type_main_menu = "main_menu"
    >>> test_user_selection = "1"
    >>> valid_user_input(test_menu_type_main_menu, test_user_selection)
    '1'

    >>> test_menu_type_main_menu = "main_menu"
    >>> test_user_selection = "2"
    >>> valid_user_input(test_menu_type_main_menu, test_user_selection)
    '2'

    >>> test_menu_type_main_menu = "main_menu"
    >>> test_user_selection = "3"
    >>> valid_user_input(test_menu_type_main_menu, test_user_selection)
    '3'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "1"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '1'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "2"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '2'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "3"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '3'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "4"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '4'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "5"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '5'

    >>> test_menu_type_search_menu = "search_menu"
    >>> test_user_selection = "6"
    >>> valid_user_input(test_menu_type_search_menu, test_user_selection)
    '6'

    >>> test_menu_type_search_menu_invalid = "search_menu"
    >>> test_invalid_user_selection = "9"
    >>> valid_user_input(test_menu_type_search_menu_invalid, test_invalid_user_selection)
    'invalid'

    >>> test_menu_type_search_menu_invalid = "search_menu"
    >>> test_invalid_user_selection = "author"
    >>> valid_user_input(test_menu_type_search_menu_invalid, test_invalid_user_selection)
    'invalid'

    >>> test_menu_type_search_menu_invalid = "search_menu"
    >>> test_invalid_user_selection = "0"
    >>> valid_user_input(test_menu_type_search_menu_invalid, test_invalid_user_selection)
    'invalid'

    >>> test_menu_type_search_menu_invalid = "search_menu"
    >>> test_invalid_user_selection = "-3"
    >>> valid_user_input(test_menu_type_search_menu_invalid, test_invalid_user_selection)
    'invalid'
    """
    incorrect_input = True
    while incorrect_input:

        if menu_type == "main_menu":
            if user_selection in ["1", "2", "3"]:
                incorrect_input = False
            else:
                user_selection = input("Please select a number from 1 to 3: ").strip().lower()

        elif menu_type == "search_menu":
            if user_selection in ["1", "2", "3", "4", "5", "6"]:
                incorrect_input = False
            else:
                search_menu_user_choice = "invalid"
                return search_menu_user_choice

        elif menu_type == "move_menu":
            if user_selection in list(map(str, range(1, len(*args) + 1))):
                incorrect_input = False
            else:
                user_selection = "-1"
                return user_selection

    return user_selection


def menu(book_collection: tuple, valid_locations: list, filename: str):
    """
    Prints multiple strings.

    Responsible for running the program. Prints strings that contains the options that the user
    can select from. The strings printed are dependant on the menu options that the user chooses
    from.

    :param book_collection: A tuple of dictionaries.
    :param valid_locations: A set.
    :param filename: A string.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :precondition: Valid_location is a set containing all of the different values of the shelf key.
    :precondition: A string representing the name of the file that the user wants to open and edit.
    :postcondition: Prints multiple strings representing menu options based on user input.
    :return: Prints multiple strings.
    """
    continue_program = True

    while continue_program:
        user_choice = menu_generator("main_menu")
        user_choice = valid_user_input("main_menu", user_choice)

        if user_choice == "1":
            print("How would you like to search for your book?")
            search_menu_user_choice = menu_generator("search_menu")
            search_menu_user_choice = valid_user_input("search_menu", search_menu_user_choice)

            if search_menu_user_choice == "invalid":
                print("\nInvalid menu option selected.\n")
            else:
                user_search_handler(book_collection, search_menu_user_choice)

        elif user_choice == "2":
            print("\nHow would you like to search for the book that you would like to move?")
            move_book_handler(book_collection, valid_locations)

        elif user_choice == "3":
            print("\nAny changes you may have made has been saved. "
                  "Thank you for using YourBookManager\u2122, goodbye.")
            quit_program(book_collection, filename)
            continue_program = False


def book_collection_empty_value_checker(temp_list: list) -> list:
    """
    Returns a list of dictionaries.

    Checks the key, value, pairs of dictionaries of books for empty values, and replaces the empty
    values with the string "None". This updated list of dictionaries of books is then returned.

    :param temp_list: A list of dictionaries.
    :precondition: A list of dictionaries of books containing the six key, value, pairs of a book.
    :postcondition: A list of dictionaries with empty values replaced with "None".
    :return: A list of dictionaries.

    >>> temp_list_two_empty = []
    >>> book_collection_empty_value_checker(temp_list_two_empty)
    []

    >>> temp_list_all_empty_shelves = [{'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': '', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': '', \
    'category': 'Technology', 'subject': 'Biography'}]
    >>> book_collection_empty_value_checker(temp_list_all_empty_shelves)
    [{'author': 'Wrede', \
'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
'shelf': 'None', 'category': 'Fiction', 'subject': 'Fantasy'}, \
{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'None', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'None', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> temp_list_all_empty_title = [{'author': 'Wrede', \
    'title': '', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': '', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': '', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'}]
    >>> book_collection_empty_value_checker(temp_list_all_empty_title)
    [{'author': 'Wrede', \
'title': 'None', 'publisher': 'SFBC', \
'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
{'author': 'Ramen Noodles', 'title': 'None', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'None', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> temp_list_one_empty_category = [{'author': 'Wrede', \
    'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': '', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
    'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'}]
    >>> book_collection_empty_value_checker(temp_list_one_empty_category)
    [{'author': 'Wrede', \
'title': 'The Enchanted Forest Chronicles', 'publisher': 'SFBC', \
'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'None', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]

    >>> temp_list_two_empty_subjects_and_title = [{'author': '', \
    'title': '', 'publisher': 'SFBC', \
    'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
    {'author': 'Ramen Noodles', 'title': '', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
    'category': 'Food', 'subject': 'Sustenance'}, {'author': '', \
    'title': '', 'publisher': 'California', 'shelf': 'Noguchi', \
    'category': 'Technology', 'subject': 'Biography'}]
    >>> book_collection_empty_value_checker(temp_list_two_empty_subjects_and_title)
    [{'author': 'None', \
'title': 'None', 'publisher': 'SFBC', \
'shelf': '30', 'category': 'Fiction', 'subject': 'Fantasy'}, \
{'author': 'Ramen Noodles', 'title': 'None', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', 'subject': 'Sustenance'}, {'author': 'None', \
'title': 'None', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}]
    """
    for book in temp_list:
        for key in book:
            if book[key] == '':
                book[key] = "None"

    return temp_list


def remove_first_entry_dupe_key_value(temp_list: list) -> list:
    """
    Returns a list of dictionaries.

    Checks the key, value, pairs for the first entry in the list of dictionaries, and removes the
    first entry if the key and value are identical. This removes the first line in book collection
    text file from user search queries.

    :param temp_list: A list of dictionaries.
    :precondition: A list of dictionaries of books containing the six key, value, pairs of a book.
    :postcondition: A list of dictionaries without dictoinaries with identical key, value, pairs.
    :return: A list of dictionaries.

    >>> test_temp_list_empty = []
    >>> remove_first_entry_dupe_key_value(test_temp_list_empty)
    []

    >>> test_temp_list_only_duplicates = [{'author': 'author', 'title': 'title', \
'publisher': 'publisher', 'shelf': 'shelf', 'category': 'category', 'subject': 'subject'}]
    >>> remove_first_entry_dupe_key_value(test_temp_list_only_duplicates)
    []

    >>> test_temp_list_only_valid_book = [{'author': 'Ramen Noodles', 'title': 'Top Ramen', \
'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food', 'subject': 'Sustenance'}]
    >>> remove_first_entry_dupe_key_value(test_temp_list_only_valid_book)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', \
'shelf': 'Lego', 'category': 'Food', 'subject': 'Sustenance'}]

    >>> test_temp_list_only_valid_book_and_dupe = [{'author': 'author', 'title': 'title', \
'publisher': 'publisher', 'shelf': 'shelf', 'category': 'category', 'subject': 'subject'}, \
{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', \
'category': 'Food', \
'subject': 'Sustenance'}]
    >>> remove_first_entry_dupe_key_value(test_temp_list_only_valid_book_and_dupe)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', \
'shelf': 'Lego', 'category': 'Food', 'subject': 'Sustenance'}]

    >>> test_temp_list_dupe_book_second_index = [{'author': 'Ramen Noodles', \
'title': 'Top Ramen', 'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food', \
'subject': 'Sustenance'}, {'author': 'author', 'title': 'title', 'publisher': 'publisher', \
'shelf': 'shelf', 'category': 'category', 'subject': 'subject'}]
    >>> remove_first_entry_dupe_key_value(test_temp_list_dupe_book_second_index)
    [{'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', \
'shelf': 'Lego', 'category': 'Food', 'subject': 'Sustenance'}, {'author': 'author', \
'title': 'title', 'publisher': 'publisher', 'shelf': 'shelf', 'category': 'category', \
'subject': 'subject'}]
    """
    if len(temp_list) > 0:
        if temp_list[0]["author"].lower() in temp_list[0].keys():
            del temp_list[0]

    return temp_list


def book_dict_append(list_of_attributes: list) -> tuple:
    """
    Returns a tuple of dictionaries.

    Accepts a list of a lists containing the attributes of various books. The keys are:
    author, title, publisher, shelf, category, and subject. The values of each book are then paired
    with their respective keys. Various helper functions are called to clean up the dictionaries of
    books.

    :param list_of_attributes: A list of lists.
    :precondition: A list of lists containing strings of the six attributes of each book.
    :postcondition: A tuple of dictionaries containing the six attributes as keys, and each value
                    containing the respective information of each attribute/key.
    :return: A tuple of dictionaries.

    >>> test_list_of_attr_empty = []
    >>> book_dict_append(test_list_of_attr_empty)
    ()

    >>> test_list_of_attr_single_book = [['Ramen Noodles', 'Top Ramen', 'Nong Shim', 'Island', \
'Food', 'Sustenance']]
    >>> book_dict_append(test_list_of_attr_single_book)
    ({'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', \
'shelf': 'Island', 'category': 'Food', 'subject': 'Sustenance'},)

    >>> test_list_of_attr_three_books = [['Ramen Noodles', 'Top Ramen', 'Nong Shim', 'Island', \
'Food', 'Sustenance'], ['Steven Jobs', 'Apple and Oranges', 'California', 'Noguchi', 'Technology', \
'Biography'], ['Gamefreak', 'Pokemon', 'Nintendo', '33', 'Video Games', 'Walkthrough']]
    >>> book_dict_append(test_list_of_attr_three_books)
    ({'author': 'Ramen Noodles', 'title': 'Top Ramen', 'publisher': 'Nong Shim', \
'shelf': 'Island', 'category': 'Food', 'subject': 'Sustenance'}, {'author': 'Steven Jobs', \
'title': 'Apple and Oranges', 'publisher': 'California', 'shelf': 'Noguchi', \
'category': 'Technology', 'subject': 'Biography'}, {'author': 'Gamefreak', 'title': 'Pokemon', \
'publisher': 'Nintendo', 'shelf': '33', 'category': 'Video Games', 'subject': 'Walkthrough'})


    """
    temp_list = []
    for attr_list in list_of_attributes:
        temp_dict = {"author": attr_list[0], "title": attr_list[1], "publisher": attr_list[2],
                     "shelf": attr_list[3], "category": attr_list[4],
                     "subject": attr_list[5].strip()}
        temp_list.append(temp_dict)

    temp_list = remove_first_entry_dupe_key_value(temp_list)
    temp_list = book_collection_empty_value_checker(temp_list)
    book_collection = tuple(temp_list)

    return book_collection


def quit_program(book_collection: tuple, filename: str):
    """
    Exits the program and saves the collection of books managed and edited by this program.

    Adds the dictionary with identical keys and values back to the top of the file. Writes the
    list of dictionaries in the same format that it is read in.

    :param book_collection: A tuple of dictionaries.
    :param filename: A string representing the filename that the program will write too.
    :precondition: Book_collection is a tuple of dictionaries of books with their
                   attributes stored as key, value, pairs.
    :precondition: Filename should be a string representing the same filename that was opened.
    :postcondition: Writes a new file containing the tuple of dictionaries of books formatted in the
                    same style of the original file.
    :return: Nothing is returned.
    """
    with open(filename, 'w', encoding="UTF-16") as file_object:
        file_object.write("Author\tTitle\tPublisher\tShelf\tCategory\tSubject\t\n")

        for book in book_collection:
            for key in book:

                if key.lower() == "subject":
                    file_object.write(book[key])
                    file_object.write("\t\n")
                else:
                    file_object.write(book[key])
                    file_object.write("\t")


def get_info(filename: str) -> list:
    """
    Reads the specified text file and returns a list of lists.

    Reads the file specified by the user line by line, splits the items in the file based on tabbed
    spaces, and appends them to a list.

    :param filename: A string.
    :precondition: A string representing the name of the text file that the user would like to open
                   and manage.
    :precondition: The string is case-sensitive, space-sensitive, and must include the file
                   extension.
    :precondition: The text file must be located in the same directory as this program, and the name
                   of the text file must be inputted correctly.
    :precondition: The text file must be encoded in a UTF-16 format.
    :precondition: The text file must contain the six key, value, pairs of a book.
    :postcondition: A list is created from the text file containing a list of the six key, value
                    attributes of each book.
    :return: Returns a list of lists.
    """
    try:
        with open(filename, encoding="UTF-16") as file_object:
            temp_book = []
            for line in file_object:
                temp_book.append(line.split("\t"))
    except FileNotFoundError:
        print("File not found!")
        exit()
    else:
        return temp_book


def books():
    """
    Runs the books program.

    Handles calling the other functions to run the program. Responsible for handling the entire
    program.

    :param: No parameters accepted.
    :return: Nothing is returned.
    """
    print("\nHello, welcome to YourBookManager\u2122 v1.0.\n")
    filename = input("Please enter the name of the file containing your book library: ")
    temp_book = get_info(filename)
    book_collection = book_dict_append(temp_book)
    valid_locations = get_valid_location(book_collection)
    menu(book_collection, valid_locations, filename)


def main():
    """Drives the program."""
    books()


if __name__ == "__main__":
    main()
