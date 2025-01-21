## Check if Array is Sorted and Rotated

**Problem Link:** https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description

**Problem Statement:**
- Input format: An integer array `nums` of length `n`.
- Constraints: `1 <= n <= 100` and `1 <= nums[i] <= 100`.
- Expected output format: A boolean indicating whether the array is sorted and rotated.
- Key requirements and edge cases to consider:
  - An empty array is considered sorted.
  - A single-element array is considered sorted.
  - An array with two elements is considered sorted if the elements are in ascending order.
- Example test cases with explanations:
  - `[3, 4, 5, 1, 2]` returns `true` because it is a rotated sorted array.
  - `[4, 5, 1, 2, 3]` returns `true` because it is a rotated sorted array.
  - `[1, 2, 3, 4, 5]` returns `true` because it is a sorted array.
  - `[5, 4, 3, 2, 1]` returns `false` because it is not a sorted or rotated sorted array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible rotation of the array and verify if it's sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible rotations of the array.
  2. For each rotation, check if the array is sorted.
  3. If any rotation is sorted, return `true`.
- Why this approach comes to mind first: It's straightforward to generate all rotations and check for sorted order.

```cpp
bool check(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        bool isSorted = true;
        for (int j = 1; j < n; j++) {
            if (nums[(i + j) % n] < nums[(i + j - 1) % n]) {
                isSorted = false;
                break;
            }
        }
        if (isSorted) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we're generating all rotations ($O(n)$) and checking each rotation for sorted order ($O(n)$).
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with input size.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the lack of additional space allocation keeps the space complexity constant.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all rotations, we can find the minimum element in the array and verify if the array is sorted when rotated around that point.
- Detailed breakdown of the approach:
  1. Find the minimum element in the array.
  2. Check if the array is sorted when rotated around the minimum element.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array to find the minimum element and check for sorted order.

```cpp
bool check(vector<int>& nums) {
    int n = nums.size();
    if (n <= 1) return true;
    int minIndex = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i] < nums[minIndex]) {
            minIndex = i;
        }
    }
    for (int i = 0; i < n - 1; i++) {
        if (nums[(minIndex + i) % n] > nums[(minIndex + i + 1) % n]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we're making a single pass through the array to find the minimum element and check for sorted order.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the minimum element in an array and checking for sorted order.
- Problem-solving patterns identified: Using a single pass through the array to optimize the solution.
- Optimization techniques learned: Avoiding unnecessary iterations and using a single pass to reduce time complexity.
- Similar problems to practice: Finding the maximum element in an array, checking for sorted order in a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty or single-element arrays.
- Edge cases to watch for: Arrays with duplicate elements, arrays with negative numbers.
- Performance pitfalls: Using nested loops or recursive functions that can lead to high time complexity.
- Testing considerations: Testing the solution with various input sizes and edge cases to ensure correctness.