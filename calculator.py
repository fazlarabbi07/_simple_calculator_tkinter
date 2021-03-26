from tkinter import *
root=Tk()
root.title("Simple Calculator using tkinter")
e=Entry(root, width=70,borderwidth=4)
e.grid(row=0,column=0,columnspan=4)
e.insert(0,"Please Enter Number")
#Button Creation
button1=Button(root,text="1",padx=45,pady=20)
button2=Button(root,text="2",padx=45,pady=20)
button3=Button(root,text="3",padx=45,pady=20)

button4=Button(root,text="4",padx=45,pady=20)
button5=Button(root,text="5",padx=45,pady=20)
button6=Button(root,text="6",padx=45,pady=20)

button7=Button(root,text="7",padx=45,pady=20)
button8=Button(root,text="8",padx=45,pady=20)
button9=Button(root,text="9",padx=45,pady=20)
button0=Button(root,text="0",padx=45,pady=20)

button_add=Button(root,text="+",padx=40,pady=20)
button_sub=Button(root,text="-",padx=40,pady=20)
button_mul=Button(root,text="*",padx=40,pady=20)
button_div=Button(root,text="/",padx=40,pady=20)
button_equal=Button(root,text="=",padx=40,pady=20)


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









root.mainloop()