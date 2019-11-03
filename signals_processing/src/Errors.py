#
# File:		Errors.py
# Author:	Alex Miu, ale18@umbc.edu
# Last Updated: 11/02/2019
# Description: File holding Errors Enum and error strings

from enum import Enum

class ErrorCodes(Enum):

    ERR_SUCCESS = 0
    ERR_UNKNOWN = 10
    ERR_GEN_CON = 20
    ERR_GEN_INT = 30

    # ADD OTHER ERRORS HERE


class Errors:
    def __init__(self):
        self.error_list = \
            {
                ErrorCodes.ERR_SUCCESS: "Operation was successful",
                ErrorCodes.ERR_UNKNOWN: "Unknown error",
                ErrorCodes.ERR_GEN_CON: "General connection error",
                ErrorCodes.ERR_GEN_INT: "General internal error"
            }

    def getError(self, code):
        return self.error_list[code]
