from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("radio Button")
root.geometry("200x200")
rbstr=StringVar()
def disp():
	print("You selected"+rbstr.get())
rb1=Radiobutton(root,text="male",variable=rbstr,value="male",command=disp)
rb2=Radiobutton(root,text="female",variable=rbstr,value="female",command=disp)
rb1.pack()
rb2.pack()
root.mainloop()