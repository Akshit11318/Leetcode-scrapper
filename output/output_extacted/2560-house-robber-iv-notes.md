## House Robber IV
**Problem Link:** https://leetcode.com/problems/house-robber-iv/description

**Problem Statement:**
- Input format: You are given an integer array `nums` and an integer `k`.
- Constraints: $1 \leq nums.length \leq 100$, $0 \leq nums[i] \leq 100$, and $1 \leq k \leq 100$.
- Expected output format: Return the maximum score you can get.
- Key requirements and edge cases to consider: The problem is a variation of the classic House Robber problem, where you need to find the maximum score that can be obtained by either keeping the current number or skipping it and keeping the previous number, with the additional constraint that you can only skip at most `k` numbers.
- Example test cases with explanations: For example, if `nums = [5,2,3,1,5,6,4]` and `k = 2`, the maximum score is 18, which can be obtained by keeping the numbers 5, 3, 5, and 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use recursion to try all possible combinations of keeping or skipping numbers, and then return the maximum score.
- Step-by-step breakdown of the solution:
  1. Define a recursive function `dfs` that takes the current index `i` and the number of skips `k` as parameters.
  2. If `i` is equal to the length of `nums`, return 0, because there are no more numbers to keep or skip.
  3. If `k` is equal to 0, return the sum of the remaining numbers, because we can no longer skip any numbers.
  4. Otherwise, try keeping the current number and skipping the next number, and recursively call `dfs` with `i + 1` and `k - 1`.
  5. Try skipping the current number and recursively call `dfs` with `i + 1` and `k`.
  6. Return the maximum score of the two possibilities.
- Why this approach comes to mind first: This approach is a straightforward way to solve the problem, but it has an exponential time complexity due to the recursive calls.

```cpp
int dfs(vector<int>& nums, int i, int k) {
    if (i == nums.size()) return 0;
    if (k == 0) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
        }
        return sum;
    }
    return max(nums[i] + dfs(nums, i + 1, k - 1), dfs(nums, i + 1, k));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of `nums`, because we are trying all possible combinations of keeping or skipping numbers.
> - **Space Complexity:** $O(n)$, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is exponential because we are trying all possible combinations, and the space complexity is linear because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum score for each subproblem, and then use these stored values to solve the larger problem.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of size $(n + 1) \times (k + 1)$, where `dp[i][j]` represents the maximum score that can be obtained by considering the first `i` numbers and using at most `j` skips.
  2. Initialize `dp[0][0]` to 0, because we have not considered any numbers yet.
  3. For each number `nums[i]`, try keeping it and skipping the next number, and update `dp[i + 1][j]` with the maximum score.
  4. Try skipping the current number and update `dp[i + 1][j]` with the maximum score.
  5. Return `dp[n][k]`, where `n` is the length of `nums`.
- Why further optimization is impossible: This approach has a time complexity of $O(nk)$, which is the best possible time complexity for this problem, because we need to consider all possible combinations of keeping or skipping numbers.

```cpp
int maxResult(vector<int>& nums, int k) {
    int n = nums.size();
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            if (j == 0) {
                dp[i][j] = dp[i - 1][j] + nums[i - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1]);
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the length of `nums`, because we are considering all possible combinations of keeping or skipping numbers.
> - **Space Complexity:** $O(nk)$, because of the 2D array `dp`.
> - **Optimality proof:** This approach is optimal because we are considering all possible combinations of keeping or skipping numbers, and we are using dynamic programming to store the maximum score for each subproblem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, and memoization.
- Problem-solving patterns identified: The problem can be solved using a bottom-up dynamic programming approach.
- Optimization techniques learned: We can use dynamic programming to store the maximum score for each subproblem, and then use these stored values to solve the larger problem.
- Similar problems to practice: House Robber, House Robber II, and other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, or not considering all possible combinations of keeping or skipping numbers.
- Edge cases to watch for: The case where `k` is equal to 0, or the case where `n` is equal to 0.
- Performance pitfalls: Using a recursive approach without memoization, or using a brute force approach that tries all possible combinations of keeping or skipping numbers.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs, to ensure that it works correctly and efficiently.