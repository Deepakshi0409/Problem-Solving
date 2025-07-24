def missingNumber(nums):
    """
    Returns the missing number from array of size n containing values 0 to n.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {"input": [3, 0, 1], "expected": 2},
        {"input": [0, 1], "expected": 2},
        {"input": [9,6,4,2,3,5,7,0,1], "expected": 8},
        {"input": [0], "expected": 1}
    ]

    for idx, case in enumerate(test_cases):
        nums = case["input"]
        expected = case["expected"]
        output = missingNumber(nums)
        print(f"Test Case {idx + 1}")
        print("Input:", nums)
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
