python
import json

def transform(raw_data):
    """
    A simple transformation function that converts raw data from JSON to a dictionary.

    Parameters:
    raw_data (str): A string of JSON-formatted data.

    Returns:
    dict: A dictionary representing the transformed data.
    """
    return json.loads(raw_data)
