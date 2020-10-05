import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search edureka: search youtube ]')
    print('speak now')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
text = r2.recognize_google(audio)
print(text)