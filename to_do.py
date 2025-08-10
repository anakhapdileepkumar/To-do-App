import tkinter as tk

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected)

def mark_done():
    selected = tasks_listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks_listbox.get(index)
        tasks_listbox.delete(index)
        tasks_listbox.insert(index, f"✔ {task}")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=2)

tasks_listbox = tk.Listbox(root, width=40, height=10)
tasks_listbox.pack(pady=5)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack(pady=2)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=2)

root.mainloop()
