import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('LABEL FRAME')

#creating labels
label_frame = ttk.Labelframe(win, text='enter your details below')
label_frame.grid(row=0, column=0)

labels = ['name : ', 'age : ', 'city : ']


for i in range(len(labels)):
    cur_label = ttk.Label(label_frame, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

name_var = tk.StringVar()


user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'city' : tk.StringVar() 
}

counter=0
for i in user_info:
    entrybox = 'entry' + i
    entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    entrybox.grid(row=counter, column=1)
    counter +=1    


def action():
    print('yes')    


sub_btn=ttk.Button(win, text='Submit', command=action)
sub_btn.grid(row=1, column=0, sticky=tk.W)


for child in label_frame.winfo_children():
    child.grid_configure(padx=4, pady=4)
    

win.mainloop()