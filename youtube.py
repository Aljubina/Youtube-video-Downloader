#Youtube Video downloader

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
#tkinker is basic 2D graphics library 

def download_video(url, save_path):     #url -> video v wanna download , save_path -> where to save that video
    try:     #when u r using api stuff can go wrong so to handle exceptions try except blocks
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")   #access to streams of the video
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video download successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

# Initializing the window
root = tk.Tk()   
# hide the window
root.withdraw()   

if __name__== "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("please enter a youtube url : ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download....")
        download_video(video_url, save_dir)
    else:
        print("Invalid save Location")