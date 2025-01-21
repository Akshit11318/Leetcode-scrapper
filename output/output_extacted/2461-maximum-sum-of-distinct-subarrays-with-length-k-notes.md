## Maximum Sum of Distinct Subarrays with Length K

**Problem Link:** https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description

**Problem Statement:**
- Input: An array `nums` of integers and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: The maximum sum of distinct subarrays with length `k`.
- Key Requirements: Find the maximum sum of all distinct subarrays of length `k` within the given array `nums`.
- Edge Cases: Consider cases where `k` equals the length of `nums`, where `nums` contains duplicate elements, and where `k` is 1.

Example Test Cases:
- For `nums = [1, 2, 3, 4]` and `k = 2`, the maximum sum is `7` (from subarray `[3, 4]`).
- For `nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]` and `k = 4`, the maximum sum is `24` (from subarray `[4, 2, 10, 2]`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subarrays of length `k`, calculating their sums, and keeping track of the maximum sum found.
- This approach involves iterating over the array to generate subarrays, summing each subarray, and updating the maximum sum as needed.
- This comes to mind first because it directly addresses the problem by considering all possible subarrays.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maximumSum(vector<int>& nums, int k) {
    int maxSum = INT_MIN;
    for (int i = 0; i <= nums.size() - k; i++) {
        int subarraySum = 0;
        for (int j = i; j < i + k; j++) {
            subarraySum += nums[j];
        }
        maxSum = max(maxSum, subarraySum);
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of `nums`. This is because we potentially generate $n - k + 1$ subarrays and sum each one, which takes $k$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for input and output, because we only use a constant amount of space to store the current sum and the maximum sum.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure, where the outer loop generates subarrays and the inner loop sums each subarray. The space complexity is low because we only use a fixed amount of space to store the maximum sum and the current subarray sum.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach, maintaining a window of size `k` over the array and updating the sum of the elements within this window as we slide it.
- This approach avoids the need to sum each subarray from scratch, reducing the time complexity.
- We initialize the window sum by summing the first `k` elements, then slide the window to the right, subtracting the leftmost element and adding the new element to the right of the window.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int maximumSum(vector<int>& nums, int k) {
    int maxSum = INT_MIN;
    int windowSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        windowSum += nums[i];
        if (i >= k) {
            windowSum -= nums[i - k];
        }
        if (i >= k - 1) {
            maxSum = max(maxSum, windowSum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for input and output, because we only use a constant amount of space to store the window sum and the maximum sum.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array, and it avoids unnecessary recalculations of subarray sums by maintaining a sliding window.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns in problems that can be solved using a sliding window approach.
- How to optimize brute force solutions by avoiding redundant calculations.
- The trade-offs between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the sliding window approach for problems involving subarrays or substrings.
- Failing to optimize the calculation of subarray sums by not using a sliding window.
- Not validating the input or handling edge cases properly.