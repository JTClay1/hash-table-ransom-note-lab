def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """

    # This dictionary will track how many times each character appears
    char_counts = {}

    # Count every character in the magazine
    for char in magazine:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Check whether each character in the ransom note is available
    for char in ransomNote:
        # If the character is missing or we already used them all up,
        # we cannot build the ransom note
        if char not in char_counts or char_counts[char] == 0:
            return False

        # Use one occurrence of that character
        char_counts[char] -= 1

    # If we made it through the whole ransom note, it can be constructed
    return True