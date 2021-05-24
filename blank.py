from tkinter import *

root = Tk()
root.config(bg="black")
root.title("Python Database")
root.geometry("400x200")





def sortselection():
    lists = [42, 12, 13, 89, 63, 11]
    #count = 0
    for x in range(len(lists)):
        minimum = lists[x]
        for y in range(x, len(lists), 1):
            if lists[y] < minimum:
                #count = +1
                minimum = lists[y]
                lists[y], lists[x] = lists[x], lists[y]
       # print(x)
    #print(count)
                result_lbl.config(text=lists)


lbl1 = Label(root, text="Loop The List", bg="#808080", fg="#202020", font="Ariel 16 bold")
lbl1.pack()
result_lbl = Label(root, text="", font="Arial 20 bold")
result_lbl.pack()
btn1 = Button(root, text="Display", bg="Yellow", fg="Red", font="Arial 18 bold", command=sortselection)
btn1.pack()
exit_btn = Button(root, text="Exit", bg="Yellow", fg="Red", font="Arial 18 bold", command='exit')
exit_btn.pack()

import SelectionSort


root.mainloop()
