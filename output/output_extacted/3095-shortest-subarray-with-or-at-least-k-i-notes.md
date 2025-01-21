## Shortest Subarray with Sum at Least K
**Problem Link:** https://leetcode.com/problems/shortest-subarray-with-or-at-least-k/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `-10^5 <= nums[i] <= 10^5`, and `1 <= k <= 10^9`.
- Expected output format: The length of the shortest subarray with a sum of at least `k`, or `-1` if no such subarray exists.
- Key requirements and edge cases to consider: Handling negative numbers, zero, and the case where no such subarray exists.
- Example test cases with explanations:
  - `nums = [1], k = 1`, the output should be `1`.
  - `nums = [1,2], k = 4`, the output should be `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible subarrays and check if their sum is at least `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, calculate its sum.
  3. If the sum is at least `k`, update the minimum length found so far.
- Why this approach comes to mind first: It's straightforward and ensures we consider all possibilities.

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        int minLen = INT_MAX;
        
        // Generate all possible subarrays
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int sum = 0;
                // Calculate the sum of the current subarray
                for (int m = i; m <= j; m++) {
                    sum += nums[m];
                }
                // Check if the sum is at least k
                if (sum >= k) {
                    // Update the minimum length
                    minLen = min(minLen, j - i + 1);
                }
            }
        }
        
        // Return -1 if no such subarray exists, otherwise return the minimum length
        return minLen == INT_MAX ? -1 : minLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because we have three nested loops: two for generating subarrays and one for calculating the sum of each subarray.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store variables like `minLen` and `sum`.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves generating and summing all possible subarrays, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a prefix sum array to efficiently calculate the sum of any subarray in constant time. Then, utilize a deque to keep track of the indices of the prefix sum array that could potentially form the shortest subarray with a sum of at least `k`.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array `preSum` of `nums`.
  2. Initialize a deque `d` to store indices of `preSum`.
  3. Iterate over `preSum`. For each index `i`, remove indices from the front of `d` that are no longer valid (i.e., their corresponding prefix sum values are less than `preSum[i] - k`).
  4. If the deque is not empty and `preSum[i] - preSum[d.front()] >= k`, update the minimum length.
  5. Push `i` to the back of `d`.
- Proof of optimality: This approach ensures we consider all possible subarrays in linear time by using the prefix sum array and the deque to efficiently track and update potential subarrays.

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> preSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        
        int minLen = INT_MAX;
        deque<int> d;
        for (int i = 0; i <= n; i++) {
            // Remove indices from the front of d that are no longer valid
            while (!d.empty() && preSum[i] - preSum[d.front()] >= k) {
                minLen = min(minLen, i - d.front());
                d.pop_front();
            }
            // Remove indices from the back of d that are larger than i
            while (!d.empty() && preSum[i] <= preSum[d.back()]) {
                d.pop_back();
            }
            d.push_back(i);
        }
        
        return minLen == INT_MAX ? -1 : minLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we perform a constant amount of work for each element in `nums`.
> - **Space Complexity:** $O(n)$, for storing the prefix sum array and the deque.
> - **Optimality proof:** This approach is optimal because it considers all possible subarrays in linear time, which is the best we can achieve given the need to examine each element at least once.