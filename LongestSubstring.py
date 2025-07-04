def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
    s (str): Input string.

    Returns:
    int: Length of the longest substring.
    """
    char_index = {}  # Stores last seen index of characters
    left = 0  # Start of sliding window
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # Repeated character found; move the window start
            left = char_index[char] + 1
        
        char_index[char] = right  # Update last seen index
        max_length = max(max_length, right - left + 1)

    return max_length

# Test case
s = "abcabcbb"
print("Length of longest substring:", length_of_longest_substring(s))
