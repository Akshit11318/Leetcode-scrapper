## Minimum Number of Days to Eat N Oranges
**Problem Link:** https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/description

**Problem Statement:**
- Input format: An integer `n` representing the number of oranges.
- Constraints: `1 <= n <= 2 * 10^9`.
- Expected output format: The minimum number of days required to eat `n` oranges.
- Key requirements and edge cases to consider: The eating process follows specific rules, and we need to find the minimum days under these constraints.
- Example test cases with explanations:
  - For `n = 10`, the minimum days would be calculated based on the eating rules provided.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To simulate the eating process day by day, considering all possible ways to eat the oranges.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to track the number of days.
  2. Simulate the eating process by reducing the number of oranges based on the given rules.
  3. Increment the day counter each time a reduction occurs.
- Why this approach comes to mind first: It directly follows the problem statement, trying to simulate the process as described.

```cpp
class Solution {
public:
    int minDays(int n) {
        int days = 0;
        while (n > 0) {
            if (n % 3 == 0) {
                n /= 3;
            } else if (n % 2 == 0) {
                n /= 2;
            } else {
                n--;
            }
            days++;
        }
        return days;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because in the worst case, we might end up reducing `n` by 1 in each step.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity is linear because of the potential sequential reduction of `n`, and the space complexity is constant since we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using dynamic programming or memoization to store and reuse the results of subproblems.
- Detailed breakdown of the approach:
  1. Create a memoization table to store the minimum days for each number of oranges up to `n`.
  2. Fill the table by considering the minimum days required for each possible reduction (by 1, by 2 if divisible by 2, or by 3 if divisible by 3) and add 1 day.
  3. Return the minimum days for `n` from the memoization table.
- Proof of optimality: This approach ensures that each subproblem is solved only once and stored for future reference, avoiding redundant calculations.

```cpp
class Solution {
public:
    int minDays(int n) {
        unordered_map<int, int> memo;
        function<int(int)> dfs = [&](int n) {
            if (n == 0) return 0;
            if (memo.count(n)) return memo[n];
            int res = dfs(n - 1) + 1;
            if (n % 2 == 0) res = min(res, dfs(n / 2) + 1);
            if (n % 3 == 0) res = min(res, dfs(n / 3) + 1);
            memo[n] = res;
            return res;
        };
        return dfs(n);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because each number up to `n` is visited at most once and stored in the memoization table.
> - **Space Complexity:** $O(n)$ for storing the memoization table.
> - **Optimality proof:** This approach is optimal because it minimizes the number of redundant calculations by storing the results of subproblems, thus avoiding the exponential time complexity of naive recursion.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization and dynamic programming for optimizing recursive solutions.
- Problem-solving patterns identified: Breaking down problems into subproblems and solving them efficiently.
- Optimization techniques learned: Using memoization to avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems involving optimization.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly or forgetting to initialize the memoization table.
- Edge cases to watch for: Handling `n = 0` or `n = 1` as base cases.
- Performance pitfalls: Not using memoization or dynamic programming, leading to exponential time complexity.
- Testing considerations: Ensuring the solution works for a range of inputs, including large numbers and edge cases.