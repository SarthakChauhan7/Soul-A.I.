
#download pyttsx3, soeechRecognition, pyaudio, pyWebBrowser, numpy, os, sys, random, OpenAI
#Must have config file to work
#Make sure to add your own API key for chatGPT to start his operations

'''******************* START OF FILE ******************'''

import pyttsx3
import speech_recognition as sr
import pyaudio
import random
import datetime
import webbrowser
import numpy
import os
import sys
import Config
from ChatbotGPT import apikey
import openai


#functions
def toung(Reply):
    engine = pyttsx3.init()
    engine.say(f'{Reply}')
    engine.runAndWait()
    engine.stop()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Soul A.I"

def chat():

# Main chat loop
    toung("Soul A.I.: Hi! How can I assist you today?")
    while True:
        user_input = takeCommand()
        if user_input.lower() == 'bye':
            toung("Goodbye!")
            print("Goodbye!")
            break
        else:
            bot_reply = chat_with_gpt(user_input)
            toung(bot_reply)
            print("Bot:", bot_reply)
# OpenAI API

def chat_with_gpt(message):
    openai.api_key = apikey
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        f.write(text)
        return text


toung("HI! I am soul A.I. designed by Sarthak for his assistance")
while True:
    print("Listening...")
    query = chat()

'''******************* END OF FILE *********************'''