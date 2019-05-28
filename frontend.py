"""
A program that stores book information about
title, author, year of publishing and ISBN
User can view all records, search an entry,
add it, update it, delete it and close
"""
from tkinter import *
import backend


window = Tk()

window.wm_title("BookStore")


def get_selected_row(event):
    try:
        global selected_tuple
        index = list_1.curselection()[0]
        selected_tuple = list_1.get(index)
        entry_1.delete(0, END)
        entry_1.insert(END, selected_tuple[1])
        entry_2.delete(0, END)
        entry_2.insert(END, selected_tuple[2])
        entry_3.delete(0, END)
        entry_3.insert(END, selected_tuple[3])
        entry_4.delete(0, END)
        entry_4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list_1.delete(0, END)
    for row in backend.view():
        list_1.insert(END, row)


def search_command():
    list_1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get()):
        list_1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get())
    list_1.delete(0, END)
    list_1.insert(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get())


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.delete(title_text.get(), author_text.get(), year_text.get(),
                   isbn_text.get())


label_1 = Label(window, text="Title")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Author")
label_2.grid(row=0, column=2)

label_3 = Label(window, text="Year")
label_3.grid(row=1, column=0)

label_4 = Label(window, text="ISBN")
label_4.grid(row=1, column=2)

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text = StringVar()
entry_4 = Entry(window, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

list_1 = Listbox(window, height=6, width=35)
list_1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar_1 = Scrollbar(window  )
scrollbar_1.grid(row=2, column=2, rowspan=6)

list_1.configure(yscrollcommand=scrollbar_1.set)
scrollbar_1.configure(command=list_1.yview())

list_1.bind('<<ListboxSelect>>', get_selected_row)

button_1 = Button(window, text="View All", width=12, command=view_command)
button_1.grid(row=2, column=3)

button_2 = Button(window, text="Search Entry", width=12, command=search_command)
button_2.grid(row=3, column=3)

button_3 = Button(window, text="Add entry", width=12, command=add_command)
button_3.grid(row=4, column=3)

button_4 = Button(window, text="Update Selected", width=12,
                  command=update_command)
button_4.grid(row=5, column=3)

button_5 = Button(window, text="Delete selected", width=12,
                  command=delete_command)
button_5.grid(row=6, column=3)

button_6 = Button(window, text="Close", width=12, command=window.destroy)
button_6.grid(row=7, column=3)


window = mainloop()
