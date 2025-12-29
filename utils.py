# utility methods for repeated use
import os

def clear_screen():
    """clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    """pauses the program for continuation"""
    input("Press enter to continue")