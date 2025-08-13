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
    
    skip_characters = {'reprise', 'response', 'voices', 'solo'}
    for line in lines:
        # Use regex to find character names and their dialogues
        match = re.match(r'(\w+):\s*(.*)', line)
        if match:
            character, dialogue = match.groups()
            # Skip if character is in the skip list (case-insensitive)
            if character.lower() in skip_characters:
                continue
            dialogue_data_list.append({'character': character, 'dialogue': dialogue})
    return pd.DataFrame(dialogue_data_list)

def get_sentiment(text):
    if not isinstance(text, str):
        return None # Handle non-string values
    return TextBlob(text).sentiment.polarity

def analyze_sentiment(dialogue_data):
    dialogue_data['sentiment'] = dialogue_data['dialogue'].apply(get_sentiment)
    return dialogue_data

def generate_sentiment_over_time_plot(dataframe):
    plt.figure(figsize=(14, 7))

    dataframe['line_number'] = range(len(dataframe))

    sns.lineplot(x='line_number', y='sentiment_score', data=dataframe, alpha=0.7)

    plt.title(f"Sentiment Over Time", fontsize=16)
    plt.xlabel("Line Number in Script", fontsize=12)
    plt.ylabel("Sentiment Score", fontsize=12)

    plt.tight_layout()
    plt.savefig(f"{movie_title.lower().replace(' ', '_')}_sentiment_over_time.png")
    plt.show()

def generate_visualizations(dataframe):
    
    generate_sentiment_over_time_plot(dataframe)