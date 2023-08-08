import pygame
import threading

class Player:
    def __init__(self, scaled=False):
        pygame.init()
        self.scaled = scaled
        self.video_clip = None
        self.is_playing = False
        self.audio_thread = None

    def load(self, video_path):
        self.video_clip = pygame.movie.Movie(video_path)
        self.video_surface = pygame.Surface(self.video_clip.get_size())

    def play_pause(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.play_audio_thread()

    def play_audio_thread(self):
        if self.audio_thread is None:
            self.audio_thread = threading.Thread(target=self.play_audio)
            self.audio_thread.start()

    def play_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.video_clip.audio)
        pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def stop(self):
        self.is_playing = False
        self.stop_audio()

    def play(self):
        self.play_pause()

    def update(self, surface):
        if self.is_playing:
            self.video_surface.blit(self.video_clip.get_surface(), (0, 0))
            if self.scaled:
                scaled_surface = pygame.transform.scale(self.video_surface, surface.get_size())
                surface.blit(scaled_surface, (0, 0))
            else:
                surface.blit(self.video_surface, (0, 0))

    def close(self):
        self.stop_audio()
        pygame.quit()

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import PhotoImage

    root = tk.Tk()

    videoplayer = Player(scaled=True)
    videoplayer.load("samplevideo.mp4")

    canvas = tk.Canvas(root, width=videoplayer.video_clip.get_size()[0], height=videoplayer.video_clip.get_size()[1])
    canvas.pack()

    def update_canvas():
        videoplayer.update(canvas)
        canvas.update()
        root.after(10, update_canvas)

    update_canvas()
    videoplayer.play()  # Play the video

    root.protocol("WM_DELETE_WINDOW", videoplayer.close)
    root.mainloop()
