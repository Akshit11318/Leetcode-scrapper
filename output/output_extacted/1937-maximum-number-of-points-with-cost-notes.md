## Maximum Number of Points with Cost
**Problem Link:** https://leetcode.com/problems/maximum-number-of-points-with-cost/description

**Problem Statement:**
- Input format and constraints: The problem provides an array `cost` where `cost[i]` represents the cost of building the `i-th` point. We need to find the maximum number of points that can be built within a certain budget `M`.
- Expected output format: The output should be the maximum number of points that can be built.
- Key requirements and edge cases to consider: The problem requires us to consider the cost of building each point and the budget constraint. We should also handle edge cases where the budget is not enough to build any points or where the cost of building a point exceeds the budget.
- Example test cases with explanations:
  - Example 1: `cost = [1,2,3,4,5], M = 10`, the output should be `3`.
  - Example 2: `cost = [1,2,3,4,5], M = 0`, the output should be `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of points and checking if the total cost exceeds the budget.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of points.
  2. For each combination, calculate the total cost.
  3. Check if the total cost exceeds the budget.
  4. If not, update the maximum number of points that can be built.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxPoints(vector<int>& cost, int M) {
        int n = cost.size();
        int maxPoints = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int totalCost = 0;
            int points = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    totalCost += cost[i];
                    points++;
                }
            }
            if (totalCost <= M) {
                maxPoints = max(maxPoints, points);
            }
        }
        return maxPoints;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of points. This is because we are generating all possible combinations of points.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum number of points and the total cost.
> - **Why these complexities occur:** The time complexity occurs because we are using a brute force approach that tries all possible combinations of points. The space complexity occurs because we are only using a constant amount of space to store the necessary variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dynamic programming approach to solve this problem. The idea is to build a 2D table where the rows represent the points and the columns represent the budget.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` of size $(n+1) \times (M+1)$, where $n$ is the number of points and $M$ is the budget.
  2. Initialize the first row and column of the table to 0.
  3. For each point $i$, consider two options: either build the point or not build the point.
  4. If we build the point, the cost is `cost[i]` and the number of points built is `dp[i-1][M-cost[i]] + 1`.
  5. If we do not build the point, the cost is 0 and the number of points built is `dp[i-1][M]`.
  6. Choose the option that maximizes the number of points built.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of points and choose the one that maximizes the number of points built within the budget constraint.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxPoints(vector<int>& cost, int M) {
        int n = cost.size();
        vector<vector<int>> dp(n + 1, vector<int>(M + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= M; j++) {
                if (cost[i-1] > j) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + 1);
                }
            }
        }
        return dp[n][M];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(nM)$, where $n$ is the number of points and $M$ is the budget. This is because we are filling up a 2D table of size $(n+1) \times (M+1)$.
> - **Space Complexity:** $O(nM)$, as we are using a 2D table to store the dynamic programming values.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of points and choose the one that maximizes the number of points built within the budget constraint.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and budget constraints.
- Problem-solving patterns identified: The problem requires us to consider all possible combinations of points and choose the one that maximizes the number of points built within the budget constraint.
- Optimization techniques learned: We can use dynamic programming to solve this problem efficiently.
- Similar problems to practice: Other problems that involve dynamic programming and budget constraints, such as the 0/1 knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly or not considering the budget constraint.
- Edge cases to watch for: The budget is not enough to build any points or the cost of building a point exceeds the budget.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of points.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it works correctly.