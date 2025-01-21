## Wiggle Sort
**Problem Link:** https://leetcode.com/problems/wiggle-sort/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `nums` as input, where `1 <= nums.length <= 5000` and `0 <= nums[i] <= 10^6`. The goal is to modify the array in-place to achieve a wiggle sort order.
- Expected output format: The output is the modified array itself, where the elements are rearranged to satisfy the wiggle sort condition.
- Key requirements and edge cases to consider: The wiggle sort condition states that for the modified array, every even-indexed element should be smaller than its adjacent elements, and every odd-indexed element should be larger than its adjacent elements.
- Example test cases with explanations:
  - For the input `[1, 5, 1, 1, 6, 4]`, one possible wiggle sort order is `[1, 6, 1, 5, 1, 4]`.
  - For the input `[1, 2, 2, 1, 2, 1, 1]`, one possible wiggle sort order is `[1, 2, 1, 2, 1, 2, 1]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach to solving this problem might involve sorting the array and then rearranging the elements to satisfy the wiggle sort condition.
- Step-by-step breakdown of the solution:
  1. Sort the array in ascending order.
  2. Initialize two pointers, one at the beginning of the array and one at the end.
  3. Create a new array to store the wiggle sorted elements.
  4. Alternate between the smallest and largest remaining elements, placing them in the new array in a way that satisfies the wiggle sort condition.
- Why this approach comes to mind first: This approach is straightforward and involves well-known operations like sorting and iterating through the array.

```cpp
void wiggleSort(vector<int>& nums) {
    // Sort the array
    sort(nums.begin(), nums.end());
    
    // Initialize pointers
    int small = 0, large = nums.size() - 1;
    
    // Create a copy of the array to store the wiggle sorted elements
    vector<int> copy = nums;
    
    // Alternate between smallest and largest elements
    for (int i = 0; i < nums.size(); i++) {
        if (i % 2 == 0) {
            // Even index, place the smallest element
            nums[i] = copy[small++];
        } else {
            // Odd index, place the largest element
            nums[i] = copy[large--];
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$ for creating a copy of the array.
> - **Why these complexities occur:** The sorting step dominates the time complexity, while the space complexity is due to the additional array needed to store the wiggle sorted elements.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire array, we can use a single pass through the array to rearrange the elements in-place, satisfying the wiggle sort condition.
- Detailed breakdown of the approach:
  1. Iterate through the array, comparing adjacent elements.
  2. If an even-indexed element is not smaller than its next element, swap them.
  3. If an odd-indexed element is not larger than its next element, swap them.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in a linear time complexity.

```cpp
void wiggleSort(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; i++) {
        if (i % 2 == 0 && nums[i] > nums[i + 1]) {
            // Even index, swap if not smaller
            swap(nums[i], nums[i + 1]);
        } else if (i % 2 == 1 && nums[i] < nums[i + 1]) {
            // Odd index, swap if not larger
            swap(nums[i], nums[i + 1]);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, since we only need a single pass through the array.
> - **Space Complexity:** $O(1)$, as we are modifying the array in-place.
> - **Optimality proof:** This approach is optimal because it achieves the wiggle sort condition in a single pass, with no additional data structures needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, single-pass algorithms, and the importance of understanding the problem constraints.
- Problem-solving patterns identified: Recognizing the need for a single pass through the data and leveraging the properties of the wiggle sort condition.
- Optimization techniques learned: Avoiding unnecessary sorting or data structure creation, and focusing on in-place modifications.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate elements, or arrays that are already in wiggle sort order.
- Performance pitfalls: Using sorting algorithms or creating unnecessary data structures, leading to suboptimal time or space complexity.
- Testing considerations: Thoroughly testing the implementation with various input cases, including edge cases and large inputs.