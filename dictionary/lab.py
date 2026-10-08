library = {
    "T101": {"book_name": "Science", "author": "R.K. Sharma", "available": True},
    "T102": {"book_name": "Math", "author": "S.C. Gupta", "available": True},
    "T103": {"book_name": "Computer", "author": "P. Kumar", "available": False},
    "T104": {"book_name": "Python", "author": "Mark Lutz", "available": True},
    "T105": {"book_name": "Java", "author": "James Gosling", "available": False}
}

for book_id, details in library.items():
    print(book_id, details["book_name"], details["author"])