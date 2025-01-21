## Maximum Subarray Sum with One Deletion

**Problem Link:** https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `2 <= nums.length <= 10^5`, `-10^5 <= nums[i] <= 10^5`.
- Expected output: The maximum sum of a subarray that can be achieved by deleting at most one element.
- Key requirements: The subarray must be contiguous, and at most one element can be deleted.
- Edge cases: Empty array, single-element array, array with all negative numbers.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subarrays and delete each element one by one to see if it increases the sum.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, try deleting each element one by one.
  3. Calculate the sum of the remaining elements after deletion.
  4. Keep track of the maximum sum found.

```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int n = nums.size();
        int maxSum = INT_MIN;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int sum = 0;
                for (int k = i; k <= j; k++) {
                    sum += nums[k];
                }
                maxSum = max(maxSum, sum);
                for (int k = i; k <= j; k++) {
                    int tempSum = sum - nums[k];
                    maxSum = max(maxSum, tempSum);
                }
            }
        }
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops: two for generating subarrays and one for trying each element deletion.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and temporary sums.
> - **Why these complexities occur:** The brute force approach tries all possible subarrays and deletions, leading to an exponential time complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of trying all possible deletions, we can maintain two arrays: one for the maximum sum of a subarray ending at each position, and another for the maximum sum of a subarray ending at each position after deleting one element.
- Detailed breakdown:
  1. Initialize two arrays, `forward` and `backward`, of the same length as the input array.
  2. Fill the `forward` array by iterating through the input array from left to right, keeping track of the maximum sum of a subarray ending at each position.
  3. Fill the `backward` array by iterating through the input array from right to left, keeping track of the maximum sum of a subarray ending at each position.
  4. Calculate the maximum sum of a subarray that can be achieved by deleting at most one element by considering the maximum sum of a subarray ending at each position and the maximum sum of a subarray ending at the previous position after deleting one element.

```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int n = nums.size();
        int forward[n], backward[n];
        int maxSum = nums[0];
        forward[0] = nums[0];
        backward[n - 1] = nums[n - 1];
        
        for (int i = 1; i < n; i++) {
            forward[i] = max(nums[i], forward[i - 1] + nums[i]);
            maxSum = max(maxSum, forward[i]);
        }
        
        for (int i = n - 2; i >= 0; i--) {
            backward[i] = max(nums[i], backward[i + 1] + nums[i]);
        }
        
        for (int i = 1; i < n - 1; i++) {
            maxSum = max(maxSum, forward[i - 1] + backward[i + 1]);
        }
        
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make two passes through the input array to fill the `forward` and `backward` arrays.
> - **Space Complexity:** $O(n)$, as we use two arrays of the same length as the input array to store the maximum sums.
> - **Optimality proof:** This approach is optimal because we only need to consider the maximum sum of a subarray ending at each position and the maximum sum of a subarray ending at the previous position after deleting one element, which can be done in linear time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, Kadane's algorithm for maximum subarray sum.
- Problem-solving patterns: Breaking down the problem into smaller subproblems, using arrays to store intermediate results.
- Optimization techniques: Avoiding redundant calculations, using two passes to fill the `forward` and `backward` arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `forward` and `backward` arrays correctly, not considering the maximum sum of a subarray ending at the previous position after deleting one element.
- Edge cases: Not handling the case where the input array has only one element, not considering the maximum sum of a subarray that can be achieved by deleting no elements.