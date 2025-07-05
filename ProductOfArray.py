def product_except_self(nums):
    """
    Returns an array where each element is the product of all other elements.

    Args:
    nums (List[int]): Input list.

    Returns:
    List[int]: Product array.
    """
    n = len(nums)
    result = [1] * n

    # Step 1: Prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Step 2: Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Test case
nums = [1, 2, 3, 4]
print("Product except self:", product_except_self(nums))
