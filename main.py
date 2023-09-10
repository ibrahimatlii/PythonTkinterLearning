import tkinter


window=tkinter.Tk()
window.title("title of tkinter window")

window.minsize(400,300)


def buton_tikla():
    user_print=entry1.get()
    print(user_print)
    print("button clicked")

#Label uasage
label1=tkinter.Label(text="label etiketi",font=("verdana",18,"italic"))
#label1.config(bg="green",fg="white")
#label1.pack()

label1.grid(row=0,column=0)


#button usage
buton1=tkinter.Button(text="Send button",command=buton_tikla)
#buton1.pack()
buton1.grid(row=1,column=1)

buton1.update()#you should use before you write code below
print(buton1.winfo_reqheight())

print(buton1.winfo_reqwidth())

#buton1.place(x=200 -38,y=150-13) #tam ortası için labelin h/2 kısmını da çıkarıyoruz

#entry usage
entry1=tkinter.Entry(width=30)
#entry1.pack()
entry1.grid(row=2,column=2)



window.mainloop()


