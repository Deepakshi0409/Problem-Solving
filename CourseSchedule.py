from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    """
    Returns True if all courses can be finished (no cyclic dependency).
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == numCourses


# ----------------------
# 🧪 Test Cases
# ----------------------
if __name__ == "__main__":
    test_cases = [
        {"input": (2, [[1,0]]), "expected": True},
        {"input": (2, [[1,0],[0,1]]), "expected": False},
        {"input": (4, [[1,0],[2,1],[3,2]]), "expected": True},
    ]

    for idx, case in enumerate(test_cases):
        numCourses, prerequisites = case["input"]
        expected = case["expected"]
        output = canFinish(numCourses, prerequisites)
        print(f"Test Case {idx + 1}")
        print("Input: {numCourses} courses, prerequisites = {prerequisites}")
        print("Expected:", expected)
        print("Output:", output)
        print("-" * 50)
