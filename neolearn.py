import tkinter as tk
import random

# global variables
debug = True
debug_text = "[debug text]"

# colors
color_question = 'white'
color_bg = 'teal'
color_text = 'black'
color_headings = 'cyan4'
color_success = 'green'
color_wrong = 'red'

# setup root
root = tk.Tk();
root.geometry('720x300')
root.title("neo learn")
root.config(bg=color_bg)

# setup labels and other elements
label1 = tk.Label(root, text=debug_text)
label1.config(font=('helvetica', 40), bg=color_bg, fg=color_question)

label2 = tk.Label(root, text=debug_text)
label2.config(font=('helvetica', 40), bg=color_bg, fg=color_headings)

entry1 = tk.Entry(root)
entry1.config(font=('helvetica', 40), bg=color_bg, bd=0, justify = 'center')

# layout
label2.pack(side='top')
label1.pack(side='top')
entry1.pack(side='top')


# code
learning_set = list()
current_question = -1


def background(color):
    root.config(bg=color)
    label1.config(bg=color)
    label2.config(bg=color)
    entry1.config(bg=color)


def read_file(file_name):
    rows = list()

    for row in open(file_name, "r"):
        q, a = row.split(",")
        rows.append([q.strip(), a.strip()])
    print(rows)
    return rows


def next_question():
    global current_question
    current_question += 1
    if current_question < len(learning_set):
        label1.config(text=learning_set[current_question][0])
    else:
        label1.config(text="all done")


# callbacks
def onenter(event):
    if learning_set[current_question][1] == entry1.get():
        background(color_bg)
        entry1.delete(0, 'end')
        next_question()
    else:
        background(color_wrong)
        print(entry1.get())
        print(learning_set[current_question][1])
        print('wrong')


# bindings
root.bind('<Return>', onenter)

# main
if __name__ == '__main__':
    label2.config(text='Math Multiplication')
    learning_set = read_file("learning-sets/math-multiplication.txt")
    random.shuffle(learning_set)
    next_question()
    root.mainloop()