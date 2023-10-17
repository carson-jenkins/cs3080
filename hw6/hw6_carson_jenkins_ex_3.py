'''
Homework 6, Exercise 3
Carson Jenkins
04/14/23
This program saves each peice of clipboard text under a keyword. This makes it
so multiple items could be copied and pasted from the clipboard at once. 
'''

import sys
import pyperclip

CLIPBOARD = {}

def save_clipboard(keyword):
    CLIPBOARD[keyword] = pyperclip.paste()
    print(f"Clipboard saved under '{keyword}'.")

def copy_clipboard(keyword):
    if keyword in CLIPBOARD:
        pyperclip.copy(CLIPBOARD[keyword])
        print(f"Clipboard contents for '{keyword}' copied to clipboard.")
    else:
        print(f"No clipboard saved under '{keyword}'.")

def list_clipboards():
    print("List of saved clipboards:")
    for keyword in CLIPBOARD:
        print(keyword)

if len(sys.argv) == 3:
    command, keyword = sys.argv[1:]
    if command == "save":
        save_clipboard(keyword)
    else:
        print("Unknown command. Use 'save', 'list', or provide a keyword to copy to clipboard.")
elif len(sys.argv) == 2:
    command = sys.argv[1]
    if command == "list":
        list_clipboards()
    else:
        copy_clipboard(command)
else:
    print("Usage: python3 mcb.py save <keyword>, python3 mcb.py <keyword>, or python3 mcb.py list")