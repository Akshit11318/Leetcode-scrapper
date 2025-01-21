## Check If Every Row and Column Contains All Numbers

**Problem Link:** https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description

**Problem Statement:**
- The input is a 2D array `matrix` with dimensions `n x n`, where `n` is the number of rows and columns.
- Each cell in the matrix contains a unique number from 1 to `n^2`.
- The goal is to check if every row and column in the matrix contains all numbers from 1 to `n`.
- The expected output is a boolean indicating whether the condition is met.
- Key requirements include handling matrices of varying sizes and ensuring that each row and column contains the numbers 1 through `n` exactly once.
- Example test cases include matrices where each row and column contains all numbers from 1 to `n`, and matrices where this condition is not met.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each row and column individually to ensure it contains all numbers from 1 to `n`.
- This can be achieved by iterating over each row and column, and for each one, checking if it contains all the required numbers.
- This approach comes to mind first because it directly addresses the problem statement by checking each condition (rows and columns containing all numbers) separately.

```cpp
#include <vector>
#include <unordered_set>

bool checkRowAndColumn(std::vector<std::vector<int>>& matrix) {
    int n = matrix.size();
    for (int i = 0; i < n; i++) {
        std::unordered_set<int> rowSet;
        std::unordered_set<int> colSet;
        for (int j = 0; j < n; j++) {
            rowSet.insert(matrix[i][j]);
            colSet.insert(matrix[j][i]);
        }
        for (int num = 1; num <= n; num++) {
            if (rowSet.find(num) == rowSet.end() || colSet.find(num) == colSet.end()) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because for each row and column, we are iterating over `n` elements to check if they contain all numbers from 1 to `n`.
> - **Space Complexity:** $O(n)$, as in the worst case, we are storing `n` elements in the `rowSet` and `colSet`.
> - **Why these complexities occur:** These complexities occur because we are essentially performing a linear scan of the matrix for each row and column to verify the condition, resulting in a quadratic time complexity and linear space complexity due to the use of sets for efficient lookups.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can use a single pass through the matrix to check both row and column conditions simultaneously.
- We can utilize two arrays, `rows` and `cols`, of size `n`, where `rows[i]` and `cols[j]` are used as bit masks to keep track of the numbers seen in row `i` and column `j`, respectively.
- This approach is optimal because it minimizes the number of passes through the matrix and uses bit manipulation for efficient tracking of seen numbers.

```cpp
#include <vector>

bool checkRowAndColumn(std::vector<std::vector<int>>& matrix) {
    int n = matrix.size();
    std::vector<int> rows(n, 0);
    std::vector<int> cols(n, 0);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int num = matrix[i][j];
            if (num < 1 || num > n) return false;
            rows[i] |= (1 << (num - 1));
            cols[j] |= (1 << (num - 1));
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (rows[i] != (1 << n) - 1 || cols[i] != (1 << n) - 1) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because we are making a single pass through the matrix.
> - **Space Complexity:** $O(n)$, for storing the `rows` and `cols` arrays.
> - **Optimality proof:** This is the optimal solution because we are making the minimum number of passes through the data (a single pass) and using a constant amount of extra space per row and column, which is the best we can achieve given the problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of bit manipulation for efficient tracking of seen numbers and the optimization of iterating through the matrix.
- Problem-solving patterns identified include recognizing the opportunity to combine row and column checks into a single pass for efficiency.
- Optimization techniques learned include minimizing the number of passes through the data and using efficient data structures for tracking seen elements.

**Mistakes to Avoid:**
- Common implementation errors include not correctly handling edge cases (e.g., matrices with duplicate numbers or numbers outside the range 1 to `n`).
- Performance pitfalls include using inefficient data structures or algorithms that result in higher than necessary time or space complexity.
- Testing considerations include ensuring that the solution works correctly for matrices of varying sizes and contents.