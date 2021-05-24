from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg="Green")
root.title("Python Database")
root.geometry("400x400")

lbl1 = Label(root, text="Username", font=("Arial 16 bold"))
lbl1.pack()
lbl1_entry = Entry(root, bg="white")
lbl1_entry.pack()

lbl2 = Label(root, text="Password", font=("Arial 16 bold"))
lbl2.pack()
lbl2_entry = Entry(root, bg="White", show="*")
lbl2_entry.pack()


# Starting the loop


def getUsername():
# Information to be stored


  Usernames = ["Zaid", "Aaliyah", "Lihle", "Thabo", "Zoe"]
  Passwords = ["1000", "5500", "7700", "1234", "0621"]
  found = False
  for x1 in range(len(Usernames)):
    if lbl1_entry.get() == Usernames[x1] and lbl2_entry.get() == Passwords[x1]:
      found=True
  if found==True:
    messagebox.showinfo("Message","Access granted")
    root.destroy()
    import blank
  else:
    messagebox.showinfo("Message","Access Denied")
def clear():
    lbl1_entry.delete(0, END)
    lbl2_entry.delete(0, END)

btn1 = Button(root, text="Enter", command=getUsername)
btn1.pack()
btn2 = Button(root, text='Exit', command='exit')
btn2.pack()
btn3 = Button(root, text="Clear", command=clear)
btn3.pack()

root.mainloop()
