Movie Dialogue Sentiment Analysis 🎬

Description

This project performs sentiment analysis on a movie script's dialogue to uncover the emotional tone of characters and the overall emotional arc of the film. It's a beginner-friendly data science project that combines text processing with data visualization.

Goals

    Data Cleaning: Transform a raw movie script into a structured dataset.

    Sentiment Analysis: Use a natural language processing library to assign a sentiment score to each line of dialogue.

    Data Visualization: Create charts and plots to visualize key insights from the data, including character-by-character sentiment and the movie's emotional journey over time.

Technologies Used

    Python

    Pandas: For data manipulation and analysis.

    Matplotlib & Seaborn: For creating clear and compelling visualizations.

    TextBlob: A simple and effective library for sentiment analysis.

    WordCloud: For generating word clouds to visualize common character vocabulary.

    Poetry: For dependency management and project setup.

How to Run the Project

    Clone the repository:
    Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install dependencies using Poetry:
Bash

poetry install

Add a movie script:

    Find a movie script online (e.g., from IMSDb).

    Create a file named script.txt in the root directory of your project.

    Copy and paste the script's raw text into script.txt.

Run the analysis script:
Bash

    poetry run python src/main.py

    This will generate several .png files directly in your project's root directory, which contain the project's visualizations.

Project Results

Here are a few of the key visualizations generated from the project's analysis of The Sound of Music script:

Character Sentiment Comparison

This bar chart reveals a clear division in character sentiment. For example, Louisa and Friedrich are among the most positive characters, while Elberfeld and Brigitta have the most negative average sentiment.

Sentiment Over Time

This line plot shows the emotional trajectory of the movie. The sentiment score fluctuates throughout the film, reflecting the dramatic and musical peaks and valleys of the story.

Character Word Clouds

The word cloud for Maria highlights her most frequent words, offering a quick visual summary of her dialogue. It shows words like "LOUISA," "FATHER," and "Fraulein" are prominent.