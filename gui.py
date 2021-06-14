from tkinter import *
from tkinter import filedialog

root = Tk()

root.title('Video Downloader')

canvas = Canvas(root,width=400,height=400)
canvas.pack()

#app label
app_label = Label(root,text="Video Downloader",fg='blue',font=('Arial',20))
canvas.create_window(200,20,window=app_label)

# entry to accecpt vid url
url_label = Label(root,text="Video URL")
url_entry = Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

# path to download
path_label = Label(root,text="Select Path to Download")
path_button = Button(root,text="Select")
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,175,window=path_button)

# button
download_button = Button(root, text="Download")
canvas.create_window(200,250,window=download_button)

root.mainloop()