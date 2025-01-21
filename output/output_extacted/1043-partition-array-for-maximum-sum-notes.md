## Partition Array for Maximum Sum
**Problem Link:** https://leetcode.com/problems/partition-array-for-maximum-sum/description

**Problem Statement:**
- Input: An array of integers `arr` and an integer `k`.
- Constraints: `1 <= k <= arr.length <= 500`, `0 <= arr[i] <= 10^6`.
- Expected Output: The maximum sum that can be obtained by partitioning `arr` into `k` non-empty subarrays and taking the maximum sum of each subarray.
- Key Requirements:
  - The array must be partitioned into exactly `k` subarrays.
  - Each subarray must be non-empty.
- Edge Cases:
  - When `k` equals the length of `arr`, the maximum sum is the sum of all elements in `arr`.
  - When `k` equals 1, the maximum sum is the maximum sum of `arr`.

Example Test Cases:
- Input: `arr = [1,15,7,9,2,5,10], k = 3`
  - Output: `84`
  - Explanation: Divide the array into subarrays `[1,15,7]`, `[9,2]`, and `[5,10]`. The maximum sum of each subarray is `23`, `11`, and `15` respectively, and the sum of these maximum sums is `23 + 11 + 15 = 49`.
- Input: `arr = [1,4,1,5,7,3,6,1,9,5], k = 4`
  - Output: `83`
  - Explanation: Divide the array into subarrays `[1,4,1]`, `[5,7,3]`, `[6,1]`, and `[9,5]`. The maximum sum of each subarray is `6`, `15`, `7`, and `14` respectively, and the sum of these maximum sums is `6 + 15 + 7 + 14 = 42`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible partitions of the array into `k` subarrays and calculate the sum of the maximum of each subarray.
- This approach involves using recursion or backtracking to generate all possible partitions and then calculating the sum for each partition.
- This approach comes to mind first because it directly addresses the problem statement without requiring any optimization or insight.

```cpp
#include <vector>
#include <algorithm>

int maxSumAfterPartitioning(vector<int>& arr, int k) {
    int n = arr.size();
    int maxSum = 0;
    vector<int> sums(n + 1, 0);
    
    // Generate all possible partitions
    for (int i = 1; i <= n; i++) {
        int maxVal = 0;
        for (int j = i; j >= 1; j--) {
            maxVal = max(maxVal, arr[j - 1]);
            sums[i] = max(sums[i], sums[j - 1] + maxVal);
        }
    }
    
    // Find the maximum sum for k partitions
    int result = sums[n];
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `arr`. This is because we have a nested loop that generates all possible partitions and calculates the sum for each partition.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `arr`. This is because we use a vector `sums` to store the maximum sum for each subarray.
> - **Why these complexities occur:** These complexities occur because we are generating all possible partitions and calculating the sum for each partition using a brute force approach.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the maximum sum for each subarray.
- We can use a vector `dp` to store the maximum sum for each subarray, where `dp[i]` represents the maximum sum that can be obtained by partitioning the first `i` elements into at most `k` subarrays.
- We can then use a nested loop to calculate the maximum sum for each subarray and update the `dp` vector accordingly.

```cpp
#include <vector>
#include <algorithm>

int maxSumAfterPartitioning(vector<int>& arr, int k) {
    int n = arr.size();
    vector<int> dp(n + 1, 0);
    
    for (int i = 1; i <= n; i++) {
        int maxVal = 0;
        for (int j = 1; j <= i && j <= k; j++) {
            maxVal = max(maxVal, arr[i - j]);
            dp[i] = max(dp[i], dp[i - j] + maxVal * j);
        }
    }
    
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the length of `arr` and $k` is the number of partitions. This is because we have a nested loop that calculates the maximum sum for each subarray and updates the `dp` vector accordingly.
> - **Space Complexity:** $O(n)$, where $n` is the length of `arr`. This is because we use a vector `dp` to store the maximum sum for each subarray.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the maximum sum for each subarray, which allows us to avoid recalculating the sum for each subarray and reduces the time complexity from $O(n^2)$ to $O(nk)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion, and backtracking.
- Problem-solving patterns identified: using dynamic programming to store the maximum sum for each subarray and using a nested loop to calculate the maximum sum for each subarray.
- Optimization techniques learned: using dynamic programming to reduce the time complexity from $O(n^2)$ to $O(nk)$.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` vector correctly, not updating the `dp` vector correctly, and not using the correct loop bounds.
- Edge cases to watch for: when `k` equals the length of `arr`, when `k` equals 1, and when the input array is empty.
- Performance pitfalls: using a brute force approach that generates all possible partitions and calculates the sum for each partition, which can result in a time complexity of $O(n^2)$.