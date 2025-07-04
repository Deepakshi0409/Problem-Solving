def merge_intervals(intervals):
    """
    Merges overlapping intervals.

    Args:
    intervals (List[List[int]]): List of [start, end] intervals.

    Returns:
    List[List[int]]: Merged list of intervals.
    """
    if not intervals:
        return []

    # Step 1: Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # Start with the first interval

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            # Overlapping — merge by extending the end
            last[1] = max(last[1], current[1])
        else:
            # No overlap — add current interval
            merged.append(current)

    return merged

# Test case
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("Merged Intervals:", merge_intervals(intervals))

