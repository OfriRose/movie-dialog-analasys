import argparse
from .functions import read_file, clean_and_parse_script, analyze_sentiment, generate_visualizations


def main():
    parser = argparse.ArgumentParser(description="Analyze sentiment of a movie script.")
    parser.add_argument("input_file", help="Path to the script file.")
    parser.add_argument("output_dir", help="Directory to save visualizations.")
    args = parser.parse_args()

    #read the raw script text from a file
    raw_script_text = read_file(args.input_file)
    #clean and parse the script text into a structured format
    dialogue_data_list = clean_and_parse_script(raw_script_text)
    #analyze sentiment of the dialogue data
    final_dataframe = analyze_sentiment(dialogue_data_list)
    #generate visualizations based on the analyzed data
    generate_visualizations(final_dataframe, args.output_dir)


if __name__ == "__main__":
    main()