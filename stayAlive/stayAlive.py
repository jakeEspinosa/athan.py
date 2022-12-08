#!/usr/bin/python3

from pydub import AudioSegment
from pydub.playback import play
import time

sound = AudioSegment.from_mp3('blank.mp3')

while True:
    play(sound)
    time.sleep(1140) 
