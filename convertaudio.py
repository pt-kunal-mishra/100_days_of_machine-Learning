# day 1 video to audio

import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()

videos=moviepy.editor.VideoFileClip(video)

audio=videos.audio
audio.write_audiofile("demo.mp3")
print('___end___')
