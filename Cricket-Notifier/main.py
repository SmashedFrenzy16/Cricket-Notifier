from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
from plyer import notification

footer_text = "Copyright © SmashedFrenzy16 and SmashedFrenzy16 Studios under the Apache 2.0 License"

class App(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for i in (Start, Notify, Display):

            frame = i(container, self)

            self.frames[i] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, contn):

        frame = self.frames[contn]

        frame.tkraise()


class Start(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        welcome_label = Label(
            self, fg="red", text="Welcome To Cricket Notifier!", font=("Arial", 48))

        welcome_label.pack()

        blank_label = Label(self, text="")

        blank_label.pack()

        button_headlines = Button(
            self, text="Notify Me ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Notify))

        button_headlines.pack()

        blank_label2 = Label(self, text="")

        blank_label2.pack()

        button_articles = Button(
            self, text="Display Scores ⇒", fg="red", bg="black", font=("Arial", 36), command=lambda: controller.show_frame(Display))

        button_articles.pack()

        footer = Label(self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)


class Notify(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        headlines_label = Label(
            self, fg="red", text="Notify Me", font=("Arial", 48))

        headlines_label.pack()

        button_back_h = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_h.place(x=0, y=20, anchor=W)

        blank_label = Label(self, text="")

        blank_label.pack()

        def execution():

            read_file = urllib.request.urlopen("http://static.cricinfo.com/rss/livescores.xml")

            soup = BeautifulSoup(read_file, "lxml")

            titles = soup.find_all("title")


            def remove_html_markup(s):
                tag = False
                quote = False
                out = ""

                for c in s:
                        if c == '<' and not quote:
                            tag = True
                        elif c == '>' and not quote:
                            tag = False
                        elif (c == '"' or c == "'") and tag:
                            quote = not quote
                        elif not tag:
                            out = out + c

                return out


            for match in titles:

                notification.notify(
                title = "Live Cricket Scores",
                message = f"{remove_html_markup(match)}\n",
                app_icon = "cricket.ico", # <a href="https://www.flaticon.com/free-icons/cricket" title="cricket icons">Cricket icons created by justicon - Flaticon</a>
                timeout = 10,
            )



        execute_button = Button(self, text="Notify", command=execution)

        execute_button.pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)

class Display(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        articles_label = Label(
            self, fg="red", text="All Cricket Scores", font=("Arial", 48))

        articles_label.pack()

        button_back_a = Button(
            self, text="⇐", fg="red", bg="black", font=("Arial", 24), command=lambda: controller.show_frame(Start))

        button_back_a.place(x=0, y=20, anchor=W)

        blank_label = Label(self, text="")

        blank_label.pack()

        def execution():

            read_file = urllib.request.urlopen("http://static.cricinfo.com/rss/livescores.xml")

            soup = BeautifulSoup(read_file, "lxml")

            titles = soup.find_all("title")


            def remove_html_markup(s):
                tag = False
                quote = False
                out = ""

                for c in s:
                        if c == '<' and not quote:
                            tag = True
                        elif c == '>' and not quote:
                            tag = False
                        elif (c == '"' or c == "'") and tag:
                            quote = not quote
                        elif not tag:
                            out = out + c

                return out

            scrollbar1 = Scrollbar(self)

            scrollbar2 = Scrollbar(self, orient="horizontal")

            scrollbar1.pack(side=RIGHT, fill=Y)

            scrollbar2.pack(side=BOTTOM, fill=X)

            list1 = Listbox(self, yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set)

            for match in titles:

                list1.insert(END, f"{remove_html_markup(match)}\n")

            list1.pack()

        execute_button = Button(self, text="Display", command=execution)

        execute_button.pack()

        footer = Label(
            self, text=footer_text, font=("Arial", 5))

        footer.place(x=500, y=950, anchor=CENTER)


root = App()

root.title("Cricket Notifier By @SmashedFrenzy16")

root.iconbitmap("cricket.ico")

root.geometry("1000x400")

root.mainloop()