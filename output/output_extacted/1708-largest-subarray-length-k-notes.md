## Largest Subarray Length K
**Problem Link:** https://leetcode.com/problems/largest-subarray-length-k/description

**Problem Statement:**
- Input format: An array of integers `arr` and an integer `k`.
- Constraints: The length of the array is `n`, where `1 <= n <= 10^5`, and `1 <= k <= n`.
- Expected output format: The maximum length of a subarray with a sum of `k`.
- Key requirements and edge cases to consider:
  - Handling arrays with negative numbers.
  - Dealing with `k` being larger than the sum of all elements in the array.
- Example test cases with explanations:
  - Input: `arr = [1,4,2,10,2,3,1,0,20], k = 33`, Output: `5`.
  - Input: `arr = [1,-1,1], k = 1`, Output: `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to consider all possible subarrays and calculate their sums.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible start indices of subarrays.
  2. For each start index, iterate over all possible end indices.
  3. Calculate the sum of the subarray from the start index to the end index.
  4. Check if the sum equals `k`. If it does, update the maximum length of such a subarray.
- Why this approach comes to mind first: It's the most intuitive method, ensuring we don't miss any potential subarrays that sum up to `k`.

```cpp
#include <vector>
#include <algorithm>

int largestSubarrayLengthK(std::vector<int>& arr, int k) {
    int n = arr.size();
    int maxLength = 0;
    for (int start = 0; start < n; ++start) {
        for (int end = start; end < n; ++end) {
            int sum = 0;
            for (int i = start; i <= end; ++i) {
                sum += arr[i];
            }
            if (sum == k) {
                maxLength = std::max(maxLength, end - start + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because we have three nested loops: one for the start index, one for the end index, and one for calculating the sum of the subarray.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of checking every possible subarray, while the space complexity is low because we only use a constant amount of space to store variables like `start`, `end`, and `sum`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to efficiently calculate the sum of any subarray in $O(1)$ time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array `prefixSum` where `prefixSum[i]` is the sum of the first `i` elements in the array.
  2. Iterate over all possible start indices of subarrays.
  3. For each start index, use the prefix sum array to calculate the sum of the subarray from the start index to the current end index in $O(1)$ time.
  4. Check if this sum equals `k`. If it does, update the maximum length of such a subarray.
- Proof of optimality: This approach reduces the time complexity to $O(n^2)$, which is the best we can achieve for this problem since we must consider all possible subarrays.

```cpp
#include <vector>
#include <algorithm>

int largestSubarrayLengthK(std::vector<int>& arr, int k) {
    int n = arr.size();
    std::vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        prefixSum[i + 1] = prefixSum[i] + arr[i];
    }
    int maxLength = 0;
    for (int start = 0; start < n; ++start) {
        for (int end = start; end < n; ++end) {
            int sum = prefixSum[end + 1] - prefixSum[start];
            if (sum == k) {
                maxLength = std::max(maxLength, end - start + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have two nested loops: one for the start index and one for the end index.
> - **Space Complexity:** $O(n)$, for storing the prefix sum array.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to calculate the sums of all subarrays, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays, optimization of brute force algorithms.
- Problem-solving patterns identified: Using prefix sums to reduce calculation time for subarray sums.
- Optimization techniques learned: Reducing nested loop operations by precalculating sums.
- Similar problems to practice: Other problems involving subarray sums or prefix sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating prefix sums or subarray sums.
- Edge cases to watch for: Handling arrays with negative numbers or when `k` is larger than the sum of all elements.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Thoroughly testing with various inputs, including edge cases.