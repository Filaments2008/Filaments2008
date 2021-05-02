from tkinter import *
import tkinter.font as font

root = Tk()
root.title("CALCULATOR")

e = Entry(root, width=19, borderwidth=6)
e.grid(row=0, column=0, columnspan=3, padx=19, pady=19)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_erase():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))


def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)
	

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)
	

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)
	
     
buttonFont = font.Font(family='Helvetica', size=16, weight='normal')
root.configure(bg="#252525")

button_1 = Button(root, text="1", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=lambda: button_click(0))
button_add = Button(root, text="+", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=button_add)
button_equal = Button(root, text="=", bg="grey", fg="white", padx=50, pady=19, borderwidth=6, font=buttonFont, command=button_equal)
button_erase = Button(root, text="Clear", bg="grey", fg="white", padx=20, pady=19, borderwidth=6, font=buttonFont, command=button_erase)     
button_subtract = Button(root, text="-", bg="grey", fg="white", padx=51, pady=19, borderwidth=6, font=buttonFont, command=button_subtract)
button_multiply = Button(root, text="*", bg="grey", fg="white", padx=45, pady=19, borderwidth=6, font=buttonFont, command=button_multiply)
button_divide = Button(root, text="÷", bg="grey", fg="white", padx=40, pady=19, borderwidth=6, font=buttonFont, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_subtract.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_erase.grid(row=1, column=3)

root.mainloop()
