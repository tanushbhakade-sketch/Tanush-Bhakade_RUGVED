# Function to rotate n*n matrix 90° clockwise
def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix


# Function to print matrix in spiral order
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from bottom to top
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# -------- Driver code --------
n = int(input("Enter size of n*n matrix: "))
matrix = []

print("Enter matrix row by row (space separated numbers):")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Rotate 90° clockwise
rotated = rotate_matrix(matrix)
print("\nMatrix after 90° clockwise rotation:")
for row in rotated:
    print(row)

# Print spiral order
print("\nSpiral order of rotated matrix:")
print(spiral_order(rotated))
