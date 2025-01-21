## Maximum Array Hopping Score II

**Problem Link:** https://leetcode.com/problems/maximum-array-hopping-score-ii/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, we can perform the following operations:
  - We can start at any index in the array.
  - We can hop to any index that is within `k` steps of the current index.
- The goal is to find the maximum score we can achieve by hopping through the array, where the score at each index is the value at that index.
- The input array `nums` has a length of at least 1 and at most $10^5$, and the integer `k` is between 1 and $10^5$.
- Expected output: The maximum score we can achieve.

**Example Test Cases:**
- For `nums = [1, -1, -2, 4, -7, 3]` and `k = 2`, the maximum score is 7.
- For `nums = [10, -5, -2, 4, 0, 3]` and `k = 3`, the maximum score is 17.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible hop sequences and keep track of the maximum score.
- We start at each index and explore all possible hops within `k` steps.
- We use a recursive function to explore all possible hop sequences.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        int max_score = INT_MIN;
        vector<int> memo(n, -1);
        
        function<int(int)> dfs = [&](int i) {
            if (i == n - 1) return nums[i];
            if (memo[i] != -1) return memo[i];
            int score = INT_MIN;
            for (int j = 1; j <= k; j++) {
                if (i + j < n) {
                    score = max(score, nums[i] + dfs(i + j));
                }
            }
            memo[i] = score;
            return score;
        };
        
        for (int i = 0; i < n; i++) {
            max_score = max(max_score, dfs(i));
        }
        
        return max_score;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the input array and $k$ is the hop size. This is because we are exploring all possible hop sequences.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are using a memoization array to store the maximum score at each index.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it involves exploring all possible hop sequences, which can be very large.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a deque to keep track of the indices with the maximum score.
- We start by initializing a deque with the first index.
- We then iterate through the array, and for each index, we remove the indices that are out of the hop range from the front of the deque.
- We also remove the indices that have a lower score than the current index from the back of the deque.
- We add the current index to the back of the deque.
- Finally, we return the score at the last index in the deque.

```cpp
class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> dq;
        vector<int> dp(n);
        
        dq.push_back(0);
        dp[0] = nums[0];
        
        for (int i = 1; i < n; i++) {
            if (dq.front() < i - k) dq.pop_front();
            int max_score = dp[dq.front()];
            dp[i] = max_score + nums[i];
            while (!dq.empty() && dp[dq.back()] < dp[i]) dq.pop_back();
            dq.push_back(i);
        }
        
        return dp[n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are using a deque and a dynamic programming array to store the maximum score at each index.
> - **Optimality proof:** The optimal approach has a linear time complexity because we are iterating through the array once and using a deque to keep track of the indices with the maximum score. This is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, deque, and memoization.
- Problem-solving patterns identified: using a deque to keep track of the indices with the maximum score, and using dynamic programming to store the maximum score at each index.
- Optimization techniques learned: using a deque to reduce the time complexity, and using dynamic programming to avoid redundant calculations.
- Similar problems to practice: other problems involving dynamic programming and deque.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using memoization, and not using a deque to keep track of the indices with the maximum score.
- Edge cases to watch for: handling the case where the input array is empty, and handling the case where the hop size is larger than the length of the input array.
- Performance pitfalls: not using dynamic programming, and not using a deque to reduce the time complexity.
- Testing considerations: testing the function with different input arrays and hop sizes, and testing the function with edge cases.