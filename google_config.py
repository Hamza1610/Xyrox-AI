from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
# get google api keys
GOOGLE_API_KEY = os.getenv(key='GOOGLE_API_KEY')

#configure gemini library
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Generative GEMINI Model
model = genai.GenerativeModel('gemini-pro')

# chat inititalize starting a chat with model 
chat = model.start_chat(history=[])

def Gemini(mode,text):
    """_summary_ : The to to_markdown format gemini generated text to markdown format
    Args:
        mode (str): types of Gemini mode:
            gen (str): for generative text only
            chat (str): for chat session
        text (str): Gemini generated text

    Returns:
        text (str): mardown formatted text 
    """
    if mode == 'gen':
        # text generated from gemini
        response = model.generate_content(text)
        # format to markdown
        # response = response.text.replace('•', '  *')
        return response.text
    elif mode == 'chat':
        # Later implement history in database
        response = chat.send_message(text)
        return response.text

    else:
        return 'Unknown parameter'