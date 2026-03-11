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
           pass
    elif choice==4:
        pass
    elif choice==5:
        print("thank for using our services!!")
        break