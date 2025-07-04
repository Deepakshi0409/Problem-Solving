from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Returns the k most frequent elements.

    Args:
    nums (List[int]): Input list of integers.
    k (int): Number of top frequent elements to return.

    Returns:
    List[int]: List of k most frequent elements.
    """
    # Step 1: Count frequencies
    freq_map = Counter(nums)

    # Step 2: Use heap to get k highest frequency elements
    return [item for item, freq in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Test case
nums = [1, 1, 1, 2, 2, 3]
k = 2
print("Top", k, "frequent elements:", top_k_frequent(nums, k))
