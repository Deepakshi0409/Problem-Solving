def search_rotated_array(nums, target):
    """
    Searches for target in a rotated sorted array.

    Args:
    nums (List[int]): Rotated sorted array.
    target (int): Value to search for.

    Returns:
    int: Index of target if found, else -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search left
            else:
                left = mid + 1  # Search right
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Search right
            else:
                right = mid - 1  # Search left

    return -1

# Test case
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Index of target:", search_rotated_array(nums, target))
