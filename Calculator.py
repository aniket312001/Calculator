
from tkinter import *

root = Tk()
root.title('Advance Calculator')  # title


e = Entry(root,width=35,borderwidth=5)  # text bar
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)     # columnspan means it will take 3 button space

def button_click(num):

    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(num))


def Button_Clear():
    e.delete(0,END)       # delete the text from the bar

sign=None
stored =0

def button_ADD():
    global sign
    sign = '+'
    global stored
    stored = e.get()
    e.delete(0,END)

def button_MULT():
    global sign
    sign = '*'
    global stored
    stored = e.get()
    e.delete(0,END)

def button_SUB():
    global sign
    sign = '-'
    global stored
    stored = e.get()
    e.delete(0,END)

def button_DIV():
    global sign
    sign = '/'
    global stored
    stored = e.get()
    e.delete(0,END)

def button_REM():
    global sign
    sign = '%'
    global stored
    stored = e.get()
    e.delete(0,END)


def button_EQUAL():
    newstored = e.get()
    e.delete(0,END)

    if sign == '+':
        ans = int(stored) + int(newstored)
        e.insert(0, ans)
    elif sign == '-':
        ans = int(stored) - int(newstored)
        e.insert(0, ans)
    elif sign == '*':
        ans = int(stored) * int(newstored)
        e.insert(0, ans)
    elif sign == '/':
        ans = int(stored) / int(newstored)
        e.insert(0, ans)
    elif sign == '%':
        ans = int(stored) % int(newstored)
        e.insert(0, ans)




# define button

button1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
button2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
button3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))
button4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
button5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
button6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))
button7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
button8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
button9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))
button0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))

button_mult = Button(root,text='*',padx=39,pady=20,command=button_MULT)
button_sub = Button(root,text='-',padx=40,pady=20,command=button_SUB)
button_rem = Button(root,text='%',padx=38,pady=20,command=button_REM)

button_squ = Button(root,text='00',padx=38,pady=20,command=lambda:button_click(00))
button_div = Button(root,text='/',padx=40,pady=20,command=button_DIV)
button_add = Button(root,text='+',padx=39,pady=20,command= button_ADD)
button_equal = Button(root,text='=',padx=91,pady=20,command= button_EQUAL)
button_clear = Button(root,text='clear',padx=79,pady=20,command=Button_Clear)          # we are not passing element so no need use lambda

# put button on the screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button_div.grid(row=4,column=2)
button_rem.grid(row=4,column=3)
button_sub.grid(row=3,column=3)
button_mult.grid(row=2,column=3)
button_add.grid(row=1,column=3)
button_squ.grid(row=4,column=0)

button0.grid(row=4,column=1)
button_clear.grid(row=5,column=2,columnspan=2)

button_equal.grid(row=5,column=0,columnspan=2)

root.mainloop()