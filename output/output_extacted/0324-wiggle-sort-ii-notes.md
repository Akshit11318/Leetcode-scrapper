## Wiggle Sort II

**Problem Link:** https://leetcode.com/problems/wiggle-sort-ii/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, reorder it such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. 
- Expected output format: Modify the input array in-place.
- Key requirements and edge cases to consider: The length of the array is at least 1 and at most 5000. The array contains only positive integers.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1, 5, 1, 1, 6, 4]`, Output: `[1, 6, 1, 5, 1, 4]`
  - Example 2: Input: `nums = [1, 3, 2, 2, 3, 1]`, Output: `[2, 3, 1, 3, 1, 2]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to generate all possible permutations of the input array and check each permutation to see if it satisfies the wiggle sort condition.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input array.
  2. For each permutation, check if it satisfies the wiggle sort condition.
  3. If a permutation satisfies the condition, return it as the result.
- Why this approach comes to mind first: This approach is straightforward and ensures that we consider all possible solutions.

```cpp
#include <algorithm>
#include <vector>

void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<int> result(nums.size());
    int small = (nums.size() - 1) / 2;
    int large = nums.size() - 1;
    for (int i = 0; i < nums.size(); i++) {
        if (i % 2 == 0) {
            result[i] = nums[small--];
        } else {
            result[i] = nums[large--];
        }
    }
    nums = result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to storing the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the sorted array to construct the wiggle sorted array.
- Detailed breakdown of the approach:
  1. Sort the input array in ascending order.
  2. Initialize two pointers, one at the middle of the sorted array and one at the end.
  3. Alternate between the two pointers to fill the result array, starting from the first element.
- Proof of optimality: This approach has a time complexity of $O(n \log n)$ due to sorting, and a space complexity of $O(n)$ for storing the result. This is optimal because we must at least read the input array and write the output array.

```cpp
#include <algorithm>
#include <vector>

void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<int> result(nums.size());
    int small = (nums.size() - 1) / 2;
    int large = nums.size() - 1;
    for (int i = 0; i < nums.size(); i++) {
        if (i % 2 == 0) {
            result[i] = nums[small--];
        } else {
            result[i] = nums[large--];
        }
    }
    nums = result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Optimality proof:** The time complexity is dominated by the sorting operation, and the space complexity is due to storing the result. This is optimal because we must at least read the input array and write the output array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two-pointer technique.
- Problem-solving patterns identified: Using sorting to simplify the problem, and then applying a two-pointer technique to construct the result.
- Optimization techniques learned: Avoiding unnecessary operations by using a single pass through the sorted array.
- Similar problems to practice: Other problems involving sorting and two-pointer techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: An input array with a single element, or an input array with duplicate elements.
- Performance pitfalls: Using an inefficient sorting algorithm, or using unnecessary operations to construct the result.
- Testing considerations: Testing the function with a variety of input arrays, including edge cases.