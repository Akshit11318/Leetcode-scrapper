## Custom Interval Problem

**Problem Link:** https://leetcode.com/problems/custom-interval/description

**Problem Statement:**
- Input format: An array of integers `nums`, an integer `lower`, and an integer `upper`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= lower <= upper <= 10^6`, and `0 <= nums[i] <= 10^6`.
- Expected output format: The number of integers in the range `[lower, upper]` inclusive that are not in the array `nums`.
- Key requirements and edge cases to consider:
  - The input array `nums` may contain duplicates.
  - The range `[lower, upper]` may be large.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 4, 5], lower = 1, upper = 5`: The output should be `0` because all integers in the range `[1, 5]` are in the array `nums`.
  - `nums = [1, 2, 3, 4, 5], lower = 1, upper = 6`: The output should be `1` because the integer `6` is not in the array `nums`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all integers in the range `[lower, upper]` and check if each integer is in the array `nums`.
- Step-by-step breakdown of the solution:
  1. Initialize a set `numSet` with the integers in the array `nums`.
  2. Initialize a counter `count` to `0`.
  3. Iterate over all integers `i` in the range `[lower, upper]`.
  4. For each integer `i`, check if `i` is not in the set `numSet`. If `i` is not in the set, increment the counter `count`.
  5. Return the counter `count` as the result.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large ranges.

```cpp
int countIntegersInInterval(vector<int>& nums, int lower, int upper) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int count = 0;
    for (int i = lower; i <= upper; i++) {
        if (numSet.find(i) == numSet.end()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the array `nums` and $m$ is the size of the range `[lower, upper]`. This is because we iterate over all integers in the array `nums` to build the set `numSet`, and then iterate over all integers in the range `[lower, upper]`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array `nums`. This is because we store all integers in the array `nums` in the set `numSet`.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all integers in the array `nums` and the range `[lower, upper]`. The space complexity occurs because we store all integers in the array `nums` in the set `numSet`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a set to store the integers in the array `nums`, and then iterate over the range `[lower, upper]` to count the integers that are not in the set.
- Detailed breakdown of the approach:
  1. Initialize a set `numSet` with the integers in the array `nums`.
  2. Initialize a counter `count` to `0`.
  3. Iterate over all integers `i` in the range `[lower, upper]`.
  4. For each integer `i`, check if `i` is not in the set `numSet`. If `i` is not in the set, increment the counter `count`.
  5. Return the counter `count` as the result.
- Proof of optimality: This approach is optimal because we only iterate over the range `[lower, upper]` once, and we use a set to store the integers in the array `nums` for efficient lookup.

```cpp
int countIntegersInInterval(vector<int>& nums, int lower, int upper) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int count = upper - lower + 1;
    for (int num : nums) {
        if (num >= lower && num <= upper) {
            count--;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the array `nums` and $m$ is the size of the range `[lower, upper]`. This is because we iterate over all integers in the array `nums` to build the set `numSet`, and then iterate over all integers in the range `[lower, upper]`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array `nums`. This is because we store all integers in the array `nums` in the set `numSet`.
> - **Optimality proof:** This approach is optimal because we only iterate over the range `[lower, upper]` once, and we use a set to store the integers in the array `nums` for efficient lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to store integers for efficient lookup, iterating over a range of integers.
- Problem-solving patterns identified: Using a set to store integers, iterating over a range of integers.
- Optimization techniques learned: Using a set to store integers for efficient lookup.
- Similar problems to practice: Counting integers in a range, finding missing integers in a range.

**Mistakes to Avoid:**
- Common implementation errors: Not using a set to store integers, not iterating over the range `[lower, upper]`.
- Edge cases to watch for: Large ranges, duplicate integers in the array `nums`.
- Performance pitfalls: Not using a set to store integers, not iterating over the range `[lower, upper]` efficiently.
- Testing considerations: Testing with large ranges, testing with duplicate integers in the array `nums`.