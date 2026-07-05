class Solution:
    def searchMatrix(self, matrix, target):
        # Number of rows
        m = len(matrix)

        # Number of columns
        n = len(matrix[0])

        # Binary search over the virtual array
        left = 0
        right = m * n - 1

        while left <= right:

            # Middle index of the virtual array
            mid = (left + right) // 2

            # Convert virtual index to matrix coordinates
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False