## Pizza Toppings Cost Analysis

**Problem Link:** https://leetcode.com/problems/pizza-toppings-cost-analysis/description

**Problem Statement:**
- Input format and constraints: The input consists of a `2D` array `costs` where each inner array represents the cost of a pizza topping at different levels of quality. The number of rows in `costs` represents the number of toppings, and the number of columns represents the number of quality levels for each topping. The goal is to find the minimum cost to achieve a target `totalCost` using the given toppings and their respective quality levels.
- Expected output format: The minimum cost to achieve the target `totalCost`, or `-1` if it's impossible.
- Key requirements and edge cases to consider: The problem involves a combinatorial optimization problem, where we need to find the optimal combination of toppings and their quality levels to minimize the cost while achieving the target `totalCost`.
- Example test cases with explanations:
    - Example 1: `costs = [[1, 3, 5], [2, 4, 6], [3, 5, 7]], totalCost = 9` should return `3`, because we can choose the first topping at quality level `1` (cost `1`) and the second topping at quality level `2` (cost `2`), for a total cost of `3`.
    - Example 2: `costs = [[1, 3, 5], [2, 4, 6], [3, 5, 7]], totalCost = 10` should return `-1`, because it's impossible to achieve a total cost of `10` using the given toppings and their quality levels.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of toppings and their quality levels to find the minimum cost that achieves the target `totalCost`.
- Step-by-step breakdown of the solution:
    1. Initialize a variable `minCost` to store the minimum cost found so far, initialized to a large value (e.g., `INT_MAX`).
    2. Iterate over all possible combinations of toppings and their quality levels using nested loops.
    3. For each combination, calculate the total cost by summing the costs of each topping at its chosen quality level.
    4. If the total cost equals the target `totalCost`, update `minCost` if the current cost is less than the stored minimum cost.
- Why this approach comes to mind first: The brute force approach is a straightforward way to solve the problem by trying all possible combinations, but it's inefficient due to its high computational complexity.

```cpp
#include <vector>
#include <climits>

int minCost(std::vector<std::vector<int>>& costs, int totalCost) {
    int minCost = INT_MAX;
    int numToppings = costs.size();
    int numQualityLevels = costs[0].size();

    // Iterate over all possible combinations of toppings and their quality levels
    for (int i = 0; i < numToppings; i++) {
        for (int j = 0; j < numQualityLevels; j++) {
            // Calculate the total cost for the current combination
            int currentCost = costs[i][j];

            // Check if the current cost equals the target totalCost
            if (currentCost == totalCost) {
                // Update minCost if the current cost is less than the stored minimum cost
                minCost = std::min(minCost, currentCost);
            }

            // Recursively explore combinations with additional toppings
            for (int k = i + 1; k < numToppings; k++) {
                for (int l = 0; l < numQualityLevels; l++) {
                    // Calculate the total cost for the current combination
                    int newCost = currentCost + costs[k][l];

                    // Check if the new cost equals the target totalCost
                    if (newCost == totalCost) {
                        // Update minCost if the new cost is less than the stored minimum cost
                        minCost = std::min(minCost, newCost);
                    }
                }
            }
        }
    }

    // Return the minimum cost found, or -1 if no combination achieves the target totalCost
    return (minCost == INT_MAX) ? -1 : minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times 2^n)$, where $n$ is the number of toppings and $m$ is the number of quality levels for each topping. This is because we're iterating over all possible combinations of toppings and their quality levels, resulting in an exponential number of iterations.
> - **Space Complexity:** $O(1)$, since we're only using a constant amount of space to store the minimum cost found.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the recursive exploration of all possible combinations, while the space complexity is low since we're not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming, where we build up a table of minimum costs for each possible total cost from `0` to `totalCost`.
- Detailed breakdown of the approach:
    1. Create a table `dp` of size `totalCost + 1`, where `dp[i]` represents the minimum cost to achieve a total cost of `i`.
    2. Initialize `dp[0] = 0`, since we can achieve a total cost of `0` with no toppings.
    3. Iterate over each topping and its quality levels, updating the `dp` table accordingly.
    4. For each topping, iterate over the quality levels and update `dp[i]` with the minimum cost to achieve a total cost of `i` using the current topping and its quality levels.
- Proof of optimality: The dynamic programming approach ensures that we're considering all possible combinations of toppings and their quality levels, while avoiding redundant calculations and minimizing the computational complexity.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n \times m \times totalCost)$, which is the best possible complexity for this problem since we need to consider all possible combinations of toppings and their quality levels.

```cpp
#include <vector>
#include <climits>

int minCost(std::vector<std::vector<int>>& costs, int totalCost) {
    std::vector<int> dp(totalCost + 1, INT_MAX);
    dp[0] = 0;

    for (const auto& topping : costs) {
        for (int qualityLevel : topping) {
            for (int i = totalCost; i >= qualityLevel; i--) {
                dp[i] = std::min(dp[i], dp[i - qualityLevel] + qualityLevel);
            }
        }
    }

    // Return the minimum cost found, or -1 if no combination achieves the target totalCost
    return (dp[totalCost] == INT_MAX) ? -1 : dp[totalCost];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times totalCost)$, where $n$ is the number of toppings and $m$ is the number of quality levels for each topping. This is because we're iterating over all possible combinations of toppings and their quality levels, resulting in a polynomial number of iterations.
> - **Space Complexity:** $O(totalCost)$, since we're using a table of size `totalCost + 1` to store the minimum costs for each possible total cost.
> - **Optimality proof:** The dynamic programming approach ensures that we're considering all possible combinations of toppings and their quality levels, while avoiding redundant calculations and minimizing the computational complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, combinatorial optimization.
- Problem-solving patterns identified: Building up a table of minimum costs for each possible total cost.
- Optimization techniques learned: Avoiding redundant calculations, minimizing computational complexity.
- Similar problems to practice: Other combinatorial optimization problems, such as the `0/1` knapsack problem or the subset sum problem.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` table, incorrect updating of the `dp` table.
- Edge cases to watch for: Handling cases where no combination achieves the target `totalCost`.
- Performance pitfalls: Using inefficient algorithms or data structures, such as recursive approaches or unbounded loops.
- Testing considerations: Thoroughly testing the implementation with various input cases, including edge cases and boundary cases.