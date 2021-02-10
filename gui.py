#IMPORTS
from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog
import json
import spotdl
from spotdl.__main__ import spotifyClient
from spotdl.download.downloader import DownloadManager
from spotdl.search.songObj import SongObj
import os

#Creating the Client ID and ClientSecret variables
clientID="6b6ace45bd094b1fa438151f35fa3fb0"
clientSecret="963f4330759a403ea6cafc2ff03dc036"
spotifyClient.initialize(clientID,clientSecret)

#Reading the json file that keeps the data saved
with open('data.json') as f:
    data=json.load(f)

#Defining the TKinter Window
root=Tk()
root.title("Harmony.")
root.iconbitmap('./assets/logo.ico')

#Runs when the Dirtbutt button is pressed
def dirselection():
    Dirfield.delete(0,END)
    directory=tkinter.filedialog.askdirectory(title="Select Download Directory", initialdir=data["Directory"])
    Dirfield.insert(0,directory)
    data["Directory"]=directory
    #changes the directory location in data
    with open('data.json', 'w') as f:
        json.dump(data, f)
    
def dlmusic():
    Dir=Dirfield.get()
    url=musfield.get()
    temp=SongObj.from_url(url)
    currdir=os.getcwd()
    os.chdir(Dir)
    download=DownloadManager()
    download.download_single_song(songObj=temp)
    os.remove('./Temp')
    os.chdir(currdir)
    return
#~~~~~~~~~~~~~~~~~~
# Creating Widgets
#~~~~~~~~~~~~~~~~~~

#Image widget
fimage=ImageTk.PhotoImage(Image.open('./assets/fimage.png'))
imglabel=Label(root,image=fimage)

#Entry Widget to show Directory
Dirfield=Entry(root)
Dirfield.insert(0,f"{data['Directory']}")

#Button Widget to open Directory
Dirbutt=Button(root,text="Select Directory", command=dirselection)

#Text widget to tell the user to Enter the spotify link below
tell=Label(root,text="Enter the link in the text field below:")

#Input widget to get the link
musfield=Entry(root)

#Button to download the song
dowbutt=Button(root, text="Download!", command=dlmusic)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packing stuff onto the GUI
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
imglabel.pack()
Dirbutt.pack()
Dirfield.pack()
tell.pack()
musfield.pack()
dowbutt.pack()



root.mainloop()
