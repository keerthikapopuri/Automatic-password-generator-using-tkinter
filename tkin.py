from tkinter import *
import random, string
import pyperclip

###initialize window

root = Tk()
root.geometry("250x250")
root.resizable(0,0)
root.title("PASSWORD GENERATOR")
root.configure(background ="light grey")

#heading
heading = Label(root, text = 'Automatic Password Generator',font ='arial 10 bold',background='white').pack()
Label(root, text ='Keerthika', font ='arial 12').pack(side = BOTTOM)

###select password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

#####define function

pass_str = StringVar()

def Generator():
    my_password = ''
	# Loop through password length
    for x in range(pass_len.get()):
	    my_password += chr(random.randint(33,126))

    pass_str.set(my_password)
   
###button

Button(root, text = "GENERATE PASSWORD" , command = Generator,fg='Black',background ="white" ).pack(pady=5)

Entry(root , textvariable = pass_str).pack()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password,fg='Black',background ="white" ).pack(pady=5)


# loop to run program
root.mainloop()
