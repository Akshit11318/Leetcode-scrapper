## Lucky Numbers in a Matrix

**Problem Link:** https://leetcode.com/problems/lucky-numbers-in-a-matrix/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `matrix` where each element is an integer. The matrix can have any number of rows and columns, but it is guaranteed to be non-empty.
- Expected output format: The function should return a list of integers representing the lucky numbers in the matrix.
- Key requirements and edge cases to consider: A lucky number is a number that is a minimum in its row and a maximum in its column. We need to find all such numbers in the matrix.
- Example test cases with explanations: For example, given the matrix `[[3,7,8],[9,11,13],[15,16,17]]`, the lucky numbers are `[15]` because 15 is the minimum in its row and the maximum in its column.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating over each element in the matrix and checking if it is a lucky number.
- Step-by-step breakdown of the solution: For each element, we need to find the minimum in its row and the maximum in its column. If the element is equal to both the minimum and the maximum, then it is a lucky number.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity because we need to iterate over the entire matrix for each element.

```cpp
class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> lucky;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                bool isLucky = true;
                // Check if the element is the minimum in its row
                for (int k = 0; k < matrix[0].size(); k++) {
                    if (matrix[i][k] < matrix[i][j]) {
                        isLucky = false;
                        break;
                    }
                }
                if (!isLucky) continue;
                // Check if the element is the maximum in its column
                for (int k = 0; k < matrix.size(); k++) {
                    if (matrix[k][j] > matrix[i][j]) {
                        isLucky = false;
                        break;
                    }
                }
                if (isLucky) lucky.push_back(matrix[i][j]);
            }
        }
        return lucky;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n^2 + m^2 \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because for each element, we are iterating over the entire row and column.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are storing the lucky numbers in a separate vector.
> - **Why these complexities occur:** These complexities occur because we are using nested loops to iterate over the matrix, and we are checking each element against all other elements in its row and column.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each element against all other elements in its row and column, we can first find the minimum in each row and the maximum in each column, and then check if the element is equal to both the minimum and the maximum.
- Detailed breakdown of the approach: We can use two separate vectors to store the minimum in each row and the maximum in each column. Then, we can iterate over the matrix again and check if each element is equal to the minimum in its row and the maximum in its column.
- Proof of optimality: This approach is optimal because we are only iterating over the matrix twice, once to find the minimum in each row and the maximum in each column, and once to find the lucky numbers.
- Why further optimization is impossible: This approach is already optimal because we need to iterate over the matrix at least once to find the lucky numbers.

```cpp
class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> lucky;
        vector<int> rowMins;
        vector<int> colMaxs;
        
        // Find the minimum in each row
        for (int i = 0; i < matrix.size(); i++) {
            int rowMin = INT_MAX;
            for (int j = 0; j < matrix[0].size(); j++) {
                rowMin = min(rowMin, matrix[i][j]);
            }
            rowMins.push_back(rowMin);
        }
        
        // Find the maximum in each column
        for (int j = 0; j < matrix[0].size(); j++) {
            int colMax = INT_MIN;
            for (int i = 0; i < matrix.size(); i++) {
                colMax = max(colMax, matrix[i][j]);
            }
            colMaxs.push_back(colMax);
        }
        
        // Find the lucky numbers
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == rowMins[i] && matrix[i][j] == colMaxs[j]) {
                    lucky.push_back(matrix[i][j]);
                }
            }
        }
        
        return lucky;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are iterating over the matrix three times, once to find the minimum in each row, once to find the maximum in each column, and once to find the lucky numbers.
> - **Space Complexity:** $O(m + n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are storing the minimum in each row and the maximum in each column in separate vectors.
> - **Optimality proof:** This approach is optimal because we are only iterating over the matrix three times, and we are using a constant amount of extra space to store the minimum in each row and the maximum in each column.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of finding the minimum and maximum in each row and column of a matrix, and using this information to find the lucky numbers.
- Problem-solving patterns identified: The problem requires the use of nested loops to iterate over the matrix, and the use of separate vectors to store the minimum in each row and the maximum in each column.
- Optimization techniques learned: The problem demonstrates the importance of optimizing the algorithm by reducing the number of iterations over the matrix, and using a constant amount of extra space to store the minimum and maximum values.
- Similar problems to practice: Similar problems include finding the maximum and minimum in each row and column of a matrix, and finding the lucky numbers in a matrix with different conditions.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to initialize the minimum and maximum values before iterating over the matrix.
- Edge cases to watch for: One edge case is when the matrix is empty, in which case the function should return an empty vector.
- Performance pitfalls: One performance pitfall is to use a brute force approach that iterates over the matrix multiple times, resulting in a high time complexity.
- Testing considerations: The function should be tested with different inputs, including an empty matrix, a matrix with a single row or column, and a matrix with multiple rows and columns.