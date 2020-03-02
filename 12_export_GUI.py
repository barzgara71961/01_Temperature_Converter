from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color_color = "#52ACD1"

        self.calc_history = ['5 degree C is 17 degree F',
                                       '5 degree C is 17 degree F',
                                       '5 degree C is 17 degree F',
                                       '5 degree C is 17 degree F',
                                       '5 degree C is 17 degree F',
                                       '5 degree C is 17 degree F',
                                       ]


        # Converter Main Screen GUT ...
        self.converter_frame = Frame (width=600 , height=500, bg=background_color_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial 20 bold"),
                                          bg="#52ACD1", fg="Black",
                                          padx=50, pady=80)

        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font="arial 10 bold",bg="#4D8889", fg="#F7FBFD",
                                     padx=12, pady=12,
                                     command=lambda: self.history(self.calc_history))
        self.history_button.grid(row=1, pady=50)

        if len(self.calc_history) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background_color = "#52ACD1"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Set up child window (ie: history box)
        self.history_box = Toplevel()

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background_color)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text="Calculation History ",
                                 font="arial 15 italic", wrap=250, bg=background_color,
                                 fg="Black")
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                               text="to much to write",
                               justify=LEFT,width=50, bg=background_color,wrap=200)
        self.history_text.grid(column=0,row=1)

        # History output goes here...

        # Generate string from list of calculation...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                                                - item - 1]+"\n"
        else:

            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history.  You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Lable to display calculation history to user
        self.calc_history_label = Label(self.history_frame, text=history_string,
                                  bg=background_color, font="arial 12", justify=LEFT)
        self.calc_history_label.grid(row=2)

        # Export / dismiss Button Frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3)

        # Help Button (row 1)
        self.export_button = Button(self.export_dismiss_frame,
                                    text="export",font="arial 12 bold",
                                    bg="#4D8889", fg="#F7FBFD",
                                    padx=10, pady=10,
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=1)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",bg="#4D8889", fg="#F7FBFD",
                                    padx=10, pady=10,
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=1, column=1)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background_color = "#52ACD1"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and
        # 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Instruction",
                                 font="arial 20 bold",bg=background_color)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename"
                                                         "in the box below"
                                                         "button to save your"
                                                         " calculation history"
                                                         "to a text file.",
                                 font="arial 13 italic",
                                 justify=LEFT,width=50, bg=background_color,wrap=200)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename"
                                                         "you enter below"
                                                         "already exists,"
                                                         "its contents will"
                                                         "be replaced with"
                                                         "your calculation"
                                                         "history",
                                 justify=LEFT, bg=background_color, fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2,pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3,pady=10)

        # error massage labels (initially blank, row 4 )
        self.save_error_label = Label (self.export_frame, text="", fg="black",
                                       bg=background_color)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5,pady=10)

        # Save and Cancel buttons 9row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  bg="#4D8889", fg="#F7FBFD",
                                  padx=10, pady=10,
                                  command=partial(lambda:self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame,text="Cancel",
                                    bg="#4D8889", fg="#F7FBFD", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        # Regular expression to check filname is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temp con")
    something = Converter()
    root.mainloop()
