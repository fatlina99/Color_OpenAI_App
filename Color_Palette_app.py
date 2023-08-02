#%%
# Libraries
import os
import json

# 3rd parties
import openai
from IPython.display import Markdown, Image, display

# for vscode : from IPythonMarkdown.display import Markdown, display

#%%
# Hiding our key in .env file

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")
openai.api_key[10]

#%%
def display_color_blocks(colors):
    # Create HTML representation of color blocks
    color_blocks = "  ".join(f"<span style='color: {color}'>{chr(9608) * 5}</span>" for color in colors)

    # Display the color blocks
    display(Markdown(color_blocks))

#%%
def color_ai(msg):
  #create a prompt for the color palette generation model

    question = 'Generate a color palette for the beach.'
    answer =' ["#255e65", "#3591a0", "#4da6c4", "#7ac1d0", "#b3dfe3"]'

    # Generate color using ai
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
              "role": "system",
              "content": "You are color palette generator that uses use text prompts to generate a color palettes based on the user theme"
            },
            {
              "role": "user",
              "content": question
            },
            {
              "role": "assistant",
              "content": answer
            },
            {
              "role": "user",
              "content": msg
            }
            ],
        max_tokens = 100,
        temperature = 1
    )
    # parse color from response
    colors = json.loads(response['choices'][0]['message']['content'])

    # Display color blocks
    display_color_blocks(colors)

    # Print the hex codes
    print(colors)

#%%
# to test the output
color_ai('rice paddy color')
# %%
