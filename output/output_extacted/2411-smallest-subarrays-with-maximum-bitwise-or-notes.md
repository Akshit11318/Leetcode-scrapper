## Smallest Subarrays with Maximum Bitwise OR

**Problem Link:** https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description

**Problem Statement:**
- Input: An array `nums` of integers.
- Output: An array of integers where the value at each index `i` is the length of the smallest subarray with a maximum bitwise OR equal to the maximum bitwise OR of all elements in `nums`.
- Key requirements and edge cases:
  - The input array can contain duplicate elements.
  - The maximum bitwise OR can be achieved by multiple subarrays.
  - The goal is to find the smallest such subarray for each starting index.

**Example Test Cases:**

* `nums = [1,0,2,1,3]`: The maximum bitwise OR of all elements is `3`. For each starting index, the smallest subarray that achieves this OR is of length `3` (for the first element), `3` (for the second element, considering the subarray `[0, 2, 1]`), `1` (for the third element), `1` (for the fourth element), and `1` (for the fifth element). Thus, the output is `[3,3,1,1,1]`.
* `nums = [1,2]`: The maximum bitwise OR is `3`. The smallest subarray that achieves this for both starting indices is of length `2`. Thus, the output is `[2,2]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray for each starting index to see if its maximum bitwise OR equals the maximum bitwise OR of the entire array.
- For each starting index `i`, we consider all possible subarrays starting at `i` and calculate their maximum bitwise OR.
- We compare this OR with the maximum OR of the entire array and update our result with the length of the smallest such subarray.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> smallestSubarrays(std::vector<int>& nums) {
    int maxOR = 0;
    for (int num : nums) {
        maxOR |= num;
    }

    std::vector<int> result(nums.size(), nums.size() + 1);
    for (int i = 0; i < nums.size(); ++i) {
        int currOR = 0;
        for (int j = i; j < nums.size(); ++j) {
            currOR |= nums[j];
            if (currOR == maxOR) {
                result[i] = std::min(result[i], j - i + 1);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because for each starting index, we potentially check every other element in the array once.
> - **Space Complexity:** $O(n)$, for storing the result array.
> - **Why these complexities occur:** The brute force approach involves nested loops over the input array, leading to quadratic time complexity. The space complexity is linear because we only store a single array of results.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach but optimized with the understanding that once we achieve the maximum OR, we can start shrinking the window from the left.
- We maintain a `maxOR` as before but now use two pointers, `left` and `right`, to represent our sliding window.
- We expand the window to the right until we achieve the `maxOR`, then try to shrink it from the left while maintaining the `maxOR`.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> smallestSubarrays(std::vector<int>& nums) {
    int maxOR = 0;
    for (int num : nums) {
        maxOR |= num;
    }

    std::vector<int> result(nums.size(), nums.size() + 1);
    for (int i = 0; i < nums.size(); ++i) {
        int currOR = 0, left = i;
        for (int right = i; right < nums.size(); ++right) {
            currOR |= nums[right];
            while (currOR == maxOR) {
                result[i] = std::min(result[i], right - left + 1);
                currOR ^= nums[left];
                ++left;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ in the worst case, but significantly optimized in practice because we stop expanding the window as soon as we achieve the `maxOR` and then try to minimize it.
> - **Space Complexity:** $O(n)$, for storing the result array.
> - **Optimality proof:** This approach is optimal because it still requires checking all elements in the worst case (e.g., when the array is filled with zeros except for one element). However, it minimizes the number of checks by stopping as soon as the condition is met and then optimizing the window size.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of bitwise operations, especially OR.
- How to apply the sliding window technique to optimize problems involving subarrays.
- The value of maintaining a clear and minimal state (e.g., `maxOR`, `currOR`, `left`, `right`) to solve complex problems efficiently.

**Mistakes to Avoid:**
- Not validating the input or handling edge cases properly.
- Failing to optimize the solution based on the problem's specific constraints or properties.
- Not considering the implications of the chosen data structures and algorithms on time and space complexity.