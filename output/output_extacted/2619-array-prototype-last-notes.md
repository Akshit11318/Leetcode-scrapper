## Array Prototype Last

**Problem Link:** https://leetcode.com/problems/array-prototype-last/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers. The constraints are that the array can be empty and the integers can be any value.
- Expected output format: The expected output is the last element of the array, or -1 if the array is empty.
- Key requirements and edge cases to consider: The key requirement is to handle the case when the array is empty. The edge cases are when the array has only one element, and when the array has multiple elements.
- Example test cases with explanations:
  - Example 1: Input: [1, 2, 3], Output: 3
  - Example 2: Input: [], Output: -1
  - Example 3: Input: [5], Output: 5

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to simply access the last element of the array. However, we need to handle the case when the array is empty.
- Step-by-step breakdown of the solution:
  1. Check if the array is empty.
  2. If the array is empty, return -1.
  3. If the array is not empty, return the last element of the array.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    int lastIndexOfOne(vector<int>& nums) {
        if (nums.empty()) {
            return -1;
        } else {
            return nums[nums.size() - 1];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only accessing the last element of the array, which takes constant time.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** These complexities occur because we are only performing a constant number of operations, regardless of the size of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can use the built-in `back()` function in C++ to access the last element of the array, which is more concise and expressive than accessing the last element using indexing.
- Detailed breakdown of the approach:
  1. Check if the array is empty.
  2. If the array is empty, return -1.
  3. If the array is not empty, return the last element of the array using the `back()` function.
- Proof of optimality: This approach is optimal because it has the same time and space complexity as the brute force approach, but it is more concise and expressive.
- Why further optimization is impossible: Further optimization is impossible because we are already accessing the last element of the array in constant time, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int lastIndexOfOne(vector<int>& nums) {
        if (nums.empty()) {
            return -1;
        } else {
            return nums.back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only accessing the last element of the array, which takes constant time.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it has the same time and space complexity as the brute force approach, but it is more concise and expressive.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated is accessing the last element of an array.
- Problem-solving patterns identified: The problem-solving pattern identified is handling edge cases, such as when the array is empty.
- Optimization techniques learned: The optimization technique learned is using built-in functions, such as `back()`, to make the code more concise and expressive.
- Similar problems to practice: Similar problems to practice include finding the first element of an array, finding the maximum element of an array, and finding the minimum element of an array.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is forgetting to handle the case when the array is empty.
- Edge cases to watch for: An edge case to watch for is when the array has only one element.
- Performance pitfalls: A performance pitfall is using a loop to find the last element of the array, which would have a time complexity of $O(n)$.
- Testing considerations: A testing consideration is to test the function with an empty array, an array with one element, and an array with multiple elements.