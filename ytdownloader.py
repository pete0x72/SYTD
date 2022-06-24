from pytube import YouTube
from os import path
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("YouTube_Downloader v0.1")

app_width = 900
app_height = 400

fontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "18")
contFontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "16")
descFontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "14")
buttonFontStyle = tkFont.Font(family = "CaskaydiaCove Nerd Font", size = "24")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.maxsize(900,400)
root.minsize(900,400)
root.config(bg = "#161B22")

downloadPath = StringVar()
def destination():
    path = filedialog.askdirectory(initialdir = "Your Directory Path")
    downloadPath.set(path)

def dlVidButtonFunc():
    folder = downloadPath.get()
    dlLink = linkContainer.get()
    YouTube(dlLink).streams.get_highest_resolution().download(folder)

def dlAudButtonFunc():
    dlLink = linkContainer.get()
    YouTube(dlLink).streams.get_audio_only().download(folder)

load=Image.open("assets/logo.png")
render=ImageTk.PhotoImage(load)
img=Label(root, image=render, bg="#161B22")
img.place(relx=0.04,rely=0.07)

linkLabel = Label(root,  text="Video Link:",
                        font=fontStyle,
                        fg = "#C6CFD7",
                        bg = "#161B22")
linkLabel.place(relx=0.04, rely=0.25)

linkContainer = Entry(root, font=contFontStyle,
                        width = 50,
                        fg = "#C6CFD7",
                        bg = "#393E46",
                        bd = 3,
                        justify =CENTER,
                        relief = SUNKEN)
linkContainer.place(relx=0.24, rely=0.25)

pathLabel = Label(root, text="Select Destination Folder:",
                        font=fontStyle,
                        fg = "#C6CFD7",
                        bg = "#161B22")
pathLabel.place(relx=0.25,rely=0.45)

pathEntry = Entry(root, font=descFontStyle,
                        text=downloadPath,
                        width = 40,
                        fg = "#C6CFD7",
                        bg = "#393E46",
                        bd = 3,
                        justify =CENTER,
                        relief = SUNKEN)
pathEntry.place(relx=0.18,rely=0.56)

browseButton = Button(text = "Browse",
                    font = buttonFontStyle,
                    bg = "#0A81AB",
                    activebackground="#035397",
                    fg = "white",
                    activeforeground="white",
                    cursor = "hand2",
                    command = destination)
browseButton.place(relx=0.7, rely=0.54)

dlVidButton = Button(text = "Download Video",
                    font = buttonFontStyle,
                    bg = "#0A81AB",
                    activebackground="#035397",
                    fg = "white",
                    activeforeground="white",
                    cursor = "hand2",
                    command = dlVidButtonFunc)
dlVidButton.place(relx = 0.1, rely = 0.77)

dlAudButton = Button(text = "Download Audio",
                    font = buttonFontStyle,
                    bg = "#0A81AB",
                    activebackground="#035397",
                    fg = "white",
                    activeforeground="white",
                    cursor = "hand2",
                    command = dlAudButtonFunc)
dlAudButton.place(relx = 0.55, rely = 0.77)

root.mainloop()


