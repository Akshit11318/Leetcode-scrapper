## Find the Difference of Two Arrays
**Problem Link:** https://leetcode.com/problems/find-the-difference-of-two-arrays/description

**Problem Statement:**
- Input format and constraints: Given two `0-indexed` integer arrays `nums1` and `nums2`, find the difference of the two arrays.
- Expected output format: Return an array containing all the elements that are in exactly one of the input arrays.
- Key requirements and edge cases to consider: Handle cases where input arrays may have duplicate elements, may have varying lengths, or may be empty.
- Example test cases with explanations: For example, `nums1 = [1, 2, 3]` and `nums2 = [2, 4, 6]`, the output should be `[1, 3, 4, 6]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element in `nums1` with every element in `nums2` to find unique elements.
- Step-by-step breakdown of the solution:
  1. Create a result array `res`.
  2. Iterate through `nums1`. For each element, check if it exists in `nums2`. If not, add it to `res`.
  3. Iterate through `nums2`. For each element, check if it exists in `nums1`. If not, add it to `res`.
- Why this approach comes to mind first: It directly addresses the requirement of finding elements that are in exactly one of the arrays by comparing each element of one array against all elements of the other array.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> findDifference(std::vector<int>& nums1, std::vector<int>& nums2) {
    std::vector<int> res;
    for (int num : nums1) {
        if (std::find(nums2.begin(), nums2.end(), num) == nums2.end()) {
            res.push_back(num);
        }
    }
    for (int num : nums2) {
        if (std::find(nums1.begin(), nums1.end(), num) == nums1.end()) {
            res.push_back(num);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n*m)$, where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively, because for each element in one array, we potentially scan the entire other array.
> - **Space Complexity:** $O(n + m)$, for storing the result array.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the input arrays, leading to quadratic time complexity in the worst case. The space complexity is linear with respect to the total number of elements across both arrays because we store unique elements from both arrays in the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a `std::unordered_set` to store elements from one array, allowing for constant time lookup when iterating through the other array.
- Detailed breakdown of the approach:
  1. Create an `unordered_set` from `nums1`.
  2. Create a result vector `res`.
  3. Iterate through `nums2`. For each element, check if it exists in the `unordered_set`. If not, add it to `res`.
  4. Iterate through the original `nums1` array. For each element, check if it exists in `nums2` (by creating a set from `nums2` or using another set). If not, add it to `res`.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the nested iteration over the arrays, instead using constant time lookups in the set.

```cpp
#include <vector>
#include <unordered_set>

std::vector<int> findDifference(std::vector<int>& nums1, std::vector<int>& nums2) {
    std::unordered_set<int> set1(nums1.begin(), nums1.end());
    std::unordered_set<int> set2(nums2.begin(), nums2.end());
    std::vector<int> res;
    for (int num : nums1) {
        if (set2.find(num) == set2.end()) {
            res.push_back(num);
        }
    }
    for (int num : nums2) {
        if (set1.find(num) == set1.end()) {
            res.push_back(num);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively, because we perform a single pass over each array to populate the sets and then another pass to find the differences.
> - **Space Complexity:** $O(n + m)$, for storing the sets and the result array.
> - **Optimality proof:** This approach is optimal because it achieves linear time complexity, which is the best possible for this problem since we must at least read the input arrays once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `unordered_set` for efficient lookups, reducing time complexity by avoiding nested iterations.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (e.g., creating sets for efficient lookup).
- Optimization techniques learned: Utilizing data structures like sets for constant time operations.
- Similar problems to practice: Other problems involving set operations or finding differences between collections.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly assuming that `std::find` on a vector is constant time, forgetting to handle edge cases like empty input arrays.
- Edge cases to watch for: Handling duplicate elements within the arrays, ensuring the solution works for arrays of different lengths.
- Performance pitfalls: Using algorithms with higher time complexity than necessary, such as nested iterations over large datasets.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and performance.