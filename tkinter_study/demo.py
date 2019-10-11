from tkinter import *
def callback():
    var.set("啦啦啦啦啦啦啦")
root=Tk()
var=StringVar()
var.set("哈哈哈哈哈哈哈哈哈")
textlable = Label(root,textvariable=var)
textlable.pack(padx=10,pady=10)
button = Button(root,text="bab",command=callback)
button.pack()
mainloop()
