## Find the Minimum Area to Cover All Ones I
**Problem Link:** https://leetcode.com/problems/find-the-minimum-area-toCover-all-ones-i/description

**Problem Statement:**
- Input format and constraints: Given a `rows` x `cols` binary matrix `mat`, return the minimum area of a rectangle that covers all ones in the matrix. If it is impossible to cover all ones with a rectangle, return -1.
- Expected output format: The minimum area of a rectangle that covers all ones in the matrix.
- Key requirements and edge cases to consider: 
  - The input matrix is a binary matrix.
  - The matrix may contain no ones.
  - The matrix may contain ones that cannot be covered by a rectangle.
- Example test cases with explanations:
  - Example 1: Input: `mat = [[0,0,1],[0,1,1],[1,1,1]]`, Output: `8`, Explanation: The minimum area rectangle that covers all ones is the rectangle with top-left corner at `(0, 2)` and bottom-right corner at `(2, 2)`.
  - Example 2: Input: `mat = [[1]]`, Output: `1`, Explanation: The minimum area rectangle that covers all ones is the rectangle with top-left corner at `(0, 0)` and bottom-right corner at `(0, 0)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible rectangles in the matrix and calculating their area.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible top-left corners of the rectangle.
  2. For each top-left corner, iterate over all possible bottom-right corners.
  3. For each rectangle, check if it covers all ones in the matrix.
  4. If it does, calculate the area of the rectangle.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible solutions.

```cpp
class Solution {
public:
    int minArea(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();
        int minArea = INT_MAX;
        
        // Iterate over all possible top-left corners
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Iterate over all possible bottom-right corners
                for (int k = i; k < rows; k++) {
                    for (int l = j; l < cols; l++) {
                        // Check if the rectangle covers all ones
                        if (coversAllOnes(mat, i, j, k, l)) {
                            // Calculate the area of the rectangle
                            int area = (k - i + 1) * (l - j + 1);
                            minArea = min(minArea, area);
                        }
                    }
                }
            }
        }
        
        return minArea == INT_MAX ? -1 : minArea;
    }
    
    bool coversAllOnes(vector<vector<int>>& mat, int x1, int y1, int x2, int y2) {
        int rows = mat.size();
        int cols = mat[0].size();
        
        // Check if the rectangle covers all ones
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 1 && !(x1 <= i && i <= x2 && y1 <= j && j <= y2)) {
                    return false;
                }
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of rows (or columns) in the matrix. This is because we are iterating over all possible rectangles in the matrix.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the minimum area.
> - **Why these complexities occur:** The time complexity is high because we are checking all possible rectangles in the matrix. The space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible rectangles, we can find the minimum and maximum row and column indices of the ones in the matrix.
- Detailed breakdown of the approach:
  1. Find the minimum and maximum row indices of the ones in the matrix.
  2. Find the minimum and maximum column indices of the ones in the matrix.
  3. Calculate the area of the rectangle that covers all ones.
- Proof of optimality: This approach is optimal because it finds the minimum area rectangle that covers all ones in the matrix.
- Why further optimization is impossible: This approach has a time complexity of $O(n^2)$, which is the minimum time complexity required to find the minimum area rectangle.

```cpp
class Solution {
public:
    int minArea(vector<vector<int>>& mat) {
        int rows = mat.size();
        int cols = mat[0].size();
        int minX = INT_MAX;
        int maxX = INT_MIN;
        int minY = INT_MAX;
        int maxY = INT_MIN;
        
        // Find the minimum and maximum row and column indices of the ones
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] == 1) {
                    minX = min(minX, i);
                    maxX = max(maxX, i);
                    minY = min(minY, j);
                    maxY = max(maxY, j);
                }
            }
        }
        
        // If no ones are found, return -1
        if (minX == INT_MAX) {
            return -1;
        }
        
        // Calculate the area of the rectangle that covers all ones
        int area = (maxX - minX + 1) * (maxY - minY + 1);
        
        return area;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows (or columns) in the matrix. This is because we are iterating over all elements in the matrix.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the minimum and maximum row and column indices.
> - **Optimality proof:** This approach is optimal because it finds the minimum area rectangle that covers all ones in the matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the minimum area rectangle that covers all ones in a binary matrix.
- Problem-solving patterns identified: Finding the minimum and maximum row and column indices of the ones in the matrix.
- Optimization techniques learned: Instead of checking all possible rectangles, find the minimum and maximum row and column indices of the ones in the matrix.
- Similar problems to practice: Finding the minimum area rectangle that covers all ones in a binary matrix with obstacles.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where no ones are found in the matrix.
- Edge cases to watch for: The matrix may contain no ones, or the ones may not be able to be covered by a rectangle.
- Performance pitfalls: Checking all possible rectangles in the matrix, which has a high time complexity.
- Testing considerations: Test the function with different input matrices, including cases where no ones are found or the ones cannot be covered by a rectangle.