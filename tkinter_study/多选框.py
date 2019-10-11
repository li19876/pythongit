from tkinter import *
root = Tk()
meinv = ["貂蝉",'西施','王昭君','杨玉环']
v=[]
for i in meinv:
    v.append(IntVar())
# print(v)
    Checkbutton(root,text=i,variable=v[-1]).pack(anchor="w")
Label(root,text=v).pack()
mainloop()