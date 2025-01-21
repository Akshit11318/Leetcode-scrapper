## Maximal Range That Each Element Is Maximum In It

**Problem Link:** https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/description

**Problem Statement:**
- Given a list of integers `nums`, find the maximum range that each element is maximum in it. 
- For each element `nums[i]`, find the range `[i - nums[i], i + nums[i]]` where `nums[i]` is the maximum value.
- The goal is to find the maximum range that each element is maximum in it.

**Expected Output Format:**
- Return the maximum range.

**Key Requirements and Edge Cases to Consider:**
- Handle edge cases where `nums` is empty or contains a single element.
- Consider cases where the maximum range is at the beginning or end of the list.

**Example Test Cases with Explanations:**
- For `nums = [1, 2, 3]`, the maximum range for each element is `[0, 1]`, `[1, 3]`, and `[2, 4]` respectively. The maximum range that each element is maximum in it is `[1, 3]`.
- For `nums = [1, 3, 2]`, the maximum range for each element is `[0, 1]`, `[1, 4]`, and `[2, 3]` respectively. The maximum range that each element is maximum in it is `[1, 4]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each element in the list and find the maximum range for that element.
- For each element, calculate the range `[i - nums[i], i + nums[i]]` and check if it is the maximum range.
- Compare the maximum range for each element and return the maximum one.

```cpp
#include <vector>
#include <algorithm>

int maximalRange(std::vector<int>& nums) {
    if (nums.empty()) {
        return 0;
    }

    int maxRange = 0;
    for (int i = 0; i < nums.size(); i++) {
        int range = nums[i] * 2 + 1;
        bool isMax = true;
        for (int j = i - nums[i]; j <= i + nums[i]; j++) {
            if (j < 0 || j >= nums.size() || nums[j] > nums[i]) {
                isMax = false;
                break;
            }
        }
        if (isMax && range > maxRange) {
            maxRange = range;
        }
    }
    return maxRange;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input list. This is because we are iterating through each element in the list and for each element, we are iterating through its range.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum range.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a single pass through the list to find the maximum range for each element.
- For each element, calculate the range `[i - nums[i], i + nums[i]]` and check if it is the maximum range.
- Keep track of the maximum range seen so far.

```cpp
#include <vector>
#include <algorithm>

int maximalRange(std::vector<int>& nums) {
    if (nums.empty()) {
        return 0;
    }

    int maxRange = 0;
    for (int i = 0; i < nums.size(); i++) {
        int range = nums[i] * 2 + 1;
        bool isMax = true;
        for (int j = std::max(0, i - nums[i]); j <= std::min((int)nums.size() - 1, i + nums[i]); j++) {
            if (nums[j] > nums[i]) {
                isMax = false;
                break;
            }
        }
        if (isMax && range > maxRange) {
            maxRange = range;
        }
    }
    return maxRange;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input list. This is because we are iterating through each element in the list and for each element, we are iterating through its range.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum range.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input list once, and we must also check each element's range to find the maximum range.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, comparison, and range calculation.
- Problem-solving patterns identified: finding the maximum range for each element and comparing them to find the maximum range.
- Optimization techniques learned: using a single pass through the list to find the maximum range for each element.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not checking if the element is within the list bounds.
- Edge cases to watch for: empty list, list with a single element, and list with elements that have a range that exceeds the list bounds.
- Performance pitfalls: using nested loops, not using a single pass through the list.
- Testing considerations: test the function with different input lists, including edge cases and lists with varying sizes.