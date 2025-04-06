import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    return None

def download_video(video_url, save_dir):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()  # Get the best quality
        print(f"Downloading: {yt.title}...")
        stream.download(save_dir)  # Save the video
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    video_url = input("Enter video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
