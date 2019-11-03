#
# File:		main.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: Entry point of the code, initializes options

from GUI import MainGUI
from GUI import ErrorWindow
import Errors

def main():

    # init GUI
    try:
        MainGUI()
    except Exception as e:
        ErrorWindow.ErrorPopup(Errors.ErrorCodes.ERR_UNKNOWN, e)


if __name__ == "__main__":
    main()
