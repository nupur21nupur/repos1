'''
ASSIGNMENT-16
GUI - I

1.Write a python program using tkinter interface to write Hello World and a exit button that closes the interface. 

2.Write a python program to in the same interface as above and  create a action when the button is click it will display some text.

3.Create a frame using tkinter with any label text and two buttons.One to  exit and other to change the label to some other text.

4.Write a python program using tkinter interface to take an input in the GUI program and print it.


'''













from tkinter import*

root=Tk()
root.title("Hello World")
root.geometry("1600x800")

text_input=StringVar()
op=""

def quit(root):
    root.destroy()

def text_print():
    lb1=Label(f2,font=("arial",60),bg="pink",bd=10,text="changed")
    lb1.grid(row=2,column=0)


f1=Frame(root,height=400,width=1300,bg="pink")
f1.pack(side=TOP)

lb1=Label(f1,font=("arial",60),bg="pink",bd=10,text="Hello world")
lb1.grid()

f2=Frame(root,height=400,width=1300,bg="blue")
f2.pack(side=BOTTOM)

e1=Entry(f2,insertwidth=10,bd=10,bg="Sky blue",font=("arial",36),justify="right",textvariable=text_input)
e1.grid()
'''
texts=textvariable

def text_print2():
    lb1=Label(f2,font=("arial",60),bg="pink",bd=10,text=texts)
    lb1.grid(row=2,column=0)

'''

b3=Button(f2,padx=25,pady=15,bd=8,fg="red",bg="pink",font=("arial",36),text="        print         ").grid(row=0,column=1)


b2=Button(f2,padx=25,pady=15,bd=8,fg="red",bg="pink",font=("arial",36),text="       Click here      ",command=lambda:text_print()).grid(row=2,column=0)

b1=Button(f2,padx=25,pady=15,bd=8,fg="red",bg="pink",font=("arial",36),text="        Exit           ",command=lambda:quit(root)).grid(row=1,column=0)



root.mainloop()
