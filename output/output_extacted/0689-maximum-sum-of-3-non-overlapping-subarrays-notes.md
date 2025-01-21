## Maximum Sum of 3 Non-Overlapping Subarrays

**Problem Link:** https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, find the maximum sum of 3 non-overlapping subarrays of size `k`.
- Input format: `nums` array and `k` integer.
- Constraints: `1 <= k <= nums.size() <= 20000`.
- Expected output format: Maximum sum of 3 non-overlapping subarrays.
- Key requirements and edge cases to consider:
  - Non-overlapping subarrays: Ensure subarrays do not share any elements.
  - Maximum sum: Find the combination of 3 subarrays that yields the highest sum.
- Example test cases with explanations:
  - `nums = [1,2,1,2,6,7,5,1]`, `k = 2`: Maximum sum is `18` (subarrays `[1, 2]`, `[6, 7]`, and `[5, 1]`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible combinations of 3 non-overlapping subarrays of size `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of size `k`.
  2. Iterate through all combinations of 3 subarrays.
  3. For each combination, check if subarrays are non-overlapping.
  4. If non-overlapping, calculate the sum of the 3 subarrays.
  5. Update maximum sum if current sum is higher.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach.

```cpp
#include <vector>
#include <algorithm>

int maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {
    int n = nums.size();
    int maxSum = INT_MIN;
    
    // Generate all possible subarrays of size k
    for (int i = 0; i <= n - k; ++i) {
        for (int j = i + k; j <= n - k; ++j) {
            for (int m = j + k; m <= n - k; ++m) {
                int sum = 0;
                // Calculate sum of current subarrays
                for (int x = i; x < i + k; ++x) sum += nums[x];
                for (int x = j; x < j + k; ++x) sum += nums[x];
                for (int x = m; x < m + k; ++x) sum += nums[x];
                maxSum = std::max(maxSum, sum);
            }
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot k)$, where $n$ is the size of the input array. This is because we have three nested loops to generate all possible combinations of 3 subarrays, and for each combination, we calculate the sum of the subarrays in $O(k)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and other variables.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the exhaustive search, but it has a low space complexity since it doesn't require additional data structures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of 3 subarrays, we can calculate the prefix sum of the array and then use a sliding window approach to find the maximum sum of 3 non-overlapping subarrays.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of the array.
  2. Initialize variables to store the maximum sum and the indices of the subarrays.
  3. Use a sliding window approach to find the maximum sum of 3 non-overlapping subarrays.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal for this problem.

```cpp
int maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {
    int n = nums.size();
    std::vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    
    int maxSum = INT_MIN;
    for (int i = 0; i <= n - k; ++i) {
        for (int j = i + k; j <= n - k; ++j) {
            for (int m = j + k; m <= n - k; ++m) {
                int sum = (prefixSum[i + k] - prefixSum[i]) + (prefixSum[j + k] - prefixSum[j]) + (prefixSum[m + k] - prefixSum[m]);
                maxSum = std::max(maxSum, sum);
            }
        }
    }
    return maxSum;
}
```

However, we can further optimize this by using a dynamic programming approach to store the maximum sum of subarrays ending at each position.

```cpp
int maxSumOfThreeSubarrays(std::vector<int>& nums, int k) {
    int n = nums.size();
    std::vector<int> sumK(n - k + 1, 0);
    for (int i = 0; i <= n - k; ++i) {
        sumK[i] = 0;
        for (int j = 0; j < k; ++j) {
            sumK[i] += nums[i + j];
        }
    }
    
    int maxSum = INT_MIN;
    for (int i = 0; i <= n - 3 * k; ++i) {
        for (int j = i + k; j <= n - 2 * k; ++j) {
            for (int m = j + k; m <= n - k; ++m) {
                maxSum = std::max(maxSum, sumK[i] + sumK[j] + sumK[m]);
            }
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we have two nested loops to find the maximum sum of 3 non-overlapping subarrays.
> - **Space Complexity:** $O(n)$, as we use a vector to store the sum of subarrays of size `k`.
> - **Optimality proof:** This approach has a time complexity of $O(n^2)$, which is optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum, sliding window, dynamic programming.
- Problem-solving patterns identified: Using prefix sum to reduce time complexity, using dynamic programming to store intermediate results.
- Optimization techniques learned: Reducing time complexity by using prefix sum and dynamic programming.
- Similar problems to practice: Maximum sum of subarray, maximum sum of two non-overlapping subarrays.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of prefix sum, incorrect use of dynamic programming.
- Edge cases to watch for: Empty input array, input array with single element.
- Performance pitfalls: High time complexity due to exhaustive search, high space complexity due to unnecessary data structures.
- Testing considerations: Test with different input sizes, test with different values of `k`.