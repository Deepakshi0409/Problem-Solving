def majorityElement(nums):
    """
    Returns the majority element using Boyer-Moore Voting Algorithm.
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {"input": [3,2,3], "expected": 3},
        {"input": [2,2,1,1,1,2,2], "expected": 2},
        {"input": [1], "expected": 1},
        {"input": [1,1,1,2,3,4], "expected": 1}
    ]

    for idx, case in enumerate(test_cases):
        nums = case["input"]
        expected = case["expected"]
        output = majorityElement(nums)
        print(f"Test Case {idx + 1}")
        print("Input:", nums)
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
