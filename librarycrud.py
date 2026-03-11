books=[]
while True:
    print("======== eLibrary ======")
    print("1:AddBooks\n2:ShowBooks\n3:updateBook\n4:DeleteBook\n5:Exit")
    choice=int(input("enter choice number:"))
    if choice==1:
        title=input("enter book title:").capitalize()
        if title not in books:
           books.append(title)
           print("Books added successfully!")
        else:
            print(f"{title} Book is aleready exists so add another book!!")
    elif choice==2:
        if len(books)==0:
             print("No books avilable try again")
        else:
             print("Available books are:", books)
        pass
    elif choice==3:
        if len(books)>0:
            old_book_title=input("enter book title to update:").capitalize() 
            if old_book_title in books:
                new_title=input("Enter Book new title to update:").capitalize()
                books[books.index(old_book_title)]=new_title.capitalize()
                print(f"{old_book_title}Book title Update successfully!!")
            else:
             print(f"{old_book_title} Book Title Not Found try again!!")
        else:
             print("No books Avialable so first add the books!!") 
        
    elif choice==4:
        if len(books)>0:
            old_book_title=input("enter book title to remove:").capitalize() 
            if old_book_title in books:
                books.remove(old_book_title.capitalize())
                print(f"{old_book_title}Book title removed successfully!!")
            else:
             print(f"{old_book_title} Book Title Not Found try again!!")
        else:
             print("No books Avialable so first add the books!!") 
    elif choice==5:
        print("thank for using our services!!")
        break