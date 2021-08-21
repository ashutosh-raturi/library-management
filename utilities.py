from book import Book
import json
def get_menu():
    print('Press 1 to add a new book')
    print('Press 2 to save books')
    print('Press 3 to load books')
    print('Press 4 to find a book')
    print('Press 5 to issue a book')
    print('Press 6 to return a book')
    print('Press 7 to show books')
    print('Press x to exit')
    print('\nEnter your choice :', end=' ')


def create_book():
    id=int(input('ID: '))
    name=input("Name of the book: ")
    description=input('Description: ')
    isbn=input('ISBN: ')
    page_count=int(input('Page count: '))
    issued=False
    author=input('Author name: ')
    year=input('Year of publication: ')
    book=Book(id,name,description,isbn,page_count,issued,author,year)
    return book


def save_books(book_store):
    books_dicts=[book.to_dict() for book in book_store]
    try:
        with open('library.dat','w') as file:
            file.write(json.dumps(books_dicts,indent=5))
            print('Saved successfully...')
    except:
        print('Something went wrong!') 


def load_books():
    try:
        with open('library.dat','r') as file:
            book_dicts=json.loads(file.read())
            books=[Book(book['id'],book['name'],book['description'],book['isbn'],book['page_count'],book['issued'],book['author'],book['year']) for book in book_dicts]
            return books
    except:
        print('Something went wrong!')   


def find_book():
    id=int(input('Enter ID: '))
    try:
        with open('library.dat','r') as file:
            book_dicts=json.loads(file.read())
            for book in book_dicts:
                if book['id']==id:
                    return Book(book['id'],book['name'],book['description'],book['isbn'],book['page_count'],book['issued'],book['author'],book['year'])
            return 'Book with id {id} not found'.format(id=id)
    except:
        print('Something went wrong!')


def issue_book(books):
    id=int(input('Enter ID: '))
    for book in books:
        if book.id==id:
            if book.issued==False:
                book.issued=True
                print('Issued successfully...')
            else:
                print('Book is already issued to someone else!')
            return
    print('Book with id {id} not found'.format(id=id))


def return_book(books):
    id=int(input('Enter ID: '))
    for book in books:
        if book.id==id:
            if book.issued==True:
                book.issued=False
                print('Returned successfully...')
            return
    print('Book with id {id} not found'.format(id=id))


def show_books(books):
    for book in books:
        print('ID: ',book.id)
        print('Name :',book.name)
        print('Author: ',book.author)
        print('-------------------------------')