## Make Array Non-Decreasing or Non-Increasing
**Problem Link:** https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`.
- Expected Output: Determine if it is possible to make the array either non-decreasing or non-increasing by modifying at most one element.
- Key Requirements:
  - At most one element can be changed.
  - The resulting array must be either non-decreasing or non-increasing.
- Edge Cases:
  - Arrays that are already non-decreasing or non-increasing.
  - Arrays with only one element.
- Example Test Cases:
  - `[4,2,3]`: Can be made non-decreasing by changing 4 to 3 or less.
  - `[4,2,1]`: Can be made non-increasing by changing 2 to 3 or more.

---

### Brute Force Approach
**Explanation:**
- Initial thought: Try all possible modifications of one element and check if the resulting array is non-decreasing or non-increasing.
- Step-by-Step:
  1. Iterate through each element in the array.
  2. For each element, try changing it to every possible value from the minimum to the maximum in the array.
  3. After changing each element, check if the resulting array is non-decreasing or non-increasing.
  4. If a modification results in a non-decreasing or non-increasing array, return `true`. If no such modification is found after checking all elements and values, return `false`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool checkPossibility(std::vector<int>& nums) {
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = 1; j <= 1000000000; ++j) {
            int original = nums[i];
            nums[i] = j;
            if (std::is_sorted(nums.begin(), nums.end()) || std::is_sorted(nums.rbegin(), nums.rend())) {
                return true;
            }
            nums[i] = original;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10^9)$, where $n$ is the number of elements in the array. This is because for each element, we are trying up to $10^9$ possible values.
> - **Space Complexity:** $O(1)$, since we are modifying the input array in place.
> - **Why these complexities occur:** The brute force approach involves nested loops that iterate over each element in the array and then over a large range of possible values for each element, leading to a high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key Insight: Instead of trying all possible values for each element, we can simply check if the array is already non-decreasing or non-increasing. If it is, we're done. If not, we identify the first pair of elements that are in the wrong order and try changing one of them to match the order.
- Step-by-Step:
  1. Initialize a variable to track if we have made a change.
  2. Iterate through the array to find the first pair of elements that are out of order (either decreasing when they should be increasing or vice versa).
  3. If such a pair is found and we haven't made a change yet, try changing the first element of the pair to match the order, and then check if the rest of the array is in order. If not, try changing the second element instead.
  4. If after trying both changes the array is still not in order, return `false`. If we successfully make the array non-decreasing or non-increasing with one change, return `true`.

```cpp
#include <iostream>
#include <vector>

bool checkPossibility(std::vector<int>& nums) {
    bool changed = false;
    for (int i = 0; i < nums.size() - 1; ++i) {
        if (nums[i] > nums[i + 1]) {
            if (changed) return false;
            if (i > 0 && nums[i - 1] > nums[i + 1] && i + 2 < nums.size() && nums[i] > nums[i + 2]) {
                return false;
            }
            changed = true;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are making a single pass through the array.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array and does not involve trying all possible values for each element, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes
**Learning Points:**
- The importance of checking for existing order in the array before attempting modifications.
- How to efficiently identify and address the first pair of elements that are out of order.
- The value of minimizing the number of changes and checks to achieve the desired array property.

**Mistakes to Avoid:**
- Trying all possible values for each element, as this leads to an unnecessarily high time complexity.
- Not checking if the array is already non-decreasing or non-increasing before making changes.
- Failing to limit the number of changes to at most one, as required by the problem statement.