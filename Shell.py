#region ------------------   ABOUT   -----------------------------
"""
##################################################################
# Created By: Gilad Barak                                        #
# Date: 09/10/2016                                               #
# Name: Python Shell - CMDish                                    #
# Version: 1.0                                                   #
# Windows Tested Versions: Win 7 32-bit                          #
# Python Tested Versions: 2.6 32-bit                             #
# Python Environment: PyCharm                                    #
##################################################################
"""
#endregion

#region ----------   IMPORTS   -----------------------------
import subprocess
#endregion

#region ----------   GLOBAL SETTINGS   ---------------------
__author__ = "Giladondon"
__name__ = "main"
#endregion

#region -----------  CONSTANTS  ----------------------------
CMD_COMMAND_PATH = "C:\Windows\System32"
PYTHON_SCRIPTS_PATH = "C:\Heights\Documents\Coding\ShellPY"
WELCOME_MESSAGE = "Giladondon's Window [Version 1.0]\n(c) 2016 Giladondon Corporation. All rights reserved.\n"
INPUT_SYMBOL = "*(.)_(.)* "
ILLEGAL_COMMAND = "Fool me once - Shame on you\nFool me twice - Shame on me"
LEGAL_INDEX = 0
OUTPUT_INDEX = 1
EXIT_COMMANDS = ["exit", "quit", "bye", "leave"]
EXIT_SYNTAX = "exit"
SPACE = " "
EMPTY = ""
#endregion

#region ----------   FUNCTIONS   ---------------------------


def show_welcome():
    """
    Print welcome text for shell
    :return : N/A
    """
    print WELCOME_MESSAGE

# ----------------------------------------------------------


def user_input():
    """"
    Receives command input from user and parses.
    :return : parsed (by spaces) user input
    """
    raw_command = raw_input(INPUT_SYMBOL)
    parsed_command = raw_command.split(SPACE)

    return parsed_command

# ----------------------------------------------------------


def run_command(parsed_command):
    """
    :param parsed_command: parsed (by spaces) command input from user
    runs command in shell
    :return : Is_Legal, Output from shell
    """
    if parsed_command[0].lower() in EXIT_COMMANDS:
        return True, EXIT_SYNTAX
    try:
        command_output = subprocess.check_output(parsed_command)
        return True, command_output
    except WindowsError:
        print ILLEGAL_COMMAND
        return False, EMPTY

#endregion

#region ----------   MAIN   --------------------------------


def main_loop():
    data_output = run_command(user_input())
    if data_output[LEGAL_INDEX] and data_output[OUTPUT_INDEX] in EXIT_COMMANDS:
        return False
    elif data_output[LEGAL_INDEX]:
        print data_output[OUTPUT_INDEX]

    return True

# ----------------------------------------------------------


def main():
    show_welcome()
    run = main_loop()
    while run:
        run = main_loop()

# ----------------------------------------------------------

if __name__ == "main":
    main()

#endregion

# ----------------------------------------------------------