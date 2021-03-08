book = str(input())
current_book = str(input())

counter = 0
is_book_found = False

while current_book != "No More Books":
    current_book = str(input())
    counter += 1
    if current_book == book:
        is_book_found = True
        print(f"You checked {counter} books and found it.")
        break


if is_book_found == False:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")