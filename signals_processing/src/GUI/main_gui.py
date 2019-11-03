#
# File:		main_gui.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: This file implements the graphical user interface for the signals processing materials.

from tkinter import *
import sys
from GUI import SettingsWindow
from GUI import ConnectionsWindow
from GUI import PlotSettingsWindow
import Errors
import Settings


class MainGUI:
    def __init__(self):
        # init vars.
        self.fullscreen = False
        self.settings = Settings.Settings()
        self.error = Errors.Errors()

        # begin init
        self.root = Tk()
        self.root.title("Signals Processing System")

        # full screen stuff
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)

        # rebind close
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.quit())

        # init main menu bar
        menubar = Menu(self.root)

        # init sub file menu bar
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Settings", command=lambda: SettingsWindow.SettingsPopup(), font=(self.settings.font, self.settings.fontSize))
        file_menu.add_command(label="Connections", command=lambda: ConnectionsWindow.ConnectionsPopup(), font=(self.settings.font, self.settings.fontSize))
        file_menu.add_command(label="Exit", command=lambda: self.quit(), font=(self.settings.font, self.settings.fontSize))
        menubar.add_cascade(label="File", menu=file_menu)

        # init sub Plot menubar
        plot_menu = Menu(menubar, tearoff=0)
        plot_menu.add_command(label="Freeze Plots", font=(self.settings.font, self.settings.fontSize))
        plot_menu.add_command(label="Resume Plotting", font=(self.settings.font, self.settings.fontSize))
        plot_menu.add_command(label="Plotting Preferences", command=lambda: PlotSettingsWindow.PlotSettingsPopup(), font=(self.settings.font, self.settings.fontSize))
        menubar.add_cascade(label="Plot", menu=plot_menu)

        self.root.config(menu=menubar)

        # creates the status bar along the bottom for event printing
        self.systemText = StringVar()
        system = Label(self.root, textvariable=self.systemText, anchor="w", width=100, font=(self.settings.font, self.settings.fontSize))
        system.pack(side="bottom", fill="x", anchor=S, expand=False)

        # set icon
        self.root.iconbitmap("GUI/MGLogo.ico")

        # Loops the window to keep it open
        self.root.mainloop()

    # Event function, toggles fullscreen on F11 keypress
    def toggle_fullscreen(self, event=None):
        self.fullscreen= not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    # Event function, disables fullscreen on ESC keypress
    def end_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    # Interrupts exit to clean up before exiting
    def quit(self):
        self.root.destroy()
        sys.exit()

