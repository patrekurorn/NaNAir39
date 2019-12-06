from tkinter import *

#Make the GUI
root = Tk()
root.geometry("300x150")

#Adding label
label = Label(root, text=" _|_ \n*---o--(_)--o---*")
label.pack(side=TOP)

#Definng all sub-Routines:
def speak():
    print("Hi")

#Add buttons
b = Button(root, text="Staff manager",width =15, command=speak)
b.pack(side=TOP)

b2 = Button(root, text="Planning manager",width =15,command=speak)
b2.pack(side=TOP)



#Everything goes above this
root.mainloop()