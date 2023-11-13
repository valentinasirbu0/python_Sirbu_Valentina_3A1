class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Item ID: {self.item_id}, Checked Out: {self.checked_out}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        return f"{super().display_info()}, Genre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}, Director: {self.director}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, issue_number, item_id):
        super().__init__(title, "N/A", item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}, Issue Number: {self.issue_number}"


book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", item_id="B001", genre="Fiction")
print(book.display_info())
print(book.check_out())
print(book.return_item())

dvd = DVD(title="Inception", director="Christopher Nolan", item_id="D001", duration=148)
print(dvd.display_info())
print(dvd.check_out())
print(dvd.return_item())

magazine = Magazine(title="National Geographic", issue_number="2022-09", item_id="M001")
print(magazine.display_info())
print(magazine.check_out())
print(magazine.return_item())
