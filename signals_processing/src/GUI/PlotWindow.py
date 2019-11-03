#
# File:		PlotWindow.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: File for separated plot window implementation

from tkinter import *


def PlotPopup():
    # init
    root = Toplevel()
    root.title("Plot")
    root.iconbitmap("GUI/MGLogo.ico")