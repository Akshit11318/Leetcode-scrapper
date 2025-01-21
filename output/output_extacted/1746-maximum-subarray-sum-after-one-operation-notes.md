## Maximum Subarray Sum After One Operation

**Problem Link:** https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/description

**Problem Statement:**
- Input format: You are given an array of integers `nums` and an integer `k`.
- Constraints: The array `nums` has at least one element and at most $10^5$ elements. Each element in `nums` is an integer in the range $[-10^9, 10^9]$. The integer `k` is in the range $[1, 10^5]$.
- Expected output format: Return the maximum possible sum of a subarray after performing the given operation.
- Key requirements and edge cases to consider:
  - The operation can be either adding `k` to each element in a subarray or multiplying each element in a subarray by `k`.
  - The subarray must be non-empty.
  - Example test cases with explanations:
    - For `nums = [1, -2, 0, 3]` and `k = 5`, the maximum sum after one operation is $5 + 5 + 5 + 3 = 18$, achieved by adding `k` to each element in the subarray `[1, -2, 0, 3]`.
    - For `nums = [-1, 0, 1]` and `k = 1`, the maximum sum after one operation is $1 + 0 + 1 = 2$, achieved by multiplying each element in the subarray `[-1, 0, 1]` by `k`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible subarray, calculate the sum after adding `k` to each element and the sum after multiplying each element by `k`. Compare these sums to find the maximum.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of the input array `nums`.
  2. For each subarray, calculate the sum after adding `k` to each element.
  3. For each subarray, calculate the sum after multiplying each element by `k`.
  4. Keep track of the maximum sum found among all subarrays and operations.
- Why this approach comes to mind first: It is straightforward and considers all possible scenarios, but it is inefficient due to its high time complexity.

```cpp
int maximumSum(vector<int>& nums, int k) {
    int n = nums.size();
    int maxSum = INT_MIN;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sumAdd = 0, sumMul = 0;
            for (int l = i; l <= j; l++) {
                sumAdd += nums[l] + k;
                sumMul += nums[l] * k;
            }
            maxSum = max(maxSum, sumAdd);
            maxSum = max(maxSum, sumMul);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`, because we have three nested loops iterating over the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum sum and temporary sums.
> - **Why these complexities occur:** The brute force approach is inefficient due to its exhaustive examination of all possible subarrays and operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of examining all possible subarrays, we can use a prefix sum array to efficiently calculate the sum of any subarray. Additionally, we can use Kadane's algorithm to find the maximum subarray sum in linear time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array for `nums`.
  2. Use Kadane's algorithm to find the maximum subarray sum for `nums`.
  3. Use Kadane's algorithm to find the maximum subarray sum for `nums` with each element multiplied by `k`.
  4. Use Kadane's algorithm to find the maximum subarray sum for `nums` with each element added by `k`.
  5. Compare the maximum sums found in steps 2-4 to determine the overall maximum sum.
- Proof of optimality: This approach is optimal because it reduces the time complexity to linear, making it much more efficient than the brute force approach for large inputs.

```cpp
int maximumSum(vector<int>& nums, int k) {
    int n = nums.size();
    int maxSum = INT_MIN;
    
    // Maximum subarray sum without operation
    int sum = 0, maxSubarraySum = INT_MIN;
    for (int num : nums) {
        sum = max(num, sum + num);
        maxSubarraySum = max(maxSubarraySum, sum);
    }
    maxSum = max(maxSum, maxSubarraySum);
    
    // Maximum subarray sum after multiplying by k
    sum = 0; maxSubarraySum = INT_MIN;
    for (int num : nums) {
        sum = max(num * k, sum + num * k);
        maxSubarraySum = max(maxSubarraySum, sum);
    }
    maxSum = max(maxSum, maxSubarraySum);
    
    // Maximum subarray sum after adding k
    sum = 0; maxSubarraySum = INT_MIN;
    for (int num : nums) {
        sum = max(num + k, sum + num + k);
        maxSubarraySum = max(maxSubarraySum, sum);
    }
    maxSum = max(maxSum, maxSubarraySum);
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we perform a constant number of linear scans over the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum sum and temporary sums.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best possible time complexity for this problem since we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Kadane's algorithm for finding the maximum subarray sum, prefix sum arrays for efficient calculation of subarray sums.
- Problem-solving patterns identified: Using a prefix sum array to reduce the time complexity of calculating subarray sums, applying Kadane's algorithm to find the maximum subarray sum in linear time.
- Optimization techniques learned: Reducing the time complexity from cubic to linear by using more efficient algorithms and data structures.
- Similar problems to practice: Finding the maximum subarray sum with other operations (e.g., subtraction, division), finding the minimum subarray sum, finding the maximum subarray sum in a circular array.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing Kadane's algorithm, forgetting to handle edge cases (e.g., an empty input array).
- Edge cases to watch for: An empty input array, an input array with a single element, an input array with all negative elements.
- Performance pitfalls: Using an inefficient algorithm with a high time complexity, failing to optimize the solution for large inputs.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large inputs.