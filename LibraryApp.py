from tkinter import *

BookList=[]
window=Tk()


window.title("Book library")
window.geometry("800x800")


label=Label(window,text ="Digital Book Library",font=("Arial",25))
label.pack()


def createBook():
    create=Tk()
    create.title("Create a book")
    create.geometry("800x800")
    label=Label(create,text="Author Name",font=("Arial",8))
    label.pack()
    authorName=Entry(create)
    authorName.pack()
    label3=Label(create,text="Book Name",font=("Arial",8))
    label3.pack()
    bookName=Entry(create)
    bookName.pack()
    label2=Label(create,text="Book Content",font=("Arial",8))
    label2.pack()
    bookContent=Text(create,width=80,height=30)
    bookContent.pack()
    def process():
        name=authorName.get()
        book=bookName.get()
        content=bookContent.get("1.0", "end-1c")
        data=[name,book,content]
        BookList.append(data)
        print(BookList)
        if(name,book,content!=NONE):
            label=Label(create,text="Book Created")
            label.pack()


    button=Button(create,text="CreateBook",command=process)
    button.pack()
def readBook():
    read=Tk()
    read.title("Read a Book")
    read.geometry("800x800")
    if(BookList==None):
        label=Label(read,text="THERE IS NO BOOK")
        label.pack()
    else:
        label=Label(read,text="Books Listed")
        label.pack()
        for index, book_data in enumerate(BookList, start=1):
            author, title, content = book_data  # Unpack book data
            
            # Display book details with labels
            Label(read, text=f"Book {index}", font=("Arial", 10, "bold")).pack(anchor="w")
            Label(read, text=f"Author: {author}", font=("Arial", 10)).pack(anchor="w", padx=20)
            Label(read, text=f"Title: {title}", font=("Arial", 10)).pack(anchor="w", padx=20)
 





readButton=Button(window, text="BookList",width=10,height=5,font=("Arial",8),command=readBook)
readButton.pack()
createButton=Button(window, text="CreateBook",width=10,height=5,command=createBook,font=("Arial",8))
createButton.pack()












window.mainloop()
