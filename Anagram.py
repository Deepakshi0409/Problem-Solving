from collections import defaultdict

def group_anagrams(strs):
    """
    Groups anagrams from a list of strings.

    Args:
    strs (List[str]): Input list of strings.

    Returns:
    List[List[str]]: Grouped anagrams.
    """
    anagram_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))  # Sort characters to create key
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Test case
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped Anagrams:", group_anagrams(words))
