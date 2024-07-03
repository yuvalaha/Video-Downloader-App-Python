from tkinter import Button, Entry, Tk, filedialog, Canvas, Label
from pytube import YouTube 
from moviepy.editor import VideoFileClip
import shutil

# Get the direction the folder that the user choose to save his video
def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)
    
# Download the video according to the url the user enters
def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading....")
    my_video = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(my_video)
    video_clip.close()
    shutil.move(my_video, file_path)
    print("Download Complete.")


# Create the main window
root = Tk()

# Main title
root.title("My Video Downloader")

# Creating canvas
canvas = Canvas(root, width=400, height=300)

# Packing the canvas
canvas.pack()

# Creating main app label
app_label = Label(root, text="Video Downloader", fg="blue", font=('Arial', 20))
canvas.create_window(200, 20, window=app_label)

# Creating URL label
url_label = Label(root, text="Enter Video URl")
canvas.create_window(200, 80, window=url_label)

# Creating URL entry
url_entry = Entry(root)
canvas.create_window(200, 100, window=url_entry)

# Creating path to the downloaded videos - label and button
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 180, window=path_button)


# Download button
download_button = Button(root, text="Download", command=download)
canvas.create_window(200, 250, window=download_button)

root.mainloop()