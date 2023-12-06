import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == "__main__":
    # Example interaction with the blind assistant
    text_to_speech("Hello, how can I assist you today?")

    user_input = speech_to_text()
    
    if user_input:
        print(f"User said: {user_input}")
        text_to_speech(f"You said: {user_input}")
    else:
        text_to_speech("Sorry, I didn't catch that. Can you please repeat?")

    