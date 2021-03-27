from tkinter import *
root=Tk()
root.title("Simple Calculator using tkinter")
e=Entry(root, width=70,borderwidth=10)
e.grid(row=0,column=0,columnspan=4)
def button_click(number):
    num=e.get()
    e.delete(0,END)
    e.insert(0,str(num)+str(number))
def button_add_clicked():
    nunu=e.get()
    global first_number
    first_number=int(nunu)
    e.delete(0,END)
def button_equal_clicked():
    #global second_number
    nunu2=e.get()
    second_number=int(nunu2)
    e.delete(0,END)
    e.insert(0,first_number+second_number)


#Button Creation
button1=Button(root,text="1",padx=45,pady=20,command=lambda:button_click(1))
button2=Button(root,text="2",padx=45,pady=20,command=lambda:button_click(2))
button3=Button(root,text="3",padx=45,pady=20,command=lambda:button_click(3))

button4=Button(root,text="4",padx=45,pady=20,command=lambda:button_click(4))
button5=Button(root,text="5",padx=45,pady=20,command=lambda:button_click(5))
button6=Button(root,text="6",padx=45,pady=20,command=lambda:button_click(6))

button7=Button(root,text="7",padx=45,pady=20,command=lambda:button_click(7))
button8=Button(root,text="8",padx=45,pady=20,command=lambda:button_click(8))
button9=Button(root,text="9",padx=45,pady=20,command=lambda:button_click(9))
button0=Button(root,text="0",padx=45,pady=20,command=lambda:button_click(0))

button_add=Button(root,text="+",padx=45,pady=20,command=button_add_clicked)
button_sub=Button(root,text="-",padx=45,pady=20)
button_mul=Button(root,text="*",padx=45,pady=20)
button_div=Button(root,text="/",padx=45,pady=20)
button_equal=Button(root,text="=",padx=45,pady=20,command=button_equal_clicked)
button_dot=Button(root,text=".",padx=45,pady=20)


#Button show
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_add.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button0.grid(row=4,column=1)
button_dot.grid(row=4,column=0)









root.mainloop()