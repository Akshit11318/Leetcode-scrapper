## Triangle Problem

**Problem Link:** https://leetcode.com/problems/triangle/description

**Problem Statement:**
- Input format: A list of lists, where each inner list represents a row in the triangle, and each integer in the list represents a value in the triangle.
- Constraints: The input triangle will have at least one row and at most 100 rows. Each row will have at least one element and at most 100 elements. Each element will be an integer between -100 and 100.
- Expected output format: The minimum path sum from top to bottom.
- Key requirements and edge cases to consider: The path must start at the top of the triangle, and at each step, you can move to the adjacent element in the next row.
- Example test cases with explanations:
  - Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The path 2 -> 3 -> 5 -> 1 minimizes the sum.
  - Example 2:
    Input: triangle = [[-10]]
    Output: -10

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use recursion to explore all possible paths from the top to the bottom of the triangle and calculate the sum of each path.
- Step-by-step breakdown of the solution: 
  1. Start at the top of the triangle.
  2. For each element in the current row, recursively calculate the minimum path sum that can be obtained by moving to the adjacent elements in the next row.
  3. Return the minimum path sum found.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it involves a lot of repeated calculations.

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        return dfs(triangle, 0, 0);
    }
    
    int dfs(vector<vector<int>>& triangle, int row, int col) {
        if (row == triangle.size() - 1) {
            return triangle[row][col];
        }
        
        int left = dfs(triangle, row + 1, col);
        int right = dfs(triangle, row + 1, col + 1);
        
        return triangle[row][col] + min(left, right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of rows in the triangle. This is because in the worst case, we have to explore all possible paths.
> - **Space Complexity:** $O(n)$, which is the maximum depth of the recursion call stack.
> - **Why these complexities occur:** The brute force approach involves a lot of repeated calculations, which leads to high time complexity. The space complexity is due to the recursion call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum path sum that can be obtained by moving to each element in the triangle.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` with the same size as the input triangle, where `dp[i][j]` represents the minimum path sum that can be obtained by moving to the element at position `(i, j)` in the triangle.
  2. Initialize the first row of `dp` with the values from the first row of the triangle.
  3. For each row in the triangle starting from the second row, calculate the minimum path sum that can be obtained by moving to each element in the row.
  4. The minimum path sum that can be obtained by moving to an element at position `(i, j)` is the minimum of the path sums that can be obtained by moving to the elements at positions `(i-1, j-1)` and `(i-1, j)` in the previous row, plus the value of the current element.
  5. Return the minimum value in the last row of `dp`.
- Proof of optimality: This approach ensures that we calculate the minimum path sum for each element in the triangle only once, which leads to a significant reduction in time complexity.

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> dp(n);
        
        for (int i = 0; i < n; i++) {
            dp[i].resize(i + 1);
        }
        
        dp[0][0] = triangle[0][0];
        
        for (int i = 1; i < n; i++) {
            dp[i][0] = dp[i-1][0] + triangle[i][0];
            dp[i][i] = dp[i-1][i-1] + triangle[i][i];
            
            for (int j = 1; j < i; j++) {
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            }
        }
        
        int minSum = INT_MAX;
        
        for (int i = 0; i < n; i++) {
            minSum = min(minSum, dp[n-1][i]);
        }
        
        return minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of rows in the triangle. This is because we need to fill up the `dp` array.
> - **Space Complexity:** $O(n^2)$, which is the size of the `dp` array.
> - **Optimality proof:** This approach ensures that we calculate the minimum path sum for each element in the triangle only once, which leads to a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and recursion.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results and avoid repeated calculations.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other dynamic programming problems, such as the `Unique Paths` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, or not updating the `dp` array correctly.
- Edge cases to watch for: The input triangle may have only one row, or the input triangle may have a large number of rows.
- Performance pitfalls: Using a brute force approach that involves a lot of repeated calculations.
- Testing considerations: Test the solution with different input triangles, including triangles with different numbers of rows and columns.