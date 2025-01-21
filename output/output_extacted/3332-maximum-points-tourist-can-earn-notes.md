## Maximum Points Tourist Can Earn
**Problem Link:** https://leetcode.com/problems/maximum-points-tourist-can-earn/description

**Problem Statement:**
- Given a list of `n` points representing the number of points that can be earned at each location, and a list of `m` travel costs between these locations.
- The goal is to find the maximum number of points that can be earned by visiting a subset of these locations, considering the travel costs.
- Input format: `n` points and `m` travel costs.
- Expected output: The maximum number of points that can be earned.
- Key requirements: The tourist must start at the first location and visit each location in order.
- Example test cases:
  - Input: `points = [2, 3, 6, 8], costs = [1, 2, 3]`
  - Output: `18`
  - Explanation: The tourist visits the first location (2 points), then travels to the second location (3 points) with a cost of 1, then travels to the third location (6 points) with a cost of 2, and finally travels to the fourth location (8 points) with a cost of 3.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of visiting locations and calculate the total points earned for each combination.
- The brute force approach involves iterating over all possible subsets of locations and calculating the total points earned for each subset.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
int maxPoints(vector<int>& points, vector<int>& costs) {
    int n = points.size();
    int maxPoints = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentPoints = 0;
        int currentCost = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentPoints += points[i];
                if (i > 0) {
                    currentCost += costs[i - 1];
                }
            }
        }
        maxPoints = max(maxPoints, currentPoints - currentCost);
    }
    return maxPoints;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of locations. This is because we are trying all possible subsets of locations and calculating the total points earned for each subset.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum points earned and the current points earned.
> - **Why these complexities occur:** The time complexity occurs because we are using a nested loop to try all possible subsets of locations. The space complexity occurs because we are only using a constant amount of space to store the maximum points earned and the current points earned.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the maximum points earned for each location.
- We can use a dynamic programming table `dp` to store the maximum points earned for each location.
- For each location, we can calculate the maximum points earned by considering two options: visiting the current location or not visiting the current location.
- If we visit the current location, we add the points earned for the current location to the maximum points earned for the previous location.
- If we do not visit the current location, we simply take the maximum points earned for the previous location.

```cpp
int maxPoints(vector<int>& points, vector<int>& costs) {
    int n = points.size();
    vector<int> dp(n);
    dp[0] = points[0];
    for (int i = 1; i < n; i++) {
        dp[i] = dp[i - 1] + points[i] - costs[i - 1];
        for (int j = 0; j < i; j++) {
            dp[i] = max(dp[i], dp[j] + points[i] - costs[j]);
        }
    }
    return *max_element(dp.begin(), dp.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of locations. This is because we are using a nested loop to calculate the maximum points earned for each location.
> - **Space Complexity:** $O(n)$, because we are using a dynamic programming table to store the maximum points earned for each location.
> - **Optimality proof:** This is the optimal solution because we are considering all possible options for visiting each location and calculating the maximum points earned for each option. We are also using dynamic programming to avoid redundant calculations and reduce the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems, using dynamic programming to store the solutions to sub-problems.
- Optimization techniques learned: using dynamic programming to avoid redundant calculations, reducing the time complexity by using a nested loop.
- Similar problems to practice: other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dynamic programming table correctly, not considering all possible options for visiting each location.
- Edge cases to watch for: the case where the input arrays are empty, the case where the input arrays have a single element.
- Performance pitfalls: using a brute force approach, not using dynamic programming to avoid redundant calculations.
- Testing considerations: testing the solution with different input arrays, testing the solution with edge cases.