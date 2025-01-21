## Median of Two Sorted Arrays
**Problem Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/description

**Problem Statement:**
- Input format and constraints: Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array.
- Expected output format: Return the median as a single number.
- Key requirements and edge cases to consider: The input arrays are sorted, and the total number of elements can be odd or even.
- Example test cases with explanations:
  - Example 1: `nums1 = [1,3]`, `nums2 = [2]`, Output: `2.00000`
  - Example 2: `nums1 = [1,2]`, `nums2 = [3,4]`, Output: `(2 + 3) / 2 = 2.5`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Merge the two sorted arrays into a single array and then find the median.
- Step-by-step breakdown of the solution:
  1. Merge `nums1` and `nums2` into a single array `merged`.
  2. Sort the `merged` array.
  3. Calculate the length of the `merged` array.
  4. If the length is odd, return the middle element. If the length is even, return the average of the two middle elements.
- Why this approach comes to mind first: It is the most straightforward way to find the median of two sorted arrays.

```cpp
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<int> merged;
    for (int num : nums1) {
        merged.push_back(num);
    }
    for (int num : nums2) {
        merged.push_back(num);
    }
    sort(merged.begin(), merged.end());
    int n = merged.size();
    if (n % 2 == 1) {
        return merged[n / 2];
    } else {
        return (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((m+n) \log(m+n))$, where $m$ and $n$ are the sizes of `nums1` and `nums2` respectively. The time complexity is dominated by the sorting operation.
> - **Space Complexity:** $O(m+n)$, as we need to store the merged array.
> - **Why these complexities occur:** The sorting operation takes $O(n \log n)$ time in the worst case, and we need to store all elements in the merged array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a modified binary search approach to find the median without actually merging the two arrays.
- Detailed breakdown of the approach:
  1. Calculate the total length of the two arrays.
  2. If the total length is odd, we need to find the middle element. If the total length is even, we need to find the average of the two middle elements.
  3. Use binary search to find the partition point for `nums1` and `nums2` such that the elements on the left side of the partition point in both arrays are less than or equal to the elements on the right side.
- Proof of optimality: This approach has a time complexity of $O(\log(\min(m,n)))$, which is optimal because we are using binary search to find the partition point.

```cpp
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size();
    int n = nums2.size();
    if (m > n) {
        return findMedianSortedArrays(nums2, nums1);
    }
    int left = 0;
    int right = m;
    while (left <= right) {
        int i = (left + right) / 2;
        int j = (m + n + 1) / 2 - i;
        int maxLeftX = (i == 0) ? INT_MIN : nums1[i - 1];
        int minRightX = (i == m) ? INT_MAX : nums1[i];
        int maxLeftY = (j == 0) ? INT_MIN : nums2[j - 1];
        int minRightY = (j == n) ? INT_MAX : nums2[j];
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((m + n) % 2 == 0) {
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
            } else {
                return (double)max(maxLeftX, maxLeftY);
            }
        } else if (maxLeftX > minRightY) {
            right = i - 1;
        } else {
            left = i + 1;
        }
    }
    return 0.0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log(\min(m,n)))$, where $m$ and $n$ are the sizes of `nums1` and `nums2` respectively. The time complexity is dominated by the binary search operation.
> - **Space Complexity:** $O(1)$, as we only need a constant amount of space to store the indices and the maximum and minimum values.
> - **Optimality proof:** The binary search approach allows us to find the partition point in $O(\log(\min(m,n)))$ time, which is optimal because we are reducing the search space by half at each step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, partitioning, and median calculation.
- Problem-solving patterns identified: Using binary search to find the partition point and calculating the median based on the total length of the arrays.
- Optimization techniques learned: Reducing the search space by half at each step using binary search.
- Similar problems to practice: Finding the k-th smallest element in two sorted arrays, finding the intersection of two sorted arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the edge cases correctly, such as when one of the arrays is empty or when the total length is odd or even.
- Edge cases to watch for: The arrays can be of different sizes, and the total length can be odd or even.
- Performance pitfalls: Using a naive approach that merges the two arrays and sorts the result, which can lead to a time complexity of $O((m+n) \log(m+n))$.
- Testing considerations: Test the function with different input cases, including edge cases and large inputs, to ensure that it works correctly and efficiently.