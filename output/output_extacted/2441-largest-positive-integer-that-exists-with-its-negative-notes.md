## Largest Positive Integer That Exists With Its Negative
**Problem Link:** https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 1000$, $-1000 \leq nums[i] \leq 1000$.
- Expected output format: The largest positive integer that exists with its negative.
- Key requirements and edge cases to consider: The input array may contain duplicates, zeros, and both positive and negative integers. The solution must handle cases where no such integer exists.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1, 2, 3, -4]`, Output: `-1` (no such integer exists).
  - Example 2: Input: `nums = [3, 1, 2, 3]`, Output: `-1` (no such integer exists).
  - Example 3: Input: `nums = [1, 2, 3, -3]`, Output: `3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each number in the array, check if its negative counterpart exists.
- Step-by-step breakdown of the solution:
  1. Iterate over the array.
  2. For each number, check if its negative exists in the array.
  3. Keep track of the largest such number.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number's negative existence.

```cpp
int findMaxK(vector<int>& nums) {
    int maxK = -1;
    for (int num : nums) {
        if (num > 0) {
            if (find(nums.begin(), nums.end(), -num) != nums.end()) {
                maxK = max(maxK, num);
            }
        }
    }
    return maxK;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`, because for each element, we are potentially searching through the entire array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The nested search operation within the loop leads to the quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a data structure like `unordered_set` to store the numbers we've seen so far allows for constant time lookup.
- Detailed breakdown of the approach:
  1. Create an `unordered_set` to store the numbers in the array.
  2. Iterate over the array, and for each number, check if its negative exists in the set.
  3. Update the maximum such number found.
- Proof of optimality: This approach minimizes the time complexity by reducing the lookup time to constant, making the overall time complexity linear.
- Why further optimization is impossible: We must examine each number at least once, so a linear time complexity is the best we can achieve.

```cpp
int findMaxK(vector<int>& nums) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int maxK = -1;
    for (int num : nums) {
        if (num > 0 && numSet.find(-num) != numSet.end()) {
            maxK = max(maxK, num);
        }
    }
    return maxK;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we perform a constant amount of work for each element.
> - **Space Complexity:** $O(n)$, as in the worst case, we store all elements in the `unordered_set`.
> - **Optimality proof:** This is optimal because we only iterate through the array twice (once to populate the set and once to check for negatives), and each operation within these iterations takes constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `unordered_set` for efficient lookup, iterating through arrays, and keeping track of maximum values.
- Problem-solving patterns identified: Reducing time complexity by using appropriate data structures.
- Optimization techniques learned: Minimizing the number of iterations and using constant time operations.
- Similar problems to practice: Other problems involving finding elements in arrays or sets.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (like an empty array), not handling duplicates correctly.
- Edge cases to watch for: Empty array, array with all zeros, array with no pairs of positive and negative integers.
- Performance pitfalls: Using linear search within a loop, leading to quadratic time complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases and large inputs to verify efficiency.