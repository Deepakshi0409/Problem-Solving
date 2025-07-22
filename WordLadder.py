from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))

    return 0


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {
            "input": ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
            "expected": 5
        },
        {
            "input": ("hit", "cog", ["hot","dot","dog","lot","log"]),
            "expected": 0
        }
    ]

    for idx, case in enumerate(test_cases):
        beginWord, endWord, wordList = case["input"]
        expected = case["expected"]
        output = ladderLength(beginWord, endWord, wordList)
        print(f"Test Case {idx + 1}")
        print(f"Input: {beginWord} -> {endWord}, List: {wordList}")
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
