## Smallest Missing Non-Negative Integer After Operations
**Problem Link:** https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 5 * 10^4`, `-5 * 10^4 <= nums[i] <= 5 * 10^4`.
- Expected Output: The smallest non-negative integer that cannot be represented by the sum of the elements in the given array.
- Key Requirements: Find the smallest non-negative integer missing from the set of all possible sums of the array elements.
- Example Test Cases:
  - Input: `nums = [1,1,1]`
    Output: `3`
    Explanation: `3` is the smallest non-negative integer that cannot be represented by the sum of the elements in the given array.
  - Input: `nums = [1,2,2]`
    Output: `0`
    Explanation: `0` is the smallest non-negative integer that cannot be represented by the sum of the elements in the given array.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of the elements in the array to find the smallest non-negative integer that cannot be represented.
- Step-by-step breakdown:
  1. Initialize an empty set to store the sums of the elements.
  2. Iterate over all possible combinations of the elements in the array.
  3. For each combination, calculate the sum of the elements.
  4. Add the sum to the set.
  5. Iterate from `0` to the maximum possible sum.
  6. Return the first non-negative integer that is not in the set.

```cpp
#include <iostream>
#include <set>

int findSmallestMissingNonNegativeInteger(int* nums, int numsSize) {
    std::set<int> sums;
    for (int i = 0; i < (1 << numsSize); i++) {
        int sum = 0;
        for (int j = 0; j < numsSize; j++) {
            if ((i & (1 << j)) != 0) {
                sum += nums[j];
            }
        }
        sums.insert(sum);
    }
    int i = 0;
    while (sums.find(i) != sums.end()) {
        i++;
    }
    return i;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we are trying all possible combinations of the elements in the array.
> - **Space Complexity:** $O(2^n)$, where $n$ is the size of the input array. This is because we are storing the sums of the elements in a set.
> - **Why these complexities occur:** These complexities occur because we are trying all possible combinations of the elements in the array, which results in exponential time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: If the smallest non-negative integer that cannot be represented is greater than `0`, then it must be greater than the sum of all non-negative elements in the array.
- Detailed breakdown:
  1. Initialize a variable to store the sum of all non-negative elements in the array.
  2. Iterate over the array to calculate the sum of all non-negative elements.
  3. If the sum is less than `0`, return `0` because we cannot represent `0` with a negative sum.
  4. Otherwise, return the sum plus `1` because we cannot represent the sum plus `1` with the given elements.

```cpp
int findSmallestMissingNonNegativeInteger(int* nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 0) {
            sum += nums[i];
        }
    }
    if (sum < 0) {
        return 0;
    } else {
        return sum + 1;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are iterating over the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array. This is because we are using a constant amount of space to store the sum.
> - **Optimality proof:** This is the optimal solution because we are only iterating over the array once and using a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and basic arithmetic operations.
- Problem-solving patterns identified: Identifying the key insight that leads to the optimal solution.
- Optimization techniques learned: Reducing the time complexity from exponential to linear.
- Similar problems to practice: Other problems that involve finding the smallest non-negative integer that cannot be represented by a set of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the sum of all non-negative elements is less than `0`.
- Edge cases to watch for: The case where the input array is empty or contains only negative numbers.
- Performance pitfalls: Using exponential time complexity algorithms when linear time complexity algorithms are available.
- Testing considerations: Testing the function with different input arrays to ensure it works correctly in all cases.