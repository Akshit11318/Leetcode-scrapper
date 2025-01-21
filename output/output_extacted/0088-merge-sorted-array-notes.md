## Merge Sorted Array

**Problem Link:** https://leetcode.com/problems/merge-sorted-array/description

**Problem Statement:**
- Input format: Two sorted arrays `nums1` and `nums2`, and their respective sizes `m` and `n`.
- Constraints: `nums1` has enough space to hold all elements from both arrays, i.e., `nums1.length = m + n`.
- Expected output: Merge `nums2` into `nums1` in a sorted manner.
- Key requirements: The resulting array should be sorted in ascending order.
- Edge cases: Handle cases where either `m` or `n` is 0.

**Example Test Cases:**

- `nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`, `nums2 = [2, 5, 6]`, `n = 3`
  Output: `nums1 = [1, 2, 2, 3, 5, 6]`
- `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
  Output: `nums1 = [1]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to merge the two arrays into a new array and then sort this new array.
- This approach involves creating a temporary array to store the merged elements and then using a sorting algorithm (like `sort()` function in C++).
- This comes to mind first because it directly addresses the requirement of merging and sorting without considering the efficiency of the operation.

```cpp
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    // Create a temporary vector to hold all elements
    vector<int> temp;
    
    // Copy elements from nums1 into temp
    for (int i = 0; i < m; i++) {
        temp.push_back(nums1[i]);
    }
    
    // Copy elements from nums2 into temp
    for (int i = 0; i < n; i++) {
        temp.push_back(nums2[i]);
    }
    
    // Sort the temporary vector
    sort(temp.begin(), temp.end());
    
    // Copy sorted elements back into nums1
    for (int i = 0; i < m + n; i++) {
        nums1[i] = temp[i];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((m + n) \log(m + n))$ due to the sorting operation.
> - **Space Complexity:** $O(m + n)$ for the temporary vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the need for a temporary vector to hold all elements dictates the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to take advantage of the fact that both input arrays are already sorted.
- We can use a two-pointer technique to compare elements from the end of both arrays and place the larger one at the end of `nums1`.
- This approach avoids the need for a temporary array and the subsequent sorting operation.
- It's optimal because it only requires a single pass through the arrays, leveraging their sorted nature.

```cpp
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int p1 = m - 1; // Pointer for nums1
    int p2 = n - 1; // Pointer for nums2
    int p = m + n - 1; // Pointer for the current position in nums1
    
    // Compare elements from nums1 and nums2 and place the larger one at the end of nums1
    while ((p1 >= 0) && (p2 >= 0)) {
        nums1[p--] = (nums1[p1] > nums2[p2]) ? nums1[p1--] : nums2[p2--];
    }
    
    // Copy remaining elements from nums2, if any
    while (p2 >= 0) {
        nums1[p--] = nums2[p2--];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, as we're making a single pass through both arrays.
> - **Space Complexity:** $O(1)$, since we're modifying the input array in-place without using any additional space that scales with input size.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each element once to merge and sort them.

---

### Final Notes

**Learning Points:**
- Utilizing the sorted nature of input arrays to simplify the merging process.
- Applying a two-pointer technique for efficient comparison and placement of elements.
- Avoiding unnecessary operations like sorting when the input is already partially ordered.

**Mistakes to Avoid:**
- Not considering the sorted nature of the input arrays, leading to inefficient solutions.
- Failing to handle edge cases where one or both of the input arrays are empty.
- Not optimizing the space complexity by using in-place modifications when possible.