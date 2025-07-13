def threeSum(nums):
    """
    Given an array nums, return all unique triplets [a,b,c] such that a + b + c = 0.
    """
    nums.sort()
    result = []

    for i in range(len(nums)):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]]
        },
        {
            "input": [0, 1, 1],
            "expected": []
        },
        {
            "input": [0, 0, 0],
            "expected": [[0, 0, 0]]
        },
        {
            "input": [-2, 0, 1, 1, 2],
            "expected": [[-2, 0, 2], [-2, 1, 1]]
        }
    ]

    for idx, case in enumerate(test_cases):
        nums = case["input"]
        expected = case["expected"]
        output = threeSum(nums)
        print(f"Test Case {idx + 1}")
        print("Input:", nums)
        print("Expected Output (order may vary):", expected)
        print("Actual Output:", output)
        print("-" * 50)
