## Partition Array According to Given Pivot
**Problem Link:** https://leetcode.com/problems/partition-array-according-to-given-pivot/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and a pivot integer `pivot`, partition the array such that all elements less than `pivot` come before elements greater than or equal to `pivot`.
- Expected output format: The modified array `nums`.
- Key requirements and edge cases to consider: 
  - Handle empty arrays.
  - Consider the case when all elements are less than the pivot.
  - Consider the case when all elements are greater than or equal to the pivot.
- Example test cases with explanations:
  - Example 1: Input: `nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10`, Output: `[9, 5, 3, 10, 10, 12, 14]`.
  - Example 2: Input: `nums = [], pivot = 9`, Output: `[]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the array and then partition it based on the pivot.
- Step-by-step breakdown of the solution:
  1. Sort the array in ascending order.
  2. Iterate through the sorted array to find the first occurrence of an element greater than or equal to the pivot.
  3. Swap elements less than the pivot with elements greater than or equal to the pivot to maintain the partition.
- Why this approach comes to mind first: It's straightforward and ensures the correct ordering of elements with respect to the pivot.

```cpp
void partitionArray(vector<int>& nums, int pivot) {
    // Sort the array
    sort(nums.begin(), nums.end());
    
    // Initialize pointers for partitioning
    int i = 0;
    for (int j = 0; j < nums.size(); j++) {
        if (nums[j] < pivot) {
            swap(nums[i], nums[j]);
            i++;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$ if we consider the sorting algorithm used has a constant space complexity, otherwise it could be $O(n)$.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity depends on the sorting algorithm's space requirements.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a two-pointer technique to partition the array in-place without sorting.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
  2. Move elements less than the pivot to the left part of the array and elements greater than or equal to the pivot to the right part.
- Proof of optimality: This approach ensures that all elements less than the pivot are on the left of elements greater than or equal to the pivot in a single pass through the array, achieving a linear time complexity.

```cpp
void partitionArray(vector<int>& nums, int pivot) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        while (left <= right && nums[left] < pivot) {
            left++;
        }
        while (left <= right && nums[right] >= pivot) {
            right--;
        }
        if (left <= right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, since we potentially visit each element once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and do not allocate any additional space that scales with input size.
> - **Optimality proof:** The linear time complexity is optimal for this problem since we must at least look at each element once to determine its position relative to the pivot.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place partitioning, two-pointer technique.
- Problem-solving patterns identified: Using a two-pointer approach to solve partitioning problems efficiently.
- Optimization techniques learned: Avoiding unnecessary sorting and using in-place algorithms to reduce space complexity.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing or updating pointers, not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with all elements less than or greater than the pivot.
- Performance pitfalls: Using sorting algorithms when a linear time solution is possible.
- Testing considerations: Thoroughly test with various inputs, including edge cases, to ensure the solution works as expected.