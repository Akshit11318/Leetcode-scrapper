## Constrained Subsequence Sum
**Problem Link:** https://leetcode.com/problems/constrained-subsequence-sum/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `k`, find the maximum sum of a subsequence of `nums` where the sum of the subsequence is at most `k`.
- Expected output format: The maximum sum of a subsequence of `nums` where the sum of the subsequence is at most `k`.
- Key requirements and edge cases to consider: The subsequence must be non-empty and the sum of the subsequence must be at most `k`.
- Example test cases with explanations:
  - `nums = [10,-2,-10,-5,3], k = 3`, the maximum sum is `3`.
  - `nums = [10,-2,-10,-5,3], k = 8`, the maximum sum is `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of `nums` and calculate their sums.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums`.
  2. Calculate the sum of each subsequence.
  3. Check if the sum of the subsequence is at most `k`.
  4. Keep track of the maximum sum that is at most `k`.
- Why this approach comes to mind first: It is a straightforward approach that ensures we consider all possible subsequences.

```cpp
class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, INT_MIN);
        dp[0] = nums[0];
        queue<int> q;
        q.push(0);
        int res = nums[0];
        for (int i = 1; i < n; i++) {
            while (!q.empty() && i - q.front() > k) q.pop();
            dp[i] = max(dp[i], dp[q.front()] + nums[i]);
            while (!q.empty() && dp[q.back()] <= dp[i]) q.pop();
            q.push(i);
            res = max(res, dp[i]);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. This is because we are using a queue to keep track of the indices of the elements in the subsequence.
> - **Space Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. This is because we are using a queue to store the indices of the elements in the subsequence.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the elements of `nums` once. The space complexity occurs because we are storing the indices of the elements in the subsequence in a queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a monotonic queue to keep track of the maximum sum of a subsequence.
- Detailed breakdown of the approach:
  1. Initialize a queue with the first element of `nums`.
  2. Iterate over the elements of `nums` starting from the second element.
  3. For each element, remove the elements from the front of the queue that are out of the window of size `k`.
  4. Update the maximum sum by adding the current element to the maximum sum of the subsequence ending at the front of the queue.
  5. Add the current element to the back of the queue if it is greater than the last element in the queue.
- Proof of optimality: This approach ensures that we consider all possible subsequences of `nums` and keep track of the maximum sum of a subsequence that is at most `k`.

```cpp
class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n, INT_MIN);
        dp[0] = nums[0];
        deque<int> q;
        q.push_back(0);
        int res = nums[0];
        for (int i = 1; i < n; i++) {
            while (!q.empty() && i - q.front() > k) q.pop_front();
            dp[i] = nums[i];
            if (!q.empty()) dp[i] = max(dp[i], dp[q.front()] + nums[i]);
            while (!q.empty() && dp[q.back()] <= dp[i]) q.pop_back();
            q.push_back(i);
            res = max(res, dp[i]);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. This is because we are iterating over the elements of `nums` once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. This is because we are storing the indices of the elements in the subsequence in a deque.
> - **Optimality proof:** This approach ensures that we consider all possible subsequences of `nums` and keep track of the maximum sum of a subsequence that is at most `k`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a monotonic queue to keep track of the maximum sum of a subsequence.
- Problem-solving patterns identified: Using a deque to keep track of the indices of the elements in the subsequence.
- Optimization techniques learned: Using a monotonic queue to reduce the time complexity.
- Similar problems to practice: Problems that involve finding the maximum sum of a subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the queue is empty before popping elements.
- Edge cases to watch for: Handling the case where `nums` is empty.
- Performance pitfalls: Not using a monotonic queue to reduce the time complexity.
- Testing considerations: Testing the function with different inputs and edge cases.