from tkinter import *
from tkinter import ttk
import pyautogui as pg
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกด')
GUI.geometry('500x300')

def Calender():
    pg.click(1843,1058)

def Google():
    webbrowser.open('https://www.google.com')

def Calculator():
    pg.click(23,1057)
    pg.click(460,477)


B1 = Button(GUI,text='Calender',command=Calender)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='Google',command=Google)
B2.pack(ipadx=20, ipady=10, pady=20)

B3 = ttk.Button(GUI,text='Calculator',command=Calculator)
B3.pack(ipadx=20, ipady=10, pady=20)

GUI.mainloop()