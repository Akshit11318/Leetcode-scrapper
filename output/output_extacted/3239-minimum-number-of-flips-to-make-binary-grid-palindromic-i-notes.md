## Minimum Number of Flips to Make Binary Grid Palindromic I

**Problem Link:** https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description

**Problem Statement:**
- Input format: A binary grid `mat` of size `n x n`.
- Constraints: `1 <= n <= 10`, `mat[i][j] == 0` or `mat[i][j] == 1`.
- Expected output format: The minimum number of flips required to make `mat` palindromic.
- Key requirements and edge cases to consider:
  - A grid is considered palindromic if it remains the same after flipping it around its horizontal axis.
  - Flipping a cell means changing its value from `0` to `1` or `1` to `0`.
- Example test cases with explanations:
  - Example 1: `mat = [[0,0],[0,1]]`, the minimum number of flips is `1` because flipping the cell at position `(1,1)` makes the grid palindromic.
  - Example 2: `mat = [[1,1],[1,0]]`, the minimum number of flips is `2` because flipping the cells at positions `(0,0)` and `(1,1)` makes the grid palindromic.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of flips for each cell and count the number of flips required to make the grid palindromic.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of flips for each cell using bit manipulation.
  2. For each combination, flip the corresponding cells and check if the grid is palindromic.
  3. If the grid is palindromic, update the minimum number of flips required.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that tries all possible solutions.

```cpp
int minFlips(vector<vector<int>>& mat) {
    int n = mat.size();
    int minFlips = INT_MAX;
    for (int mask = 0; mask < (1 << (n * n)); mask++) {
        int flips = __builtin_popcount(mask);
        vector<vector<int>> flippedMat = mat;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((mask >> (i * n + j)) & 1) {
                    flippedMat[i][j] ^= 1;
                }
            }
        }
        bool isPalindromic = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (flippedMat[i][j] != flippedMat[n - i - 1][j]) {
                    isPalindromic = false;
                    break;
                }
            }
            if (!isPalindromic) break;
        }
        if (isPalindromic) {
            minFlips = min(minFlips, flips);
        }
    }
    return minFlips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n^2} \cdot n^2)$, where $n$ is the size of the grid. This is because we generate all possible combinations of flips and check if the grid is palindromic for each combination.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we need to store the flipped grid.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of flips, and the space complexity occurs because we need to store the flipped grid.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to flip the cells. We start from the top row and flip the cells that are not equal to the corresponding cells in the bottom row.
- Detailed breakdown of the approach:
  1. Initialize the minimum number of flips to `0`.
  2. Iterate over the rows of the grid from top to bottom.
  3. For each row, iterate over the columns from left to right.
  4. If the current cell is not equal to the corresponding cell in the bottom row, flip the current cell and increment the minimum number of flips.
- Proof of optimality: This approach is optimal because it always chooses the minimum number of flips required to make the grid palindromic.

```cpp
int minFlips(vector<vector<int>>& mat) {
    int n = mat.size();
    int minFlips = 0;
    for (int i = 0; i < n / 2; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[n - i - 1][j]) {
                minFlips++;
                mat[i][j] ^= 1;
            }
        }
    }
    return minFlips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we iterate over the rows and columns of the grid.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the grid. This is because we only use a constant amount of space to store the minimum number of flips.
> - **Optimality proof:** This approach is optimal because it always chooses the minimum number of flips required to make the grid palindromic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, bit manipulation.
- Problem-solving patterns identified: Using a greedy approach to solve problems that require finding the minimum number of operations.
- Optimization techniques learned: Using a greedy approach to reduce the time complexity of the solution.
- Similar problems to practice: Problems that require finding the minimum number of operations to achieve a certain goal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using a greedy approach when possible.
- Edge cases to watch for: Grids with odd size, grids with all cells equal to `0` or `1`.
- Performance pitfalls: Using a brute force approach when a greedy approach is possible.
- Testing considerations: Test the solution with different grid sizes, test the solution with grids that have all cells equal to `0` or `1`.