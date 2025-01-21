## Sum in a Matrix
**Problem Link:** https://leetcode.com/problems/sum-in-a-matrix/description

**Problem Statement:**
- Input format and constraints: The input is a 2D `matrix` and two points `x1`, `y1`, `x2`, `y2` representing the top-left and bottom-right corners of a rectangle.
- Expected output format: The sum of all elements within the rectangle defined by the two points.
- Key requirements and edge cases to consider: The rectangle's sides are parallel to the matrix's sides, and the points are 0-indexed.
- Example test cases with explanations: For example, given a matrix `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` and points `(0, 0, 1, 1)`, the output should be `1 + 2 + 4 + 5 = 12`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate over each element within the rectangle and sum them up.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `sum` to 0.
  2. Iterate over each row from `x1` to `x2` (inclusive).
  3. For each row, iterate over each column from `y1` to `y2` (inclusive).
  4. Add the current element to the `sum`.
- Why this approach comes to mind first: It's a straightforward, intuitive solution that directly addresses the problem statement.

```cpp
class NumMatrix {
public:
    vector<vector<int>> matrix;
    NumMatrix(vector<vector<int>>& matrix) : matrix(matrix) {}

    int sumRegion(int x1, int y1, int x2, int y2) {
        int sum = 0;
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                sum += matrix[i][j];
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the rectangle. This occurs because in the worst case, we're iterating over every element in the rectangle once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we're only using a constant amount of space to store the sum and loop variables.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops that iterate over the rectangle, but it has low space complexity because it doesn't require any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of summing the elements in the rectangle every time `sumRegion` is called, we can precompute the sum of all elements in every possible rectangle and store these sums in a separate data structure.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` where `dp[i][j]` represents the sum of all elements in the rectangle from `(0,0)` to `(i,j)`.
  2. Initialize `dp[0][0]` to `matrix[0][0]`.
  3. For each cell `(i, j)` in `dp`, calculate `dp[i][j]` as the sum of `matrix[i][j]`, `dp[i-1][j]`, `dp[i][j-1]`, and `-dp[i-1][j-1]` (to avoid double-counting the overlap).
  4. When `sumRegion(x1, y1, x2, y2)` is called, calculate the sum as `dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]`.
- Proof of optimality: This approach reduces the time complexity of `sumRegion` to $O(1)$ because it only requires accessing and performing a constant number of operations on elements in the `dp` array.
- Why further optimization is impossible: This is because we must at least read the input once to precompute the sums, and we must store these sums somewhere, making the time and space complexities optimal for the given problem constraints.

```cpp
class NumMatrix {
public:
    vector<vector<int>> dp;
    NumMatrix(vector<vector<int>>& matrix) : dp(matrix.size() + 1, vector<int>(matrix[0].size() + 1, 0)) {
        for (int i = 1; i <= matrix.size(); i++) {
            for (int j = 1; j <= matrix[0].size(); j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1];
            }
        }
    }

    int sumRegion(int x1, int y1, int x2, int y2) {
        return dp[x2+1][y2+1] - dp[x1][y2+1] - dp[x2+1][y1] + dp[x1][y1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `sumRegion` calls, $O(m \cdot n)$ for the constructor where $m$ and $n$ are the dimensions of the input matrix. This is because the constructor precomputes the sums for all possible rectangles.
> - **Space Complexity:** $O(m \cdot n)$ for storing the `dp` array.
> - **Optimality proof:** The optimal approach achieves $O(1)$ time complexity for `sumRegion` calls by precomputing and storing the sums of all possible rectangles, making it the most efficient solution given the constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Precomputation, dynamic programming, and the importance of understanding the problem's constraints to optimize the solution.
- Problem-solving patterns identified: Looking for ways to precompute or store intermediate results to reduce the time complexity of repeated operations.
- Optimization techniques learned: Using dynamic programming to store and reuse previously computed results.
- Similar problems to practice: Other problems involving range queries or cumulative sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing or boundary handling in the `dp` array.
- Edge cases to watch for: Handling cases where `x1`, `y1`, `x2`, or `y2` are at the boundaries of the matrix.
- Performance pitfalls: Failing to precompute and store intermediate results, leading to inefficient repeated computations.
- Testing considerations: Thoroughly testing the solution with various input sizes and edge cases to ensure correctness and performance.