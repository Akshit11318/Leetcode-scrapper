## Minimum Number of Operations to Make Array Elements Equal

**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `x` and `y`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^6`, `1 <= x, y <= 10^6`.
- Expected output format: The minimum number of operations to make all elements in `nums` equal to either `x` or `y`.
- Key requirements and edge cases to consider:
  - The array can be empty.
  - `x` and `y` can be equal.
  - All elements in `nums` can be equal to `x` or `y`.
- Example test cases with explanations:
  - `nums = [1, 3, 5], x = 2, y = 3`, the minimum number of operations is 1 (change 1 and 5 to 2 or 3).
  - `nums = [2, 2, 2], x = 2, y = 3`, the minimum number of operations is 0 (all elements are already equal to `x`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of changing each element to either `x` or `y` and count the number of operations.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the minimum number of operations.
  2. Iterate over each element in `nums`.
  3. For each element, try changing it to `x` and `y` and count the number of operations.
  4. Update the minimum number of operations if a smaller count is found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
int minOperations(vector<int>& nums, int x, int y) {
    int minOps = INT_MAX;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        int ops = 0;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i)) && nums[i] != x) {
                ops++;
            } else if (!(mask & (1 << i)) && nums[i] != y) {
                ops++;
            }
        }
        minOps = min(minOps, ops);
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of `nums`. This is because we are trying all possible combinations of changing each element to either `x` or `y`.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the minimum number of operations.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because it tries all possible combinations of changing each element to either `x` or `y`. The space complexity is constant because we are using a fixed amount of space to store the minimum number of operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer approach to find the minimum number of operations.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start and end of `nums`, respectively.
  2. Initialize a counter for the minimum number of operations.
  3. Iterate over `nums` and try to change each element to either `x` or `y`.
  4. If an element is equal to `x`, move the `left` pointer to the right.
  5. If an element is equal to `y`, move the `right` pointer to the left.
  6. Update the minimum number of operations if a smaller count is found.
- Proof of optimality: This approach is optimal because it tries all possible combinations of changing each element to either `x` or `y` in a single pass.

```cpp
int minOperations(vector<int>& nums, int x, int y) {
    int minOps = 0;
    for (int num : nums) {
        if (num != x && num != y) {
            minOps++;
        }
    }
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`. This is because we are iterating over `nums` once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the minimum number of operations.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of changing each element to either `x` or `y` in a single pass, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer approach, iteration over an array.
- Problem-solving patterns identified: Using a counter to store the minimum number of operations, trying all possible combinations of changing each element to either `x` or `y`.
- Optimization techniques learned: Reducing the time complexity from exponential to linear by using a two-pointer approach.
- Similar problems to practice: Minimum number of operations to make all elements in an array equal, minimum number of operations to make all elements in a matrix equal.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the counter for the minimum number of operations, not updating the counter correctly.
- Edge cases to watch for: Empty array, `x` and `y` are equal, all elements in `nums` are equal to `x` or `y`.
- Performance pitfalls: Using an exponential time complexity approach, not using a counter to store the minimum number of operations.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.