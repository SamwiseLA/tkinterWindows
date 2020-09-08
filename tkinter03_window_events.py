from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI Samwise")
        self.pack(fill=BOTH, expand=1)

        quit_button = Button(self, text="Quit!!!", width=10, height=1, command=self.client_exit)
        quit_button.place(relx=.5, rely=1, anchor="s")
        button_1 = Button(self, text="1", width=10, height=1, command=self.from_btn1)
        button_1.place(x=0, y=0)
        button_1.id = "btn1"
        button_2 = Button(self, text="2", width=10, height=1, command=self.from_btn2)
        button_2.place(in_=button_1, relx=0, rely=1, y=3)
        button_2.id = "btn2"

        field_1 = Label(self, text="xyz", width=10, height=1, bg="lightgray", anchor='center')
        field_1.place(in_=button_1, relx=1, rely=0, x=5)  # Place field1 relx right + 5 to button_1

    def client_exit(self):
        print("In client_exit Method")
        exit()

    def from_btn1(self):
        print("In from_btn1 Method")
        self.common_function("btn1")

    def from_btn2(self):
        print("In from_btn2 Method")
        self.common_function("btn2")

    def common_function(self, obj):
        print(f"Common Function from {obj}")
        old_value = self.children['!label']["text"]
        self.children['!label']["text"] = obj.upper()


root = Tk()
root.geometry("400x300")

app = Window(root)

#  app.master.title("FRED")

root.mainloop()
