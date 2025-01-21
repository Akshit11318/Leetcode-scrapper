## Height Checker
**Problem Link:** [https://leetcode.com/problems/height-checker/description](https://leetcode.com/problems/height-checker/description)

**Problem Statement:**
- Input: An array of integers `heights` where `heights[i]` is the height of the `i-th` student.
- Output: The number of students that are not standing in the correct position in the sorted array.
- Constraints: `1 <= heights.length <= 100`, `1 <= heights[i] <= 100`.
- Key requirements: Count the number of students that are not standing in the correct position after sorting the heights in non-decreasing order.
- Edge cases: An empty array or an array with a single element.

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each student's height with their corresponding height in the sorted array.
- Step-by-step breakdown of the solution:
  1. Create a copy of the input array `heights`.
  2. Sort the copied array in non-decreasing order.
  3. Iterate through the original and sorted arrays simultaneously.
  4. If the heights at the current index are different, increment a counter.
  5. Return the counter as the result.
- Why this approach comes to mind first: It directly addresses the problem by comparing each student's height with their expected height in the sorted array.

```cpp
int heightChecker(vector<int>& heights) {
    vector<int> sortedHeights = heights;
    sort(sortedHeights.begin(), sortedHeights.end());
    int count = 0;
    for (int i = 0; i < heights.size(); i++) {
        if (heights[i] != sortedHeights[i]) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of students.
> - **Space Complexity:** $O(n)$ for creating a copy of the input array.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and creating a copy of the array contributes to the space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of sorting the entire array, we can use a frequency count of heights to determine the correct position of each student.
- Detailed breakdown of the approach:
  1. Count the frequency of each height in the input array.
  2. Initialize an index to keep track of the current position in the sorted array.
  3. Iterate through the input array, and for each height, find its correct position in the sorted array by using the frequency count.
  4. If the current height does not match the expected height at the current position, increment a counter.
  5. Update the frequency count and index accordingly.
- Proof of optimality: This approach has a linear time complexity, which is optimal for this problem.

```cpp
int heightChecker(vector<int>& heights) {
    vector<int> count(101, 0); // Frequency count of heights
    for (int height : heights) {
        count[height]++;
    }
    int res = 0;
    int j = 0; // Index for the sorted array
    for (int i = 0; i < heights.size(); i++) {
        while (count[j] == 0) {
            j++;
        }
        if (j != heights[i]) {
            res++;
        }
        count[j]--;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of students.
> - **Space Complexity:** $O(1)$, since the space used does not grow with the input size (assuming a fixed range of heights).
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array and uses a constant amount of extra space.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, iteration, and comparison.
- Problem-solving patterns identified: Using frequency counts to solve problems involving arrays and sorting.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary operations (in this case, sorting the entire array).
- Similar problems to practice: Other problems involving array manipulation and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays with duplicate heights.
- Performance pitfalls: Using inefficient algorithms or data structures, such as sorting the entire array when a more efficient approach is available.
- Testing considerations: Test the function with various input arrays, including edge cases, to ensure correctness and efficiency.