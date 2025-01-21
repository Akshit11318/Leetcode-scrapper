## Build a Matrix with Conditions
**Problem Link:** https://leetcode.com/problems/build-a-matrix-with-conditions/description

**Problem Statement:**
- Given `n`, `upper`, `lower`, and `colsum`, construct an `n x n` matrix such that the sum of elements in the upper triangle equals `upper`, the sum of elements in the lower triangle equals `lower`, and the sum of elements in each column equals `colsum`.
- The matrix should contain only integers between `0` and `n`.
- If no such matrix exists, return an empty matrix.

**Key Requirements and Edge Cases:**
- The input constraints are `1 <= n <= 5`, `0 <= upper, lower <= n * n`, and `colsum.length == n`.
- All elements in `colsum` are between `0` and `n * n`.
- The matrix must be valid according to the given constraints.

**Example Test Cases:**
- For `n = 3`, `upper = 0`, `lower = 7`, and `colsum = [1, 2, 3]`, a valid matrix can be constructed.
- For `n = 3`, `upper = 1`, `lower = 7`, and `colsum = [1, 2, 3]`, no valid matrix can be constructed.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible `n x n` matrices and checking if each one satisfies the given conditions.
- This approach comes to mind first because it guarantees finding a solution if one exists, but it is inefficient due to its high computational complexity.

```cpp
#include <iostream>
#include <vector>

using namespace std;

// Function to check if a matrix satisfies the conditions
bool checkMatrix(vector<vector<int>>& matrix, int upper, int lower, vector<int>& colsum) {
    int n = matrix.size();
    int upperSum = 0, lowerSum = 0;
    
    // Calculate the sum of elements in the upper triangle
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            upperSum += matrix[i][j];
        }
    }
    
    // Calculate the sum of elements in the lower triangle
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            lowerSum += matrix[i][j];
        }
    }
    
    // Check if the sums match the given conditions
    if (upperSum != upper || lowerSum != lower) {
        return false;
    }
    
    // Calculate the sum of elements in each column
    for (int j = 0; j < n; j++) {
        int colSum = 0;
        for (int i = 0; i < n; i++) {
            colSum += matrix[i][j];
        }
        if (colSum != colsum[j]) {
            return false;
        }
    }
    
    return true;
}

vector<vector<int>> buildMatrix(int n, int upper, int lower, vector<int>& colsum) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    
    // Generate all possible matrices and check if any satisfy the conditions
    // This is a brute force approach and is not efficient for large inputs
    // ...
    
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^{n^2})$, where $n$ is the size of the matrix. This is because we are generating all possible matrices and checking each one.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to store the matrix in memory.
> - **Why these complexities occur:** The high time complexity occurs because we are generating all possible matrices, which results in an exponential number of possibilities. The space complexity occurs because we need to store the matrix in memory.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a backtracking approach to construct the matrix.
- We start by initializing an empty matrix and then fill in the elements one by one, using backtracking to ensure that the conditions are satisfied.
- This approach is optimal because it uses a systematic and efficient method to construct the matrix, avoiding the need to generate all possible matrices.

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> buildMatrix(int n, int upper, int lower, vector<int>& colsum) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int upperSum = 0, lowerSum = 0;
    
    // Function to check if it is safe to place a value in the matrix
    bool isSafe(int row, int col, int val) {
        if (row < col) {
            lowerSum += val;
        } else if (row > col) {
            upperSum += val;
        }
        
        // Check if the sums exceed the given conditions
        if (upperSum > upper || lowerSum > lower) {
            return false;
        }
        
        // Check if the column sum exceeds the given condition
        if (colsum[col] < val) {
            return false;
        }
        
        return true;
    }
    
    // Function to backtrack and construct the matrix
    bool backtrack(int row, int col) {
        if (row == n) {
            // Check if the matrix satisfies the conditions
            if (upperSum == upper && lowerSum == lower) {
                return true;
            }
            return false;
        }
        
        if (col == n) {
            return backtrack(row + 1, 0);
        }
        
        for (int val = 0; val <= n; val++) {
            if (isSafe(row, col, val)) {
                matrix[row][col] = val;
                colsum[col] -= val;
                
                if (backtrack(row, col + 1)) {
                    return true;
                }
                
                // Backtrack and reset the values
                matrix[row][col] = 0;
                colsum[col] += val;
            }
        }
        
        return false;
    }
    
    if (backtrack(0, 0)) {
        return matrix;
    }
    
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^{n^2})$, where $n$ is the size of the matrix. However, the backtracking approach significantly reduces the number of possibilities to consider.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to store the matrix in memory.
> - **Optimality proof:** The backtracking approach is optimal because it uses a systematic and efficient method to construct the matrix, avoiding the need to generate all possible matrices. The time complexity is still exponential due to the nature of the problem, but the backtracking approach reduces the number of possibilities to consider.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is backtracking.
- The problem-solving pattern identified is to use a systematic and efficient method to construct the matrix, avoiding the need to generate all possible matrices.
- The optimization technique learned is to use backtracking to reduce the number of possibilities to consider.

**Mistakes to Avoid:**
- A common implementation error is to not properly reset the values during backtracking.
- An edge case to watch for is when the input values are invalid or inconsistent.
- A performance pitfall is to not use a systematic and efficient method to construct the matrix, resulting in high computational complexity.
- A testing consideration is to thoroughly test the implementation with different input values and edge cases.