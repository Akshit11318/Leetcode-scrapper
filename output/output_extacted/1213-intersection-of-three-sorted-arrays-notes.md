## Intersection of Three Sorted Arrays
**Problem Link:** https://leetcode.com/problems/intersection-of-three-sorted-arrays/description

**Problem Statement:**
- Input format: Three sorted arrays `nums1`, `nums2`, and `nums3`.
- Constraints: All elements in each array are distinct.
- Expected output format: A list of common elements in all three arrays.
- Key requirements and edge cases to consider: Handling empty arrays, duplicate elements across arrays, and arrays of varying lengths.
- Example test cases with explanations:
  - Example 1: `nums1 = [1,2,3]`, `nums2 = [4,5,6]`, `nums3 = [7,8,9]`. Output: `[]`.
  - Example 2: `nums1 = [1,2,3]`, `nums2 = [1,2,3]`, `nums3 = [1,2,3]`. Output: `[1,2,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every element in `nums1` against all elements in `nums2` and `nums3` to find common elements.
- Step-by-step breakdown of the solution:
  1. Iterate through each element in `nums1`.
  2. For each element in `nums1`, iterate through all elements in `nums2` and `nums3` to find a match.
  3. If a match is found in both `nums2` and `nums3`, add it to the result list.
- Why this approach comes to mind first: It's the most straightforward way to ensure we find all common elements, but it's inefficient due to the nested loops.

```cpp
#include <vector>

std::vector<int> intersectionOfThreeSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<int>& nums3) {
    std::vector<int> result;
    for (int num : nums1) {
        bool foundInNums2 = false;
        bool foundInNums3 = false;
        for (int n : nums2) {
            if (n == num) {
                foundInNums2 = true;
                break;
            }
        }
        for (int n : nums3) {
            if (n == num) {
                foundInNums3 = true;
                break;
            }
        }
        if (foundInNums2 && foundInNums3) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot p)$, where $n$, $m$, and $p$ are the lengths of `nums1`, `nums2`, and `nums3`, respectively. This is because for each element in `nums1`, we potentially iterate through all elements in `nums2` and `nums3`.
> - **Space Complexity:** $O(k)$, where $k$ is the number of common elements. This is for storing the result.
> - **Why these complexities occur:** The brute force approach involves nested loops, leading to high time complexity, and the space complexity is directly related to the number of common elements found.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the arrays are sorted, we can use three pointers to traverse `nums1`, `nums2`, and `nums3` simultaneously, comparing the elements at the current positions of the pointers.
- Detailed breakdown of the approach:
  1. Initialize three pointers, one for each array, to the beginning of each array.
  2. Compare the elements at the current positions of the pointers. If they are equal, add the element to the result and move all three pointers forward.
  3. If the elements are not equal, move the pointer pointing to the smallest element forward, as it cannot be part of the intersection if it's smaller than the others.
- Proof of optimality: This approach ensures we find all common elements in a single pass through the arrays, resulting in the best possible time complexity for this problem.
- Why further optimization is impossible: We must at least look at each element once to determine if it's part of the intersection, making the time complexity of this approach optimal.

```cpp
#include <vector>

std::vector<int> intersectionOfThreeSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<int>& nums3) {
    std::vector<int> result;
    int i = 0, j = 0, k = 0;
    while (i < nums1.size() && j < nums2.size() && k < nums3.size()) {
        if (nums1[i] == nums2[j] && nums2[j] == nums3[k]) {
            result.push_back(nums1[i]);
            i++; j++; k++;
        } else if (nums1[i] <= nums2[j] && nums1[i] <= nums3[k]) {
            i++;
        } else if (nums2[j] <= nums1[i] && nums2[j] <= nums3[k]) {
            j++;
        } else {
            k++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + p)$, where $n$, $m`, and $p$ are the lengths of `nums1`, `nums2`, and `nums3`, respectively. This is because we make a single pass through each array.
> - **Space Complexity:** $O(k)$, where $k$ is the number of common elements. This is for storing the result.
> - **Optimality proof:** The optimal approach has a linear time complexity with respect to the total number of elements across all arrays, which is the best achievable for this problem since we must examine each element at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using multiple pointers to traverse sorted arrays, comparing elements, and making decisions based on those comparisons.
- Problem-solving patterns identified: The importance of recognizing the structure of the input data (sorted arrays) and leveraging that to reduce the complexity of the solution.
- Optimization techniques learned: Reducing the number of comparisons needed by moving pointers based on the relative sizes of the elements they point to.
- Similar problems to practice: Finding the intersection of two sorted arrays, merging sorted arrays, and other problems involving sorted data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases such as empty arrays or arrays of different lengths.
- Edge cases to watch for: Ensuring the solution correctly handles arrays with duplicate elements (though in this problem, all elements in each array are distinct).
- Performance pitfalls: Failing to recognize the sorted nature of the input arrays and using a brute force approach instead of a more efficient algorithm.
- Testing considerations: Thoroughly testing the solution with a variety of input cases, including edge cases, to ensure correctness and performance.