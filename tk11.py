from tkinter import *
root=Tk()
root.title("Login page")
root.geometry("300x300")

def auth():
	root.destroy()
	dash=Tk()
	dash.title("Dashboard")
	dash.geometry("1200x800")
	dash.mainloop()

btn=Button(root,text="Login",command=auth)
btn.pack()
root.mainloop()
