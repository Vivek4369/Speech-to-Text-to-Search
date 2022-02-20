import speech_recognition as sr
from gtts import gTTS  
from playsound import playsound  
import webbrowser as wb

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('speak')
    audio = r.listen(source)
    
try:
    get = r.recognize_google(audio)
    print(get)
    url = 'https://www.google.com/search?q='
    wb.get().open_new(url+get)
except:
    print('error')
get = r.recognize_google(audio)

language = 'en'  

obj = gTTS(text="Result for"+get, lang=language, slow=False)  

obj.save("exam.mp3")  
  
playsound("exam.mp3")  