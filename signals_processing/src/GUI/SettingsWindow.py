#
# File:		SettingsWindow.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: File holding SettingsPopup implementation for Settings GUI

from tkinter import *


def SettingsPopup():
    # init
    root = Toplevel()
    root.title("Settings")
    root.iconbitmap("GUI/MGLogo.ico")

    # apply and cancel buttons
    ButtonFrame = Frame(root)
    ButtonFrame.grid(row=7, column=0, columnspan=2)

    SaveButton = Button(ButtonFrame, text=" Apply ")
    SaveButton.grid(row=0, column=0)

    SaveButton = Button(ButtonFrame, text=" Save and Quit ", command=root.destroy)
    SaveButton.grid(row=0, column=1)

    CancelButton = Button(ButtonFrame, text=" Cancel ", command=root.destroy)
    CancelButton.grid(row=0, column=2)
