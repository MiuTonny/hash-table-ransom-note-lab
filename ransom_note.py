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
     # Count letters
    letter_count = {}
    
    for char in magazine:
        letter_count[char] = letter_count.get(char, 0) + 1

    #Check if ransomNote can be build
    for char in ransomNote:
        if char not in letter_count or letter_count[char] == 0:
            return False
        letter_count[char] -= 1

    return True

