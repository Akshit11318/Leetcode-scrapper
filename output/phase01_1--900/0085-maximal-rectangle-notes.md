## Maximal Rectangle

**Problem Link:** [https://leetcode.com/problems/maximal-rectangle/description](https://leetcode.com/problems/maximal-rectangle/description)

**Problem Statement:**
- Input format: A 2D binary matrix filled with 0's and 1's.
- Constraints: The number of rows and columns in the matrix.
- Expected output format: The maximum area of a rectangle containing all ones.
- Key requirements and edge cases to consider: The input matrix may be empty, or it may contain only zeros.
- Example test cases with explanations:
  - For an input `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]`, the output should be `6`.
  - For an input `matrix = [["0"]]`, the output should be `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over all possible sub-matrices in the given matrix and calculate the area of the rectangle for each sub-matrix.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible sub-matrices in the given matrix.
  2. For each sub-matrix, check if all elements are ones.
  3. If all elements are ones, calculate the area of the rectangle.
  4. Keep track of the maximum area found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible sub-matrices.

```cpp
int maximalRectangle(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int rows = matrix.size(), cols = matrix[0].size();
    int maxArea = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            for (int k = i; k < rows; k++) {
                for (int end = j; end < cols; end++) {
                    bool isAllOnes = true;
                    for (int x = i; x <= k; x++) {
                        for (int y = j; y <= end; y++) {
                            if (matrix[x][y] == '0') {
                                isAllOnes = false;
                                break;
                            }
                        }
                        if (!isAllOnes) break;
                    }
                    if (isAllOnes) {
                        maxArea = max(maxArea, (k - i + 1) * (end - j + 1));
                    }
                }
            }
        }
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of rows (or columns) in the matrix. This is because we have four nested loops that iterate over the rows and columns.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum area.
> - **Why these complexities occur:** The time complexity is high because we are checking all possible sub-matrices, which results in a large number of iterations. The space complexity is low because we only need to store a single variable to keep track of the maximum area.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the concept of histograms to solve this problem. For each row, we can calculate the height of the histogram at each column and then use the `largestRectangleArea` function to find the maximum area of the rectangle.
- Detailed breakdown of the approach:
  1. Initialize an array to store the height of the histogram at each column.
  2. Iterate over each row in the matrix.
  3. For each row, update the height of the histogram at each column.
  4. Use the `largestRectangleArea` function to find the maximum area of the rectangle for the current row.
  5. Keep track of the maximum area found so far.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n^4)$ to $O(n^3)$, where $n$ is the number of rows (or columns) in the matrix.

```cpp
int maximalRectangle(vector<vector<char>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int rows = matrix.size(), cols = matrix[0].size();
    vector<int> heights(cols, 0);
    int maxArea = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            heights[j] = matrix[i][j] == '1' ? heights[j] + 1 : 0;
        }
        maxArea = max(maxArea, largestRectangleArea(heights));
    }
    return maxArea;
}

int largestRectangleArea(vector<int>& heights) {
    int n = heights.size();
    vector<int> left(n), right(n);
    stack<int> s;
    for (int i = 0; i < n; i++) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        left[i] = s.empty() ? 0 : s.top() + 1;
        s.push(i);
    }
    while (!s.empty()) s.pop();
    for (int i = n - 1; i >= 0; i--) {
        while (!s.empty() && heights[s.top()] >= heights[i]) {
            s.pop();
        }
        right[i] = s.empty() ? n - 1 : s.top() - 1;
        s.push(i);
    }
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        maxArea = max(maxArea, (right[i] - left[i] + 1) * heights[i]);
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of rows (or columns) in the matrix. This is because we have three nested loops that iterate over the rows and columns.
> - **Space Complexity:** $O(n)$, as we use a stack to store the indices of the heights.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^4)$ to $O(n^3)$, where $n$ is the number of rows (or columns) in the matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Histograms, stacks, and dynamic programming.
- Problem-solving patterns identified: Using histograms to solve problems involving rectangles and areas.
- Optimization techniques learned: Reducing the time complexity by using histograms and stacks.
- Similar problems to practice: `largestRectangleArea`, `maximalSquare`, and `minimumAreaRectangle`.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty matrix or a matrix with only zeros.
- Edge cases to watch for: The input matrix may be empty, or it may contain only zeros.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases and large matrices.