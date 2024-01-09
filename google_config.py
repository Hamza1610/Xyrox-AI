from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
# get google api keys
GOOGLE_API_KEY = os.getenv(key='GOOGLE_API_KEY')

#configure gemini library
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 512,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Initialize Generative GEMINI Model
model = genai.GenerativeModel('gemini-pro', generation_config=generation_config, safety_settings=safety_settings)


# chat inititalize starting a chat with model 
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Who are you?"]
    },
    {
        "role": "model",
        "parts": ["I'm Xyrox, your personal assistant, I do many things, I can create poems, make jokes, I  can gist and converse with you on any topic"]
    },
])

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