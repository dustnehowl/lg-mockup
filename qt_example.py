import vlc
import os
import time

class Player:

    def __init__(self):
        self.player = vlc.Instance()
        self.mediaPlayer = self.player.media_player_new()

    def addPlayList(self, localPath):
        self.mediaList = self.player.media_list_new()
        path = os.path.join(os.getcwd(), localPath)
        media = self.player.media_new(path)
        self.mediaList.add_media(media)
        self.listPlayer = self.player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
        self.listPlayer.set_media_player(self.mediaPlayer)
        self.listPlayer.set_playback_mode(vlc.PlaybackMode.loop)

    def play(self):
        self.listPlayer.play()

    def stop(self):
        self.listPlayer.stop()

play = Player()
play.addPlayList("./2.mp4")
play.play()
while True:
    time.sleep(4)
