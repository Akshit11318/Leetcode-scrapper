## Shortest Subarray with Sum at Least K
**Problem Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description

**Problem Statement:**
- Input format: Given an integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `-10^5 <= nums[i] <= 10^5`, `1 <= k <= 10^5`.
- Expected output format: The length of the shortest subarray whose sum is at least `k`, or `-1` if no such subarray exists.
- Key requirements and edge cases to consider: Handling arrays with negative numbers, zero, and positive numbers, as well as arrays with large sums.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1], k = 1`, Output: `1`. Explanation: The only subarray is `[1]` and its sum is `1`, which is equal to `k`.
  - Example 2: Input: `nums = [1,2], k = 4`, Output: `-1`. Explanation: There is no subarray with a sum of at least `4`.
  - Example 3: Input: `nums = [2,-1,2], k = 3`, Output: `3`. Explanation: The subarray `[2,-1,2]` has a sum of `3`, which is equal to `k`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the shortest subarray with a sum of at least `k`, we can check all possible subarrays and calculate their sums.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible start indices for the subarray.
  2. For each start index, iterate over all possible end indices.
  3. Calculate the sum of the subarray from the start index to the end index.
  4. Check if the sum is at least `k`.
  5. If it is, update the minimum length of the subarray.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible subarrays.

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        int min_length = INT_MAX;
        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                int sum = 0;
                for (int i = start; i <= end; i++) {
                    sum += nums[i];
                }
                if (sum >= k) {
                    min_length = min(min_length, end - start + 1);
                }
            }
        }
        return min_length == INT_MAX ? -1 : min_length;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops: two for iterating over the start and end indices of the subarray, and one for calculating the sum of the subarray.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum length and the sum of the subarray.
> - **Why these complexities occur:** The time complexity is cubic because we are checking all possible subarrays, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to calculate the sum of any subarray in constant time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array `prefix_sum` where `prefix_sum[i]` is the sum of the first `i` elements of the input array.
  2. Initialize a deque `dq` to store the indices of the prefix sum array.
  3. Iterate over the prefix sum array, and for each element, remove all elements from the front of the deque that are greater than the current element.
  4. For each element, check if the difference between the current element and the element at the front of the deque is at least `k`.
  5. If it is, update the minimum length of the subarray.
- Why further optimization is impossible: We are using a prefix sum array to calculate the sum of any subarray in constant time, and a deque to keep track of the indices of the prefix sum array. This is the most efficient way to solve the problem.

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefix_sum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix_sum[i + 1] = prefix_sum[i] + nums[i];
        }
        int min_length = INT_MAX;
        deque<int> dq;
        for (int i = 0; i <= n; i++) {
            while (!dq.empty() && prefix_sum[i] - prefix_sum[dq.front()] >= k) {
                min_length = min(min_length, i - dq.front());
                dq.pop_front();
            }
            while (!dq.empty() && prefix_sum[i] <= prefix_sum[dq.back()]) {
                dq.pop_back();
            }
            dq.push_back(i);
        }
        return min_length == INT_MAX ? -1 : min_length;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are iterating over the prefix sum array once, and using a deque to keep track of the indices.
> - **Space Complexity:** $O(n)$, as we are using a prefix sum array and a deque to store the indices.
> - **Optimality proof:** We are using a prefix sum array to calculate the sum of any subarray in constant time, and a deque to keep track of the indices of the prefix sum array. This is the most efficient way to solve the problem, as we are only iterating over the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum array, deque.
- Problem-solving patterns identified: Using a prefix sum array to calculate the sum of any subarray in constant time, using a deque to keep track of the indices of the prefix sum array.
- Optimization techniques learned: Using a prefix sum array to avoid recalculating the sum of subarrays, using a deque to keep track of the indices of the prefix sum array.
- Similar problems to practice: Shortest Subarray with Sum at Least K, Minimum Window Substring.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the prefix sum array correctly, not handling edge cases correctly.
- Edge cases to watch for: Empty input array, input array with negative numbers, input array with large sums.
- Performance pitfalls: Not using a prefix sum array, not using a deque to keep track of the indices of the prefix sum array.
- Testing considerations: Test the solution with different input arrays, including empty arrays, arrays with negative numbers, and arrays with large sums.