import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import time

def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def main():
    sourcePath = "./2.mp4"
    camera = getVideoSource(sourcePath, 720, 480)
    player = MediaPlayer(sourcePath)

    while True:
        start_time = time.time()
            
        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (720, 480))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if val != 'eof' and audio_frame is not None:
            frame, t = audio_frame
            current_time = time.time() - start_time
            sleep_time = max(0, t - current_time)
            time.sleep(sleep_time)

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
