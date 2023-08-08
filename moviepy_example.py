import tkinter as tk
from tkinter import ttk
from moviepy.editor import VideoFileClip
import threading

class MultimediaPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multimedia Player")

        self.play_button = ttk.Button(root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.video_path = "./video.mp4"
        self.video_clip = VideoFileClip(self.video_path)
        self.audio = self.video_clip.audio

        self.is_playing = False
        self.current_time = 0

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.play_audio_thread()

    def play_audio_thread(self):
        self.audio_thread = threading.Thread(target=self.play_audio)
        self.audio_thread.start()

    def play_audio(self):
        self.audio.set_start(self.current_time)
        self.audio.play()

    def pause(self):
        if self.is_playing:
            self.audio.pause()

    def stop(self):
        self.is_playing = False
        self.audio.stop()
        self.audio = self.video_clip.audio

    def update(self):
        if self.is_playing:
            self.current_time += 0.1  # Increment time by 0.1 seconds
            if self.current_time >= self.video_clip.duration:
                self.stop()
                return
            frame = self.video_clip.get_frame(self.current_time)
            self.video_label.config(image=self.convert_frame_to_tk_image(frame))
            self.root.update()
        self.root.after(100, self.update)  # Update every 100 milliseconds

    def convert_frame_to_tk_image(self, frame):
        height, width, _ = frame.shape
        return tk.PhotoImage(master=self.root, width=width, height=height, data=self.rgb_to_ppm(frame))

    def rgb_to_ppm(self, frame):
        return ''.join(['{0:03}'.format(value) for value in frame.flatten()])

root = tk.Tk()
app = MultimediaPlayerApp(root)

app.video_label = tk.Label(root)
app.video_label.pack()

app.update()  # Start updating the video playback
root.mainloop()
