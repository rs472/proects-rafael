import speech_recognition as sr
import pyttsx3
import time

voice = pyttsx3.init()
voice.say('Olá, sou a Samantha, e irei transformar suas falas em escritas')
voice.runAndWait()

rec = sr.Recognizer()

#ativar o microfone

with sr.Microphone() as mic:

#ajustando ruidos:

    rec.adjust_for_ambient_noise(mic)
    print('Ouvindo...')
#captando audio:
    
    audio = rec.listen(mic)

#transformando em texto:
try:
    print ('a Samantha acha que você disse: ' + rec.recognize_google(audio, language='PT-BR'))

except sr.UnknownValueError:
    voice.say('Desculpe, a Samantha não entendeu')
    voice.runAndWait()