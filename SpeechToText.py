import speech_recognition as sr

# Initialize the recognizer
r=sr.Recognizer()

a=sr.AudioFile('file1.wav')
with a as source:
    audio=r.record(source)
  
# Using ggogle to recognize audio
text=r.recognize_google(audio)

file_1=open(r,'file2.txt',"a")
file_1.writelines(text)
file_1.close()
