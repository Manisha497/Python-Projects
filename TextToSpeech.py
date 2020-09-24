from gtts import gTTS

# This module is imported so that we can play the converted audio 
import os

f=open('file1.txt')
x=f.read()
audio=gTTS(text=x,lang='en',slow=False)

# Saving the converted audio in a .wav file named 
audio.save('file1.wav')

# Playing the converted file
os.system('file1.wav')
