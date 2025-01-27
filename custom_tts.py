import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.setProperty('rate', 150)  # Set speaking speed
    engine.setProperty('volume', 0.9)  # Set volume (0.0 to 1.0)
    
    engine.say(text)  # Queue the text to speak
    engine.runAndWait()  # Run the engine to process the queue

if __name__ == "__main__":
    user_text = input("Enter the text you want to convert to speech: ")
    text_to_speech(user_text)
