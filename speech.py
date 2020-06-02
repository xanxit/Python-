from gtts import gTTS #import the gTTS package
import os 
mytext = 'My Name is Sanchit'#write the text you need to convert to speech
language = 'en'#select the shortform of the language you want the speech
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") #it'll save the mp3 file in your workspace folder
os.system("welcome.mp3")
