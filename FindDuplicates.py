def findDuplicates(nums):
    """
    Returns all elements that appear twice in the array.
    """
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] *= -1

    return result


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {"input": [4,3,2,7,8,2,3,1], "expected": [2,3]},
        {"input": [1,1,2], "expected": [1]},
        {"input": [1], "expected": []}
    ]

    for idx, case in enumerate(test_cases):
        nums = case["input"]
        expected = case["expected"]
        output = findDuplicates(nums.copy())
        print(f"Test Case {idx + 1}")
        print("Input:", nums)
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
