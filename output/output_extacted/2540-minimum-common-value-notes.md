## Minimum Common Value
**Problem Link:** https://leetcode.com/problems/minimum-common-value/description

**Problem Statement:**
- Input format: Two integer arrays `nums1` and `nums2`.
- Constraints: `1 <= nums1.length, nums2.length <= 1000`, `1 <= nums1[i], nums2[i] <= 1000`.
- Expected output format: The minimum common value between the two arrays, or `-1` if no common value exists.
- Key requirements and edge cases to consider:
  - The arrays may not be sorted.
  - The arrays may contain duplicate values.
  - The arrays may not have any common values.
- Example test cases with explanations:
  - `nums1 = [1,2,3], nums2 = [3,4,5]`, output: `3`
  - `nums1 = [1,2,3], nums2 = [4,5,6]`, output: `-1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element in `nums1` with each element in `nums2`.
- Step-by-step breakdown of the solution:
  1. Iterate over each element in `nums1`.
  2. For each element in `nums1`, iterate over each element in `nums2`.
  3. If a common value is found, store it and break out of the inner loop.
  4. If no common value is found after iterating over all elements, return `-1`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution, but it has a high time complexity.

```cpp
int findCommonValue(vector<int>& nums1, vector<int>& nums2) {
    int minCommon = INT_MAX;
    for (int num1 : nums1) {
        for (int num2 : nums2) {
            if (num1 == num2) {
                minCommon = min(minCommon, num1);
                break;
            }
        }
    }
    return minCommon == INT_MAX ? -1 : minCommon;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `nums1` and `nums2`, respectively. This is because we are iterating over each element in `nums1` and for each element, we are iterating over each element in `nums2`.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the minimum common value.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `unordered_set` to store the elements of `nums1`, and then iterate over `nums2` to find the minimum common value.
- Detailed breakdown of the approach:
  1. Create an `unordered_set` to store the elements of `nums1`.
  2. Iterate over `nums2` and check if each element exists in the `unordered_set`.
  3. If a common value is found, store it and break out of the loop.
  4. If no common value is found after iterating over all elements, return `-1`.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal because we must at least read the input arrays once.

```cpp
int findCommonValue(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> numSet(nums1.begin(), nums1.end());
    int minCommon = INT_MAX;
    for (int num : nums2) {
        if (numSet.find(num) != numSet.end()) {
            minCommon = min(minCommon, num);
        }
    }
    return minCommon == INT_MAX ? -1 : minCommon;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `nums1` and `nums2`, respectively. This is because we are iterating over each element in `nums1` once to populate the `unordered_set`, and then iterating over each element in `nums2` once to find the minimum common value.
> - **Space Complexity:** $O(n)$, as we are storing the elements of `nums1` in the `unordered_set`.
> - **Optimality proof:** This approach is optimal because we must at least read the input arrays once, and the `unordered_set` allows us to check for existence in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Use of `unordered_set` to reduce time complexity.
- Problem-solving patterns identified: Using a data structure to store one array and then iterating over the other array to find a common value.
- Optimization techniques learned: Reducing time complexity by using a data structure with constant time lookup.
- Similar problems to practice: Problems that involve finding common elements between two arrays or sets.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for existence in the `unordered_set` correctly.
- Edge cases to watch for: Empty input arrays, arrays with duplicate values.
- Performance pitfalls: Using a data structure with high time complexity, such as a `vector` or `list`, to store the elements of `nums1`.
- Testing considerations: Test with different input sizes, including edge cases such as empty arrays or arrays with duplicate values.