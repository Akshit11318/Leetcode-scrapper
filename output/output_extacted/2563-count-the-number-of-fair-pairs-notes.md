## Count the Number of Fair Pairs
**Problem Link:** https://leetcode.com/problems/count-the-number-of-fair-pairs/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, and two integers `lower` and `upper`, return the number of pairs of indices `(i, j)` such that `lower <= nums[i] + nums[j] <= upper`.
- Expected output format: The number of pairs of indices that satisfy the given condition.
- Key requirements and edge cases to consider: The array `nums` can contain duplicate elements, and the range of possible sums is large.
- Example test cases with explanations:
  - For `nums = [1, 7, 5, 9], lower = 10, upper = 20`, the number of fair pairs is 3, corresponding to the pairs `(0, 2)`, `(0, 3)`, and `(2, 3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all pairs of indices in the array and check if the sum of the elements at these indices falls within the given range.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of fair pairs.
  2. Iterate over all pairs of indices `(i, j)` in the array.
  3. For each pair, calculate the sum of the elements at these indices.
  4. Check if the sum falls within the given range `[lower, upper]`.
  5. If it does, increment the counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks all possible pairs.

```cpp
int countFairPairs(vector<int>& nums, int lower, int upper) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int sum = nums[i] + nums[j];
            if (lower <= sum && sum <= upper) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because we are iterating over all pairs of indices.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the counter.
> - **Why these complexities occur:** The brute force approach has a quadratic time complexity because it checks all pairs of indices, resulting in $n \times (n-1)$ comparisons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to find the number of pairs that satisfy the given condition.
- Detailed breakdown of the approach:
  1. Sort the array `nums` in ascending order.
  2. Initialize two pointers, `left` and `right`, to the start of the array.
  3. Iterate over the array with the `left` pointer.
  4. For each element at the `left` pointer, find the range of elements that can be paired with it to fall within the given range.
  5. Use the `right` pointer to find the upper bound of this range.
- Proof of optimality: This approach has a linear time complexity after sorting, making it more efficient than the brute force approach for large inputs.

```cpp
int countFairPairs(vector<int>& nums, int lower, int upper) {
    sort(nums.begin(), nums.end());
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        int left = i + 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[i] + nums[mid] < lower) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int lowerBound = left;
        left = i + 1;
        right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[i] + nums[mid] <= upper) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int upperBound = left;
        count += upperBound - lowerBound;
    }
    return count / 2; // Divide by 2 to avoid counting each pair twice
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \log n) = O(n \log n)$, where $n$ is the number of elements in the array, because we are sorting the array and then using a two-pointer technique.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the pointers and the counter.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from quadratic to linear after sorting, making it more efficient for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting, and binary search.
- Problem-solving patterns identified: Using a two-pointer technique to find the number of pairs that satisfy a given condition.
- Optimization techniques learned: Sorting the array and using a two-pointer technique to reduce the time complexity.
- Similar problems to practice: Other problems that involve finding the number of pairs that satisfy a given condition, such as finding the number of pairs with a given sum or difference.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Handling cases where the array contains duplicate elements or where the range of possible sums is large.
- Performance pitfalls: Using a brute force approach for large inputs, which can result in a quadratic time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs, to ensure that it works correctly and efficiently.