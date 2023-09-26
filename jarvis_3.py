"""
    Name: jarvis_3.py
    Author: Adam Frisch
    Created: 2/19/23
    Purpose: Voice recognition text to speech 
"""

# pip install SpeechRecognition
from sys import exit
from time import sleep
import speech_recognition as sr
import pyttsx3
import wikipedia
import utils 


class Jarvis:
    def __init__(self) -> None:
        # Create SpeechRecognition recognizer object
        self.r = sr.Recognizer()
        self.init_text_to_speech()
        # Display menu choices
        self.main_menu()
        self.greet_user()
        
# -------------------- GET WIKIPEDIA ------------------------ #
    def get_wikipedia(self):
        """
            Search Wikipedia
        """
        try:
            # Type in your search term
            print(utils.get_title("Search Wikipedia:"))
            print("What would you like to search for on Wikipedia?")
            self.engine.say("What would you like to search for on Wikipedia?")
            self.engine.runAndWait()

            self.get_voice_input()
            
            # Return a summary result of three sentences
            summary = wikipedia.summary(self.__query, sentences=3)
            print(f"\n{summary}")
            self.engine.say(summary)
            self.engine.runAndWait()
            
        except:
            # If there is an exception, allow the user to try again
            print("Try a different search term.")

        # Display menu choices
        self.main_menu()

    def get_voice_input(self):
        """Recognizes user voice input using
            Speech recognition module, converts it to text
        """
        # Your local microphone as the source
        with sr.Microphone() as source:
            print('Listening . . . .')
            self.r.pause_threshold = 1
            # Start listening for speech
            audio = self.r.listen(source, timeout=3)

            try:
                print('Recognizing . . .')
                # Capture the recognized word in a string variable
                recognized_words = self.r.recognize_google(audio, language="en-in", show_all=True)
                # Google Speech Recognition returns a list of dictionaries
                # Pull only the transcript with the highest confidence
                self.__query = recognized_words['alternative'][0]['transcript']
                print(self.__query)
                # If you say quit, the program will exit

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand what you said.")

            except sr.RequestError as e:
                # If there was an error communicating with Google Speech
                print(f"Google Speech did not respond: {e}")

# ------------------ MAIN MENU --------------------- #
    def main_menu(self):
        print(utils.get_title("JARVIS Main Menu"))
        print("Commands: Wikipedia, quit")

# ------------------ VOICE COMMANDS -------------------- #
    def voice_commands(self):
        if self.__query.lower() == "quit":  
            print("Goodbye!")
            self.quit_program()
        elif self.__query.lower() == "wikipedia":
            self.get_wikipedia()

# ------------------------- SPEAK ----------------------------- #
    def speak(self):
        # Get text from command line
        spoken_text = input("((<< ")
        # Call the say method to spreak the text
        print("Talking . . .")
        self.engine.say(spoken_text)
        self.engine.runAndWait()

# ------------------------ CALIBRATE SPEECH ENGINE ------------------------ #
    def init_text_to_speech(self):
        # Change these constants to experiment with the speech engine
        RATE = 150     # Integer default: 200 words per minute
        VOLUME = 0.9   # float default: 1.0, range: 0.0-1.0 inclusive
        VOICE = 0      # Integer default: 0 for David, 1 for Zira
        # Initialize the pyttxs3 voice engine
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", RATE)
        self.engine.setProperty("volume", VOLUME)
        # Retrieves all available voices from your system
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[VOICE].id)
        # Run engine to set properties
        self.engine.runAndWait()

# ------------------- GREET USER -------------------------- #
    def greet_user(self):
        self.engine.say("Hello, I am David.")
        self.engine.say(
            "What would you like me to do for you? Press CTRL C to exit")
        print("Talking . . .")
        self.engine.runAndWait()

# -------------------- QUIT PROGRAM ---------------------- #
    def quit_program(self):
        # Quit program
        print("\nHave a good day!")
        self.engine.say("Have a good day!")
        self.engine.runAndWait()
        self.engine.stop()
        sleep(2)
        exit(0)
        
        

# Create a jarvis program object
jarvis = Jarvis()
while True:
    jarvis.get_voice_input()
    jarvis.voice_commands()

