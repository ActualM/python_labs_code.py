import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class Note:
    def __init__(self, title, content, group, date):
        self.title = title
        self.content = content
        self.group = group
        self.date = date

class NoteBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note Book App")

        self.notes = []
        self.groups = ["Группа 1", "Группа 2", "Группа 3"]

        self.create_widgets()

    def create_widgets(self):

        self.note_frame = ttk.Frame(self.root)
        self.note_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


        self.note_treeview = ttk.Treeview(self.note_frame, columns=("Title", "Description", "Group", "Date"), show="headings")
        self.note_treeview.heading("Title", text="Заголовок", command=lambda: self.sort_column("Title", False))
        self.note_treeview.heading("Description", text="Описание", command=lambda: self.sort_column("Description", False))
        self.note_treeview.heading("Group", text="Группа", command=lambda: self.sort_column("Group", False))
        self.note_treeview.heading("Date", text="Дата", command=lambda: self.sort_column("Date", False))
        self.note_treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.note_treeview.bind("<Double-1>", self.edit_note)


        scrollbar = ttk.Scrollbar(self.note_frame, orient=tk.VERTICAL, command=self.note_treeview.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.note_treeview.configure(yscrollcommand=scrollbar.set)


        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, pady=5)

        ttk.Button(button_frame, text="Добавить заметку", command=self.add_note).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Редактировать заметку", command=self.edit_note).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Удалить заметку", command=self.delete_note).pack(side=tk.LEFT, padx=5)


        filter_frame = ttk.Frame(self.root)
        filter_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


        ttk.Label(filter_frame, text="Фильтр по группе:").pack(side=tk.LEFT)
        self.group_var = tk.StringVar()
        self.group_var.set("Все")
        group_options = ["Все"] + self.groups
        group_dropdown = ttk.Combobox(filter_frame, textvariable=self.group_var, values=group_options)
        self.group_dropdown = group_dropdown
        group_dropdown.pack(side=tk.LEFT, padx=5)
        group_dropdown.bind("<<ComboboxSelected>>", self.filter_notes)


        sort_frame = ttk.Frame(filter_frame)
        sort_frame.pack(side=tk.RIGHT)

        ttk.Button(sort_frame, text="Сортировать по дате (новые)", command=lambda: self.sort_column("Date", False)).pack(side=tk.LEFT, padx=5)
        ttk.Button(sort_frame, text="Сортировать по дате (старые)", command=lambda: self.sort_column("Date", True)).pack(side=tk.LEFT, padx=5)


        group_button_frame = ttk.Frame(self.root)
        group_button_frame.grid(row=3, column=0, pady=5)

        ttk.Button(group_button_frame, text="Добавить группу", command=self.add_group).pack(side=tk.LEFT, padx=5)
        ttk.Button(group_button_frame, text="Удалить группу", command=self.delete_group).pack(side=tk.LEFT, padx=5)

    def add_note(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить заметку")

        title_label = ttk.Label(add_window, text="Заголовок:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = ttk.Entry(add_window, width=30)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        content_label = ttk.Label(add_window, text="Содержание:")
        content_label.grid(row=1, column=0, padx=5, pady=5)
        content_entry = tk.Text(add_window, wrap=tk.WORD, width=30, height=5)
        content_entry.grid(row=1, column=1, padx=5, pady=5)

        group_label = ttk.Label(add_window, text="Группа:")
        group_label.grid(row=2, column=0, padx=5, pady=5)
        group_var = tk.StringVar()
        group_var.set(self.groups[0])
        group_dropdown = ttk.Combobox(add_window, textvariable=group_var, values=self.groups)
        group_dropdown.grid(row=2, column=1, padx=5, pady=5)

        save_button = ttk.Button(add_window, text="Сохранить", command=lambda: self.save_new_note(add_window, title_entry.get(), content_entry.get("1.0", tk.END), group_var.get()))
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_new_note(self, add_window, new_title, new_content, new_group):
        if new_title:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_note = Note(new_title, new_content, new_group, date)
            self.notes.append(new_note)
            self.update_note_list()
            add_window.destroy()
        else:
            messagebox.showwarning("Пустой заголовок", "Пожалуйста, укажите заголовок заметки.")

    def edit_note(self, event=None):
        selected_item = self.note_treeview.selection()
        if selected_item:
            selected_index = self.note_treeview.index(selected_item)
            selected_note = self.notes[selected_index]
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Редактировать заметку")

            title_label = ttk.Label(edit_window, text="Заголовок:")
            title_label.grid(row=0, column=0, padx=5, pady=5)
            title_entry = ttk.Entry(edit_window, width=30)
            title_entry.grid(row=0, column=1, padx=5, pady=5)
            title_entry.insert(0, selected_note.title)

            content_label = ttk.Label(edit_window, text="Содержание:")
            content_label.grid(row=1, column=0, padx=5, pady=5)
            content_entry = tk.Text(edit_window, wrap=tk.WORD, width=30, height=5)
            content_entry.grid(row=1, column=1, padx=5, pady=5)
            content_entry.insert(tk.END, selected_note.content)

            group_label = ttk.Label(edit_window, text="Группа:")
            group_label.grid(row=2, column=0, padx=5, pady=5)
            group_var = tk.StringVar()
            group_var.set(selected_note.group)
            group_dropdown = ttk.Combobox(edit_window, textvariable=group_var, values=self.groups)
            group_dropdown.grid(row=2, column=1, padx=5, pady=5)

            save_button = ttk.Button(edit_window, text="Сохранить", command=lambda: self.save_edited_note(edit_window, selected_index, title_entry.get(), content_entry.get("1.0", tk.END), group_var.get()))
            save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_edited_note(self, edit_window, index, new_title, new_content, new_group):
        edited_note = self.notes[index]
        edited_note.title = new_title
        edited_note.content = new_content
        edited_note.group = new_group
        self.update_note_list()
        edit_window.destroy()

    def delete_note(self):
        selected_item = self.note_treeview.selection()
        if selected_item:
            selected_index = self.note_treeview.index(selected_item)
            result = messagebox.askquestion("Удаление заметки", "Вы уверены, что хотите удалить заметку?", icon='warning')
            if result == 'yes':
                del self.notes[selected_index]
                self.update_note_list()

    def add_group(self):
        new_group = simpledialog.askstring("Добавить группу", "Введите название новой группы:")
        if new_group:
            self.groups.append(new_group)
            self.update_group_list()
            self.group_var.set(new_group)
            self.filter_notes()

    def delete_group(self):
        selected_group = self.group_var.get()
        if selected_group != "Все" and selected_group in self.groups:
            result = messagebox.askquestion("Удаление группы", f"Вы уверены, что хотите удалить группу '{selected_group}'? Все заметки в этой группе также будут удалены.", icon='warning')
            if result == 'yes':
                self.groups.remove(selected_group)
                self.update_group_list()
                self.group_var.set("Все")
                self.filter_notes()

    def update_group_list(self):
        self.group_dropdown['values'] = ["Все"] + self.groups

    def filter_notes(self, event=None):
        selected_group = self.group_var.get()
        if selected_group == "Все":
            self.update_note_list()
        else:
            filtered_notes = [note for note in self.notes if note.group == selected_group]
            self.update_note_list(filtered_notes)

    def sort_notes(self, reverse=False):
        sorted_notes = sorted(self.notes, key=lambda x: datetime.strptime(x.date, "%Y-%m-%d %H:%M:%S"), reverse=reverse)
        self.update_note_list(sorted_notes)

    def sort_column(self, column, reverse):
        self.note_treeview.delete(*self.note_treeview.get_children())
        if column == "Date":
            self.sort_notes(reverse)
        else:
            sorted_notes = sorted(self.notes, key=lambda x: getattr(x, column), reverse=reverse)
            self.update_note_list(sorted_notes)

    def update_note_list(self, notes=None):
        self.note_treeview.delete(*self.note_treeview.get_children())
        notes = notes or self.notes
        for note in notes:
            self.note_treeview.insert("", tk.END, values=(note.title, note.content, note.group, note.date))

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteBookApp(root)
    root.mainloop()
