from tkinter import *
from tkinter import ttk, messagebox 

GUI = Tk()
GUI.title('โปรแกรมคำนวณราคามะม่วง')
GUI.geometry('500x300')


bg = PhotoImage(file='Mango.png')

BG = Label(GUI, image=bg)
BG.pack()

FONT = ('Angsana New',20)

L = Label(GUI,text='กรุณากรอกจำนวนมะม่วง ( Kg )',font=FONT)
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity,font=FONT)
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 50
        messagebox.showinfo('ราคามะม่วง','ราคาทั้งหมด {} บาท'.format(calc))
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set(1)
        E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=15)

GUI.mainloop()
