import speech_recognition as sr 
import webbrowser
import time 
import playsound
import os
import random
from gtts import gTTS
from time import ctime




r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Mr_Pickles(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Mr_Pickles('sorry I did not get that')
        except sr.RequestError:
            Mr_Pickles('sorry my speech service is down')
        return voice_data

def Mr_Pickles(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def repond(voice_data):
    if 'what is your name?' in voice_data:
        Mr_Pickles('My name is Mr Pickles')
    if 'what time is it?' in voice_data:
        Mr_Pickles(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Mr_Pickles('Here is what I found ' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Mr_Pickles('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
Mr_Pickles('How can I help you sir?')
while 1:
        voice_data = record_audio()
        respond(voice_data)
