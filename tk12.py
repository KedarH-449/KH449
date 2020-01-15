from tkinter import *
import sqlite3
import tkinter.messagebox

root=Tk()
root.geometry("800x400")
root.title("LOGIN PAGE")
label1=Label(root,text="LOGIN ID")
label2=Label(root,text="Password")
entry1=Entry(root)
entry2=Entry(root,show="*")
entry1.place(x=100,y=20)
entry2.place(x=100,y=60)
label1.place(x=30,y=20)
label2.place(x=30,y=60)
def login():
	if entry1.get()=="k" and entry2.get()=="k":
		root.destroy()
		dash=Tk()
		dash.title("Doctor")
		dash.geometry("1200x800")
		label1=Label(dash,text="Name")
		label1.place(x=20,y=20)

		label2=Label(dash,text="Qualification")
		label2.place(x=20,y=50)

		label3=Label(dash,text="Specialisation")
		label3.place(x=20,y=80)

		entry3=Entry(dash)
		entry3.place(x=110,y=20)

		entry4=Entry(dash)
		entry4.place(x=110,y=50)

		entry5=Entry(dash)
		entry5.place(x=110,y=80)
		
		
		
		def disp():
			#print(""+entry1.get()+entry2.get())
			docName=entry3.get()
			docQualification=entry4.get()
			docSpecialisation=entry5.get()
			conn=sqlite3.connect("demo2.db")

			with conn:
				cur = conn.cursor()
				cur.execute('INSERT INTO Doctor(Name,Qualif,Speci) VALUES(?,?,?)',(docName,docQualification,docSpecialisation))
				msg=tkinter.messagebox.showinfo("Submit Status","Successful")
			entry1.delete(0,END)
			entry2.delete(0,END)
			entry3.delete(0,END)
	
				
				

		btn1=Button(dash,text="Submit",command=disp)
		btn1.place(x=20,y=100)
		def clr2():
			entry3.delete(0,END)
			entry4.delete(0,END)
			entry5.delete(0,END)
		btn3=Button(dash,text="CLEAR",command=clr2)
		btn3.place(x=70,y=100)
			


		dash.mainloop()
	else:
		print("Password doesnt match")
def clr():
	entry1.delete(0,END)
	entry2.delete(0,END)
	
btn1=Button(root,text="LOGIN",command=login)
btn1.place(x=50,y=80)
btn2=Button(root,text="CLEAR",command=clr)
btn2.place(x=100,y=80)
root.mainloop()
