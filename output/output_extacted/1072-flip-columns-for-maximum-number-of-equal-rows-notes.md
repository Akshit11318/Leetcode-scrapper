## Flip Columns For Maximum Number Of Equal Rows
**Problem Link:** https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description

**Problem Statement:**
- Input: A 2D array `matrix` of size `m x n` containing binary strings.
- Constraints: `1 <= m <= 100`, `1 <= n <= 10`.
- Expected output: The maximum number of rows that can be made equal by flipping columns.
- Key requirements and edge cases: Handle cases where `m` or `n` is 1, and when the matrix is empty.
- Example test cases: 
  - `matrix = [["0","0","0"],["1","1","1"],["1","1","0"]]`, output: `2`.
  - `matrix = [["0"] ,"1" ,"1"]]`, output: `2`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible combinations of column flips and check for each combination how many rows become equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of column flips.
  2. For each combination, flip the corresponding columns in the matrix.
  3. Count the number of equal rows in the modified matrix.
  4. Keep track of the maximum count found across all combinations.
- Why this approach comes to mind first: It is a straightforward way to ensure all possibilities are considered.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<string>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int maxCount = 0;
        
        // Generate all possible combinations of column flips
        for (int mask = 0; mask < (1 << n); mask++) {
            int count = 0;
            vector<string> targetRow(n, "0");
            
            // Flip columns according to the current combination
            for (int j = 0; j < n; j++) {
                if (mask & (1 << j)) {
                    targetRow[j] = "1";
                }
            }
            
            // Count the number of rows that can be made equal to the target row
            for (int i = 0; i < m; i++) {
                bool canMatch = true;
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] != targetRow[j] && matrix[i][j] != string(1, '1' - (targetRow[j] - '0'))) {
                        canMatch = false;
                        break;
                    }
                }
                if (canMatch) {
                    count++;
                }
            }
            
            // Update the maximum count
            maxCount = max(maxCount, count);
        }
        
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the number of columns and $m$ is the number of rows. The $2^n$ factor comes from generating all possible combinations of column flips.
> - **Space Complexity:** $O(n)$, for storing the target row.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of column flips, leading to an exponential time complexity in terms of $n$. The space complexity is linear due to the storage needed for the target row.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of flipping columns, consider the pattern of each row and how it can be transformed into another pattern by flipping bits.
- Detailed breakdown of the approach:
  1. Normalize each row by flipping all bits if the first bit is '1'.
  2. Count the occurrences of each normalized row pattern.
  3. The maximum count of equal rows after flipping columns is the maximum count of any normalized row pattern.
- Proof of optimality: This approach ensures that each row is considered in its simplest form (after normalization), and the maximum count of equal rows is determined by the most frequent normalized pattern.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<string>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        unordered_map<string, int> patternCounts;
        int maxCount = 0;
        
        // Iterate over each row
        for (int i = 0; i < m; i++) {
            string pattern = matrix[i][0];
            
            // Normalize the row pattern by flipping all bits if the first bit is '1'
            if (matrix[i][0] == "1") {
                for (int j = 0; j < n; j++) {
                    pattern += string(1, '1' - (matrix[i][j] - '0'));
                }
            } else {
                for (int j = 1; j < n; j++) {
                    pattern += matrix[i][j];
                }
            }
            
            // Count the occurrences of the normalized pattern
            patternCounts[pattern]++;
            maxCount = max(maxCount, patternCounts[pattern]);
        }
        
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
> - **Space Complexity:** $O(m \cdot n)$, for storing the normalized row patterns.
> - **Optimality proof:** This approach ensures that each row is considered in its simplest form and determines the maximum count of equal rows by the most frequent normalized pattern, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Normalization, pattern counting, and optimization.
- Problem-solving patterns: Consider simplifying complex problems by normalizing inputs and counting patterns.
- Optimization techniques: Focus on simplifying the problem space to reduce complexity.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty matrices or matrices with a single row or column.
- Performance pitfalls: Failing to optimize the solution, leading to high time or space complexity.
- Testing considerations: Ensure thorough testing of edge cases and large inputs to validate the solution's correctness and performance.