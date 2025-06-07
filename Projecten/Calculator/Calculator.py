from tkinter import *
import re

def knop_ingedrukt(num):
    global berekening_text, berekening_label
    if berekening_label.get() == "0":
        berekening_text = ""  
    berekening_text += str(num)
    berekening_label.set(berekening_text)

def berekening():
    global berekening_text, berekening_label
    try:
        total = str(eval(berekening_text))
        berekening_label.set(total)
        berekening_text = total
    except ZeroDivisionError:
        berekening_label.set("Rekenfout")
        berekening_text = ""
    except SyntaxError:
        berekening_label.set("Syntaxis Fout")
        berekening_text = ""

def verwijder_input():
    global berekening_text, berekening_label
    berekening_text = ""
    berekening_label.set("0")

def verwijderenkel_input():
    global berekening_text, berekening_label
    if berekening_text:
        berekening_text = berekening_text[:-1]
    if re.match(pattern, berekening_label.get()):
        berekening_label.set(berekening_label.get()[:-1])
    if berekening_label.get() == "":
        berekening_label.set("0")

window = Tk()
window.configure(bg="gray15")
window.resizable(0, 0)
window.title("Calculator")
try:
    window.iconbitmap(default="Calculator.ico")
except:
    pass

berekening_text = ""
berekening_label = StringVar(value="0")
pattern = r'^[0-9\+\.\-\*/]+$'

label = Label(window, textvariable=berekening_label, font=("consolas",30), bg="gray15", fg="white", width=15, height=3, anchor="e", padx=10)
label.pack()

frame = Frame(window)
frame.pack()

Button(frame, text="1", height=3, width=9, font=35, command=lambda: knop_ingedrukt(1)).grid(row=0,column=0)
Button(frame, text="2", height=3, width=9, font=35, command=lambda: knop_ingedrukt(2)).grid(row=0,column=1)
Button(frame, text="3", height=3, width=9, font=35, command=lambda: knop_ingedrukt(3)).grid(row=0,column=2)
Button(frame, text="+", height=3, width=9, font=35, command=lambda: knop_ingedrukt("+")).grid(row=0,column=3)

Button(frame, text="4", height=3, width=9, font=35, command=lambda: knop_ingedrukt(4)).grid(row=1,column=0)
Button(frame, text="5", height=3, width=9, font=35, command=lambda: knop_ingedrukt(5)).grid(row=1,column=1)
Button(frame, text="6", height=3, width=9, font=35, command=lambda: knop_ingedrukt(6)).grid(row=1,column=2)
Button(frame, text="-", height=3, width=9, font=35, command=lambda: knop_ingedrukt("-")).grid(row=1,column=3)

Button(frame, text="7", height=3, width=9, font=35, command=lambda: knop_ingedrukt(7)).grid(row=2,column=0)
Button(frame, text="8", height=3, width=9, font=35, command=lambda: knop_ingedrukt(8)).grid(row=2,column=1)
Button(frame, text="9", height=3, width=9, font=35, command=lambda: knop_ingedrukt(9)).grid(row=2,column=2)
Button(frame, text="*", height=3, width=9, font=35, command=lambda: knop_ingedrukt("*")).grid(row=2,column=3)

Button(frame, text="0", height=3, width=9, font=35, command=lambda: knop_ingedrukt(0)).grid(row=3,column=0)
Button(frame, text=".", height=3, width=9, font=35, command=lambda: knop_ingedrukt(".")).grid(row=3,column=1)
Button(frame, text="=", height=3, width=9, font=35, command=berekening).grid(row=3,column=2)
Button(frame, text="/", height=3, width=9, font=35, command=lambda: knop_ingedrukt("/")).grid(row=3,column=3)

Button(frame, text="Invoer Verwijderen", height=2, width=29, font=35, command=verwijder_input).grid(row=4,column=0, columnspan=3)
Button(frame, text="◄◄", height=2, width=9, font=35, command=verwijderenkel_input).grid(row=4,column=3)

window.update_idletasks()
window.geometry(f"+{(window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)}+{(window.winfo_screenheight() // 2) - (window.winfo_height() // 2 + 30)}")
window.mainloop()
