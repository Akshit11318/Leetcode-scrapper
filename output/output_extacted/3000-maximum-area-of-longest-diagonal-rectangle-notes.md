## Maximum Area of Longest Diagonal Rectangle
**Problem Link:** https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description

**Problem Statement:**
- Input format and constraints: Given a binary matrix `mat` of size `m x n`, where `0 <= m <= 10^3` and `0 <= n <= 10^3`, and each element is either `0` or `1`.
- Expected output format: The maximum area of a rectangle that has a diagonal in the binary matrix.
- Key requirements and edge cases to consider: 
    * The binary matrix can be empty.
    * The rectangle's sides must be parallel to the x and y axes.
    * The rectangle must have at least one non-zero element.
- Example test cases with explanations:
    * `mat = [[0,0,1],[0,1,1],[1,1,1]]`, output: `1`
    * `mat = [[0,0,0],[0,0,0],[0,0,0]]`, output: `0`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can start by checking all possible rectangles in the binary matrix and calculate their areas.
- Step-by-step breakdown of the solution:
    1. Iterate over all possible rectangles in the binary matrix.
    2. For each rectangle, check if it has a diagonal by verifying that the top-left and bottom-right corners have the same value and the top-right and bottom-left corners have the same value.
    3. If the rectangle has a diagonal, calculate its area.
    4. Keep track of the maximum area found.
- Why this approach comes to mind first: It is a straightforward solution that checks all possible cases.

```cpp
int maximalRectangle(vector<vector<char>>& mat) {
    int m = mat.size();
    if (m == 0) return 0;
    int n = mat[0].size();
    int maxArea = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = i; k < m; k++) {
                for (int l = j; l < n; l++) {
                    int area = (k - i + 1) * (l - j + 1);
                    bool hasDiagonal = true;
                    for (int x = i; x <= k; x++) {
                        for (int y = j; y <= l; y++) {
                            if (mat[x][y] != '1') {
                                hasDiagonal = false;
                                break;
                            }
                        }
                        if (!hasDiagonal) break;
                    }
                    if (hasDiagonal) maxArea = max(maxArea, area);
                }
            }
        }
    }
    
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3 * n^3)$, where $m$ and $n$ are the dimensions of the binary matrix. This is because we are iterating over all possible rectangles in the matrix and checking each one for a diagonal.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum area.
> - **Why these complexities occur:** The time complexity is high because we are checking all possible rectangles in the matrix, and for each rectangle, we are checking all its elements for a diagonal.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a histogram-based approach to calculate the maximum area of a rectangle with a diagonal in the binary matrix.
- Detailed breakdown of the approach:
    1. Iterate over each row in the binary matrix.
    2. For each row, calculate the histogram of the row by treating each element as a height.
    3. Use the histogram to calculate the maximum area of a rectangle that can be formed with the current row as the base.
    4. Keep track of the maximum area found.
- Proof of optimality: This approach is optimal because it only checks each element in the binary matrix once and uses the histogram to efficiently calculate the maximum area.

```cpp
int maximalRectangle(vector<vector<char>>& mat) {
    if (mat.empty()) return 0;
    int m = mat.size();
    int n = mat[0].size();
    vector<int> height(n + 1, 0);
    int maxArea = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            height[j] = (mat[i][j] == '1') ? height[j] + 1 : 0;
        }
        stack<int> s;
        for (int j = 0; j <= n; j++) {
            while (!s.empty() && height[j] < height[s.top()]) {
                int h = height[s.top()];
                s.pop();
                int w = s.empty() ? j : j - s.top() - 1;
                maxArea = max(maxArea, h * w);
            }
            s.push(j);
        }
    }
    
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m * n)$, where $m$ and $n$ are the dimensions of the binary matrix. This is because we are iterating over each element in the matrix once.
> - **Space Complexity:** $O(n)$, as we are using a stack to store the histogram.
> - **Optimality proof:** This approach is optimal because it only checks each element in the binary matrix once and uses the histogram to efficiently calculate the maximum area.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Histogram-based approach, stack-based solution.
- Problem-solving patterns identified: Using a histogram to efficiently calculate the maximum area of a rectangle.
- Optimization techniques learned: Using a stack to store the histogram and efficiently calculate the maximum area.
- Similar problems to practice: Maximum Area of a Rectangle with a Given Perimeter, Maximum Area of a Rectangle with a Given Diagonal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty input, not handling edge cases correctly.
- Edge cases to watch for: Empty input, input with only one row or column.
- Performance pitfalls: Using a brute force approach that checks all possible rectangles in the binary matrix.
- Testing considerations: Test the solution with different input sizes, including large inputs, and edge cases.