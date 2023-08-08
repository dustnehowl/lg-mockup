import kivy
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class MyApp(App):
    def build(self):
        player = VideoPlayer(source='./2.mp4', state='play')
        return player
    
if __name__ == '__main__':
    MyApp().run()