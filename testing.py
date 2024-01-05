import speech_recognition as sr

def listen_and_convert():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen to the user's voice
        audio = recognizer.listen(source)
        print("Recognition complete. Converting to text...")

    try:
        # Use Google Web Speech API for speech-to-text conversion
        text = recognizer.recognize_google(audio)
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error with the speech recognition service; {0}".format(e))

if __name__ == "__main__":
    listen_and_convert()
