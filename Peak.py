def find_peak_element(nums):
    """
    Finds a peak element in the array.

    Args:
    nums (List[int]): Input array.

    Returns:
    int: Index of any one peak element.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Peak must be to the right
        else:
            right = mid  # Peak is at mid or to the left

    return left  # or right, since left == right

# Test case
nums = [1, 2, 3, 1]
print("Peak found at index:", find_peak_element(nums))
