import tkinter as tk
from videoPlayer import Player

root = tk.Tk()

videoplayer = Player(master=root, scaled=True)
videoplayer.load("./video.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

root.mainloop()