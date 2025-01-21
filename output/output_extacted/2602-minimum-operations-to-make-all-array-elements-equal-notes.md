## Minimum Operations to Make All Array Elements Equal
**Problem Link:** https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums`. The goal is to make all elements in the array equal by performing the minimum number of operations. An operation is defined as incrementing or decrementing an element by 1.
- Expected output format: The minimum number of operations required to make all elements equal.
- Key requirements and edge cases to consider: The array can be empty, or all elements can already be equal. The optimal solution should handle these cases efficiently.
- Example test cases with explanations:
  - For `nums = [1, 2, 3]`, the minimum number of operations is 2 (either increment the first element to 3 or decrement the last two elements to 1).
  - For `nums = [1, 1, 1]`, the minimum number of operations is 0, as all elements are already equal.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible target values and calculate the total number of operations required to make all elements equal to each target value.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible target values (from the minimum to the maximum element in the array).
  2. For each target value, calculate the total number of operations required to make all elements equal to the target.
  3. Keep track of the minimum total number of operations found so far.
- Why this approach comes to mind first: It is a straightforward, exhaustive approach that considers all possibilities.

```cpp
int minOperations(vector<int>& nums) {
    if (nums.empty()) return 0; // Edge case: empty array
    
    int minVal = *min_element(nums.begin(), nums.end());
    int maxVal = *max_element(nums.begin(), nums.end());
    
    int minOps = INT_MAX;
    for (int target = minVal; target <= maxVal; target++) {
        int ops = 0;
        for (int num : nums) {
            ops += abs(num - target);
        }
        minOps = min(minOps, ops);
    }
    
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of elements in the array and $m$ is the range of values in the array ($maxVal - minVal + 1$). This is because we iterate over all elements for each possible target value.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum values, the target value, and the minimum number of operations.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops over all possible target values and all elements in the array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal target value is the median of the array, as it minimizes the sum of absolute differences with all other elements.
- Detailed breakdown of the approach:
  1. Find the median of the array.
  2. Calculate the total number of operations required to make all elements equal to the median.
- Proof of optimality: The median is the value that minimizes the sum of absolute differences with all other elements. This is because the absolute difference function is convex, and the median is the point where the derivative of the sum of absolute differences is zero.
- Why further optimization is impossible: The median is the optimal target value, and calculating the total number of operations required to make all elements equal to the median is a straightforward, linear-time operation.

```cpp
int minOperations(vector<int>& nums) {
    if (nums.empty()) return 0; // Edge case: empty array
    
    sort(nums.begin(), nums.end());
    int median = nums[nums.size() / 2];
    
    int ops = 0;
    for (int num : nums) {
        ops += abs(num - median);
    }
    
    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we sort the array to find the median.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the median and the total number of operations.
> - **Optimality proof:** The median is the optimal target value, and calculating the total number of operations required to make all elements equal to the median is a straightforward, linear-time operation.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the median, calculating the sum of absolute differences.
- Problem-solving patterns identified: Using the median as the optimal target value.
- Optimization techniques learned: Avoiding brute force approaches, using properties of convex functions.
- Similar problems to practice: Finding the minimum number of operations to make all elements in an array equal to a given target value.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., empty array).
- Edge cases to watch for: Empty array, all elements already equal.
- Performance pitfalls: Using brute force approaches.
- Testing considerations: Test with different input sizes, edge cases, and target values.