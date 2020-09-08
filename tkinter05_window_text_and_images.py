from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI Samwise")
        self.pack(fill=BOTH, expand=1)

        quit_button = Button(self, text="Quit!!!", width=10, height=1, command=self.quit_btn)
        quit_button.place(relx=.5, rely=1, anchor="s")

        # Add Menu
        our_menu = Menu(self.master)
        self.master.config(menu=our_menu)

        # Menu add 1 Item to "File" header
        file = Menu(our_menu)
        file.add_command(label='Exit', command=self.client_exit)
        our_menu.add_cascade(label='File', menu=file)

        # Menu add 2 Items "Edit" header
        # They will appear in the order they were added IE: Undo, then Dummy1, then Dummy2
        edit = Menu(our_menu)
        edit.add_command(label='Undo', command=self.menu_edit_undo)
        edit.add_command(label='Dummy1', command=self.f_dummy)
        edit.add_command(label='Dummy2', command=self.f_dummy)
        our_menu.add_cascade(label='Edit', menu=edit)

        # Add a few extra Buttons
        button_1 = Button(self, text="1", width=10, height=1, command=self.from_btn1)
        button_1.place(x=0, y=0)
        button_1.id = "btn1"

        button_2 = Button(self, text="2", width=10, height=1, command=self.from_btn2)
        button_2.place(in_=button_1, relx=0, rely=1, y=3)  # place button_2 rely + 3 to button_1
        button_2.id = "btn2"

        # Add a label
        label_1 = Label(self, text="xyz", width=20, height=1, bg="lightgray", anchor='center')
        label_1.place(in_=button_1, relx=1, rely=0, x=5)  # Place field1 relx right + 5 to button_1

    def client_exit(self):
        print("In client_exit Method")
        exit()

    def menu_edit_undo(self):
        print("Menu->Edit->Undo")
        self.children['!label']["text"] = "Menu->Edit->Undo"


    def quit_btn(self):
        self.children['!label']["text"] = "Please use menu File->Exit"

    def from_btn1(self):
        print("In from_btn1 Method")
        self.common_function("btn1")

    def from_btn2(self):
        print("In from_btn2 Method")
        self.common_function("btn2")

    def common_function(self, obj):
        print(f"Common function from {obj}")
        old_value = self.children['!label']["text"]
        self.children['!label']["text"] = obj.upper()

    # Dummy print function to test function call
    def f_dummy(self):
        print("Dummy Call for Test")
        self.children['!label']["text"] = "Dummy Call for Test"

root = Tk()
root.geometry("400x300")

app = Window(root)

#  app.master.title("FRED")

root.mainloop()
