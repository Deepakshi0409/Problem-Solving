def maxArea(height):
    """
    Returns the maximum area of water that can be contained.
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {"input": [1,8,6,2,5,4,8,3,7], "expected": 49},
        {"input": [1,1], "expected": 1},
        {"input": [4,3,2,1,4], "expected": 16},
        {"input": [1,2,1], "expected": 2}
    ]

    for idx, case in enumerate(test_cases):
        heights = case["input"]
        expected = case["expected"]
        output = maxArea(heights)
        print(f"Test Case {idx + 1}")
        print("Input:", heights)
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
