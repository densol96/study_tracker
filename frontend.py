from tkinter import *
from tkinter import messagebox
from backend import Manager
import time

BG_COLOR = "#d0f4de"
BUTTON_COLLOR = "#84a59d"


def on_entry_click(entry: Entry):
    entry.delete(0, END)


class HabitTracker:
    def __init__(self, manager: Manager):
        self.manager = manager
        self.window = Tk()
        self.window.title("HabitTracker")
        self.window.geometry("600x500")
        self.window.config(bg=BG_COLOR)
        self.window.resizable(0, 0)
        self.welcome()
        self.window.mainloop()

    def welcome(self):
        self.welcome_frame = Frame(self.window, bg=BG_COLOR, pady=50, padx=80)

        def on_entry_click(entry):
            entry.delete(0, "end")

        # self.window.config(pady=50, padx=80)
        self.greeting = Label(
            self.welcome_frame,
            text="Welcome to Habit Tracker!",
            bg=BG_COLOR,
            font=("Arial", 25, "bold"),
        )
        self.greeting.grid(row=0, column=0, columnspan=2, pady=30)

        self.username_label = Label(
            self.welcome_frame,
            text="Username:",
            font=("Arial", 15, "normal"),
            bg=BG_COLOR,
        )
        self.username_label.grid(row=1, column=0)

        self.username_entry = Entry(self.welcome_frame, width=35)
        self.username_entry.grid(row=1, column=1, sticky="w")
        self.username_entry.insert(0, "Validation rule: [a-z][a-z0-9-]{1,32}")
        self.username_entry.bind(
            "<Button-1>", lambda event: on_entry_click(self.username_entry)
        )
        self.graph_id_label = Label(
            self.welcome_frame,
            text=" Graph ID:",
            font=("Arial", 15, "normal"),
            bg=BG_COLOR,
        )
        self.graph_id_label.grid(row=2, column=0)

        self.graph_id_entry = Entry(self.welcome_frame, width=35)
        self.graph_id_entry.grid(row=2, column=1, sticky="w")
        self.graph_id_entry.insert(0, "graph1")

        self.token_label = Label(
            self.welcome_frame,
            text="      Token:",
            font=("Arial", 15, "normal"),
            bg=BG_COLOR,
        )
        self.token_label.grid(row=3, column=0)

        self.token_entry = Entry(self.welcome_frame, width=35)
        self.token_entry.grid(row=3, column=1, sticky="w")
        self.token_entry.insert(0, "Validation rule: [ -~]{8,128}")
        self.token_entry.bind(
            "<Button-1>", lambda event: on_entry_click(self.token_entry)
        )

        self.register_button = Button(self.welcome_frame, text="Register")
        self.register_button.config(
            bg=BUTTON_COLLOR,
            fg="white",
            font=("Arial", 20, "bold"),
            padx=20,
            command=self.register,
        )
        self.register_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.login_button = Button(
            self.welcome_frame, text="Log In", command=self.login
        )
        self.login_button.config(
            bg=BUTTON_COLLOR, fg="white", font=("Arial", 20, "bold"), padx=33
        )
        self.login_button.grid(row=5, column=0, columnspan=2)
        self.welcome_frame.pack()

    def register(self):
        self.manager.username = self.username_entry.get()
        self.manager.id = self.graph_id_entry.get()
        self.manager.token = self.token_entry.get()
        self.manager.headers["X-USER-TOKEN"] = self.manager.token
        boolean, text = self.manager.create_user()
        if boolean:
            boolean_two, tex_two = self.manager.create_graph()
            if boolean:
                messagebox.showinfo(
                    title="Save the Link!",
                    message=f"https://pixe.la/v1/users/{self.manager.username}/graphs/{self.manager.id}",
                )
            self.loged_in_screen()
        else:
            messagebox.showerror(title="Error!", message=text[12:-21])

    def login(self):
        self.manager.username = self.username_entry.get()
        self.manager.id = self.graph_id_entry.get()
        self.manager.token = self.token_entry.get()
        self.manager.headers["X-USER-TOKEN"] = self.manager.token
        self.loged_in_screen()

    def loged_in_screen(self):
        self.welcome_frame.pack_forget()
        self.loged_in_frame = Frame(self.window, bg=BG_COLOR, pady=40, padx=30)

        self.intro_label = Label(
            self.loged_in_frame,
            text="You have 4 options(buttons)",
            font=("Arial", 20, "bold"),
            bg=BG_COLOR,
        )
        self.intro_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.update_label = Label(
            self.loged_in_frame,
            text="Update today's minutes:",
            bg=BG_COLOR,
            font=("Arial", 15, "normal"),
        )
        self.update_label.grid(row=1, column=0, sticky="w")

        self.update_label_entry = Entry(self.loged_in_frame)
        self.update_label_entry.grid(row=1, column=1, pady=50)

        self.update_button = Button(
            self.loged_in_frame,
            text="Update",
            padx=17,
            bg=BUTTON_COLLOR,
            fg="white",
            font=("Arial", 13, "normal"),
            command=self.update,
        )
        self.update_button.grid(row=1, column=2, padx=20)

        self.edit_label1 = Label(
            self.loged_in_frame,
            text="Choose a date for edit:",
            bg=BG_COLOR,
            font=("Arial", 15, "normal"),
        )
        self.edit_label1.grid(row=2, column=0, sticky="w")

        self.edit_label_entry1 = Entry(self.loged_in_frame)
        self.edit_label_entry1.grid(row=2, column=1)
        self.edit_label_entry1.insert(0, "yyyyMMdd")

        self.edit_button = Button(
            self.loged_in_frame,
            text="Edit",
            padx=28,
            bg=BUTTON_COLLOR,
            fg="white",
            font=("Arial", 13, "normal"),
        )
        self.edit_button.grid(row=2, column=2, rowspan=2)

        self.edit_label_2 = Label(
            self.loged_in_frame,
            text="Edit the minutes for this date:",
            bg=BG_COLOR,
            font=("Arial", 15, "normal"),
        )
        self.edit_label_2.grid(row=3, column=0, sticky="w")

        self.edit_label_entry2 = Entry(self.loged_in_frame)
        self.edit_label_entry2.grid(row=3, column=1, padx=15)

        self.date_for_delete_label = Label(
            self.loged_in_frame,
            text="Choose the date for delete: ",
            bg=BG_COLOR,
            font=("Arial", 15, "normal"),
        )
        self.date_for_delete_label.grid(row=4, column=0, sticky="w", pady=40)

        self.delete_entry = Entry(self.loged_in_frame)
        self.delete_entry.grid(row=4, column=1)
        self.delete_entry.insert(0, "yyyyMMdd")

        self.delete_from_button = Button(
            self.loged_in_frame,
            text="Delete date",
            bg=BUTTON_COLLOR,
            fg="white",
            font=("Arial", 13, "normal"),
        )
        self.delete_from_button.grid(row=4, column=2)
        self.loged_in_frame.pack()

        self.delete_user_button = Button(
            self.loged_in_frame,
            text="Delete the User",
            bg=BUTTON_COLLOR,
            fg="white",
            font=("Arial", 20, "bold"),
            padx=30,
            command=self.delete_user,
        )
        self.delete_user_button.grid(row=5, column=0, columnspan=3)

    def update(self):
        boolean, text = self.manager.update_graph(self.update_label_entry.get())
        messagebox.showinfo(text)

    def delete_user(self):
        if self.manager.delete_user():
            messagebox.showinfo(
                title="Information", message=f"{self.manager.username} deleted!"
            )


tracker = HabitTracker(Manager())
