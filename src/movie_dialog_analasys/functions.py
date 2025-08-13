import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import re
from wordcloud import WordCloud

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
    plt.savefig(f"sentiment_over_time.png")
    plt.show()

def generate_character_sentiment_bar_chart(dataframe):
    # Calculate the average sentiment score for each character
    # Note: Ensure the column name is 'sentiment_score' from your analysis step
    character_sentiment = dataframe.groupby('character')['sentiment_score'].mean()
    character_sentiment = character_sentiment.sort_values(ascending=False)
  
    top_characters = character_sentiment.head(3)
    bottom_characters = character_sentiment.tail(3)
    selected_characters = pd.concat([top_characters, bottom_characters])

    plt.figure(figsize=(10, 6))
    
    sns.barplot(x=selected_characters.index, y=selected_characters.values, palette='coolwarm')
    
    plt.title("Top & Bottom 3 Character Sentiment Comparison", fontsize=16)
    plt.xlabel("Character", fontsize=12)
    plt.ylabel("Average Sentiment Score", fontsize=12)
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("character_sentiment_comparison.png")
    plt.show()

def generate_word_cloud(dataframe, character_name):
    character_df = dataframe[dataframe['character'] == character_name.upper()]
    
    text = " ".join(character_df['dialogue'].tolist()) 

    if not text:
        print(f"No dialogue found for character: {character_name}")
        return

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Word Cloud for {character_name}")
    
    plt.savefig(f"{character_name.lower()}_word_cloud.png")
    plt.show()


def generate_visualizations(dataframe):
    
    generate_sentiment_over_time_plot(dataframe)
    generate_character_sentiment_bar_chart(dataframe)