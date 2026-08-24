# library_system.py    # main file

# Book class
class Book:
    def __init__(self, title, author, book_id, total_copies):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.total_copies = total_copies  # Starting Me All Copies Available hain
        self.available_copies = total_copies
    
    # Book Issue 
    def issue_copy(self):
        if self.available_copies <= 0:
            print("No Copies Available")
            return False
        
        self.available_copies -= 1
        return True
    
    # Book Return And Add in Availability
    def return_copy(self):
        if self.available_copies >= self.total_copies:
            print("All Copies Already Returned")
            return False
        self.available_copies += 1
        return True
    
    # Book Details Display
    def display(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Book ID", self.book_id)
        print("Available", self.available_copies, "/" , self.total_copies)


# Library class
class Library: #Ab yeh class sab books manage karegi + student tracking + search
    def __init__(self):
        self.books = {} # key book_id , value: book object
        self.student_records = {} # key student_name/id , value list of book_ids issued

    # New Book Add Karna
    def add_book(self):
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book_id = input("Enter Book_ID: ")
        total_copies = int(input("Enter Total_Copies: "))

        if book_id in self.books:
            print("Book ID Already Exists")
            return
        new_book = Book(title, author, book_id, total_copies)
        self.books[book_id] = new_book
        print("Book Added Successfully")

    # Book Student ko Issue Karna
    def issue_book(self):
        student_name = input("Enter Student Name: ")
        book_id = input("Enter Book_ID: ")

        if book_id not in self.books:
            print("Book Not Found")
            return
        book = self.books[book_id]
        if book.issue_copy() is True:
            if student_name not in self.student_records:
                self.student_records[student_name] = []
            self.student_records[student_name].append(book_id)
            print(f"Book Issued to {student_name}")

    # Book Return karna 
    def return_book(self):
        student_name = input("Enter Student Name: ")
        book_id = input("Enter Book_ID: ")
        if book_id not in self.books:
            print("Book Not Found")
            return
        book = self.books[book_id]
        if student_name not in self.student_records or book_id not in self.student_records[student_name]:
            print("This Student Did Not Issue this book")
            return
        if book.return_copy() is True:
            self.student_records[student_name].remove(book_id)
            print("Book Returned Successfully")

    # All Availables Books
    def show_all_books(self):
        for book in self.books.values():
            book.display()
            print("---")

    # Book Search By (Title)
    def search_book(self):
        search_title = input("Enter Book_Title for Search: ")
        found = False
        for book in self.books.values():
            if search_title.lower() in book.title.lower():
                book.display()
                found = True
        if not found:
            print("No Book Found")

    # Show Student Books
    def show_student_books(self):
        student_name = input("Enter Student Name: ")
        if student_name not in self.student_records or self.student_records[student_name] == []:
            print("No Books issued to this Student")
            return
        print(f"Books Issued to {student_name}")
        for book_id in self.student_records[student_name]:
            print(f"{book_id}")


    # run() method — Main Menu Loop
    def run(self):
        while True:
            print("Menu Options\n1.Add Book\n2.Issue Book\n3.Return Book\n4.Show All Books\n5.Search Book\n6.Show Student's Books\n7.Exit")

            choice = int(input("Enter Choice Option: "))

            if choice == 1: self.add_book()
            if choice == 2: self.issue_book()
            if choice == 3: self.return_book()
            if choice == 4: self.show_all_books()
            if choice == 5: self.search_book()
            if choice == 6: self.show_student_books()
            if choice == 7: 
                print("GoodBye")
                break

if __name__ == "__main__":
    library = Library()
    library.run()
            
