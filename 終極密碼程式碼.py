# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:17:18 2021

@author: Administrator
"""

import tkinter as tk

from random import randint
pw=int(randint(0,100))
l=int(0)
h=int(100)


def calculate():
    global pw_entry,l,h,start_label
    key=int(pw_entry.get())
    if key!=pw:
        if key<l or key>h:
            tt=str(l)+"~"+str(h)
            start_label.config(text="不在範圍內,請輸入"+tt)
        elif key<=pw:
            l=key
            tt=str(l)+"~"+str(h)
            start_label.config(text="請輸入"+tt)
        elif key>=pw:
            h=key 
            tt=str(l)+"~"+str(h)
            start_label.config(text="請輸入"+tt)
    if key==pw:
        start_label.config(text="你猜對了")
    pw_entry.delete(0,len(str(key)))

window = tk.Tk()
window.title("終極密碼")
window.geometry('400x200')
window.configure(background='white')
header_label = tk.Label(window, text="終極密碼")
header_label.pack()
start_label=tk.Label(window,text="輸入數字")
start_label.pack(side=tk.TOP)

pw_frame = tk.Frame(window)
pw_frame.pack(side=tk.TOP)
pw_entry = tk.Entry(pw_frame)
pw_entry.pack(side=tk.LEFT)

calculate = tk.Button(window, text='送出', command=calculate)
calculate.pack()


window.mainloop()




