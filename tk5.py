from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("Demo Title")
label1=Label(root,text="student")
label2=Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root,show="*")
entry1.place(x=100,y=20)
entry2.place(x=100,y=60)
label1.place(x=30,y=20)
label2.place(x=30,y=60)
root.mainloop()