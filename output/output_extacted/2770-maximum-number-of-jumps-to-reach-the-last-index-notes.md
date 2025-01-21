## Maximum Number of Jumps to Reach the Last Index

**Problem Link:** https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `arr` and an integer `d` as input. The array `arr` contains non-negative integers, and `d` represents the maximum allowed jump distance. The goal is to find the maximum number of jumps to reach the last index.
- Expected output format: The output should be the maximum number of jumps.
- Key requirements and edge cases to consider:
  - The input array `arr` can be empty.
  - The maximum allowed jump distance `d` can be greater than the length of the array.
  - The array `arr` can contain zeros.
- Example test cases with explanations:
  - Example 1: Input: `arr = [1, 1, 1], d = 2`, Output: `2`.
  - Example 2: Input: `arr = [0, 0, 0], d = 2`, Output: `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible jump combinations to reach the last index.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_jumps` to store the maximum number of jumps.
  2. Iterate over all possible jump combinations using recursion or iteration.
  3. For each combination, check if it reaches the last index within the allowed jump distance `d`.
  4. Update `max_jumps` if a valid combination is found.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it has exponential time complexity due to the recursive nature of the solution.

```cpp
class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        int max_jumps = -1;
        
        function<void(int, int)> dfs = [&](int index, int jumps) {
            if (index == n - 1) {
                max_jumps = max(max_jumps, jumps);
                return;
            }
            for (int i = 1; i <= d; i++) {
                if (index + i < n) {
                    dfs(index + i, jumps + 1);
                }
            }
        };
        
        if (n > 0) {
            dfs(0, 0);
        }
        
        return max_jumps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^d)$, where $n$ is the length of the input array and $d$ is the maximum allowed jump distance. This is because in the worst case, we need to try all possible jump combinations.
> - **Space Complexity:** $O(n)$, which is the maximum recursion depth.
> - **Why these complexities occur:** The exponential time complexity is due to the recursive nature of the solution, and the space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum number of jumps to reach each index.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size `n`, where `dp[i]` stores the maximum number of jumps to reach index `i`.
  2. Iterate over the array from left to right, and for each index `i`, try all possible jump distances `j` from `1` to `d`.
  3. Update `dp[i]` with the maximum number of jumps to reach index `i` by considering all possible jumps from previous indices.
- Proof of optimality: This approach has linear time complexity, which is optimal because we need to visit each index at least once.

```cpp
class Solution {
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> dp(n, -1);
        
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= d; j++) {
                if (i - j >= 0 && dp[i - j] != -1) {
                    dp[i] = max(dp[i], dp[i - j] + 1);
                }
            }
        }
        
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the length of the input array and $d$ is the maximum allowed jump distance. This is because we iterate over the array and for each index, we try all possible jump distances.
> - **Space Complexity:** $O(n)$, which is the size of the dynamic programming table.
> - **Optimality proof:** The linear time complexity is optimal because we need to visit each index at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and recursion.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results and avoid redundant computations.
- Optimization techniques learned: Reducing time complexity by using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array or a maximum allowed jump distance greater than the length of the array.
- Edge cases to watch for: Handling cases where the input array contains zeros or the maximum allowed jump distance is greater than the length of the array.
- Performance pitfalls: Not using dynamic programming to store intermediate results, which can lead to exponential time complexity.
- Testing considerations: Testing the solution with different input arrays and maximum allowed jump distances to ensure correctness.