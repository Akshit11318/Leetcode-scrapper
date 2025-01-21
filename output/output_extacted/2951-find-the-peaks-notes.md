## Find the Peaks
**Problem Link:** https://leetcode.com/problems/find-the-peaks/description

**Problem Statement:**
- Input format and constraints: The input is a 2D `matrix` of integers, and the goal is to find all the peak elements.
- Expected output format: Return a list of coordinates of all the peak elements.
- Key requirements and edge cases to consider: A peak element is an element that is strictly greater than its neighbors.
- Example test cases with explanations:
  - For a 2D matrix:
    ```
    [
      [1, 2, 3],
      [4, 5, 4],
      [3, 2, 1]
    ]
    ```
    The output should be `[1, 2]` because the peak element is at `(1, 2)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each element in the matrix to see if it is a peak by comparing it with its neighbors.
- Step-by-step breakdown of the solution:
  1. Iterate through each element in the matrix.
  2. For each element, compare it with its neighbors (up, down, left, right).
  3. If the element is greater than all its neighbors, it is a peak.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solving the problem.

```cpp
vector<vector<int>> findPeaks(vector<vector<int>>& matrix) {
  vector<vector<int>> peaks;
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      bool isPeak = true;
      for (int x = -1; x <= 1; x++) {
        for (int y = -1; y <= 1; y++) {
          if (x == 0 && y == 0) continue;
          int nx = i + x, ny = j + y;
          if (nx >= 0 && nx < matrix.size() && ny >= 0 && ny < matrix[nx].size()) {
            if (matrix[nx][ny] >= matrix[i][j]) {
              isPeak = false;
              break;
            }
          }
        }
        if (!isPeak) break;
      }
      if (isPeak) {
        peaks.push_back({i, j});
      }
    }
  }
  return peaks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$ where $m$ is the number of rows, $n$ is the number of columns, and $k$ is the number of neighbors for each cell (in this case, $k = 9$ because we are considering all 8 neighbors plus the cell itself). This is because for each cell, we are potentially checking all its neighbors.
> - **Space Complexity:** $O(m \cdot n)$ for storing the peaks, in the worst case when all elements are peaks.
> - **Why these complexities occur:** The time complexity is high because we are checking each cell and potentially all its neighbors. The space complexity is directly related to the output size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite straightforward and optimal in terms of time complexity for finding peaks in a matrix, given that we must check each element at least once.
- Detailed breakdown of the approach: The approach remains similar to the brute force, with the optimization that we can stop checking neighbors as soon as we find one that is not less than the current element.
- Proof of optimality: This approach is optimal because it has to check each element and its neighbors at least once to determine if it's a peak, resulting in a time complexity of $O(m \cdot n \cdot k)$.
- Why further optimization is impossible: Without additional information or constraints on the matrix, further optimization in terms of time complexity is not possible because we must examine each element and potentially its neighbors.

```cpp
vector<vector<int>> findPeaksOptimal(vector<vector<int>>& matrix) {
  vector<vector<int>> peaks;
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix[i].size(); j++) {
      bool isPeak = true;
      for (int x = -1; x <= 1; x++) {
        for (int y = -1; y <= 1; y++) {
          if (x == 0 && y == 0) continue;
          int nx = i + x, ny = j + y;
          if (nx >= 0 && nx < matrix.size() && ny >= 0 && ny < matrix[nx].size()) {
            if (matrix[nx][ny] >= matrix[i][j]) {
              isPeak = false;
              break;
            }
          }
        }
        if (!isPeak) break;
      }
      if (isPeak) {
        peaks.push_back({i, j});
      }
    }
  }
  return peaks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$ where $m$ is the number of rows, $n$ is the number of columns, and $k$ is the number of neighbors for each cell. This is the same as the brute force because the optimization does not reduce the number of operations in the worst case.
> - **Space Complexity:** $O(m \cdot n)$ for storing the peaks.
> - **Optimality proof:** The time complexity is optimal given that we must check each element and potentially its neighbors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and understanding of time and space complexity.
- Problem-solving patterns identified: Checking each element and its neighbors to find peaks.
- Optimization techniques learned: Stopping the check as soon as a condition is not met.
- Similar problems to practice: Finding valleys, finding local maxima or minima in arrays, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking boundary conditions correctly, not handling the case where an element is equal to its neighbor.
- Edge cases to watch for: Elements on the edges or corners of the matrix.
- Performance pitfalls: Not optimizing the checks by stopping as soon as a condition is not met.
- Testing considerations: Testing with matrices of different sizes, with and without peaks, and with peaks at the edges or corners.