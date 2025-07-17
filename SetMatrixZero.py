def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use first row and first column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out cells based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero out first row and column if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


# ----------------------
# 🧪 Test Cases
# ----------------------
def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    print("Test Case 1")
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix1)
    print_matrix(matrix1)

    print("\nTest Case 2")
    matrix2 = [
        [0, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    setZeroes(matrix2)
    print_matrix(matrix2)
