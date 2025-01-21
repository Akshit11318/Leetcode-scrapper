## Smallest Range II
**Problem Link:** https://leetcode.com/problems/smallest-range-ii/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `2 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`, `0 <= k <= 10^5`.
- Expected Output: The smallest possible range of values after applying the given operations.
- Key Requirements: Find the minimum range that can be achieved by increasing some numbers in the array by `k`.
- Edge Cases: Consider scenarios where all numbers are the same, or where the array is already sorted.

**Example Test Cases:**
- `nums = [1,3,6], k = 3` -> The smallest range is `[3,5]`.
- `nums = [1,2,3], k = 1` -> The smallest range is `[1,3]`.
- `nums = [7,8,8,8,8], k = 5` -> The smallest range is `[7,7]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to consider all possible combinations of increasing numbers by `k`.
- However, this approach is impractical due to the large number of possible combinations.
- A brute force solution would involve iterating over all possible subsets of the array, applying the operation to each subset, and calculating the range for each subset.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int smallestRangeII(std::vector<int>& nums, int k) {
    int n = nums.size();
    std::sort(nums.begin(), nums.end());
    int minRange = nums[n-1] - nums[0];
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int left = std::min(nums[i], nums[j] - k);
            int right = std::max(nums[i] + k, nums[j]);
            minRange = std::min(minRange, right - left);
        }
    }
    
    return minRange;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is due to the nested loops iterating over the array.
> - **Space Complexity:** $O(n)$, for sorting the input array.
> - **Why these complexities occur:** The brute force approach involves iterating over all possible subsets of the array, resulting in quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to recognize that the smallest range can be achieved by finding the minimum difference between the maximum of the first `i` elements (increased by `k`) and the minimum of the last `n-i` elements.
- This approach involves iterating over the array once, keeping track of the minimum and maximum values, and calculating the range for each possible split point.
- The optimal solution uses a two-pointer technique to find the minimum range.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int smallestRangeII(std::vector<int>& nums, int k) {
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    int minRange = nums[n-1] - nums[0];
    
    for (int i = 0; i < n - 1; i++) {
        int right = std::max(nums[i] + k, nums[n-1]);
        int left = std::min(nums[0] + k, nums[i+1]);
        minRange = std::min(minRange, right - left);
    }
    
    return std::min(minRange, nums[n-1] - k - (nums[0] + k));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, for sorting the input array.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n \log n)$ due to the sorting operation, which is necessary to find the minimum and maximum values in the array. The subsequent iteration over the array has a time complexity of $O(n)$, resulting in an overall time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- The importance of recognizing the key insight in the problem, which leads to the optimal solution.
- The use of a two-pointer technique to find the minimum range.
- The need to consider edge cases, such as when all numbers are the same or when the array is already sorted.

**Mistakes to Avoid:**
- Failing to recognize the key insight in the problem, leading to an inefficient brute force solution.
- Not considering edge cases, which can result in incorrect solutions.
- Not optimizing the solution, resulting in unnecessary time complexity.