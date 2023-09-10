from tkinter import *


window=Tk()
window.title("Widgets")
window.minsize(400,300)


def click_button():
    print(entry1.get())
    print(text1.get("1.0",END))# take texts from first line

button1=Button(text="Send :",command=click_button)
button1.config(padx=10,pady=20)
button1.pack()
window.config(pady=50)

#single line
entry1=Entry()
entry1.focus()#show cursor for usr
entry1.pack(padx=5,pady=5)

#multiline
text1=Text(width=20,height=10)
text1.pack()
#text1.focus() #show curor for user
window.mainloop()