from tkinter import *

f = open(r'D:\учеба\step\lesson12\graph_func\path\inst.txt')


def instr():
    root = Tk()

    text = Text(width=100, height=30)
    text.insert(INSERT, f.read())
    text.configure(state='disabled')
    text.pack(side=LEFT)

    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)

    return root.mainloop()


