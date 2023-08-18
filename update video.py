import cv2
import numpy as np
import pygame

# Function to play the soundtrack
def play_soundtrack(soundtrack_file):
    pygame.mixer.init()
    pygame.mixer.music.load(soundtrack_file)
    pygame.mixer.music.play()

# Function to stop the soundtrack
def stop_soundtrack():
    pygame.mixer.music.stop()

# Main video playback function
def play_video_with_soundtrack(video_file, soundtrack_file):
    new_capture = cv2.VideoCapture('marmots_family_animals_furry_cute_968.mp4')

    # Check if the file opened successfully
    if not new_capture.isOpened():
        print("Error opening the video file")
        return

    # Read the video frames and play the soundtrack
    play_soundtrack(soundtrack_file)
    while new_capture.isOpened():
        ret, frame = new_capture.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Release resources
    new_capture.release()
    cv2.destroyAllWindows()
    stop_soundtrack()

if __name__ == "__main__":
    video_file = 'marmots_family_animals_furry_cute_968.mp4'
    soundtrack_file = 'Jack Sparrow.mp3'  # Replace with your soundtrack file

    play_video_with_soundtrack(video_file, soundtrack_file)
