## Maximum Array Hopping Score I

**Problem Link:** https://leetcode.com/problems/maximum-array-hopping-score-i/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of length `n`, find the maximum score that can be achieved by hopping from one index to another.
- Expected output format: Return the maximum score.
- Key requirements and edge cases to consider: 
    - The score of hopping from index `i` to index `j` is `nums[j] - nums[i]`.
    - You can only hop to an index `j` if `nums[j] > nums[i]`.
    - You can only hop if `j` is within `k` steps from `i`, where `k` is the given step size.
    - You start at index `0`.
- Example test cases with explanations:
    - `nums = [1,2,3,4,5], k = 1` => The maximum score is `4`, achieved by hopping from `0` to `1`, then to `2`, then to `3`, then to `4`.
    - `nums = [1,2,3,4,5], k = 2` => The maximum score is `4`, achieved by hopping from `0` to `2`, then to `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible hops from each index and keep track of the maximum score.
- Step-by-step breakdown of the solution:
    1. Initialize the maximum score to `0`.
    2. For each index `i`, try all possible hops to index `j` within `k` steps.
    3. If `nums[j] > nums[i]`, update the maximum score if the current score plus `nums[j] - nums[i]` is greater than the current maximum score.
    4. Recursively try all possible hops from index `j`.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, INT_MIN);
        dp[0] = nums[0];
        for (int i = 1; i < n; i++) {
            for (int j = max(0, i - k); j < i; j++) {
                if (dp[j] != INT_MIN && nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + nums[i] - nums[j]);
                }
            }
        }
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `nums` and $k$ is the given step size. This is because we try all possible hops from each index.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we use a dynamic programming array to store the maximum score for each index.
> - **Why these complexities occur:** The time complexity occurs because we have a nested loop that tries all possible hops from each index. The space complexity occurs because we use a dynamic programming array to store the maximum score for each index.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a deque to store the indices of the maximum score for each window of size `k`.
- Detailed breakdown of the approach:
    1. Initialize a deque to store the indices of the maximum score for each window of size `k`.
    2. Initialize the maximum score to `0`.
    3. For each index `i`, try all possible hops to index `j` within `k` steps.
    4. If `nums[j] > nums[i]`, update the maximum score if the current score plus `nums[j] - nums[i]` is greater than the current maximum score.
    5. Remove the indices that are out of the window from the deque.
    6. Add the current index to the deque if it's greater than the last index in the deque.
- Proof of optimality: This approach is optimal because it only tries the indices that are within the window of size `k` and have a greater score than the current index.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        deque<int> q;
        dp[0] = nums[0];
        q.push_back(0);
        for (int i = 1; i < n; i++) {
            if (!q.empty() && q.front() < i - k) q.pop_front();
            dp[i] = dp[q.front()] + nums[i];
            while (!q.empty() && dp[i] >= dp[q.back()]) q.pop_back();
            q.push_back(i);
        }
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we only try the indices that are within the window of size `k` and have a greater score than the current index.
> - **Space Complexity:** $O(n)$, where $n` is the length of `nums`. This is because we use a deque to store the indices of the maximum score for each window of size `k`.
> - **Optimality proof:** This approach is optimal because it only tries the indices that are within the window of size `k` and have a greater score than the current index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, deque.
- Problem-solving patterns identified: Using a deque to store the indices of the maximum score for each window.
- Optimization techniques learned: Removing the indices that are out of the window from the deque.
- Similar problems to practice: Maximum subarray, longest increasing subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not removing the indices that are out of the window from the deque.
- Edge cases to watch for: When `k` is greater than `n`.
- Performance pitfalls: Not using a deque to store the indices of the maximum score for each window.
- Testing considerations: Test the function with different values of `k` and `nums`.