#
# File:		ErrorWindow.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: File holding Error Window Implementation

from tkinter import *
import Errors


def ErrorPopup(code, e=None):
    # init
    root = Toplevel()
    root.title("Error")
    root.iconbitmap("GUI/MGLogo.ico")
    Codes = Errors.Errors()

    errorLabel = Label(root, text=("An Error Occurred! Error Code:", code))
    if e == None:
        errorMessage = Label(root, text=Codes.getError(code))
    else:
        errorMessage = Label(root, text=(Codes.getError(code), '\n', e))

    ok = Button(root, text=" Ok ", command=root.destroy)
    errorLabel.grid(row=0)
    errorMessage.grid(row=1)
    ok.grid(row=2, sticky="e")

    root.mainloop()
