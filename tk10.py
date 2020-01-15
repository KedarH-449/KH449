from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("radio Button")
root.geometry("200x200")
rbstr=StringVar()
def disp():
	lb1=Label(root,text=rbstr.get()).pack()
	#lb1.pack()
	#lb1.place(x=120,y=120)
rb1=Radiobutton(root,text="male",variable=rbstr,value="male")
rb2=Radiobutton(root,text="female",variable=rbstr,value="female")
btn1=Button(root,text="submit",command=disp)
btn1.place(x=20,y=120)
rb1.place(x=20,y=40)
rb2.place(x=40,y=80)
root.mainloop()