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
import smtplib
import uuid
from random import sample

# setup
root = Tk()
# window size
root.geometry('800x600')
# background colour
root.config(bg='#f9db17')
# window title
root.title("Login")
# date and time
now = datetime.now()
# variables
winnings = [0, 0, 20, 100.50, 2384, 8584, 10000000]
lotto_list1 = []
lotto_list2 = []
lotto_list3 = []
total_amount = 0
user_id = []

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
        self.clear_btn = Button(master, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black",
                                command=self.clear_input)
        self.clear_btn.place(x=70, y=320)
        self.exit_btn = Button(master, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black",
                               command=self.exit_program)
        self.exit_btn.place(x=523, y=320)

        self.e_address_lbl2 = Entry(master)
        self.e_address_lbl2.place(x=450, y=230)

    def age_verification(self):
        email = self.e_address_lbl2.get()
        try:
            id_number = rsaidnumber.parse(self.age_lbl.get())
            age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
            if len(self.full_name_lbl2.get()) == 0 or len(self.physical_lbl2.get()) == 0:
                messagebox.showerror("Error", "Please Fill In Each Section")
            elif int(age) >= 18:
                # player id
                player_id = user_id.append(uuid.uuid4())
                # appending text
                f = open("details.txt", "a+")
                f.write(
                    self.full_name_lbl2.get() + " " + self.age_lbl.get() + " " + self.e_address_lbl2.get() + " " + self.physical_lbl2.get() + " " + "Logged into App at:" + str(
                        now) + "\n" + "Your Player ID Is: " + str(player_id))
                f.close()
                messagebox.showinfo("Success", "Let's Play")
                playsound("./Audio/lotto-sound.mp3")
                root.withdraw()
                self.lotto_window()
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
        # setup
        lotto = Tk()
        # window size
        lotto.geometry('800x500')
        # background colour
        lotto.config(bg='#f9db17')
        # window title
        lotto.title("The South African National Lottery")

        def play_again():
            lotto_list1.clear()
            lotto_list2.clear()
            lotto_list3.clear()
            lotto_nums1.config(text="", bg="#f9db17")
            lotto_nums2.config(text="", bg="#f9db17")
            lotto_nums3.config(text="", bg="#f9db17")
            lotto_nums4.config(text="", bg="#f9db17")
            lotto_nums5.config(text="", bg="#f9db17")
            lotto_nums6.config(text="", bg="#f9db17")
            num_dis1.config(text="")
            num_dis7.config(text="")
            num_dis13.config(text="")
            num1.config(state=NORMAL)
            num2.config(state=NORMAL)
            num3.config(state=NORMAL)
            num4.config(state=NORMAL)
            num5.config(state=NORMAL)
            num6.config(state=NORMAL)
            num7.config(state=NORMAL)
            num8.config(state=NORMAL)
            num9.config(state=NORMAL)
            num10.config(state=NORMAL)
            num11.config(state=NORMAL)
            num12.config(state=NORMAL)
            num13.config(state=NORMAL)
            num14.config(state=NORMAL)
            num15.config(state=NORMAL)
            num16.config(state=NORMAL)
            num17.config(state=NORMAL)
            num18.config(state=NORMAL)
            num19.config(state=NORMAL)
            num20.config(state=NORMAL)
            num21.config(state=NORMAL)
            num22.config(state=NORMAL)
            num23.config(state=NORMAL)
            num24.config(state=NORMAL)
            num25.config(state=NORMAL)
            num26.config(state=NORMAL)
            num27.config(state=NORMAL)
            num28.config(state=NORMAL)
            num29.config(state=NORMAL)
            num30.config(state=NORMAL)
            num31.config(state=NORMAL)
            num32.config(state=NORMAL)
            num33.config(state=NORMAL)
            num34.config(state=NORMAL)
            num35.config(state=NORMAL)
            num36.config(state=NORMAL)
            num37.config(state=NORMAL)
            num38.config(state=NORMAL)
            num39.config(state=NORMAL)
            num40.config(state=NORMAL)
            num41.config(state=NORMAL)
            num42.config(state=NORMAL)
            num43.config(state=NORMAL)
            num44.config(state=NORMAL)
            num45.config(state=NORMAL)
            num46.config(state=NORMAL)
            num47.config(state=NORMAL)
            num48.config(state=NORMAL)
            num49.config(state=NORMAL)

        def exit_program2():
            return root.destroy()

        def create_sets(num):
            if len(lotto_list1) < 6 and num not in lotto_list1:
                lotto_list1.append(num)
                num_dis1.config(text=lotto_list1)
            elif len(lotto_list1) == 6 and len(lotto_list2) < 6 and num not in lotto_list2:
                lotto_list2.append(num)
                num_dis7.config(text=lotto_list2)
            elif len(lotto_list1) == 6 and len(lotto_list2) == 6 and len(lotto_list3) < 6 and num not in lotto_list3:
                lotto_list3.append(num)
                num_dis13.config(text=lotto_list3)

            if len(lotto_list3) == 6:
                num1.config(state=DISABLED)
                num2.config(state=DISABLED)
                num3.config(state=DISABLED)
                num4.config(state=DISABLED)
                num5.config(state=DISABLED)
                num6.config(state=DISABLED)
                num7.config(state=DISABLED)
                num8.config(state=DISABLED)
                num9.config(state=DISABLED)
                num10.config(state=DISABLED)
                num11.config(state=DISABLED)
                num12.config(state=DISABLED)
                num13.config(state=DISABLED)
                num14.config(state=DISABLED)
                num15.config(state=DISABLED)
                num16.config(state=DISABLED)
                num17.config(state=DISABLED)
                num18.config(state=DISABLED)
                num19.config(state=DISABLED)
                num20.config(state=DISABLED)
                num21.config(state=DISABLED)
                num22.config(state=DISABLED)
                num23.config(state=DISABLED)
                num24.config(state=DISABLED)
                num25.config(state=DISABLED)
                num26.config(state=DISABLED)
                num27.config(state=DISABLED)
                num28.config(state=DISABLED)
                num29.config(state=DISABLED)
                num30.config(state=DISABLED)
                num31.config(state=DISABLED)
                num32.config(state=DISABLED)
                num33.config(state=DISABLED)
                num34.config(state=DISABLED)
                num35.config(state=DISABLED)
                num36.config(state=DISABLED)
                num37.config(state=DISABLED)
                num38.config(state=DISABLED)
                num39.config(state=DISABLED)
                num40.config(state=DISABLED)
                num41.config(state=DISABLED)
                num42.config(state=DISABLED)
                num43.config(state=DISABLED)
                num44.config(state=DISABLED)
                num45.config(state=DISABLED)
                num46.config(state=DISABLED)
                num47.config(state=DISABLED)
                num48.config(state=DISABLED)
                num49.config(state=DISABLED)

        def generate_nums():
            global total_amount
            winnings_won1 = []
            winnings_won2 = []
            winnings_won3 = []

            active = 0
            active2 = 0
            active3 = 0

            count_1 = 0
            count_2 = 0
            count_3 = 0

            # generating random numbers
            gen_nums = sample(range(1, 49), 6)
            gen_nums.sort()  # sorting generated nums

            if len(lotto_list1) < 6 and active == 0 or len(lotto_list2) < 6 and active2 == 0 or len(
                    lotto_list3) < 6 and active3 == 0:
                messagebox.showerror("Error", "Please Select 6 Numbers")
            elif len(lotto_list2) < 6 and active2 == 0:
                messagebox.showinfo("Attention", "You Did Not Play The Second Set")
            elif len(lotto_list3) < 6 and active3 == 0:
                messagebox.showinfo("Attention", "You Did Not Play The Third Set")

            # display in empty label
            lotto_nums1.configure(text=gen_nums[0], bg="white")
            lotto_nums2.configure(text=gen_nums[1], bg="white")
            lotto_nums3.configure(text=gen_nums[2], bg="white")
            lotto_nums4.configure(text=gen_nums[3], bg="white")
            lotto_nums5.configure(text=gen_nums[4], bg="white")
            lotto_nums6.configure(text=gen_nums[5], bg="red")

            for x in gen_nums:
                if len(lotto_list1) == 6:
                    active = 1
                    if x in lotto_list1:
                        count_1 += 1
                        winnings_won1.append(lotto_list1)
                if len(lotto_list2) == 6:
                    active2 = 1
                    if x in lotto_list2:
                        count_2 += 1
                        winnings_won2.append(lotto_list2)
                if len(lotto_list3) == 6:
                    active3 = 1
                    if x in lotto_list3:
                        count_3 += 1
                        winnings_won3.append(lotto_list3)
            # one set
            if active == 1 and active2 == 0 and active3 == 0:
                total_amount = winnings[count_1]
                if count_1 <= 1:
                    messagebox.showinfo("Bad Luck!",
                                        str(count_1) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            total_amount))
                    f = open("details.txt", "a+")
                    f.write(
                        "\n" + "Number Of Correct Guesses: " + str(count_1) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    results = messagebox.askquestion("Choose", "Would You Like To Play Again?")
                    if results == "yes":
                        play_again()
                    else:
                        lotto.withdraw()
                        self.bank_window()
                elif count_1 >= 2:
                    messagebox.showinfo("Congratulations!",
                                        str(count_1) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            total_amount))
                    f = open("details.txt", "a+")
                    f.write(
                        "\n" + "Number Of Correct Guesses: " + str(count_1) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    result = messagebox.askquestion("Choose", "Would You Like To Convert Your Winnings?")
                    if result == "yes":
                        lotto.withdraw()
                        self.currency_window()
                    else:
                        lotto.withdraw()
                        self.bank_window()
            # two sets
            elif active == 1 and active2 == 1 and active3:
                total_amount = winnings[count_1] + winnings[count_2]

                if count_2 <= 1:
                    messagebox.showinfo("Bad Luck!",
                                        str(count_2) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            total_amount))
                    f = open("details.txt", "a+")
                    f.write("\n" + "Number Of Correct Guesses in Set 1 : " + str(count_1) + "Number Of Correct "
                                                                                            "Guesses in Set 2:  " +
                            str(count_2) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    results = messagebox.askquestion("Choose", "Would You Like To Play Again?")
                    if results == "yes":
                        play_again()
                    else:
                        lotto.withdraw()
                        self.bank_window()
                elif count_2 >= 2:
                    messagebox.showinfo("Congratulations!",
                                        str(count_1) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            winnings[count_1]))
                    messagebox.showinfo("Congratulations!",
                                        str(count_2) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            winnings[count_2]))
                    messagebox.showinfo("Congrats", "Your total winnings are: " + str(total_amount))
                    f = open("details.txt", "a+")
                    f.write("\n" + "Number Of Correct Guesses in Set 1 : " + str(count_1) + "Number Of Correct "
                                                                                            "Guesses in Set 2:  " +
                            str(count_2) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    result = messagebox.askquestion("Choose", "Would You Like To Convert Your Winnings?")
                    if result == "yes":
                        lotto.withdraw()
                        self.currency_window()
                    else:
                        lotto.withdraw()
                        self.bank_window()
                    # 3 sets
            elif active == 1 and active2 == 1 and active3 == 1:
                total_amount = winnings[count_1] + winnings[count_2] + winnings[count_3]
                if count_3 <= 1:
                    messagebox.showinfo("Bad Luck!",
                                        str(count_3) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            total_amount))
                    f = open("details.txt", "a+")
                    f.write("\n" + "Number Of Correct Guesses in Set 1 : " + str(count_1) + "Number Of Correct "
                                                                                            "Guesses in Set 2:  " +
                            str(count_2) + "Number Of Correct Guesses in Set 3: " + str(
                        count_3) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    results = messagebox.askquestion("Choose", "Would You Like To Play Again?")
                    if results == "yes":
                        play_again()
                    else:
                        lotto.withdraw()
                        self.bank_window()
                elif count_3 >= 2:
                    messagebox.showinfo("Congratulations!",
                                        str(count_1) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            winnings[count_1]))
                    messagebox.showinfo("Congratulations!",
                                        str(count_2) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            winnings[count_2]))
                    messagebox.showinfo("Congratulations!",
                                        str(count_3) + " " + "Numbers" + "\n" + "Your Winnings Are:" + " " + "R" + str(
                                            winnings[count_3]))
                    messagebox.showinfo("Congratulations!", "Your Winnings Are:" + " " + "R" + str(
                        total_amount))
                    f = open("details.txt", "a+")
                    f.write("\n" + "Number Of Correct Guesses in Set 1 : " + str(count_1) + "Number Of Correct "
                                                                                            "Guesses in Set 2:  " +
                            str(count_2) + "Number Of Correct Guesses in Set 3: " + str(
                        count_3) + "Winnings: " + "R" + str(total_amount))
                    f.close()
                    result = messagebox.askquestion("Choose", "Would You Like To Convert Your Winnings?")
                    if result == "yes":
                        lotto.withdraw()
                        self.currency_window()
                    else:
                        lotto.withdraw()
                        self.bank_window()

        # labels
        num_lbl = Label(lotto, text="Set 1:", font="Consolas 12 bold", bg="#f9db17")
        num_lbl.place(x=600, y=5)
        num_dis1 = Label(lotto, text="", bg="#f9db17")
        num_dis1.place(x=570, y=50)

        num_lbl2 = Label(lotto, text="Set 2:", font="Consolas 12 bold", bg="#f9db17")
        num_lbl2.place(x=600, y=100)
        num_dis7 = Label(lotto, text="", bg="#f9db17")
        num_dis7.place(x=570, y=145)

        num_lbl3 = Label(lotto, text="Set 3:", font="Consolas 12 bold", bg="#f9db17")
        num_lbl3.place(x=600, y=195)
        num_dis13 = Label(lotto, text="", bg="#f9db17")
        num_dis13.place(x=570, y=240)

        lotto_nums_lbl = Label(lotto, text="The Lotto Numbers Are:", font="Consolas 12 bold", bg="#f9db17")
        lotto_nums_lbl.place(x=520, y=280)
        lotto_nums1 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums1.place(x=550, y=310)
        lotto_nums2 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums2.place(x=580, y=310)
        lotto_nums3 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums3.place(x=610, y=310)
        lotto_nums4 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums4.place(x=640, y=310)
        lotto_nums5 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums5.place(x=670, y=310)
        lotto_nums6 = Label(lotto, text="", bg="#f9db17", width=4)
        lotto_nums6.place(x=700, y=310)

        # buttons
        num1 = Button(lotto, text="01", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(1))
        num1.place(x=5, y=5)
        num2 = Button(lotto, text="02", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(2))
        num2.place(x=70, y=5)
        num3 = Button(lotto, text="03", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(3))
        num3.place(x=135, y=5)
        num4 = Button(lotto, text="04", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(4))
        num4.place(x=200, y=5)
        num5 = Button(lotto, text="05", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(5))
        num5.place(x=265, y=5)
        num6 = Button(lotto, text="06", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(6))
        num6.place(x=330, y=5)
        num7 = Button(lotto, text="07", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(7))
        num7.place(x=395, y=5)
        num8 = Button(lotto, text="08", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(8))
        num8.place(x=5, y=50)
        num9 = Button(lotto, text="09", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(9))
        num9.place(x=70, y=50)
        num10 = Button(lotto, text="10", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(10))
        num10.place(x=135, y=50)
        num11 = Button(lotto, text="11", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(11))
        num11.place(x=200, y=50)
        num12 = Button(lotto, text="12", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(12))
        num12.place(x=265, y=50)
        num13 = Button(lotto, text="13", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(13))
        num13.place(x=330, y=50)
        num14 = Button(lotto, text="14", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(14))
        num14.place(x=395, y=50)
        num15 = Button(lotto, text="15", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(15))
        num15.place(x=5, y=100)
        num16 = Button(lotto, text="16", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(16))
        num16.place(x=70, y=100)
        num17 = Button(lotto, text="17", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(17))
        num17.place(x=135, y=100)
        num18 = Button(lotto, text="18", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(18))
        num18.place(x=200, y=100)
        num19 = Button(lotto, text="19", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(19))
        num19.place(x=265, y=100)
        num20 = Button(lotto, text="20", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(20))
        num20.place(x=330, y=100)
        num21 = Button(lotto, text="21", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(21))
        num21.place(x=395, y=100)
        num22 = Button(lotto, text="22", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(22))
        num22.place(x=5, y=150)
        num23 = Button(lotto, text="23", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(23))
        num23.place(x=70, y=150)
        num24 = Button(lotto, text="24", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(24))
        num24.place(x=135, y=150)
        num25 = Button(lotto, text="25", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(25))
        num25.place(x=200, y=150)
        num26 = Button(lotto, text="26", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(26))
        num26.place(x=265, y=150)
        num27 = Button(lotto, text="27", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(27))
        num27.place(x=330, y=150)
        num28 = Button(lotto, text="28", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(28))
        num28.place(x=395, y=150)
        num29 = Button(lotto, text="29", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(29))
        num29.place(x=5, y=200)
        num30 = Button(lotto, text="30", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(30))
        num30.place(x=70, y=200)
        num31 = Button(lotto, text="31", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(31))
        num31.place(x=135, y=200)
        num32 = Button(lotto, text="32", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(32))
        num32.place(x=200, y=200)
        num33 = Button(lotto, text="33", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(33))
        num33.place(x=265, y=200)
        num34 = Button(lotto, text="34", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(34))
        num34.place(x=330, y=200)
        num35 = Button(lotto, text="35", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(35))
        num35.place(x=395, y=200)
        num36 = Button(lotto, text="36", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(36))
        num36.place(x=5, y=250)
        num37 = Button(lotto, text="37", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(37))
        num37.place(x=70, y=250)
        num38 = Button(lotto, text="38", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(38))
        num38.place(x=135, y=250)
        num39 = Button(lotto, text="39", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(39))
        num39.place(x=200, y=250)
        num40 = Button(lotto, text="40", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(40))
        num40.place(x=265, y=250)
        num41 = Button(lotto, text="41", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(41))
        num41.place(x=330, y=250)
        num42 = Button(lotto, text="42", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(42))
        num42.place(x=395, y=250)
        num43 = Button(lotto, text="43", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(43))
        num43.place(x=5, y=300)
        num44 = Button(lotto, text="44", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(44))
        num44.place(x=70, y=300)
        num45 = Button(lotto, text="45", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(45))
        num45.place(x=135, y=300)
        num46 = Button(lotto, text="46", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(46))
        num46.place(x=200, y=300)
        num47 = Button(lotto, text="47", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(47))
        num47.place(x=265, y=300)
        num48 = Button(lotto, text="48", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(48))
        num48.place(x=330, y=300)
        num49 = Button(lotto, text="49", bg="black", fg="#f9db17", borderwidth=5, command=lambda: create_sets(49))
        num49.place(x=395, y=300)
        gen_lotto = Button(lotto, text="Generate Numbers", borderwidth=10, bg="black", fg="#f9db17",
                           font="Consolas 12 bold",
                           command=generate_nums)
        gen_lotto.place(x=280, y=400)
        clear_btn = Button(lotto, text="Clear", borderwidth=10, bg="black", fg="#f9db17", font="Consolas 12 bold",
                           command=play_again)
        clear_btn.place(x=120, y=400)
        exit_btn = Button(lotto, text="Exit", borderwidth=10, bg="black", fg="#f9db17", font="Consolas 12 bold",
                          command=exit_program2)
        exit_btn.place(x=500, y=400)

        lotto.mainloop()

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
        canvas = Canvas(root, width=500, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
        canvas.place(x=-15, y=0)
        img2 = PhotoImage(file='./Images/ITHUBA-NATIONAL-LOTTERY.png')
        canvas.create_image(20, 20, anchor=NW, image=img2)

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
            display_amount.config(text="", bg="#f9db17")

        def convert_currency():
            f = open("details.txt", "a+")
            f.write("\n" + "Converted Winnings:" + " " + str(display_amount.cget("text")))
            playsound("./Audio/counting-money.mp3")
            amount_entered = float(amount_label.cget('text'))
            formula = round(amount_entered * response["conversion_rates"][currency_2_cb.get()], 2)
            display_amount.config(text=float(formula))
            messagebox.showinfo("Success", "Please Enter Your Banking Details In The Next Window")
            f = open("details.txt", "a+")
            f.write("Your Converted Winnings Are: " + str(amount_label.cget("text")))
            f.close()
            currency.withdraw()
            self.bank_window()

        amount = Label(currency, text="Your Amount Won:", font="Consolas 12 bold", bg="#f9db17")
        amount.place(x=5, y=180)
        currency_1 = Label(currency, text="From Currency:", font="Consolas 12 bold", bg="#f9db17")
        currency_1.place(x=5, y=230)
        currency_2 = Label(currency, text="To Currency:", font="Consolas 12 bold", bg="#f9db17")
        currency_2.place(x=5, y=280)
        converted_amount = Label(currency, text="Converted Amount:", font="Consolas 12 bold", bg="#f9db17")
        converted_amount.place(x=5, y=330)
        display_amount = Label(currency, text="", bg="#f9db17")
        display_amount.place(x=190, y=330)
        currency_value = Label(currency, text="Default Currency is set to Rands(ZAR)", bg="#f9db17",
                               font="Consolas 10 bold")
        currency_value.place(x=190, y=230)

        # entry
        amount_label = Label(currency, text=total_amount, bg="#f9db17")
        amount_label.place(x=190, y=180)

        # combo box
        currency_2_cb = Combobox(currency)
        currency_2_cb['values'] = currency_options
        currency_2_cb['state'] = 'readonly'
        currency_2_cb.set('Select Currency')
        currency_2_cb.place(x=190, y=280)
        display_amount.config(text='')

        # buttons
        exit_btn2 = Button(currency, borderwidth="10", text="Exit", font="Consolas 15 bold", fg="white", bg="black",
                           command=exit_program3)
        exit_btn2.place(x=400, y=400)
        clear_btn = Button(currency, borderwidth="10", text="Clear", font="Consolas 15 bold", fg="white", bg="black",
                           command=clear_program3)
        clear_btn.place(x=5, y=400)
        convert_btn = Button(currency, borderwidth="10", text="Convert", font="Consolas 15 bold", fg="white",
                             bg="black",
                             command=convert_currency)
        convert_btn.place(x=203, y=400)

        # calling API
        response = requests.get("https://v6.exchangerate-api.com/v6/48fdd8d31b8c3c5e6b84fa6f/latest/ZAR")
        response = response.json()

        currency.mainloop()  # to run the program

    def bank_window(self):
        bank_wndw = Toplevel()
        # setting up the window
        bank_wndw.geometry("500x500")  # window size
        bank_wndw.title("Banking Details")  # window title
        bank_wndw.config(bg="#f9db17")

        global user_id

        # bank function
        def bank_number():
            try:
                bank_num = acc_num_entry.get()
                branch = branch_num_entry.get()
                if len(bank_num) == 11 and len(branch) == 6:
                    f = open("details.txt", "a+")
                    f.write(
                        acc_num_entry.get() + " " + acc_num_entry.get() + " " + branch_num_entry.get() + " " + combo_box_banks.get() + "\n")
                    f.close()
                    # creates SMTP session
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    sender_email_id = 'jeandre.lotto@gmail.com'
                    receiver_email_id = self.e_address_lbl2.get()
                    password = "lifechoices2021"
                    p_id = user_id
                    # start TLS for security
                    s.starttls()
                    # Authentication
                    s.login(sender_email_id, password)
                    # message to be sent
                    message = "Congratulations\n"
                    message = message + "Your Winnings Are: " + str(total_amount) + "Your Player ID is: " + str(
                        p_id) + "Your Banking " \
                                "Details Are: " + \
                              acc_name_entry.get() + " " + acc_num_entry.get() + " " + branch_num_entry.get() + " " + \
                              combo_box_banks.get()
                    # sending the mail
                    s.sendmail(sender_email_id, receiver_email_id, message)
                    # terminating the session
                    s.quit()
                    playsound("./Audio/submit.mp3")
                    messagebox.showinfo("Success", "Please Check Your Email For Further Instructions")
                else:
                    messagebox.showinfo("Failure",
                                        "Please Enter A 11 Digit Bank Account Number and A 6 Digit Branch Code")
            except ValueError:
                messagebox.showinfo("Invalid", "Please Use Digits Only")

            try:
                acc_holder = str(acc_name_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Please Use Letters Only")

        # clear function
        def clear_input():
            acc_name_entry.delete(0, END)
            acc_num_entry.delete(0, END)
            branch_num_entry.delete(0, END)

        # exit function
        def exit_program():
            return root.destroy()

        # for an image
        canvas = Canvas(root, width=450, height=200, bg='#f9db17', borderwidth=0, highlightthickness=0)
        canvas.place(x=-15, y=5)
        img = ImageTk.PhotoImage(Image.open('./Images/ITHUBA-NATIONAL-LOTTERY.png'))
        canvas.create_image(20, 20, anchor=NW, image=img)

        # account labels
        acc_name = Label(bank_wndw, text="Account Holder:", font="Consolas 12 bold", bg="#f9db17")
        acc_name.place(x=50, y=180)
        acc_num = Label(bank_wndw, text="Account Number:", font="Consolas 12 bold", bg="#f9db17")
        acc_num.place(x=50, y=230)
        branch_num = Label(bank_wndw, text="Branch Code:", font="Consolas 12 bold", bg="#f9db17")
        branch_num.place(x=50, y=280)
        acc_bank = Label(bank_wndw, text="Select Your Bank:", font="Consolas 12 bold", bg="#f9db17")
        acc_bank.place(x=50, y=330)

        # account entries
        acc_name_entry = Entry(bank_wndw)
        acc_name_entry.place(x=250, y=180)
        acc_num_entry = Entry(bank_wndw)
        acc_num_entry.place(x=250, y=230)
        branch_num_entry = Entry(bank_wndw)
        branch_num_entry.place(x=250, y=280)

        # buttons
        submit_btn = Button(bank_wndw, text="Submit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                            command=bank_number)
        submit_btn.place(x=177, y=400)
        clear_btn = Button(bank_wndw, text="Clear", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                           command=clear_input)
        clear_btn.place(x=320, y=400)
        exit_btn3 = Button(bank_wndw, text="Exit", font="Consolas 12 bold", bg="black", fg="#f9db17", borderwidth=10,
                           command=exit_program)
        exit_btn3.place(x=50, y=400)

        # ComboBox
        combo_box_banks = Combobox(bank_wndw)
        combo_box_banks["values"] = "FNB", "Absa", "Standard Bank", "Capitec"
        combo_box_banks.place(x=250, y=330)
        combo_box_banks.set("Select Your Bank")
        combo_box_banks['state'] = 'readonly'

        bank_wndw.mainloop()


# calling the class
AllInOne(root)

# to run the program
root.mainloop()
