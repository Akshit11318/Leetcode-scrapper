## Find Minimum in Rotated Sorted Array

**Problem Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description

**Problem Statement:**
- Input: A rotated sorted array of integers.
- Constraints: The array will have at least one element, and all elements are distinct.
- Expected Output: The minimum element in the rotated sorted array.
- Key Requirements and Edge Cases:
  - The array is sorted in ascending order but rotated (shifted) an unknown number of times.
  - The solution should find the minimum element efficiently, considering the rotation.
  - Example Test Cases:
    - Input: `[3, 4, 5, 1, 2]`
    - Output: `1`
    - Input: `[4, 5, 6, 7, 0, 1, 2]`
    - Output: `0`
    - Input: `[1]`
    - Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simply iterate through the array and find the smallest element.
- This approach is straightforward but not efficient for large arrays because it does not take advantage of the fact that the array is sorted and rotated.

```cpp
int findMin(vector<int>& nums) {
    int minElement = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < minElement) {
            minElement = nums[i];
        }
    }
    return minElement;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are potentially checking every element once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum element found so far.
> - **Why these complexities occur:** The time complexity is linear because, in the worst case, we have to check every element in the array to find the minimum. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that the array is sorted but rotated. This means we can use a modified binary search algorithm to find the minimum element efficiently.
- The idea is to divide the array into two halves and determine which half contains the minimum element based on the values at the middle and the ends of the array.
- We continue this process until we narrow down the search to the minimum element.

```cpp
int findMin(vector<int>& nums) {
    int left = 0, right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return nums[left];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array, because we divide the search space roughly in half with each iteration.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the indices and the middle element.
> - **Optimality proof:** This is optimal because we are using a binary search-like approach, which is the most efficient way to search in a sorted or partially sorted array. The rotation does not affect the overall time complexity because we adapt our search based on the comparison of elements.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated here is the adaptation of binary search for rotated sorted arrays.
- The problem-solving pattern identified involves recognizing the structure of the input data (sorted but rotated) and leveraging that to improve efficiency.
- The optimization technique learned is to divide the problem space efficiently, similar to binary search, to reduce the number of comparisons needed.

**Mistakes to Avoid:**
- A common mistake is not properly handling the edge cases, such as when the array is not rotated or when it contains duplicate elements.
- Another mistake is not correctly implementing the binary search logic, leading to incorrect results or inefficiencies.
- Testing considerations include ensuring the solution works for arrays of various sizes, including edge cases like arrays with one or two elements, and arrays that are rotated zero times (i.e., not rotated at all).