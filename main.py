# login form for lottery program #
# calling modules
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import Image, ImageTk
from datetime import *
import rsaidnumber
import re
from playsound import playsound
import requests

# setup
root = Tk()
# window size
root.geometry('800x600')
# background colour
root.config(bg='#f9db17')
# window title
root.title("Login")
# variables
now = datetime.now()

# regular expression for validating email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


class AllInOne:
    def __init__(self, master):
        # for an image
        self.canvas = Canvas(master, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
        self.canvas.place(x=135, y=5)
        self.img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)
        # label
        self.entry_age_lbl = Label(master, text="Please Enter Your ID Number:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.entry_age_lbl.place(x=70, y=200)
        self.full_name_lbl = Label(master, text="Please Enter Your Full Name:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.full_name_lbl.place(x=70, y=170)
        self.e_address_lbl = Label(root, text="Please Enter Your Email Address:", fg="black", bg="#f9db17",
                                   font="Consolas 12 bold")
        self.e_address_lbl.place(x=70, y=230)
        self.physical_lbl = Label(master, text="Please Enter Your Physical Address:", fg="black", bg="#f9db17",
                                  font="Consolas 12 bold")
        self.physical_lbl.place(x=70, y=260)
        self.t_c = Label(root, text="Terms & Conditions:", bg="#f9db17", font="Consolas 12 bold", fg="red")
        self.t_c.place(x=0, y=500)
        self.legal_age = Label(master, text="1. You Must Be 18 Years or Older To Enter", bg="#f9db17", fg="black",
                               font="Consolas 10 bold")
        self.legal_age.place(x=0, y=530)
        self.legal_age2 = Label(master, text="2. You Must Have A Valid ID", bg="#f9db17", fg="black",
                                font="Consolas 10 bold")
        self.legal_age2.place(x=0, y=550)
        self.legal_age3 = Label(master, text="3. User Must Be A SA Citizen", bg="#f9db17", fg="black",
                                font="Consolas 10 bold")
        self.legal_age3.place(x=0, y=570)
        # entry label
        self.age_lbl = Entry(master)
        self.age_lbl.place(x=450, y=200)
        self.full_name_lbl2 = Entry(master)
        self.full_name_lbl2.place(x=450, y=170)
        self.physical_lbl2 = Entry(master)
        self.physical_lbl2.place(x=450, y=260)

        # buttons
        self.confirm_btn = Button(master, borderwidth="10", text="Verify", font="Consolas 15 bold", fg="white",
                                  bg="black", command=self.age_verification)
        self.confirm_btn.place(x=296, y=320)
        self.clear_btn = Button(root, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black",
                                command=self.clear_input)
        self.clear_btn.place(x=70, y=320)
        self.exit_btn = Button(root, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black",
                               command=self.exit_program)
        self.exit_btn.place(x=523, y=320)

        self.e_address_lbl2 = Entry(master)
        self.e_address_lbl2.place(x=450, y=230)

    def age_verification(self):
        email = self.e_address_lbl2.get()
        try:
            id_number = rsaidnumber.parse(self.age_lbl.get())
            age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
            if int(age) >= 18:
                # appending text
                f = open("details.txt", "a+")
                f.write(
                    self.full_name_lbl2.get() + " " + self.age_lbl.get() + " " + self.e_address_lbl2.get() + " " + self.physical_lbl2.get() + " " + "Logged into App at:" + str(
                        now) + "\n")
                f.close()
                messagebox.showinfo("Success", "Let's Play")
                playsound("./Audio/lotto-sound.mp3")
                root.withdraw()
                import lotto
            else:
                messagebox.showinfo('Failure', "You Are Too Young To Play")
            if re.search(regex, email):
                pass
            else:
                messagebox.showinfo("Failure", "Invalid Email")
        except ValueError:
            messagebox.showinfo("Failure", "Please Enter A Valid 13 Digit ID Number")

    def clear_input(self):
        self.age_lbl.delete(0, END)
        self.physical_lbl2.delete(0, END)
        self.e_address_lbl2.delete(0, END)
        self.full_name_lbl2.delete(0, END)

    def exit_program(self):
        return root.destroy()

    def lotto_window(self):
        pass

    def currency_window(self):
        # setting up window
        currency = Toplevel()
        # window size
        currency.geometry("500x500")
        # window color
        currency.config(bg="#f9db17")
        # window title
        currency.title("Currency Convertor")
        # for an image
        canvas = Canvas(currency, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
        canvas.place(x=-15, y=5)
        img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
        canvas.create_image(20, 20, anchor=NW, image=img)

        # calling API
        response = requests.get("https://v6.exchangerate-api.com/v6/48fdd8d31b8c3c5e6b84fa6f/latest/ZAR")
        response = response.json()

        conversion_rate = response["conversion_rates"]

        currency_options = []
        for i in conversion_rate.keys():
            currency_options.append(i)

        # exit function
        def exit_program3():
            return root.destroy()

        # clear function
        def clear_program3():
            amount_entry.delete(0, END)
            display_amount.config(text="", bg="#f9db17")

        def convert_currency():
            f = open("details.txt", "a+")
            f.write("\n" + "Converted Winnings:" + " " + str(display_amount.cget("text")))
            playsound("./Audio/counting-money.mp3")
            amount_entered = float(amount_entry.get())
            formula = round(amount_entered * response["conversion_rates"][currency_2_cb.get()], 2)
            display_amount.config(text=float(formula))
            messagebox.showinfo("Success", "Please Enter Your Banking Details In The Next Window")
            root.withdraw()
            self.bank_window()

        amount = Label(root, text="Your Amount Won:", font="Consolas 12 bold", bg="#f9db17")
        amount.place(x=5, y=180)
        currency_1 = Label(root, text="From Currency:", font="Consolas 12 bold", bg="#f9db17")
        currency_1.place(x=5, y=230)
        currency_2 = Label(root, text="To Currency:", font="Consolas 12 bold", bg="#f9db17")
        currency_2.place(x=5, y=280)
        converted_amount = Label(root, text="Converted Amount:", font="Consolas 12 bold", bg="#f9db17")
        converted_amount.place(x=5, y=330)
        display_amount = Label(root, text="", bg="#f9db17")
        display_amount.place(x=190, y=330)
        currency_value = Label(root, text="Default Currency is set to Rands(ZAR)", bg="#f9db17",
                               font="Consolas 10 bold")
        currency_value.place(x=190, y=230)

        # entry
        amount_entry = total_winnings.get()
        amount_entry.place(x=190, y=180)

        # combo box
        currency_2_cb = Combobox(root)
        currency_2_cb['values'] = currency_options
        currency_2_cb['state'] = 'readonly'
        currency_2_cb.set('Select Currency')
        currency_2_cb.place(x=190, y=280)
        # currency_2_cb.config(bg="#f9db17")
        display_amount.config(text='')

        # buttons
        exit_btn = Button(root, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black",
                          command=exit_program3)
        exit_btn.place(x=400, y=400)
        clear_btn = Button(root, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black",
                           command=clear_program3)
        clear_btn.place(x=5, y=400)
        convert_btn = Button(root, borderwidth="10", text="Convert", font="Consolas 15 bold", fg="white", bg="black",
                             command=convert_currency)
        convert_btn.place(x=203, y=400)

        # calling API
        response = requests.get("https://v6.exchangerate-api.com/v6/48fdd8d31b8c3c5e6b84fa6f/latest/ZAR")
        response = response.json()

    def bank_window(self):
        bank_wndw = Toplevel()
        # setting up the window
        bank_wndw.geometry("500x350")  # window size
        bank_wndw.title("Banking Details")  # window title
        bank_wndw.config(bg="#f9db17")
