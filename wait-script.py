from tkinter import Tk, simpledialog
from sys import argv

def wait():
    root = Tk()
    title = ''
    message = ''
    if len(argv) > 0:
        title = argv[0]
    if len(argv) > 1:
        message = argv[1]
    simpledialog.askstring(title, message)

if __name__ == "__main__":
    wait()
