## Maximum Distance Between a Pair of Values

**Problem Link:** https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description

**Problem Statement:**
- Input format and constraints: Given two arrays `nums1` and `nums2` of length `m` and `n`, respectively, find the maximum distance between a pair of values, one from each array, such that the value from `nums1` is less than or equal to the value from `nums2`.
- Expected output format: The maximum distance between the pair of values.
- Key requirements and edge cases to consider: Handle cases where one or both arrays are empty, and consider the scenario where no such pair exists.
- Example test cases with explanations:
  - Example 1: `nums1 = [55,30,5,4,2]`, `nums2 = [100,20,10,10,5]`. The maximum distance is `2`, achieved by pairing `nums1[1] = 30` with `nums2[0] = 100`.
  - Example 2: `nums1 = [2,2,2,10,10]`, `nums2 = [10]`. The maximum distance is `8`, achieved by pairing `nums1[0] = 2` with `nums2[0] = 10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element from `nums1` with every element in `nums2` to find pairs where the value from `nums1` is less than or equal to the value from `nums2`.
- Step-by-step breakdown of the solution:
  1. Iterate over each element in `nums1`.
  2. For each element in `nums1`, iterate over each element in `nums2`.
  3. Check if the current element from `nums1` is less than or equal to the current element from `nums2`.
  4. If the condition is met, calculate the distance between the indices of the two elements.
  5. Update the maximum distance found so far.
- Why this approach comes to mind first: It is straightforward to consider comparing each element from one array with every element in the other array to find the maximum distance.

```cpp
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int maxDist = 0;
        for (int i = 0; i < nums1.size(); i++) {
            for (int j = 0; j < nums2.size(); j++) {
                if (nums1[i] <= nums2[j]) {
                    maxDist = max(maxDist, abs(j - i));
                }
            }
        }
        return maxDist;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ and $n$ are the sizes of `nums1` and `nums2`, respectively. This is because we have nested loops iterating over both arrays.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum distance and indices.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, but it has a low space complexity since it only uses a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since we want the maximum distance, we can start from the end of both arrays and move backwards. This allows us to take advantage of the fact that the maximum distance will be obtained by pairing elements that are as far apart as possible.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the end of `nums1` and one at the end of `nums2`.
  2. Move the pointers backwards, checking if the current elements satisfy the condition `nums1[i] <= nums2[j]`.
  3. If the condition is met, update the maximum distance.
  4. Continue moving the pointers until one of them reaches the beginning of its array.
- Proof of optimality: This approach is optimal because it ensures that we consider the maximum possible distance between elements from `nums1` and `nums2` by starting from the end and moving backwards.

```cpp
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int maxDist = 0;
        int i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] <= nums2[j]) {
                maxDist = max(maxDist, j - i);
                j++;
            } else {
                i++;
            }
        }
        return maxDist;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where $m$ and $n$ are the sizes of `nums1` and `nums2`, respectively. This is because we only need to iterate over both arrays once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum distance and indices.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and only requires a constant amount of space, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, optimization of brute force approach.
- Problem-solving patterns identified: Considering the maximum possible distance between elements, using pointers to iterate over arrays.
- Optimization techniques learned: Starting from the end of arrays and moving backwards to take advantage of the maximum distance.
- Similar problems to practice: Other problems involving arrays and pointers, such as finding the maximum sum of a subarray.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty arrays.
- Edge cases to watch for: Handling cases where one or both arrays are empty.
- Performance pitfalls: Using nested loops instead of the two-pointer technique.
- Testing considerations: Testing the function with different input arrays, including edge cases.