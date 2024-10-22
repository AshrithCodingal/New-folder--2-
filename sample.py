from tkinter import *

window = Tk()


window.title('Project')
window.geometry('400x300')




lbl = Label(text = "hello ",fg = "white",bg="#072F5F",height =1 ,width = 300)


name_lbl = Label(text = " Full name", bg = "#b0bfbd")

name_entery =Entry()


def display():
  text_box.insert(END,"HELLO HOW ARE YOU")



btn= Button(text = "begin",command=display ,height= 1,bg = "#05f2d3",fg="white")

text_box = Text(height = 3)


lbl.pack()
name_lbl.pack()
name_entery.pack()
btn.pack()
text_box.pack()








window.mainloop()





