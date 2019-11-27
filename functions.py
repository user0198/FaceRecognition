from tkinter import Tk
from tkinter.filedialog import askopenfilename


def getFile():
    Tk().withdraw() 
    filename = askopenfilename() 
    return filename