from tkinter import*
mansLogs=Tk()
import math
mansLogs.title('Kalkulators')

def btnClick(number):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā jauno skaitli
    return 0


def btnCommand(command):
    global number
    global num1 #jāiegaumē skaitlis,darbība
    global mathOp #matemātiskais operators
    mathOp=commandnum1=int(e.get())
    e.delete(0,END)
    return 0

def Vienads():
    num2=int(e.get())
    result=0
    if mathOp=="+":
       result=num1+num2
    elif mathOp=="-":
       result=num1-num2
    elif mathOp=="*":
       result=num1*num2
    elif mathOp=="/":
       result=num1/num2
    else: 
       result=0 
    e.delete(0,END) 
    e.insert(0,str(result)) 
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 



    
e=Entry(mansLogs,width=15,bd=10,font=("Arial Black",20),justify="right") #izveido ievades logu
e.grid(row=0,column=0,columnspan=4)#atrašanās vieta 

btn0=Button(mansLogs,text='0',padx='40',pady='20',command=lambda:btnClick(0))
btn1=Button(mansLogs,text='1',padx='40',pady='20',command=lambda:btnClick(1))
btn2=Button(mansLogs,text='2',padx='40',pady='20'command=lambda:btnClick(2))
btn3=Button(mansLogs,text='3',padx='40',pady='20'command=lambda:btnClick(3))
btn4=Button(mansLogs,text='4',padx='40',pady='20'command=lambda:btnClick(4))
btn5=Button(mansLogs,text='5',padx='40',pady='20'command=lambda:btnClick(5))
btn6=Button(mansLogs,text='6',padx='40',pady='20'command=lambda:btnClick(6))
btn7=Button(mansLogs,text='7',padx='40',pady='20'command=lambda:btnClick(7))
btn8=Button(mansLogs,text='8',padx='40',pady='20'command=lambda:btnClick(8))
btn9=Button(mansLogs,text='9',padx='40',pady='20'command=lambda:btnClick(9))
btnC=Button(mansLogs,text='C',padx='40',pady='20'command=notirit)
btnPlus=Button(mansLogs,text='+',padx='40',pady='20'command=lambda:btnCommand('+'))
btnMinus=Button(mansLogs,text='-',padx='40',pady='20'command=lambda:btnCommand('-'))
btnreizinasana=Button(mansLogs,text='*',padx='40',pady='20'command=lambda:btnCommand('*'))
btndalisana=Button(mansLogs,text='/',padx='40',pady='20'command=lambda:btnCommand('/'))
btnvienads=Button(mansLogs,text='=',padx='40',pady='20'  command=Vienads)


btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn0.grid(row=4,column=0)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btnC.grid(row=1,column=4)
btnPlus.grid(row=2,column=4)
btnMinus.grid(row=3,column=4)
btnreizinasana.grid(row=4,column=4)
btndalisana.grid(row=4,column=2)
btnvienads.grid(row=4,column=1)

mansLogs.mainloop()

