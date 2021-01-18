from tkinter import *
new_window = ''
def openwindow():
    global new_window
    new_window = Toplevel(root)
    new_window.geometry("250x250")
    new_window.title("New Window")
    new_window.resizable(False,False)
    lbl = Label(new_window,text="I am in new window")
    lbl.pack()
    btn2=Button(new_window,text="Close Me",command=lambda:new_window.destroy())
    btn2.pack()

root = Tk()

btn=Button(root,text="Open new Window",command=openwindow)
btn.pack(padx=20,pady=20)

Button(root,text="Close Newly Opened Window",command=lambda:new_window.destroy()).pack()

root.geometry("500x500")
root.title("My Main Window")
root.mainloop()