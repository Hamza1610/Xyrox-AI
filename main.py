from engine import Xyrox
from threading import Thread, Event
from pygame_player import Player
import sqlite3
from db_wrapper import DB

# Initializing engine class
engine = Xyrox()
wrapper = DB('chat_history')

class Xyrox_loop:

    def __init__(self):
        # Event variables
        self.START = True
        self.EXIT = False
        self.LISTEN = True
        self.REPLY = False
        self.SR_GEN = ''
        self.GEMINI_GEN = ''
        self.INTERRUPT = Event()


    def run(self):

        engine.make_speech('Hello how are you doing today!, any thing for me')
        self.START = True
        # Xyrox loop
        while self.START:
            # if LISTEN is True then call  record speech method and set LISTEN to False, REPLY TO True
            if self.LISTEN:

                while True:
            
                    #  # text generated from Speech recognition engine
                    self.SR_GEN = engine.listen_to_speech()

                    # Lenght of text genreated us 
                    if self.SR_GEN:

                        wrapper.insert({ 'Me': self.SR_GEN})
                        # send SR_GEN to engine to give response
                        self.GEMINI_GEN = engine.compute_text(mode='chat',text=self.SR_GEN)

                        # Added SR_GEN and GEMINI_GEN to Chat hisotry
                        break

                # State controller
                if self.GEMINI_GEN:


                    wrapper.insert({ 'Xyrox': self.GEMINI_GEN })
                    self.LISTEN = False
                    self.REPLY = True

            # if REPLY is True then call  make speech method and set REPLY to False, LISTEN to True
            if self.REPLY:

                # self.INTERRUPT.clear()
                # calling engine method
                engine.make_speech(self.GEMINI_GEN)

                # State controller     
                self.REPLY = False
                self.LISTEN = True


    def start(self):
        Thread(target= self.run).start()
        print('Xyrox loop started')

    def stop(self):
        self.START = False
        print('Xyrox lopp ended')
    
    def interrupt(self):
        
        Player.stop()
        print('Xyrox voice interupted')

    def apply(self):
        print('Apply settings clicked!')