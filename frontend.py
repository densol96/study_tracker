from tkinter import *
from tkinter import messagebox
from backend import Manager

BG_COLOR = "#d0f4de"
BUTTON_COLLOR = "#84a59d"


def on_entry_click(entry: Entry):
    entry.delete(0, END)


class HabbitTracker:
    def __init__(self, manager: Manager):
        self.manager = manager
        self.window = Tk()
        self.window.title("HabbitTracker")
        self.window.geometry("600x500")
        self.window.config(bg=BG_COLOR)
        self.window.resizable(0, 0)

        self.welcome_frame = Frame(self.window)

        self.setup()
        self.window.mainloop()

    def setup(self):
        def on_entry_click(entry):
            entry.delete(0, "end")

        self.window.config(pady=50, padx=100)
        self.greeting = Label(
            text="Welcome to Habbit Tracker!", bg=BG_COLOR, font=("Arial", 25, "bold")
        )
        self.greeting.grid(row=0, column=0, columnspan=2, pady=30)

        self.username_label = Label(
            text="Username:", font=("Arial", 15, "normal"), bg=BG_COLOR
        )
        self.username_label.grid(row=1, column=0)

        self.username_entry = Entry(width=35)
        self.username_entry.grid(row=1, column=1, sticky="w")
        self.username_entry.insert(0, "Validation rule: [a-z][a-z0-9-]{1,32}")
        self.username_entry.bind(
            "<Button-1>", lambda event: on_entry_click(self.username_entry)
        )
        self.graph_id_label = Label(
            text=" Graph ID:", font=("Arial", 15, "normal"), bg=BG_COLOR
        )
        self.graph_id_label.grid(row=2, column=0)

        self.graph_id_entry = Entry(width=35)
        self.graph_id_entry.grid(row=2, column=1, sticky="w")
        self.graph_id_entry.insert(0, "graph1")

        self.token_label = Label(
            text="      Token:", font=("Arial", 15, "normal"), bg=BG_COLOR
        )
        self.token_label.grid(row=3, column=0)

        self.token_entry = Entry(width=35)
        self.token_entry.grid(row=3, column=1, sticky="w")
        self.token_entry.insert(0, "Validation rule: [ -~]{8,128}")
        self.token_entry.bind(
            "<Button-1>", lambda event: on_entry_click(self.token_entry)
        )

        self.register_button = Button(text="Register")
        self.register_button.config(
            bg=BUTTON_COLLOR, fg="white", font=("Arial", 20, "bold"), padx=20
        )
        self.register_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.login_button = Button(text="Log In")
        self.login_button.config(
            bg=BUTTON_COLLOR, fg="white", font=("Arial", 20, "bold"), padx=33
        )
        self.login_button.grid(row=5, column=0, columnspan=2)


tracker = HabbitTracker(Manager())
