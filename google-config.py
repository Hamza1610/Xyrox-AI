import pathlib
# import textwrap

import google.generativeai as genai

# Used to securely store your API key
# from google.colab import userdata

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

GOOGLE_API_KEY = ''
genai.configure(api_key=GOOGLE_API_KEY)

# list GEMINI moodel
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

# Generate text from GEMINI
model = genai.GenerativeModel('gemini-pro')

# generate text from GENINI
response = model.generate_content("What is the meaning of life?")

print(response.text)