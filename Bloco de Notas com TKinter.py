# -*- coding: utf-8 -*-

# Import libraries
import tkinter

# Crete a TKinter window
window = tkinter.Tk()
# Properties of the window

# Functions
def new_file():
    text_area.delete(1.0,'end')

def save():
    text = text_area.get(1.0,'end')
    file_save = open('file.txt', 'w')
    file_save.write(text)
    file_save.close()

def save_as():
    print('Save as')

window.title("Bloco de Notas com TKinter")
window.minsize(width=1280, height=720)
# window.geometry("1280x720")

# Area of text
text_area = tkinter.Text(window, font='Arial 15 bold', width=1280, height=720)
text_area.pack()

#  Create a menu main and options

menu = tkinter.Menu(window)

file = tkinter.Menu(window, tearoff=0)
file.add_command(label="New", command=new_file)
file.add_command(label= 'Save As', command=save_as)
file.add_command(label='Save', command=save)
file.add_command(label='Exit', command=window.quit)

menu = tkinter.Menu(window)
menu.add_cascade(labe='File', menu=file)
window.config(menu=menu)


window.mainloop()