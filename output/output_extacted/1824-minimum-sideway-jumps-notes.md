## Minimum Sideway Jumps
**Problem Link:** https://leetcode.com/problems/minimum-sideway-jumps/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `obstacles` as input, representing the obstacles on each lane. The goal is to find the minimum number of sideway jumps required to reach the end of the road.
- Expected output format: The function should return the minimum number of sideway jumps.
- Key requirements and edge cases to consider: The function should handle cases where there are no obstacles, or where there are obstacles in all lanes.
- Example test cases with explanations:
  - Example 1: `obstacles = [0,1,2,0,3,0]`, the function should return `2` because the minimum number of sideway jumps is 2.
  - Example 2: `obstacles = [0,1,1,3,3,0]`, the function should return `4` because the minimum number of sideway jumps is 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of sideway jumps and counting the minimum number of jumps required to reach the end of the road.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `min_jumps` to store the minimum number of jumps.
  2. Iterate over all possible combinations of sideway jumps.
  3. For each combination, simulate the journey and count the number of jumps required to reach the end of the road.
  4. Update `min_jumps` if the current combination requires fewer jumps.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
#include <vector>
using namespace std;

int minSideJumps(vector<int>& obstacles) {
    int n = obstacles.size();
    int min_jumps = INT_MAX;
    for (int i = 0; i < (1 << (n - 1)); i++) {
        int jumps = 0;
        int current_lane = 2; // Start on lane 2
        for (int j = 0; j < n - 1; j++) {
            if (obstacles[j + 1] == current_lane) {
                // If there is an obstacle on the current lane, jump to a different lane
                if (((i >> j) & 1) == 0) {
                    // Jump to lane 1
                    current_lane = 1;
                } else {
                    // Jump to lane 3
                    current_lane = 3;
                }
                jumps++;
            }
        }
        min_jumps = min(min_jumps, jumps);
    }
    return min_jumps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1})$ because we are iterating over all possible combinations of sideway jumps.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the minimum number of jumps.
> - **Why these complexities occur:** The time complexity is exponential because we are trying all possible combinations of sideway jumps, and the space complexity is constant because we are using a fixed amount of space to store the minimum number of jumps.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using dynamic programming to store the minimum number of jumps required to reach each lane at each position.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` to store the minimum number of jumps required to reach each lane at each position.
  2. Iterate over each position and each lane.
  3. For each lane, check if there is an obstacle on the current lane. If there is, update the minimum number of jumps required to reach the current lane.
  4. Return the minimum number of jumps required to reach the end of the road.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <vector>
using namespace std;

int minSideJumps(vector<int>& obstacles) {
    int n = obstacles.size();
    vector<vector<int>> dp(4, vector<int>(n, INT_MAX));
    dp[2][0] = 0; // Start on lane 2 with 0 jumps
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= 3; j++) {
            if (obstacles[i] != j) {
                for (int k = 1; k <= 3; k++) {
                    if (k != j) {
                        dp[j][i] = min(dp[j][i], dp[k][i - 1] + 1);
                    }
                }
                dp[j][i] = min(dp[j][i], dp[j][i - 1]);
            }
        }
    }
    return min({dp[1][n - 1], dp[2][n - 1], dp[3][n - 1]});
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are iterating over each position and each lane.
> - **Space Complexity:** $O(n)$ because we are using a 2D array to store the minimum number of jumps required to reach each lane at each position.
> - **Optimality proof:** The dynamic programming approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and iteration.
- Problem-solving patterns identified: Using dynamic programming to store the minimum number of jumps required to reach each lane at each position.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other dynamic programming problems, such as the `Longest Increasing Subsequence` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, or not updating the minimum number of jumps required to reach each lane at each position correctly.
- Edge cases to watch for: Cases where there are no obstacles, or where there are obstacles in all lanes.
- Performance pitfalls: Using an exponential time complexity approach, such as the brute force approach.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it is working correctly.