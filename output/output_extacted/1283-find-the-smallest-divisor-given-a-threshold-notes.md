## Find the Smallest Divisor Given a Threshold
**Problem Link:** https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `threshold`.
- Output: The smallest divisor that makes the sum of the results of the division of each element in `nums` by this divisor less than or equal to `threshold`.
- Key requirements and edge cases:
  - The divisor must be greater than 0.
  - The division result should be rounded up if it's not an integer.
  - The input array `nums` will not be empty.

**Example Test Cases:**
- For `nums = [1, 2, 5, 9]` and `threshold = 6`, the output should be `5`.
- For `nums = [2, 3, 5, 7, 11]` and `threshold = 11`, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Start by considering all possible divisors from 1 to the maximum number in `nums`.
- For each potential divisor, calculate the sum of the results of the division of each element in `nums` by this divisor, rounding up to the nearest integer.
- Check if this sum is less than or equal to `threshold`.
- The first divisor that meets this condition is the smallest divisor that satisfies the given condition.

```cpp
#include <vector>
#include <cmath>

int smallestDivisor(std::vector<int>& nums, int threshold) {
    int maxNum = *std::max_element(nums.begin(), nums.end());
    for (int divisor = 1; divisor <= maxNum; divisor++) {
        int sum = 0;
        for (int num : nums) {
            sum += std::ceil(static_cast<double>(num) / divisor);
        }
        if (sum <= threshold) {
            return divisor;
        }
    }
    return -1; // Should not reach here
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of elements in `nums` and $m$ is the maximum number in `nums`. This is because for each potential divisor, we iterate through all elements in `nums`.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the sum and the current divisor.
> - **Why these complexities occur:** The brute force approach checks every possible divisor, leading to a linear search in the range of potential divisors, and for each divisor, it calculates the sum of the division results for all numbers in `nums`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to use binary search to find the smallest divisor. The search space is from 1 to the maximum number in `nums`.
- We define a helper function `checkDivisor` that takes a potential divisor and returns whether the sum of the division results for this divisor is less than or equal to `threshold`.
- We use binary search to find the smallest divisor that satisfies the condition. If the sum for the current divisor is less than or equal to `threshold`, we try a smaller divisor. Otherwise, we try a larger divisor.

```cpp
#include <vector>
#include <cmath>

int checkDivisor(std::vector<int>& nums, int divisor, int threshold) {
    int sum = 0;
    for (int num : nums) {
        sum += std::ceil(static_cast<double>(num) / divisor);
    }
    return sum <= threshold;
}

int smallestDivisor(std::vector<int>& nums, int threshold) {
    int left = 1;
    int right = *std::max_element(nums.begin(), nums.end());
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (checkDivisor(nums, mid, threshold)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of elements in `nums` and $m$ is the maximum number in `nums`. This is because we perform a binary search over the range of potential divisors, and for each potential divisor, we calculate the sum of the division results for all numbers in `nums`.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the search boundaries and the sum.
> - **Optimality proof:** This approach is optimal because it uses binary search to find the smallest divisor, reducing the search space by half at each step, which is the most efficient way to search a sorted range.

---

### Final Notes

**Learning Points:**
- Binary search can be applied to find the smallest element that satisfies a certain condition, not just to find an element in a sorted array.
- The key to applying binary search is to define a condition that can be checked for any potential solution and to ensure that the condition is monotonic (i.e., if the condition is true for a certain value, it is also true for all larger values).

**Mistakes to Avoid:**
- Not checking the condition for the final value of `left` after the binary search loop ends.
- Not handling the case where `threshold` is less than the sum of the division results for all numbers in `nums` divided by 1.