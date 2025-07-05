def max_subarray(nums):
    """
    Finds the maximum sum of a contiguous subarray.

    Args:
    nums (List[int]): Input array.

    Returns:
    int: Maximum subarray sum.
    """
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # Decide whether to extend or start new subarray
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Max Subarray Sum:", max_subarray(nums))
