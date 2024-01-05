from engine import Xyrox

# Initializing engine class
engine = Xyrox()

# Event variables
START = True
EXIT = False
LISTEN = True
REPLY = False
GEN_TEXT = ''
GEMINI_GEN = ''

# The welcome speech method welcome user to the appilcation
# engine.welcome_speech()
while START:

    # if LISTEN is True then call  record speech method and set LISTEN to False, REPLY TO True
    if LISTEN:
        #  # text generated from Speech recognition engine
        SR_GEN = engine.listen_to_speech()


        GEMINI_GEN = engine.compute_text(mode='chat',text=SR_GEN)
        # checks if SR_GEN is a local command
        # iscommand = engine.iscommand(SR_GEN)
        
        # if iscommand == True:
        #     EXIT = True
        # else:
        #     # text generated from gemini engine
        #     GEMINI_GEN = engine.compute_text(mode='gen',text=SR_GEN)

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