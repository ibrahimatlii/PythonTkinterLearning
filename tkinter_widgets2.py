from tkinter import *


window=Tk()
window.title("Widgets")
window.minsize(400,300)

#scale usafe
'''def user_scaled1(val=0):
    print(scale1.get())

var1=DoubleVar()
scale1=Scale(from_=0,to=100,variable=var1,command=user_scaled1)
scale1.pack()
'''
def user_scaled2(value):
    print(value)

scale2=Scale(from_=0,to=100,command=user_scaled2)
scale2.pack()

#spinbox usage
def selected_spinbox():
    print(spinbox1.get())
spinbox1=Spinbox(from_=0,to=50,command=selected_spinbox)
spinbox1.pack()

#checkbutton usage
def checkbutton_selected():
    print(check_state.get())

check_state=IntVar() #chose or not chosen give 0 or 1 value
checkbutton1=Checkbutton(text="book",variable=check_state,command=checkbutton_selected)
checkbutton1.pack()



window.mainloop()
