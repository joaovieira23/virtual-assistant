import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Eu sou a Alexa')
engine.say('Em que posso te ajudar?')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('Ouvindo...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
except:
    print("Deu ruim")
