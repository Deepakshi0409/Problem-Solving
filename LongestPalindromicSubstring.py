def longestPalindrome(s):
    """
    Returns the longest palindromic substring in s.
    """
    if not s or len(s) < 1:
        return ""

    start = 0
    end = 0

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of palindrome

    for i in range(len(s)):
        len1 = expandAroundCenter(i, i)      # Odd length
        len2 = expandAroundCenter(i, i + 1)  # Even length
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {
            "input": "babad",
            "expected": ["bab", "aba"]  # both are valid
        },
        {
            "input": "cbbd",
            "expected": ["bb"]
        },
        {
            "input": "a",
            "expected": ["a"]
        },
        {
            "input": "ac",
            "expected": ["a", "c"]
        }
    ]

    for idx, case in enumerate(test_cases):
        s = case["input"]
        expected = case["expected"]
        output = longestPalindrome(s)
        print(f"Test Case {idx + 1}")
        print("Input: {s}")
        print("Expected Output (any):", expected)
        print("Actual Output:", output)
        print("-" * 50)
