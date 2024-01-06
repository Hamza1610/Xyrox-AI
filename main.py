from engine import Xyrox

# Initializing engine class
engine = Xyrox()


class Xyrox_loop:

    @staticmethod
    def run():

        # Event variables
        START = True
        EXIT = False
        LISTEN = True
        REPLY = False
        SR_GEN = ''
        GEMINI_GEN = ''

        engine.make_speech('Hello how are you doing today, how may I help you!')
        # Xyrox loop
        while START:

            # if LISTEN is True then call  record speech method and set LISTEN to False, REPLY TO True
            if LISTEN:

                while True:
            
                    #  # text generated from Speech recognition engine
                    SR_GEN = engine.listen_to_speech()

                    # Lenght of text genreated us 
                    if SR_GEN:
                        GEMINI_GEN = engine.compute_text(mode='chat',text=SR_GEN)
                        break
                    # checks if SR_GEN is a local command
                    # iscommand = engine.iscommand(SR_GEN)
                
                    #if iscommand == True:
                    #EXIT = True
                    #else:
                    # text generated from gemini engine
                    #GEMINI_GEN = engine.compute_text(mode='gen',text=SR_GEN)

                # State controller
                if GEMINI_GEN:
                    LISTEN = False
                    REPLY = True

            # if REPLY is True then call  make speech method and set REPLY to False, LISTEN to True
            if REPLY:
                # calling engine method
                engine.make_speech(GEMINI_GEN)

                # State controller     
                REPLY = False
                LISTEN = True

            # If Exit is True then Start is equals to False 
            if EXIT:

                engine.exit_speech()

                # State controller
                START = False
