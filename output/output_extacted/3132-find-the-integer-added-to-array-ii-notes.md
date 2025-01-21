## Find the Integer Added to Array II

**Problem Link:** https://leetcode.com/problems/find-the-integer-added-to-array-ii/description

**Problem Statement:**
- Given an array of integers `nums` that is sorted in ascending order and rotated at some pivot unknown to you beforehand, find the integer added to the array.
- The input array is guaranteed to have at least one element and will not have any duplicates.
- For example, if the input array is `[3, 4, 5, 0, 2]`, then the pivot is `3`, and the integer added is `3`.
- If the input array is `[4, 5, 6, 7, 0, 1, 2]`, then the pivot is `0`, and the integer added is `0`.
- The expected output is the integer that was added to the array.

**Key Requirements and Edge Cases:**
- The array is sorted in ascending order and rotated at some pivot.
- The array does not contain duplicates.
- The pivot is unknown beforehand.

**Example Test Cases:**
- Input: `[3, 4, 5, 0, 2]`, Output: `3`
- Input: `[4, 5, 6, 7, 0, 1, 2]`, Output: `0`
- Input: `[0, 1, 2, 3, 4, 5]`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to find the pivot element in the array, which is the smallest element.
- We can find the pivot element by iterating through the array and checking if the current element is smaller than the previous element.
- Once we find the pivot element, we can return it as the integer added to the array.

```cpp
int findIntegerAdded(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i - 1]) {
            return nums[i];
        }
    }
    return nums[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are checking each element in the array once, and the space complexity occurs because we are only using a constant amount of space to store the pivot element.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a binary search approach to find the pivot element.
- We can use a binary search approach because the array is sorted in ascending order and rotated at some pivot.
- We can find the pivot element by checking the middle element of the array and determining which half of the array it belongs to.

```cpp
int findIntegerAdded(vector<int>& nums) {
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
> - **Time Complexity:** $O(\log n)$, where $n$ is the size of the input array, because we are using a binary search approach.
> - **Space Complexity:** $O(1)$, because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This is the optimal solution because we are using a binary search approach, which has a time complexity of $O(\log n)$, and we are not using any extra space that scales with the input size.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a binary search approach to find the pivot element in a sorted and rotated array.
- The problem-solving pattern identified is to use a divide-and-conquer approach to solve the problem.
- The optimization technique learned is to use a binary search approach to reduce the time complexity of the solution.

**Mistakes to Avoid:**
- A common implementation error is to not handle the edge case where the input array is not rotated.
- A performance pitfall is to use a brute force approach to find the pivot element, which has a time complexity of $O(n)$.
- A testing consideration is to test the solution with different input arrays to ensure that it works correctly in all cases.