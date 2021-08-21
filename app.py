from book import Book
import utilities as ut
import os
book_store=[]
while True:
    ut.get_menu()
    user_input=input()
    if user_input=='x' or user_input=='X':
        break
    elif user_input=='1':
        book_store.append(ut.create_book())
    elif user_input=='2':
        ut.save_books(book_store)
    elif user_input=='3':
        book_store=ut.load_books()
        print('Loaded successfully...')
    elif user_input=='4':
        res=ut.find_book()
        if type(res)==Book:
            print('Name of the book is {name} and it is written by {author}'.format(name=res.name,author=res.author))
        else:
            print(res)
    elif user_input=='5':
        ut.issue_book(book_store)
    elif user_input=='6':
        ut.return_book(book_store)
    elif user_input=='7':
        ut.show_books(book_store)
    else:
        print('Invalid input!')
    input('\nPress enter to continue...')
    os.system('cls')