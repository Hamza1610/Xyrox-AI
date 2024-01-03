from engine import Engine

# Initializing engine class
engine = Engine()

# Event variables
START = True
EXIT = False
LISTEN = True
REPLY = False
GEN_TEXT = ''

# The welcome speech method welcome user to the appilcation

engine.welcome_speech()
while START:

    # if LISTEN is True then call  record speech method and set LISTEN to False, REPLY TO True
    if LISTEN:
        #  # text generated from Speech recognition engine
        # SR_GEN = engine.listen_to_speech()
        SR_GEN = 'Hello how are you, are you in chat or generative'
        # text generated from gemini engine
        GEMINI_GEN = engine.compute_text(mode='chat', text= SR_GEN)

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