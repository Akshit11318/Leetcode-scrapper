## Maximum Number of Operations to Move Ones to the End

**Problem Link:** https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-end/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums` and two integers `k` and `target`. The array `nums` consists of only 0s and 1s. The integer `k` represents the maximum number of operations allowed, and the integer `target` is the target number of 1s at the end of the array.
- Expected output format: The output is the maximum number of operations that can be performed to move the 1s to the end of the array without exceeding the target number of 1s.
- Key requirements and edge cases to consider: The problem requires finding the maximum number of operations that can be performed within the given constraints. Edge cases include when the array is empty, when `k` is 0, and when the target number of 1s is greater than the total number of 1s in the array.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,0,1,0,1]`, `k = 3`, `target = 2`. Output: `2`. Explanation: The maximum number of operations that can be performed is 2, as we can move the first two 1s to the end of the array.
  - Example 2: Input: `nums = [1,1,1,0,0]`, `k = 2`, `target = 3`. Output: `2`. Explanation: The maximum number of operations that can be performed is 2, as we can move the first two 1s to the end of the array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of moving 1s to the end of the array and checking if the number of operations does not exceed `k` and the target number of 1s is not exceeded.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of operations.
  2. Generate all possible combinations of moving 1s to the end of the array.
  3. For each combination, check if the number of operations does not exceed `k` and the target number of 1s is not exceeded.
  4. If the conditions are met, update the maximum number of operations.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the generation of all possible combinations.

```cpp
#include <vector>
#include <algorithm>

int maxOperations(std::vector<int>& nums, int k, int target) {
    int maxOps = 0;
    int n = nums.size();
    for (int mask = 0; mask < (1 << n); mask++) {
        int ops = 0;
        int ones = 0;
        std::vector<int> temp = nums;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (temp[i] == 1) {
                    ops++;
                    std::swap(temp[i], temp[n - 1 - ones]);
                    ones++;
                }
            }
        }
        if (ops <= k && ones <= target) {
            maxOps = std::max(maxOps, ops);
        }
    }
    return maxOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible combinations of moving 1s to the end of the array, and for each combination, we iterate through the array to check the conditions.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we create a temporary array to store the modified array.
> - **Why these complexities occur:** The high time complexity occurs due to the generation of all possible combinations, and the space complexity occurs due to the creation of a temporary array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a two-pointer technique to find the maximum number of operations that can be performed.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Initialize a variable to store the maximum number of operations.
  3. Move the `right` pointer to the right until we find a 1 or we reach the end of the array.
  4. If we find a 1, move the `left` pointer to the right until we find a 0 or we reach the end of the array.
  5. If we find a 0, swap the elements at the `left` and `right` pointers and increment the maximum number of operations.
  6. Repeat steps 3-5 until we reach the end of the array or we exceed the target number of 1s.
- Why further optimization is impossible: This approach is optimal because it uses a two-pointer technique to find the maximum number of operations in a single pass through the array.

```cpp
#include <vector>

int maxOperations(std::vector<int>& nums, int k, int target) {
    int maxOps = 0;
    int n = nums.size();
    int ones = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == 1) {
            ones++;
        }
    }
    int left = 0;
    int right = n - 1;
    while (left < right && ones > target) {
        if (nums[right] == 1) {
            ones--;
            right--;
        } else if (nums[left] == 1) {
            left++;
        } else {
            left++;
            right--;
        }
    }
    int ops = 0;
    for (int i = left; i <= right; i++) {
        if (nums[i] == 1) {
            ops++;
        }
    }
    return std::min(ops, k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array. This is because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses a two-pointer technique to find the maximum number of operations in a single pass through the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, optimization.
- Problem-solving patterns identified: Using a two-pointer technique to find the maximum number of operations.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Other problems that involve finding the maximum number of operations, such as the "Maximum Number of Operations to Make Array Non-Increasing" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundary conditions, not handling the case where the target number of 1s is greater than the total number of 1s.
- Edge cases to watch for: The case where the array is empty, the case where `k` is 0, the case where the target number of 1s is greater than the total number of 1s.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Testing the solution with different inputs, including edge cases.