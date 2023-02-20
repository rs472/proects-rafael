import os
from moviepy.editor import *

video = VideoFileClip(os.path.join("Nao da mais pra voltar-Pe Jonas.mp4"))
video.audio.write_audiofile(os.path.join("Nao da mais pra voltar-Pe Jonas.mp3"))