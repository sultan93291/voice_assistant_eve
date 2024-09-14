# importing required packages

# external dependencies
import speech_recognition as sr
import webbrowser
import pyttsx3
import sympy as sp
import time
import pygetwindow as gw
import pyautogui
import requests
from dotenv import load_dotenv
import os

# internal dependencies
from appLibary import patterns 
from musicLibary import musicPatterns

# intializing voice recognition
recgonizer = sr.Recognizer()

# initializing pyttsx3 engine support
engine = pyttsx3.init()

# Get and list all voices
voices = engine.getProperty('voices')

# configuring dot env 
load_dotenv()

# defining news api key 
newsAPIKey = "8c37d58220834131a28bfde36ffa922b"



# Set the engine to use the female voice (manually select based on output)
female_voice_id = voices[1].id  
engine.setProperty('voice', female_voice_id)


# initializing speak function
def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(command):

  for pattern,action in patterns.items():
    if(pattern in command.lower()):
      speak(f"opening: {pattern}")
      action()
      return
  
  for musicPattern,music_action in musicPatterns.items():
    if(musicPattern in command.lower()):
      speak(f"palying: {musicPattern}")
      music_action()
      return
  
  if "exit" in command.lower():
      speak("exiting command ! goodbye")
      return"exit"
  
  if "news" in command.lower():
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv('NEWS__API_KEY')}")

    if response.status_code ==200:
        data = response.json()
        articles = data.get('articles',[])

        for article in articles:
          speak(article['title'])


  elif "search for" in command.lower():
    search_web(command)
  
  elif "calculate" in command.lower():
      calculate_expression(command)
  
  elif "repeat after me" in command.lower():
    repeat_text = command.lower().split("repeat after me",1)[1].strip()
    speak(repeat_text)

  elif "stop music" in command.lower():
    window = find_youtube_tab()
    if window:
      try:
          print(f"Activating window: {window.title}")
          window.activate()
          time.sleep(2)  # Increase time for activation
          print("Attempting to play music ....")
          pyautogui.press('space')
          time.sleep(1)  # Wait to ensure the action is registered
          print("stopping music.")
      except Exception as e:
          print(f"Error interacting with the YouTube tab: {e}")
    else:
          print("No YouTube tab found.")

  elif "start music" in command.lower():
    window = find_youtube_tab()
    if window:
      try:
          print(f"Activating window: {window.title}")
          window.activate()
          time.sleep(2)  # Increase time for activation
          print("Attempting to pause music ....")
          pyautogui.press('space')
          time.sleep(1)  # Wait to ensure the action is registered
          print("Music should be paused now.")
      except Exception as e:
          print(f"Error interacting with the YouTube tab: {e}")
    else:
          print("No YouTube tab found.")
    

  else:
    speak("I'm not sure how to respond to that.")

def search_web(command):
    search_query = command.split("search for", 1)[1].strip()
    speak(f"Searching for {search_query}")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

def calculate_expression(command):
  try:
        # Extract the expression after "draw some"
        expression = command.split("calculate", 1)[1].strip()
        
        # Parse and evaluate the expression using sympy
        result = sp.sympify(expression).evalf()
        
        speak(f"The result of {expression} is {round(result)}")
  except Exception as e:
        speak("Sorry, I couldn't calculate that.")
        print(f"Error: {e}")

def listen():
    try:
      with sr.Microphone() as source:
        print("Listening ....")
        audio = recgonizer.listen(source)
        word = recgonizer.recognize_google(audio)


      if(word.lower() == "alexa"):
        speak("yes i'm listening baby") 
        print("babe activated")

        with sr.Microphone() as source:
          audio = recgonizer.listen(source)
          command = recgonizer.recognize_google(audio)
          print(f"command recognized: {command}")
          
          return command
          
    except Exception as e:
        print(e)

def find_youtube_tab():
    for window in gw.getAllWindows():
        if "(277)" in window.title.lower(): 
            print(f"Found potential YouTube window: {window.title}")
            return window
    return None



if __name__ =="__main__":
  speak("Hey ! i'm your virtual machine eve . how can i help you today")

  while True:
    command = listen()
    if command:
        result = processCommand(command)
        if result =="exit":
          break
      





