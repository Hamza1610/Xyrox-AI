import io
import pygame
import speech_recognition
from gtts import gTTS
import speech_recognition as sr

class Engine :

    """
    _summary_: AI engine for TTS and STT

    """
    @staticmethod 
    def welcome_speech():

        """
        _summary_: Method the make welcoming speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text='Welcome to Xyrox AI, what can I help you with today.', lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)
            # Initialize Pygame mixer
            pygame.mixer.init()
            # Load the audio from the buffer
            pygame.mixer.music.load(audio_buffer)
            # Play the audio
            pygame.mixer.music.play()
            # Optional: Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            print('Welcoming speech generate!')
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Welcoming Done!')


    @staticmethod 
    def listen_to_speech():

        """
        _summary_: Method the listening to speech for reply, note: the listing code lies here
        """
        return sr.Microphone(device_index = None)
 

    @staticmethod 
    def make_speech(text):

        """
        _summary_: Method the make speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text=text, lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)
            # Initialize Pygame mixer
            pygame.mixer.init()
            # Load the audio from the buffer
            pygame.mixer.music.load(audio_buffer)
            # Play the audio
            pygame.mixer.music.play()
            # Optional: Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            print('Speech generation done!')
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Done!')

    @staticmethod 
    def compute_text(text):
        """
        _summary_: Compute text by Gemini API
        """
        # Gemini api keys
        api_keys = {}
        return "GEMINI TEXT"

    @staticmethod 
    def exit_speech():

        """
        _summary_: Method the make speech
        """
        try:
            # Create the text-to-speech object
            tts = gTTS(text='Good bye for now see you later in the day.', lang='en')
            # Create a buffer to hold the audio data
            audio_buffer = io.BytesIO()
            # Write the audio data to the buffer
            tts.write_to_fp(audio_buffer)
            # Rewind the buffer to the beginning
            audio_buffer.seek(0)
            # Initialize Pygame mixer
            pygame.mixer.init()
            # Load the audio from the buffer
            pygame.mixer.music.load(audio_buffer)
            # Play the audio
            pygame.mixer.music.play()
            # Optional: Wait for the audio to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            print('Exit processing..')
        except:
            print('Something went wrong: Please check your network')
        finally:
            print('Exit..')
