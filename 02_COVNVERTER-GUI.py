from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "#52ACD1"

        # Initialise list to hold calculation history
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame (bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial 20 bold"),
                                          fg="Black", bg=background_color,
                                          padx=50, pady=80)

        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be \n"
                                                  "converted and then push \n"
                                                  "one of the buttons below.\n",
                                             font="arial 15 italic", wrap=250,bg=background_color,
                                             fg="Black",justify=LEFT)
        self.temp_instructions_label.grid(row=1)

        # temperture entry box (row2)
        self.to_convert_entry = Entry(self.converter_frame,width=50,
                                      font= ("arial 10 bold"))
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3) ,orchid3 | khakil
        self.converter_buttons_frame = Frame(self.converter_frame)
        self.converter_buttons_frame.grid(row=3, pady=30)

        self.to_c_button = Button(self.converter_buttons_frame,
                                  text = " To Centigrade ",
                                  font = ( " arial 10 bold " ),
                                  bg="#4D8889", fg="#F7FBFD",
                                  padx = 10, pady = 10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.converter_buttons_frame,
                                  text="To Fahreneit", font="Arial 10 bold",
                                  bg="#4D8889", fg="#F7FBFD", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)

        self.converted_label = Label (self.converter_frame,
                                      text="Answer", font="Arial 10 bold",
                                      bg=background_color, padx=10, pady=10)
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.History_buttons_frame = Frame(self.converter_frame)
        self.History_buttons_frame.grid(rows=5, pady=10, padx=10)

        # History button
        self.History_buttons = Button(self.History_buttons_frame,
                                      text="History", font="Arial 10 bold",
                                      command=lambda: self.history(self.all_calc_list),
                                      bg="#4D8889",fg="#F7FBFD", padx=10, pady=10)
        self.History_buttons.grid(row=0,column=0)

        if len(self.all_calc_list) == 0:
            self.History_buttons.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.History_buttons_frame,
                                  text="help",font="arial 10 bold",bg="#4D8889",
                                  fg="#F7FBFD",padx=10, pady=10, command=self.help)
        self.help_button.grid(row=0, column=1 )

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="you fix it by getting of my app")



    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" # pale pink when a error

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_error = "no"

            # convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C if {} degree F".format(to_convert, fahrenheit)

            # convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C if {} degree F".format(to_convert, celsius)

            else:
                # input is invalid
                answer = " Too cold "
                has_error = " yes "

            # Display answer
            if has_error == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for History
            if answer != "Too Cold":
                self.all_calc_list.append(answer)
                print(self.all_calc_list)

        except ValueError:
            self.converted_label.configure(text="enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = (to_round)

        return rounded

class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg="#52ACD1")
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                             text="Help / Instruction",
                             font="arial 20 bold", bg="#52ACD1")
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                           text="i have no idea where this is going to be",
                           justify=LEFT, width=50, bg="#52ACD1", wrap=200)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#4D8889",
                              font="arial 10 bold", fg="#F7FBFD",
                              command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()

