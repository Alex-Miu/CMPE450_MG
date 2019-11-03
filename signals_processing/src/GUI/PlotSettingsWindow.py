#
# File:		PlotSettingsWindow.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: File for settings popup for plotting config

from tkinter import *


def PlotSettingsPopup():
    # init
    root = Toplevel()
    root.title("Plotting Preferences")
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
