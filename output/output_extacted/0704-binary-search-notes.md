## Binary Search

**Problem Link:** https://leetcode.com/problems/binary-search/description

**Problem Statement:**
- Input: A sorted array `nums` of integers and a target value `target`.
- Constraints: `1 <= nums.length <= 10^4`, `-10^4 <= nums[i], target <= 10^4`, and `nums` is sorted in ascending order.
- Expected Output: The index of the `target` in the array if it exists, otherwise -1.
- Key Requirements: The solution must efficiently search for the target in the sorted array.
- Edge Cases: Handle cases where the target is not present, the array is empty, or the array contains duplicate elements.
- Example Test Cases:
  - Input: `nums = [-1,0,3,5,9,12], target = 9`, Output: `4`
  - Input: `nums = [-1,0,3,5,9,12], target = 2`, Output: `-1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and check each element to see if it matches the target.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
int search(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) {
            return i;
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through each element once.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the index and target.
> - **Why these complexities occur:** The time complexity is linear because we are checking each element individually, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search algorithm, which takes advantage of the fact that the array is sorted.
- We can divide the search space in half at each step, reducing the number of elements to check.
- This approach is optimal because it has the best possible time complexity for searching a sorted array.

```cpp
int search(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array, because we are dividing the search space in half at each step.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the indices and target.
> - **Optimality proof:** This is the best possible time complexity for searching a sorted array because we are reducing the search space by half at each step, which is the most efficient way to search a sorted array.

---

### Final Notes

**Learning Points:**
- The importance of taking advantage of the structure of the input data (in this case, the sorted array).
- The use of binary search as an efficient algorithm for searching sorted arrays.
- The trade-off between time and space complexity.

**Mistakes to Avoid:**
- Not checking for edge cases, such as an empty array or a target that is not present in the array.
- Not using a binary search algorithm, which can lead to inefficient search times for large arrays.
- Not considering the structure of the input data when designing an algorithm.