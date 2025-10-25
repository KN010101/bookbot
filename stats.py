def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text, lowercase=True):
    """
    Counts the occurrences of each character in the given text.

    Args:
        text (str): The input text to analyze.
        lowercase (bool, optional): If True, converts text to lowercase before counting. Defaults to True.

    Returns:
        dict: A dictionary where keys are characters and values are their counts in the text.
    """
    if lowercase:
        text = text.lower()
    chars = {}
    for char in text:
        chars[char] = chars.get(char, 0) + 1
    return chars