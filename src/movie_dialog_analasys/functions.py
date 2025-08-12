import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import re

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def clean_and_parse_script(raw_script_text):
    # Split the script into lines
    lines = raw_script_text.split('\n')
    
    # Initialize a list to hold structured dialogue data
    dialogue_data_list = []
    
    for line in lines:
        # Use regex to find character names and their dialogues
        match = re.match(r'(\w+):\s*(.*)', line)
        if match:
            character, dialogue = match.groups()
            dialogue_data_list.append({'character': character, 'dialogue': dialogue})
    
    return pd.DataFrame(dialogue_data_list)

 def get_sentiment(text):
    if not isinstance(text, str):
        return None # Handle non-string values
    return TextBlob(text).sentiment.polarity

def analyze_sentiment(dialogue_data):
    dialogue_data['sentiment'] = dialogue_data['dialogue'].apply(get_sentiment)
    return dialogue_data
