## Maximum Points in an Archery Competition

**Problem Link:** https://leetcode.com/problems/maximum-points-in-an-archery-competition/description

**Problem Statement:**
- Input format and constraints: The problem takes a 2D array `points` where each `points[i]` is a list of two integers, a score and a number of arrows, and the number of arrows `k`.
- Expected output format: The function should return the maximum points that can be obtained.
- Key requirements and edge cases to consider: The score is obtained by hitting the target with the number of arrows required for that score. If the number of arrows required for a score is more than the remaining arrows, that score cannot be obtained.
- Example test cases with explanations: For example, if `points = [[2,2],[3,4],[5,1],[4,5]]` and `k = 5`, the function should return `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of scores and check which combination gives the maximum points.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of scores.
  2. For each combination, calculate the total points and the total arrows required.
  3. If the total arrows required is less than or equal to `k`, update the maximum points.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity.

```cpp
class Solution {
public:
    int maximumPoints(vector<vector<int>>& points, int k) {
        int n = points.size();
        int maxPoints = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int pointsObtained = 0;
            int arrowsUsed = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    pointsObtained += points[i][0];
                    arrowsUsed += points[i][1];
                }
            }
            if (arrowsUsed <= k) {
                maxPoints = max(maxPoints, pointsObtained);
            }
        }
        return maxPoints;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of points. This is because we are generating all possible combinations of scores and for each combination, we are calculating the total points and the total arrows required.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible combinations of scores, and for each combination, we are performing a constant amount of work.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient algorithm to solve this problem. The problem can be solved using dynamic programming.
- Detailed breakdown of the approach:
  1. Initialize a DP array `dp` of size `k + 1`, where `dp[i]` represents the maximum points that can be obtained with `i` arrows.
  2. Iterate over each point and for each point, iterate over the DP array in reverse order.
  3. For each `dp[i]`, update `dp[i + points[j][1]]` with the maximum of its current value and `dp[i] + points[j][0]`.
- Proof of optimality: This approach is optimal because it tries all possible combinations of scores in a more efficient way.

```cpp
class Solution {
public:
    int maximumPoints(vector<vector<int>>& points, int k) {
        int n = points.size();
        vector<int> dp(k + 1, 0);
        for (int i = 0; i < n; i++) {
            for (int j = k; j >= points[i][1]; j--) {
                dp[j] = max(dp[j], dp[j - points[i][1]] + points[i][0]);
            }
        }
        return dp[k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of points and $k$ is the number of arrows.
> - **Space Complexity:** $O(k)$, as we are using a DP array of size `k + 1`.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of scores in a more efficient way.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: Trying all possible combinations of scores, using dynamic programming to optimize the solution.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity.
- Similar problems to practice: Other problems that involve trying all possible combinations of scores or using dynamic programming to optimize the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP array correctly, not updating the DP array correctly.
- Edge cases to watch for: When the number of arrows is 0, when the number of points is 0.
- Performance pitfalls: Not using dynamic programming to optimize the solution, trying all possible combinations of scores in a brute force way.
- Testing considerations: Testing the solution with different inputs, testing the solution with edge cases.