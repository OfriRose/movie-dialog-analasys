
from src.movie_dialog_analasys.functions import read_file, clean_and_parse_script, analyze_sentiment, generate_visualizations


def main():
    # Step 1: Read the Raw Data
    raw_script_text = read_file("script.txt")

    # Step 2: Clean and Structure the Data
    dialogue_data_list = clean_and_parse_script(raw_script_text)

    # Step 3: Analyze the Sentiment
    final_dataframe = analyze_sentiment(dialogue_data_list)

    # Step 4: Visualize the Results
    generate_visualizations(final_dataframe)


if __name__ == "__main__":
    main()