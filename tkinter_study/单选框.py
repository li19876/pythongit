from tkinter import *
root= Tk()
lm=LabelFrame(root,text="最好的脚本语言是什么?",padx=10,pady=10)
lm.pack(padx=10,pady=10)
langes=[
    ("python",1),
    ("php",2),
    ("java",3),
    ("js",4),
    ("html",5)
]
v=IntVar()
for lan,num in langes:
    Radiobutton(lm,variable=v,text=lan,value=num,indicatoron=False).pack(fill=X)
mainloop()