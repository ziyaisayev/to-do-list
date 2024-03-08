import tkinter
import tkinter.messagebox
import pickle
root=tkinter.Tk()
root.title("To-do List")
root.configure(background="black")
def add_task():
    task=entry_task.get()
    if task!="":
      listbox_task.insert(tkinter.END,task)
      entry_task.delete(0,tkinter.END)       

    else:
        tkinter.messagebox.showwarning(title="XEberdarliq",message="taski duzgun yazin")

def delete_task():
    try:
        task_index=listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="xeta",message="task elave edin")

def save_task():
    tasks=listbox_task.get(0,listbox_task.size())
    pickle.dump(tasks,open("tasks.dat","wb"))




def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_task.delete(0,tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END,task) 
    except:
        tkinter.messagebox.showwarning(title="xeta",message="fayl tapilmadi")









frame_tasks=tkinter.Frame(root)
frame_tasks.pack()

listbox_task=tkinter.Listbox(frame_tasks,height=15,width=60)

listbox_task.pack(side=tkinter.LEFT)
scrollbar_tasks=tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_task.yview)


entry_task=tkinter.Entry(root,width=60)

entry_task.pack()


button_add_task=tkinter.Button(root,text="add task",command=add_task)
button_add_task.pack()



button_delete_task=tkinter.Button(root,text="delete task",width=42,bg="purple",command=delete_task)
button_delete_task.pack()


save_task=tkinter.Button(root,text="Save task",width=42,bg="green",command=save_task)


save_task.pack()

load_task=tkinter.Button(root,text="load_task",width=42,bg="blue",command=load_task)
load_task.pack()



root.mainloop()