## Find Minimum in Rotated Sorted Array II

**Problem Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description

**Problem Statement:**
- Input: A `nums` array of integers, which is a rotated version of a sorted array (either ascending or descending) with duplicates allowed.
- Constraints: The array is non-empty and contains at least one element.
- Expected Output: The minimum element in the array.
- Key Requirements: The solution must handle arrays with duplicates and find the minimum element efficiently.
- Edge Cases: Consider arrays that are already sorted, arrays with all elements being the same, and arrays with a single rotation.

**Example Test Cases:**
- Example 1: `nums = [4,5,6,7,0,1,2]`, Output: `0`
- Example 2: `nums = [1]`, Output: `1`
- Example 3: `nums = [3,3,1,3]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves simply iterating through the array to find the minimum element.
- This approach is straightforward but may not be efficient for large arrays.

```cpp
int findMin(vector<int>& nums) {
    int minVal = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < minVal) {
            minVal = nums[i];
        }
    }
    return minVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we potentially check every element once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the minimum value.
> - **Why these complexities occur:** The time complexity is linear because we might have to check every element in the worst case, and the space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a modified binary search algorithm to find the minimum element in the rotated sorted array.
- We maintain two pointers, `left` and `right`, representing the current search range.
- If the middle element is greater than the rightmost element, the minimum must be in the right half; otherwise, it could be in the left half.
- We adjust the `left` and `right` pointers accordingly to narrow down the search range.

```cpp
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            // If nums[mid] equals nums[right], we can't be sure which half the minimum is in,
            // so we just decrement right to reduce the search space.
            right--;
        }
    }
    return nums[left];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ in the worst case (when all elements are the same), but $O(\log n)$ on average, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the pointers and the minimum value.
> - **Optimality proof:** The algorithm is optimal because it reduces the search space by half at each step on average, leading to a logarithmic time complexity. However, in the worst case (all elements being the same), it degrades to linear time complexity due to the need to check every element.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and adapting the algorithm accordingly.
- The use of binary search in solving problems related to sorted or partially sorted arrays.
- Handling edge cases and duplicates in the array.

**Mistakes to Avoid:**
- Not considering the case where all elements in the array are the same.
- Failing to adjust the search range correctly based on the comparison of the middle element and the rightmost element.
- Not handling the scenario where the middle element equals the rightmost element properly.

By following this approach, you can efficiently find the minimum element in a rotated sorted array with duplicates, leveraging the power of modified binary search to achieve an optimal solution.