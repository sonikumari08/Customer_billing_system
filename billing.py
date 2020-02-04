from tkinter import*
from tkinter import messagebox

list = []
def add():
    tb.insert(END, "\n%s"%(prodname.get()))
    tb.insert(END, "\t%d"%(MRP.get()))
    tb.insert(END, "X%d"%(qnt.get()))
    list.append(MRP.get()*qnt.get())
    nm = prodname.get()
    tp = MRP.get()*qnt.get()
    pname.append(nm)
    pprice.append(tp)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def total():
    top = Toplevel()
    Label(top , text = "TOTAL BILL" , font  = "Helvetica 18 bold").grid(row =0 , column = 0)
    Label(top, text="Item", font="Roboto 14 bold").grid(row=1, column=0)
    Label(top, text="Price", font="Roboto 14 bold").grid(row=1, column=1)
    i = 1
    for x in range(len(pname)):
        Label(top, text = pname[x],font="Arial 12 bold").grid(row = i+1 , column =0)
        Label(top, text = pprice[x],font="Arial 12 bold").grid(row=i + 1, column=1)
        i += 1
    Label(top, text="", font="Roboto 14 bold").grid(row=i+1, column=0)
    Label(top, text="THANKS FOR SHOPPING WITH US %s !!"%(nameinfo.get()), font="Roboto 14 bold").grid(row=i+2, column=0 , padx = 2 )
    Label(top, text="KINDLY PAY TOTAL : ", font="Roboto 14 bold").grid(row=i+3, column=0)
    Label(top, text="%d"%(sum(pprice)), font="Roboto 14 bold").grid(row=i+3, column=1)
    Label(top, text="Print Bill", width = 12 , bd = 3 , command = top.quit).grid(row=i+4, column=1)

def clr():
    tb.delete(1.0,END)
    list.clear()
    pname.clear()
    pprice.clear()

root = Tk()
root.title("Billing")
nameinfo = StringVar()
prodname = StringVar()
qnt = IntVar()
MRP = IntVar()
pname = []
pprice = []

tle = Label(root , text = "BILLING SYSTEM" , font = "Helvetica 18 bold")
name = Label(root , text = "Name : ")
e1 = Entry(root , width = 15 , bd =3 , textvariable = nameinfo)

prod=  Label(root , text = "Product :" , bd = 3)
e3 = Entry(root , width = 15 , bd =3 , textvariable = prodname)
mrp = Label(root , text = "Price :", bd = 3)
e4 = Entry(root , width = 15 , bd =3 , textvariable = MRP)

quan = Label(root, text = "Quantity :", bd = 3 )
e2 = Entry(root , width = 15 , bd =3 , textvariable = qnt)



b1 = Button (root , text = "Add Items" , width = 12 , bd = 3 , command = add)

tb = Text(root , width = 30 , bd = 3)

b3 = Button (root , text = "Clear Items" , width = 12 , bd = 3 , command = clr)
b2 = Button (root , text = "Total" , width = 12 , bd = 3 , command = total)
tle.grid(row =0 )
name.grid(row = 1 , column = 0)
e1.grid(row = 1 , column = 1 , padx = 10 , pady = 10)

prod.grid(row = 2 , column = 0)
e3.grid(row = 2 , column = 1)
mrp.grid(row = 3 , column= 0)
e4.grid(row = 3 , column = 1)

quan.grid(row = 4 , column = 0)
e2.grid(row = 4 , column = 1)

b1.grid (row = 5 , column = 1)
tb.grid(row = 6 , columnspan = 2)
b3.grid (row = 7 , column = 0)
b2.grid (row = 7 , column = 1)


root.mainloop()