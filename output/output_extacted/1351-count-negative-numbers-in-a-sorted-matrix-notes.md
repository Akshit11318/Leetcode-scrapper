## Count Negative Numbers in a Sorted Matrix

**Problem Link:** https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description

**Problem Statement:**
- Input: A `m x n` matrix `grid` where each element is an integer and all rows are sorted in non-decreasing order.
- Constraints: `1 <= m <= 100`, `1 <= n <= 100`, and `-100 <= grid[i][j] <= 100`.
- Expected Output: The number of negative numbers in the `grid`.
- Key Requirements: Efficiently count negative numbers in a sorted matrix.
- Edge Cases: Consider cases where the matrix is empty, contains all non-negative numbers, or all negative numbers.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each element in the matrix and checking if it's negative.
- Step-by-step breakdown:
  1. Initialize a counter for negative numbers.
  2. Iterate over each row in the matrix.
  3. For each row, iterate over each column.
  4. Check if the current element is negative; if so, increment the counter.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int countNegatives(vector<vector<int>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] < 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we are potentially checking every element once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our count and loop indices.
> - **Why these complexities occur:** The brute force approach requires checking each element in the matrix, leading to linear time complexity relative to the total number of elements. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Since each row is sorted in non-decreasing order, once we encounter a negative number, all numbers to its right in the same row will also be negative.
- Detailed breakdown:
  1. Initialize a counter for negative numbers.
  2. Iterate over each row in the matrix.
  3. For each row, find the first negative number using a binary search approach.
  4. Once the first negative number is found in a row, increment the counter by the number of elements to its right (including itself).
- Proof of optimality: This approach minimizes the number of comparisons needed by leveraging the sorted nature of the rows.

```cpp
int countNegatives(vector<vector<int>>& grid) {
    int count = 0;
    for (auto& row : grid) {
        int left = 0, right = row.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (row[mid] < 0) {
                right = mid - 1; // Continue searching in the left half
            } else {
                left = mid + 1; // Continue searching in the right half
            }
        }
        // 'left' now points to the first negative number or is equal to row.size() if no negatives are found
        count += row.size() - left;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot \log n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because for each row, we perform a binary search.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space for our loop indices and counter.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find all negative numbers in the sorted rows, leveraging the property that once a negative number is found, all subsequent numbers in the row are also negative.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, leveraging sorted data for efficiency.
- Problem-solving patterns identified: Finding the first occurrence of a condition in a sorted sequence.
- Optimization techniques learned: Using binary search to reduce the number of comparisons needed.
- Similar problems to practice: Other problems involving finding elements in sorted arrays or matrices.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing binary search, not handling edge cases (like an empty matrix or rows/columns with all non-negative numbers).
- Edge cases to watch for: Empty matrices, matrices with all non-negative or all negative numbers.
- Performance pitfalls: Not leveraging the sorted nature of the data, leading to inefficient solutions.
- Testing considerations: Thoroughly test with various input scenarios, including edge cases.