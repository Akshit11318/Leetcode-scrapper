## Jump Game VI
**Problem Link:** https://leetcode.com/problems/jump-game-vi/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`, `1 <= k <= nums.length`.
- Expected Output: The maximum score that can be achieved.
- Key Requirements: The score is calculated by summing the elements at the current index and the previous `k` indices.
- Edge Cases: If the current index is less than `k`, the score is the sum of all elements up to the current index.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the score at each index by summing the current element and the previous `k` elements.
- We then keep track of the maximum score achieved so far.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n);
        dp[0] = nums[0];
        
        for (int i = 1; i < n; i++) {
            dp[i] = nums[i];
            for (int j = 1; j <= k && i - j >= 0; j++) {
                dp[i] = max(dp[i], dp[i - j] + nums[i]);
            }
        }
        
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the input array and $k$ is the number of previous indices to consider.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Why these complexities occur:** The brute force approach involves iterating over the input array and for each index, iterating over the previous `k` indices to calculate the score.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a deque to keep track of the indices of the maximum scores.
- We use a deque to store the indices of the maximum scores in the last `k` indices.
- We iterate over the input array, and for each index, we remove the indices that are out of the last `k` indices from the deque.
- We then add the current index to the deque if the current score is greater than the score at the last index in the deque.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> dq;
        vector<int> dp(n);
        
        for (int i = 0; i < n; i++) {
            if (!dq.empty() && dq.front() < i - k) {
                dq.pop_front();
            }
            if (!dq.empty()) {
                dp[i] = dp[dq.front()] + nums[i];
            } else {
                dp[i] = nums[i];
            }
            while (!dq.empty() && dp[dq.back()] <= dp[i]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Optimality proof:** The optimal approach involves using a deque to keep track of the indices of the maximum scores, which reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a deque to keep track of the indices of the maximum scores.
- The problem-solving pattern identified is the use of dynamic programming to solve the problem.
- The optimization technique learned is the use of a deque to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that involves iterating over the previous `k` indices for each index.
- An edge case to watch for is when the current index is less than `k`, in which case the score is the sum of all elements up to the current index.
- A performance pitfall is to use a naive approach that involves iterating over the input array multiple times.