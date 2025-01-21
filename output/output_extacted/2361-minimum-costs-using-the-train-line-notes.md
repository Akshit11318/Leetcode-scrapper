## Minimum Costs Using the Train Line

**Problem Link:** https://leetcode.com/problems/minimum-costs-using-the-train-line/description

**Problem Statement:**
- Input: An array of integers representing the costs of traveling from one city to another using different train lines.
- Constraints: The input array will have a length of at least 1 and at most 1000, and each cost will be a non-negative integer.
- Expected Output: The minimum cost to travel from the first city to the last city.
- Key Requirements: The minimum cost should be calculated by considering all possible paths and choosing the one with the lowest total cost.
- Example Test Cases:
  - Input: `[10, 20, 30]`
  - Output: `10`
  - Explanation: The minimum cost is achieved by traveling directly from the first city to the last city.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to consider all possible paths from the first city to the last city and calculate the total cost for each path.
- The brute force approach involves iterating over all possible subsets of the input array and calculating the total cost for each subset.
- This approach comes to mind first because it guarantees finding the minimum cost by considering all possible paths.

```cpp
int minCost(vector<int>& cost) {
    int n = cost.size();
    int min_cost = INT_MAX;
    for (int mask = 1; mask < (1 << n); mask++) {
        int current_cost = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                current_cost += cost[i];
            }
        }
        min_cost = min(min_cost, current_cost);
    }
    return min_cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we iterate over all possible subsets of the input array, and for each subset, we iterate over the elements of the subset.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum cost and the current cost.
> - **Why these complexities occur:** The time complexity is exponential because we consider all possible subsets of the input array, and the space complexity is constant because we only use a fixed amount of space to store the minimum cost and the current cost.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the minimum cost of traveling from the first city to each city.
- We can calculate the minimum cost of traveling from the first city to each city by considering the minimum cost of traveling from the first city to the previous city and adding the cost of traveling from the previous city to the current city.
- This approach is optimal because it avoids recalculating the minimum cost of traveling from the first city to each city by storing the results of subproblems.

```cpp
int minCost(vector<int>& cost) {
    int n = cost.size();
    vector<int> dp(n);
    dp[0] = cost[0];
    for (int i = 1; i < n; i++) {
        dp[i] = min(dp[i-1], cost[i]);
    }
    return dp[n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate over the input array once to calculate the minimum cost of traveling from the first city to each city.
> - **Space Complexity:** $O(n)$, because we use a dynamic programming array to store the minimum cost of traveling from the first city to each city.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a minimal amount of space to store the results of subproblems.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is dynamic programming, which is used to store the results of subproblems and avoid recalculating them.
- The problem-solving pattern identified is to use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- The optimization technique learned is to use dynamic programming to reduce the time complexity of a problem by storing the results of subproblems.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the dynamic programming array or to use an incorrect index to access the array.
- An edge case to watch for is when the input array is empty, in which case the function should return 0 or throw an exception.
- A performance pitfall is to use a brute force approach to solve the problem, which can result in an exponential time complexity.