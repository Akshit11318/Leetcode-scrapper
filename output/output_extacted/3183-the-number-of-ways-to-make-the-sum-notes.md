## The Number of Ways to Make the Sum
**Problem Link:** https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` and an integer `k`, return the number of ways to make the sum `k` using the elements of `nums`.
- Expected output format: The number of ways to make the sum `k`.
- Key requirements and edge cases to consider: Each element in `nums` can only be used once, and the order of the elements does not matter.
- Example test cases with explanations:
  - Input: `nums = [1, 2, 3, 4], k = 5`
    Output: `2`
    Explanation: There are two ways to make the sum `5`: `[1, 4]` and `[2, 3]`.
  - Input: `nums = [1, 2, 3, 4], k = 10`
    Output: `0`
    Explanation: There is no way to make the sum `10` using the elements of `nums`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a recursive approach to try all possible combinations of elements in `nums` to make the sum `k`.
- Step-by-step breakdown of the solution:
  1. Define a recursive function `dfs` that takes the current index `i`, the current sum `sum`, and the number of ways `count`.
  2. If `sum` equals `k`, increment `count`.
  3. If `sum` exceeds `k` or `i` reaches the end of `nums`, return.
  4. Recursively call `dfs` with `i + 1` and `sum + nums[i]` to include the current element.
  5. Recursively call `dfs` with `i + 1` and `sum` to exclude the current element.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible combinations.

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int k) {
        vector<int> dp(k + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= k; i++) {
            for (int num : nums) {
                if (i >= num) {
                    dp[i] += dp[i - num];
                }
            }
        }
        return dp[k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n)$, where $n$ is the size of `nums`.
> - **Space Complexity:** $O(k)$.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is due to the dynamic programming array `dp`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of ways to make each sum from `0` to `k`.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `k + 1` with all elements set to `0`, except `dp[0]` which is set to `1`.
  2. Iterate over each sum from `1` to `k`.
  3. For each sum `i`, iterate over each element `num` in `nums`.
  4. If `i` is greater than or equal to `num`, add the number of ways to make the sum `i - num` to `dp[i]`.
- Proof of optimality: This approach has a time complexity of $O(k \cdot n)$, which is optimal because we need to consider each element in `nums` for each sum from `1` to `k`.

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int k) {
        vector<int> dp(k + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= k; i++) {
            for (int num : nums) {
                if (i >= num) {
                    dp[i] += dp[i - num];
                }
            }
        }
        return dp[k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n)$.
> - **Space Complexity:** $O(k)$.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(k \cdot n)$, which is the minimum required to consider each element in `nums` for each sum from `1` to `k`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and recursive approaches.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results and avoid redundant calculations.
- Optimization techniques learned: Using a bottom-up dynamic programming approach to avoid the overhead of recursive function calls.
- Similar problems to practice: Other dynamic programming problems, such as the `0/1 Knapsack Problem` and the `Longest Common Subsequence Problem`.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the dynamic programming array, or using an incorrect recursive approach.
- Edge cases to watch for: Handling the case where `k` is `0`, or where `nums` is empty.
- Performance pitfalls: Using a recursive approach without memoization, or using a dynamic programming approach with an incorrect recurrence relation.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.