## Maximum Sum Circular Subarray
**Problem Link:** https://leetcode.com/problems/maximum-sum-circular-subarray/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^3`, `-10^5 <= nums[i] <= 10^5`.
- Expected Output: The maximum sum of a contiguous subarray within the given array, considering the array can be treated as circular (i.e., the last element can be connected to the first element).
- Key Requirements:
  - The subarray must be non-empty.
  - The array can be empty.
- Edge Cases:
  - Single element array.
  - All negative numbers.
  - All positive numbers.
- Example Test Cases:
  - `[1, -2, 3, -2]`: Expected output is `3`.
  - `[5, -3, 5]`: Expected output is `10`.
  - `[-3, -2, -1]`: Expected output is `-1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subarray within the given array, including the circular subarrays.
- Step-by-step breakdown:
  1. Iterate over the array to consider each element as a starting point.
  2. For each starting point, iterate over the rest of the array (including wrapping around to the beginning for circular consideration) to consider all possible ending points.
  3. Calculate the sum of each subarray and keep track of the maximum sum found.
- This approach comes to mind first because it directly addresses the problem by exhaustively considering all possibilities.

```cpp
int maxSubarraySumCircular(vector<int>& nums) {
    int maxSum = INT_MIN;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        int currentSum = 0;
        for (int j = i; j < 2 * n - 1; ++j) {
            currentSum += nums[j % n];
            if (j - i + 1 <= n) { // Only consider subarrays not exceeding array length
                maxSum = max(maxSum, currentSum);
            }
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially iterate over the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space to store variables like `maxSum`, `n`, `i`, `j`, and `currentSum`.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the minimal use of extra space results in constant space complexity.

---

### Optimal Approach
**Explanation:**
- The key insight is to use Kadane's algorithm for finding the maximum sum of a subarray within a linear array, and then apply a similar approach for the circular case.
- Detailed breakdown:
  1. Calculate the total sum of the array.
  2. Use Kadane's algorithm to find the maximum sum of a subarray.
  3. Use a modified version of Kadane's algorithm to find the minimum sum of a subarray (since the minimum subarray sum can contribute to the maximum circular sum by being excluded).
  4. The maximum circular sum is either the maximum linear sum or the total sum minus the minimum linear sum.
- Proof of optimality:
  - This approach covers all possible subarrays (both linear and circular) in linear time.
  - It correctly identifies the maximum sum by considering both the maximum sum of a linear subarray and the maximum sum achievable by wrapping around the array.

```cpp
int maxSubarraySumCircular(vector<int>& nums) {
    int totalSum = 0;
    int maxKadane = nums[0];
    int minKadane = nums[0];
    int currentMax = nums[0];
    int currentMin = nums[0];
    
    for (int i = 0; i < nums.size(); ++i) {
        totalSum += nums[i];
        currentMax = max(nums[i], currentMax + nums[i]);
        maxKadane = max(maxKadane, currentMax);
        currentMin = min(nums[i], currentMin + nums[i]);
        minKadane = min(minKadane, currentMin);
    }
    
    if (totalSum == minKadane) {
        return maxKadane; // All numbers are negative
    } else {
        return max(maxKadane, totalSum - minKadane);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we only need to make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store variables like `totalSum`, `maxKadane`, `minKadane`, `currentMax`, and `currentMin`.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem by using Kadane's algorithm, which is known for its efficiency in finding maximum subarray sums.

---

### Final Notes
**Learning Points:**
- **Kadane's Algorithm:** A powerful tool for finding the maximum sum of a subarray within a linear array.
- **Circular Array Consideration:** How to extend linear array algorithms to handle circular cases by considering the total sum and the minimum subarray sum.
- **Optimization Techniques:** The importance of understanding the problem fully before diving into optimizations.

**Mistakes to Avoid:**
- Not considering the circular nature of the array.
- Failing to handle edge cases like all negative numbers or a single-element array.
- Not optimizing the solution to achieve linear time complexity.