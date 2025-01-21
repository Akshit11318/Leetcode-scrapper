## Longest Arithmetic Subsequence of Given Difference

**Problem Link:** https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description

**Problem Statement:**
- Input format: `nums` array and `diff` integer.
- Constraints: $1 \leq nums.length \leq 10^5$ and $0 \leq nums[i] \leq 10^9$ for all $i$, $0 \leq diff \leq 10^9$.
- Expected output format: Length of the longest arithmetic subsequence.
- Key requirements and edge cases to consider: Handling duplicates, negative differences, and sequences with varying lengths.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4], diff = 1` should return `4` because the longest arithmetic subsequence is `[1, 2, 3, 4]`.
  - `nums = [1, 3, 5, 7], diff = 2` should return `1` because there is no arithmetic subsequence with difference `2`.
  - `nums = [1, 1, 1], diff = 0` should return `3` because the longest arithmetic subsequence is `[1, 1, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subsequence of `nums` to see if it forms an arithmetic sequence with difference `diff`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums`.
  2. For each subsequence, check if the difference between consecutive elements is `diff`.
  3. Keep track of the longest subsequence that satisfies the condition.

```cpp
int longestSubsequence(vector<int>& nums, int diff) {
    int n = nums.size();
    int maxLength = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }
        bool isValid = true;
        for (int i = 1; i < subsequence.size(); i++) {
            if (subsequence[i] - subsequence[i - 1] != diff) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            maxLength = max(maxLength, (int)subsequence.size());
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because we generate all possible subsequences and check each one.
> - **Space Complexity:** $O(n)$, for storing the subsequence.
> - **Why these complexities occur:** Generating all subsequences leads to exponential time complexity, and checking each subsequence leads to linear time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a `map` to store the longest arithmetic subsequence ending at each number.
- Detailed breakdown of the approach:
  1. Initialize a `map` to store the length of the longest arithmetic subsequence ending at each number.
  2. Iterate through `nums`. For each number, check if `num - diff` is in the `map`.
  3. If it is, update the length of the longest arithmetic subsequence ending at `num` to be one more than the length of the longest arithmetic subsequence ending at `num - diff`.
  4. Keep track of the maximum length seen so far.

```cpp
int longestSubsequence(vector<int>& nums, int diff) {
    unordered_map<int, int> dp;
    int maxLength = 0;
    for (int num : nums) {
        int length = dp[num - diff] + 1;
        dp[num] = max(dp[num], length);
        maxLength = max(maxLength, dp[num]);
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we make a single pass through `nums`.
> - **Space Complexity:** $O(n)$, for storing the `map`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `nums` and uses a `map` to store the necessary information.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, use of `map` to store intermediate results.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, using a `map` to store the results of subproblems.
- Optimization techniques learned: Using a `map` to avoid redundant computation.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `map`, not updating the `map` correctly.
- Edge cases to watch for: Handling duplicates, negative differences.
- Performance pitfalls: Using a naive approach that generates all possible subsequences.
- Testing considerations: Testing the function with different inputs, including edge cases.