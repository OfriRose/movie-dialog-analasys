
from src.movie_dialog_analasys.functions import read_file, clean_and_parse_script, analyze_sentiment, generate_visualizations


def main():
    #read the raw script text from a file
    raw_script_text = read_file("script.txt")
    #clean and parse the script text into a structured format
    dialogue_data_list = clean_and_parse_script(raw_script_text)
    #analyze sentiment of the dialogue data
    final_dataframe = analyze_sentiment(dialogue_data_list)
    #generate visualizations based on the analyzed data
    generate_visualizations(final_dataframe)


if __name__ == "__main__":
    main()