import pandas as pd
from src.movie_dialog_analasys.functions import clean_and_parse_script
import pytest

@pytest.fixture
def sample_script():
    return """
    CHARACTER ONE: This is a line.
    CHARACTER TWO: This is another line.
    SOLO: This line should be skipped.
      SPACED CHARACTER: This line has leading spaces.
    CHARACTER ONE: A second line for this character.
    """

def test_clean_and_parse_script_basic(sample_script):
    expected_data = {
        'character': ['CHARACTER ONE', 'CHARACTER TWO', 'SPACED CHARACTER', 'CHARACTER ONE'],
        'dialogue': ['This is a line.', 'This is another line.', 'This line has leading spaces.', 'A second line for this character.']
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = clean_and_parse_script(sample_script)

    pd.testing.assert_frame_equal(result_df, expected_df)

def test_clean_and_parse_script_skip_characters():
    raw_script = """
    SOLO: Should be skipped.
    MARIA: Should be included.
    """
    expected_data = {
        'character': ['MARIA'],
        'dialogue': ['Should be included.']
    }
    expected_df = pd.DataFrame(expected_data)

    result_df = clean_and_parse_script(raw_script)

    pd.testing.assert_frame_equal(result_df, expected_df)

def test_clean_and_parse_script_empty_script():
    raw_script = ""
    expected_df = pd.DataFrame({'character': [], 'dialogue': []})

    result_df = clean_and_parse_script(raw_script)

    pd.testing.assert_frame_equal(result_df, expected_df, check_dtype=False)

def test_clean_and_parse_script_no_dialogue():
    raw_script = """
    This is just some text.
    (A stage direction)
    """
    expected_df = pd.DataFrame({'character': [], 'dialogue': []})

    result_df = clean_and_parse_script(raw_script)

    pd.testing.assert_frame_equal(result_df, expected_df, check_dtype=False)
