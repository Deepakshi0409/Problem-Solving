import heapq

def findKthLargest(nums, k):
    """
    Returns the kth largest element in the array.
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {
            "input": ([3,2,1,5,6,4], 2),
            "expected": 5
        },
        {
            "input": ([3,2,3,1,2,4,5,5,6], 4),
            "expected": 4
        },
        {
            "input": ([1], 1),
            "expected": 1
        }
    ]

    for idx, case in enumerate(test_cases):
        nums, k = case["input"]
        expected = case["expected"]
        output = findKthLargest(nums, k)
        print(f"Test Case {idx + 1}")
        print("Input: nums = {nums}, k = {k}")
        print("Expected Output:", expected)
        print("Actual Output:", output)
        print("-" * 50)
