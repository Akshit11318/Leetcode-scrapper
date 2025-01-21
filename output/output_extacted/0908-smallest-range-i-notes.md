## Smallest Range I
**Problem Link:** https://leetcode.com/problems/smallest-range-i/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `0 <= nums[i] <= 1000`, `0 <= k <= 1000`.
- Expected Output: The smallest possible range of the array after incrementing some of the elements by any amount less than or equal to `k`.
- Key Requirements: Find the minimum possible range of the array after applying the given operation.

**Example Test Cases:**
- `nums = [1], k = 0` -> `0` because the range of `[1]` is `1 - 1 = 0`.
- `nums = [0, 10], k = 2` -> `6` because we can make the array `[2, 8]`, and the range is `8 - 2 = 6`.
- `nums = [1, 3, 6], k = 3` -> `0` because we can make the array `[3, 3, 3]`, and the range is `3 - 3 = 0`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying to increment each element by all possible amounts less than or equal to `k` and then calculating the range of the resulting array.
- This approach comes to mind first because it involves directly applying the given operation to each element and observing the effect on the range.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int smallestRangeI(std::vector<int>& nums, int k) {
    int minRange = INT_MAX;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        std::vector<int> temp = nums;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i))) {
                temp[i] += k;
            }
        }
        std::sort(temp.begin(), temp.end());
        int range = temp.back() - temp.front();
        minRange = std::min(minRange, range);
    }
    return minRange;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \log n)$, where $n$ is the number of elements in the array. This is because we generate all subsets of the array (which takes $O(2^n)$ time), and for each subset, we sort the array (which takes $O(n \log n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we create a temporary array to store the modified elements.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets of the array and applying the operation to each subset. This leads to an exponential time complexity due to the number of subsets. The sorting operation within each subset contributes to the $n \log n$ factor in the time complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that the range of the array is minimized when the smallest element is maximized and the largest element is minimized.
- We can achieve this by adding `k` to the smallest element and subtracting `k` from the largest element.
- If the resulting range is negative, it means we can make all elements equal, and the range becomes `0`.

```cpp
int smallestRangeI(std::vector<int>& nums, int k) {
    int minVal = *std::min_element(nums.begin(), nums.end());
    int maxVal = *std::max_element(nums.begin(), nums.end());
    int range = maxVal - minVal;
    range -= 2 * k;
    return std::max(0, range);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we find the minimum and maximum elements in the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum possible range by maximizing the smallest element and minimizing the largest element. Further optimization is impossible because we have considered all possible operations that can reduce the range.

### Final Notes

**Learning Points:**
- The importance of identifying key insights that can simplify the problem.
- The use of `std::min_element` and `std::max_element` to find the minimum and maximum elements in an array.
- The concept of maximizing the smallest element and minimizing the largest element to reduce the range.

**Mistakes to Avoid:**
- Generating all possible subsets of the array, which leads to an exponential time complexity.
- Failing to consider the case where the resulting range is negative, which means the range can be reduced to `0`.
- Not using the `std::max` function to ensure the range is not negative.