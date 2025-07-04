def two_sum(nums, target):
    """
    Returns indices of two numbers in `nums` such that they add up to `target`.

    Args:
    nums (List[int]): List of integers.
    target (int): The target sum.

    Returns:
    List[int]: Indices of the two numbers.
    """
    num_to_index = {}  # Dictionary to store number → index mapping

    for i, num in enumerate(nums):
        difference = target - num  # What we need to find


        if difference in num_to_index:
            # Found the pair
            return [num_to_index[difference], i]
        
        num_to_index[num] = i  # Save current number with index

    # If no pair is found (shouldn’t happen due to constraints)
    return []

# Test case
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)
print("Values:", nums[result[0]], "+", nums[result[1]], "=", target)
