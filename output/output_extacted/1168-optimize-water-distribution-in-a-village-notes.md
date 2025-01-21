## Optimize Water Distribution in a Village
**Problem Link:** https://leetcode.com/problems/optimize-water-distribution-in-a-village/description

**Problem Statement:**
- Input format: The function takes two parameters: `n` representing the number of houses and `wells` which is a list of integers representing the cost to build a well at each house.
- Constraints: $1 \leq n \leq 10^4$, $1 \leq wells.length \leq 10^4$, $1 \leq wells[i] \leq 10^5$.
- Expected output format: The minimum total cost to supply water to all houses.
- Key requirements and edge cases to consider: The village is represented as a straight line, and each house can either be supplied water directly from a well or through pipes from adjacent houses. The cost of building a well at each house and the cost of laying pipes between houses are given. The goal is to minimize the total cost of supplying water to all houses.
- Example test cases with explanations: For example, given `n = 3` and `wells = [1, 2, 2]`, the minimum total cost to supply water to all houses is 3 because we can build a well at the first house and lay pipes to the other two houses.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by considering all possible combinations of building wells and laying pipes.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of houses where wells can be built.
  2. For each subset, calculate the cost of building wells at these houses.
  3. Calculate the cost of laying pipes to supply water to the remaining houses.
  4. Sum up the costs and keep track of the minimum total cost.
- Why this approach comes to mind first: It is a straightforward approach that considers all possibilities.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int minCostToSupplyWater(int n, vector<int>& wells) {
    int minCost = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        int cost = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                cost += wells[i];
            }
        }
        // Calculate the cost of laying pipes
        vector<int> houses;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                houses.push_back(i);
            }
        }
        for (int i = 0; i < houses.size(); i++) {
            if (i == 0) {
                cost += abs(houses[i] - houses[0]);
            } else {
                cost += abs(houses[i] - houses[i - 1]);
            }
        }
        minCost = min(minCost, cost);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of houses. The reason is that we generate all possible subsets of houses, and for each subset, we calculate the cost of laying pipes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of houses. The reason is that we need to store the costs of laying pipes for each subset of houses.
> - **Why these complexities occur:** The brute force approach considers all possible combinations of building wells and laying pipes, which leads to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to maintain a `dp` array where `dp[i]` represents the minimum cost to supply water to the first `i` houses.
- Detailed breakdown of the approach:
  1. Initialize the `dp` array with infinity.
  2. For each house, calculate the minimum cost to supply water to this house by considering two options: building a well at this house or laying a pipe from the previous house.
  3. Update the `dp` array accordingly.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of building wells and laying pipes, and we always choose the minimum cost option.

```cpp
#include <vector>
#include <climits>

using namespace std;

int minCostToSupplyWater(int n, vector<int>& wells) {
    vector<int> dp(n, INT_MAX);
    dp[0] = wells[0];
    for (int i = 1; i < n; i++) {
        dp[i] = min(dp[i], dp[i - 1] + 1); // Lay a pipe from the previous house
        dp[i] = min(dp[i], wells[i]); // Build a well at this house
        if (i > 1) {
            dp[i] = min(dp[i], dp[i - 2] + 1 + 1); // Lay pipes from the house two positions before
        }
    }
    return dp[n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of houses. The reason is that we only need to iterate through the `dp` array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of houses. The reason is that we need to store the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of building wells and laying pipes, and we always choose the minimum cost option.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, greedy algorithm.
- Problem-solving patterns identified: The problem can be solved by breaking it down into smaller subproblems and solving each subproblem only once.
- Optimization techniques learned: Memoization, dynamic programming.
- Similar problems to practice: [Other dynamic programming problems](https://leetcode.com/tag/dynamic-programming/).

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not considering all possible combinations of building wells and laying pipes.
- Edge cases to watch for: The case where there is only one house, the case where there are no houses.
- Performance pitfalls: Not using memoization or dynamic programming, which can lead to exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.