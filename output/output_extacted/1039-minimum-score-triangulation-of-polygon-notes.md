## Minimum Score Triangulation of Polygon

**Problem Link:** https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description

**Problem Statement:**
- Input: A list of `n` points on the 2D plane, represented by their coordinates `(x, y)`.
- Constraints: `3 <= n <= 50`.
- Expected Output: The minimum score you can achieve.
- Key Requirements:
  - The score of a triangle is the product of the lengths of its three sides.
  - The length of a side is the Euclidean distance between its two endpoints.
- Edge Cases:
  - The input points form a convex polygon.
  - The input points do not have any three points that are collinear.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating all possible triangulations of the polygon and then computing the score for each triangulation.
- Step-by-step breakdown:
  1. Generate all possible triangulations of the polygon.
  2. For each triangulation, calculate the score by summing the products of the lengths of the sides of each triangle.
  3. Return the minimum score among all triangulations.
- Why this approach comes to mind first: It is the most straightforward approach to solve the problem by considering all possibilities.

```cpp
int minScoreTriangulation(vector<vector<int>>& A) {
    int n = A.size();
    int res = INT_MAX;
    // Generate all possible triangulations
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) != n - 2) continue;
        int score = 0;
        // Calculate the score for the current triangulation
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (((mask >> i) & 1) && ((mask >> j) & 1) && ((mask >> k) & 1)) {
                        int side1 = calculateDistance(A[i], A[j]);
                        int side2 = calculateDistance(A[j], A[k]);
                        int side3 = calculateDistance(A[k], A[i]);
                        score += side1 * side2 * side3;
                    }
                }
            }
        }
        res = min(res, score);
    }
    return res;
}

int calculateDistance(vector<int>& p1, vector<int>& p2) {
    return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^3)$, where $n$ is the number of points. This is because we generate all possible triangulations, which takes $O(2^n)$ time, and for each triangulation, we calculate the score, which takes $O(n^3)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and the current triangulation.
> - **Why these complexities occur:** The time complexity is high because we consider all possible triangulations, and for each triangulation, we calculate the score by summing the products of the lengths of the sides of each triangle.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the minimum score for each sub-problem.
- Detailed breakdown of the approach:
  1. Define a 2D array `dp` where `dp[i][j]` represents the minimum score for the sub-problem from point `i` to point `j`.
  2. Initialize the base case where `i` and `j` are adjacent points.
  3. Fill up the `dp` array in a bottom-up manner by considering all possible triangulations.
- Proof of optimality: This approach is optimal because it considers all possible triangulations and uses dynamic programming to avoid redundant calculations.

```cpp
int minScoreTriangulation(vector<vector<int>>& A) {
    int n = A.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i + 2; j < n; j++) {
            dp[i][j] = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                int side1 = calculateDistance(A[i], A[k]);
                int side2 = calculateDistance(A[k], A[j]);
                int side3 = calculateDistance(A[j], A[i]);
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + side1 * side2 * side3);
            }
        }
    }
    return dp[0][n - 1];
}

int calculateDistance(vector<int>& p1, vector<int>& p2) {
    return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of points. This is because we fill up the `dp` array in a bottom-up manner, and for each sub-problem, we consider all possible triangulations.
> - **Space Complexity:** $O(n^2)$, as we use a 2D array to store the minimum score for each sub-problem.
> - **Optimality proof:** This approach is optimal because it considers all possible triangulations and uses dynamic programming to avoid redundant calculations, resulting in a time complexity of $O(n^3)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, triangulation, and optimization.
- Problem-solving patterns identified: breaking down the problem into sub-problems and using dynamic programming to avoid redundant calculations.
- Optimization techniques learned: using dynamic programming to store the minimum score for each sub-problem.
- Similar problems to practice: other optimization problems that involve triangulation or dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the base case correctly, not filling up the `dp` array in a bottom-up manner, and not considering all possible triangulations.
- Edge cases to watch for: the input points forming a convex polygon, and the input points not having any three points that are collinear.
- Performance pitfalls: using a brute force approach that considers all possible triangulations, resulting in a high time complexity.
- Testing considerations: testing the implementation with different input points and verifying that the output is correct.