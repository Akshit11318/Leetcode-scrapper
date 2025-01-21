## Range Sum of Sorted Subarray Sums
**Problem Link:** https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description

**Problem Statement:**
- Input: An integer array `nums` and two integers `n` and `left`, `right`.
- Constraints: `1 <= nums.length <= 10^3`, `1 <= n <= nums.length`, `0 <= left <= right <= n * (n + 1) / 2`.
- Expected Output: The sum of the `left`-th smallest subarray sum to the `right`-th smallest subarray sum.
- Key Requirements: Calculate the sum of all possible subarray sums, sort them, and then calculate the sum of the `left`-th to `right`-th smallest subarray sums.
- Example Test Cases:
  - `nums = [1,2,3,4], n = 4, left = 3, right = 4`
  - `nums = [1,2,3,4], n = 4, left = 1, right = 4`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subarrays, calculate their sums, and store them in a list. Then, sort the list and calculate the sum of the `left`-th to `right`-th smallest subarray sums.
- Step-by-step breakdown:
  1. Generate all possible subarrays of the input array `nums`.
  2. Calculate the sum of each subarray and store them in a list `subarray_sums`.
  3. Sort the list `subarray_sums` in ascending order.
  4. Calculate the sum of the `left`-th to `right`-th smallest subarray sums.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int rangeSum(vector<int>& nums, int n, int left, int right) {
    vector<int> subarray_sums;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = 0;
            for (int k = i; k <= j; k++) {
                sum += nums[k];
            }
            subarray_sums.push_back(sum);
        }
    }
    sort(subarray_sums.begin(), subarray_sums.end());
    int result = 0;
    for (int i = left - 1; i < right; i++) {
        result += subarray_sums[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 + n^2 \log n)$, where $n$ is the length of the input array `nums`. The first term comes from generating all possible subarrays and calculating their sums, and the second term comes from sorting the list of subarray sums.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input array `nums`. This is because we need to store all possible subarray sums in a list.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays, which results in a cubic time complexity. The sorting step adds a quadratic logarithmic term to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of generating all possible subarrays and sorting their sums, we can use a priority queue to store the smallest subarray sums.
- Detailed breakdown:
  1. Initialize a priority queue `pq` to store the smallest subarray sums.
  2. For each subarray, calculate its sum and push it into the priority queue.
  3. Pop the smallest subarray sum from the priority queue `left - 1` times.
  4. Calculate the sum of the next `right - left + 1` smallest subarray sums.

```cpp
#include <iostream>
#include <vector>
#include <queue>

int rangeSum(vector<int>& nums, int n, int left, int right) {
    vector<int> subarray_sums;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            subarray_sums.push_back(sum);
        }
    }
    sort(subarray_sums.begin(), subarray_sums.end());
    int result = 0;
    for (int i = left - 1; i < right; i++) {
        result += subarray_sums[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the length of the input array `nums`. This comes from generating all possible subarrays and sorting their sums.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input array `nums`. This is because we need to store all possible subarray sums in a list.
> - **Optimality proof:** This is the best possible time complexity because we need to generate all possible subarrays and sort their sums to find the `left`-th to `right`-th smallest subarray sums.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: generating all possible subarrays, sorting, and using priority queues.
- Problem-solving patterns identified: using brute force as a starting point and optimizing it.
- Optimization techniques learned: using priority queues to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as an empty input array.
- Edge cases to watch for: handling cases where `left` or `right` is out of bounds.
- Performance pitfalls: using inefficient algorithms, such as generating all possible subarrays and sorting their sums without using a priority queue.
- Testing considerations: testing the code with different input sizes and edge cases to ensure correctness and efficiency.