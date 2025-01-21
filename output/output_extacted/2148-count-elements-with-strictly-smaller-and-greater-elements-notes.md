## Count Elements with Strictly Smaller and Greater Elements

**Problem Link:** https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums`.
- Expected output format: The output should be the count of elements that have both a strictly smaller and a strictly greater element in the array.
- Key requirements and edge cases to consider: The array can contain duplicate elements, and the count should only include elements that have both a smaller and a greater element.
- Example test cases with explanations:
  - For `nums = [11, 7, 2, 15]`, the output is `2` because `7` and `11` have both a smaller and a greater element.
  - For `nums = [1, 2, 3]`, the output is `1` because only `2` has both a smaller and a greater element.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each element in the array to see if it has a smaller and a greater element.
- Step-by-step breakdown of the solution:
  1. Iterate through each element in the array.
  2. For each element, iterate through the rest of the array to find a smaller and a greater element.
  3. If both a smaller and a greater element are found, increment the count.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
int countElements(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        bool hasSmaller = false;
        bool hasGreater = false;
        for (int j = 0; j < nums.size(); j++) {
            if (i != j) {
                if (nums[j] < nums[i]) {
                    hasSmaller = true;
                }
                if (nums[j] > nums[i]) {
                    hasGreater = true;
                }
            }
        }
        if (hasSmaller && hasGreater) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array, because for each element, we potentially iterate through the entire array again.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store the count and the flags.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the minimum and maximum elements in the array first, then iterate through the array to count the elements that are between these two extremes.
- Detailed breakdown of the approach:
  1. Find the minimum and maximum elements in the array.
  2. Iterate through the array and count the elements that are greater than the minimum and less than the maximum.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array to find the minimum and maximum, and then another pass to count the elements, resulting in a linear time complexity.

```cpp
int countElements(vector<int>& nums) {
    int minVal = *min_element(nums.begin(), nums.end());
    int maxVal = *max_element(nums.begin(), nums.end());
    int count = 0;
    for (int num : nums) {
        if (minVal < num && num < maxVal) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we make two passes through the array: one to find the minimum and maximum, and another to count the elements.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store the count, minimum, and maximum.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each element once to determine if it meets the condition, and our approach does this in a single pass after finding the minimum and maximum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding minimum and maximum values, iterating through an array, and counting elements based on conditions.
- Problem-solving patterns identified: The importance of finding the extremes (minimum and maximum) to simplify the counting process.
- Optimization techniques learned: Reducing the number of passes through the data and avoiding unnecessary comparisons.
- Similar problems to practice: Other problems that involve counting elements based on conditions, such as finding elements within a certain range.

**Mistakes to Avoid:**
- Common implementation errors: Not correctly handling edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate elements, arrays with all elements being the same, and arrays with negative numbers or zero.
- Performance pitfalls: Using inefficient algorithms that result in high time complexities, such as nested loops when a single pass is possible.
- Testing considerations: Thoroughly testing the function with various input arrays, including edge cases, to ensure it works correctly in all scenarios.