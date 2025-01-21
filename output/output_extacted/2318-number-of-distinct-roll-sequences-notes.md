## Number of Distinct Roll Sequences
**Problem Link:** https://leetcode.com/problems/number-of-distinct-roll-sequences/description

**Problem Statement:**
- Input: `n` - the number of rolls, `k` - the number of sides on each die, and `target` - the target number.
- Output: The number of distinct sequences of `n` rolls that sum up to `target`.
- Constraints: `1 <= n <= 30`, `1 <= k <= 30`, `1 <= target <= 1000`.
- Key requirements: Each roll can have `k` possible outcomes, and we need to find the number of distinct sequences that sum up to `target`.
- Example test cases:
  - `n = 3`, `k = 6`, `target = 7` => Output: `15`.
  - `n = 2`, `k = 6`, `target = 7` => Output: `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use recursion to generate all possible sequences of `n` rolls and count the number of sequences that sum up to `target`.
- Step-by-step breakdown:
  1. Define a recursive function that takes the current roll number and the current sum as arguments.
  2. For each possible outcome of the current roll, recursively call the function with the updated sum and roll number.
  3. If the current sum equals `target` and we have completed `n` rolls, increment the count of distinct sequences.
- Why this approach comes to mind first: It's a straightforward way to generate all possible sequences and count the ones that meet the condition.

```cpp
int distinctRolls(int n, int k, int target) {
    int count = 0;
    function<void(int, int)> dfs = [&](int roll, int sum) {
        if (roll == n) {
            if (sum == target) count++;
            return;
        }
        for (int i = 1; i <= k; i++) {
            dfs(roll + 1, sum + i);
        }
    };
    dfs(0, 0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, where `k` is the number of sides on each die and `n` is the number of rolls. This is because we have `k` possible outcomes for each roll, and we recursively generate all possible sequences.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The recursive approach generates all possible sequences, resulting in exponential time complexity. The space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to store the number of distinct sequences that sum up to each possible target value for each roll number.
- Detailed breakdown:
  1. Create a 2D array `dp` where `dp[i][j]` represents the number of distinct sequences of `i` rolls that sum up to `j`.
  2. Initialize `dp[0][0] = 1`, as there is one way to sum up to 0 with 0 rolls (i.e., no rolls).
  3. For each roll number `i` from 1 to `n`, and for each possible target value `j` from 1 to `target`, update `dp[i][j]` by summing up the number of distinct sequences that sum up to `j - k` for each `k` from 1 to `min(j, k)`.
- Proof of optimality: This approach ensures that we count each distinct sequence exactly once, as we only update `dp[i][j]` based on the number of distinct sequences that sum up to `j - k` for each `k`.

```cpp
int distinctRolls(int n, int k, int target) {
    vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= target; j++) {
            for (int x = 1; x <= min(j, k); x++) {
                dp[i][j] += dp[i - 1][j - x];
            }
        }
    }
    return dp[n][target];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot target \cdot k)$, where `n` is the number of rolls, `target` is the target sum, and `k` is the number of sides on each die. This is because we have three nested loops to update the `dp` array.
> - **Space Complexity:** $O(n \cdot target)$, due to the `dp` array.
> - **Optimality proof:** This approach ensures that we count each distinct sequence exactly once, resulting in optimal time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive approach.
- Problem-solving patterns identified: Counting distinct sequences, using dynamic programming to optimize recursive approaches.
- Optimization techniques learned: Using dynamic programming to store intermediate results and avoid redundant computations.
- Similar problems to practice: Counting distinct sequences, dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect update of the `dp` array.
- Edge cases to watch for: Handling cases where `n` or `target` is 0.
- Performance pitfalls: Using a recursive approach without optimization, resulting in exponential time complexity.
- Testing considerations: Testing with different values of `n`, `k`, and `target` to ensure correctness.