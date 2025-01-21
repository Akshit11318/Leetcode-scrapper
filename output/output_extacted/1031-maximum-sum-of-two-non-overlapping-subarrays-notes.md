## Maximum Sum of Two Non-Overlapping Subarrays
**Problem Link:** https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description

**Problem Statement:**
- Given an array `nums` and two integers `firstLen` and `secondLen`, find the maximum sum of two non-overlapping subarrays of lengths `firstLen` and `secondLen` respectively.
- The subarrays should not overlap, meaning that no element in `nums` should be part of both subarrays.
- The function should return the maximum sum of these two subarrays.

**Input Format and Constraints:**
- `nums` is a list of integers.
- `firstLen` and `secondLen` are integers representing the lengths of the two subarrays.
- The lengths of `nums`, `firstLen`, and `secondLen` are all positive integers.
- The maximum length of `nums` is 1000.

**Expected Output Format:**
- The maximum sum of two non-overlapping subarrays of lengths `firstLen` and `secondLen`.

**Key Requirements and Edge Cases:**
- Handle cases where `firstLen` or `secondLen` is greater than the length of `nums`.
- Consider scenarios where the maximum sum occurs at the beginning or end of `nums`.
- Edge cases include when `firstLen` equals `secondLen`, or when either `firstLen` or `secondLen` equals 1.

**Example Test Cases:**
- For `nums = [0,6,5,2,2,5,1,9,4]`, `firstLen = 1`, and `secondLen = 2`, the output should be `20`.
- For `nums = [3,8,1,3,2,1,8,9,0]`, `firstLen = 3`, and `secondLen = 2`, the output should be `29`.
- For `nums = [2,1,5,6,0,9,5,0,3,8]`, `firstLen = 4`, and `secondLen = 3`, the output should be `31`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking all possible non-overlapping subarrays of lengths `firstLen` and `secondLen`.
- For each pair of non-overlapping subarrays, calculate the sum of their elements and keep track of the maximum sum found.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
    int maxSum = INT_MIN;
    for (int i = 0; i <= nums.size() - firstLen; i++) {
        for (int j = i + firstLen; j <= nums.size() - secondLen; j++) {
            int sum1 = 0, sum2 = 0;
            for (int k = i; k < i + firstLen; k++) sum1 += nums[k];
            for (int k = j; k < j + secondLen; k++) sum2 += nums[k];
            maxSum = max(maxSum, sum1 + sum2);
        }
    }
    for (int i = 0; i <= nums.size() - secondLen; i++) {
        for (int j = i + secondLen; j <= nums.size() - firstLen; j++) {
            int sum1 = 0, sum2 = 0;
            for (int k = i; k < i + secondLen; k++) sum1 += nums[k];
            for (int k = j; k < j + firstLen; k++) sum2 += nums[k];
            maxSum = max(maxSum, sum1 + sum2);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. This is because for each pair of indices $i$ and $j$, we are iterating over `firstLen` and `secondLen` to calculate the sums.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum sum and the current sums.
> - **Why these complexities occur:** The brute force approach involves nested loops to check all possible subarrays, leading to high time complexity. However, it uses minimal extra space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use prefix sums to efficiently calculate the sum of any subarray in $O(1)$ time.
- We then iterate through all possible non-overlapping subarrays, using the prefix sums to calculate their sums in constant time.
- This approach significantly reduces the time complexity.

```cpp
int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    int maxSum = INT_MIN;
    for (int i = 0; i <= n - firstLen; i++) {
        for (int j = i + firstLen; j <= n - secondLen; j++) {
            int sum1 = prefixSum[i + firstLen] - prefixSum[i];
            int sum2 = prefixSum[j + secondLen] - prefixSum[j];
            maxSum = max(maxSum, sum1 + sum2);
        }
    }
    for (int i = 0; i <= n - secondLen; i++) {
        for (int j = i + secondLen; j <= n - firstLen; j++) {
            int sum1 = prefixSum[i + secondLen] - prefixSum[i];
            int sum2 = prefixSum[j + firstLen] - prefixSum[j];
            maxSum = max(maxSum, sum1 + sum2);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we have two nested loops to iterate through all possible subarrays.
> - **Space Complexity:** $O(n)$, for storing the prefix sums.
> - **Optimality proof:** This approach is optimal because it checks all possible non-overlapping subarrays in the most efficient manner possible, using prefix sums to reduce the time complexity of calculating subarray sums.

---

### Final Notes
**Learning Points:**
- The importance of using prefix sums to efficiently calculate subarray sums.
- How to approach problems involving subarrays and their sums.
- The trade-off between time and space complexity.

**Mistakes to Avoid:**
- Not considering edge cases where `firstLen` or `secondLen` is greater than the length of `nums`.
- Failing to optimize the calculation of subarray sums.
- Not checking all possible non-overlapping subarrays.