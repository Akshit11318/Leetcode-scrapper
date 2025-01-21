## Maximize Total Tastiness of Purchased Fruits

**Problem Link:** https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/description

**Problem Statement:**
- Input format and constraints: Given a list of integers representing the tastiness of different fruits and a limit on the number of fruits that can be purchased.
- Expected output format: The maximum total tastiness that can be achieved.
- Key requirements and edge cases to consider: The number of fruits purchased must not exceed the given limit, and each fruit can only be purchased once.
- Example test cases with explanations: 
  - For example, if the tastiness of fruits is `[1, 2, 3]` and the limit is `2`, the maximum total tastiness is `5` (purchasing fruits with tastiness `2` and `3`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of purchasing fruits and calculate the total tastiness for each combination.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of purchasing fruits.
  2. For each combination, calculate the total tastiness.
  3. Keep track of the maximum total tastiness found.
- Why this approach comes to mind first: It's a straightforward and intuitive approach to solve the problem.

```cpp
#include <vector>
#include <algorithm>

int maximizeTastiness(std::vector<int>& fruits, int limit) {
    int n = fruits.size();
    int maxTastiness = 0;
    
    // Generate all possible combinations of purchasing fruits
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentTastiness = 0;
        int count = 0;
        
        // Calculate the total tastiness for the current combination
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentTastiness += fruits[i];
                count++;
            }
        }
        
        // Update the maximum total tastiness if the current combination is valid
        if (count <= limit) {
            maxTastiness = std::max(maxTastiness, currentTastiness);
        }
    }
    
    return maxTastiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of fruits. The reason is that we generate all possible combinations of purchasing fruits, which has a time complexity of $O(2^n)$. For each combination, we calculate the total tastiness, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum total tastiness and other variables.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to generating all possible combinations of purchasing fruits. The space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve the problem more efficiently. The idea is to build a table that stores the maximum total tastiness that can be achieved for each possible number of fruits purchased.
- Detailed breakdown of the approach: 
  1. Create a table `dp` of size $(limit + 1) \times (n + 1)$, where `dp[i][j]` represents the maximum total tastiness that can be achieved by purchasing `i` fruits from the first `j` fruits.
  2. Initialize the table by setting `dp[0][j] = 0` for all `j`, since purchasing no fruits results in a total tastiness of 0.
  3. Fill in the table using the following recurrence relation: `dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + fruits[j-1])`. This relation says that the maximum total tastiness that can be achieved by purchasing `i` fruits from the first `j` fruits is either the same as purchasing `i` fruits from the first `j-1` fruits or purchasing `i-1` fruits from the first `j-1` fruits and adding the tastiness of the `j`-th fruit.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of purchasing fruits and calculate the maximum total tastiness that can be achieved. The recurrence relation used to fill in the table is optimal because it considers the two possible cases: purchasing the current fruit or not purchasing it.

```cpp
int maximizeTastiness(std::vector<int>& fruits, int limit) {
    int n = fruits.size();
    std::vector<std::vector<int>> dp(limit + 1, std::vector<int>(n + 1, 0));
    
    // Fill in the table using the recurrence relation
    for (int i = 1; i <= limit; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = std::max(dp[i][j-1], dp[i-1][j-1] + fruits[j-1]);
        }
    }
    
    // The maximum total tastiness is stored in the bottom-right corner of the table
    return dp[limit][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(limit \cdot n)$, where $n$ is the number of fruits and $limit$ is the maximum number of fruits that can be purchased. The reason is that we fill in a table of size $(limit + 1) \times (n + 1)$ using a nested loop.
> - **Space Complexity:** $O(limit \cdot n)$, as we use a table of size $(limit + 1) \times (n + 1)$ to store the maximum total tastiness that can be achieved for each possible number of fruits purchased.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of purchasing fruits and calculate the maximum total tastiness that can be achieved. The recurrence relation used to fill in the table is optimal because it considers the two possible cases: purchasing the current fruit or not purchasing it.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recurrence relations, and table filling.
- Problem-solving patterns identified: The problem can be solved using a bottom-up dynamic programming approach, where we fill in a table using a recurrence relation.
- Optimization techniques learned: The dynamic programming approach optimizes the solution by avoiding redundant calculations and considering all possible combinations of purchasing fruits.
- Similar problems to practice: Other problems that can be solved using dynamic programming, such as the 0/1 knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the table correctly or not using the correct recurrence relation.
- Edge cases to watch for: The case where the number of fruits is 0 or the limit is 0.
- Performance pitfalls: Using a naive approach that has an exponential time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it produces the correct output.