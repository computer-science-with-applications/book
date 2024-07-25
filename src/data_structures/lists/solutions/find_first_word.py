def find_first_word(sentence, character):
    """
    Find the first word in a sentence that contains a given
    character or None, if the character does not occur in
    the sentence.

    Args:
        sentence (str): the sentence to search
        character (str): the character of interest

    Returns (str | None): The first word in the sentence that contains
        the character or None, if the character does not
        occur in the sentence.
    """
    words = sentence.split()
    
    for word in words:
        if character in word:
            return word

    # did not find the character in a word
    return None


def find_first_word_1(sentence, character):
    """
    Find the first word in a sentence that contains a given
    character or None, if the character does not occur in
    the sentence.

    Args:
        sentence (str): the sentence to search
        character (str): the character of interest

    Returns (str | None): The first word in the sentence that contains
        the character or None, if the character does not
        occur in the sentence.
    """

    # keep track of the beginning of most recent word
    beginning = 0
    # keep track of the location of the letter of interest
    location = None

    # look for the the beginning of each word and look for the character
    # of interest
    for i, letter in enumerate(sentence):
        if letter.isspace():
            beginning = i + 1
        elif letter == character:
            location = i
            break

    if location is None:
        # did not find the letter
        return None

    # find the end of the word
    end = location + 1
    while end < len(sentence):
        if sentence[end].isspace():
            break
        end += 1

    return sentence[beginning:end]        


def test_find_first_word():
    """ Test code for find_first_word """
    test_cases = [
        # Example from problem write-up
        ("I am learning a lot and having fun this quarter", "n", "learning"),

        # Letter does not occur
        ("I am learning a lot and having fun this quarter", "z", None),

        # Word of iterest (lot) ends in a character other than a space
        ("I am learning a lot\n and having fun this quarter", "t", "lot"),

        # Empty sentence
        ("", "n", None),

        # First word in the sentence matches
        ("I am learning a lot\n and having fun this quarter", "I", "I"),

        # Last word in sentence matches
        ("I am learning a lot\t and having fun this quarter", "q", "quarter"),

        # Letter occurs as the last character in the string
        ("Let's use Zoom", "m", "Zoom"),
    ]
    for sentence, letter, expected in test_cases:
        assert find_first_word(sentence, letter) == expected
