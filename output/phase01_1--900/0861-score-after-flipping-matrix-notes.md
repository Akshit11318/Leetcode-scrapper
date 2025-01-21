## Score After Flipping Matrix
**Problem Link:** https://leetcode.com/problems/score-after-flipping-matrix/description

**Problem Statement:**
- Input format: A 2D array `A` of size `n x n`, where `n` is between 1 and 20, and each element is either 0 or 1.
- Constraints: The input matrix is guaranteed to be square.
- Expected output format: The maximum score that can be achieved after flipping the matrix.
- Key requirements and edge cases to consider: Flipping a row means changing all 0s to 1s and all 1s to 0s in that row. The score is calculated by summing the number of 1s in each column.
- Example test cases with explanations:
  - For the input `[[0,0,1,1],[1,0,1,0],[1,1,0,1]]`, the maximum score is 39 because we can flip the first and third rows to get `[[1,1,0,0],[1,0,1,0],[0,0,1,1]]`, resulting in a score of 39.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of row flips and calculating the score for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of row flips. This can be done using a binary counter, where each bit corresponds to a row.
  2. For each combination, flip the corresponding rows in the matrix.
  3. Calculate the score for the flipped matrix by summing the number of 1s in each column.
  4. Keep track of the maximum score achieved across all combinations.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int matrixScore(std::vector<std::vector<int>>& A) {
    int n = A.size();
    int m = A[0].size();
    int maxScore = 0;

    // Generate all possible combinations of row flips
    for (int mask = 0; mask < (1 << n); mask++) {
        // Flip the corresponding rows in the matrix
        std::vector<std::vector<int>> flippedA = A;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                for (int j = 0; j < m; j++) {
                    flippedA[i][j] = 1 - flippedA[i][j];
                }
            }
        }

        // Calculate the score for the flipped matrix
        int score = 0;
        for (int j = 0; j < m; j++) {
            int count = 0;
            for (int i = 0; i < n; i++) {
                count += flippedA[i][j];
            }
            score += std::max(count, n - count);
        }

        // Update the maximum score
        maxScore = std::max(maxScore, score);
    }

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns. The dominant term is the generation of all possible combinations of row flips, which has a time complexity of $O(2^n)$.
> - **Space Complexity:** $O(n \cdot m)$, which is the space required to store the flipped matrix.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of row flips, which leads to an exponential time complexity. The space complexity is dominated by the storage of the flipped matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible combinations of row flips, we can fix the first row and then try all possible combinations of flips for the remaining rows.
- Detailed breakdown of the approach:
  1. Fix the first row by flipping it if necessary to maximize the number of 1s in the first column.
  2. For each of the remaining rows, try all possible combinations of flips and calculate the score for each combination.
  3. Keep track of the maximum score achieved across all combinations.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int matrixScore(std::vector<std::vector<int>>& A) {
    int n = A.size();
    int m = A[0].size();
    int maxScore = 0;

    // Fix the first row
    for (int i = 0; i < n; i++) {
        if (A[i][0] == 0) {
            for (int j = 0; j < m; j++) {
                A[i][j] = 1 - A[i][j];
            }
        }
    }

    // Generate all possible combinations of row flips for the remaining rows
    for (int mask = 0; mask < (1 << (n - 1)); mask++) {
        // Flip the corresponding rows in the matrix
        std::vector<std::vector<int>> flippedA = A;
        for (int i = 1; i < n; i++) {
            if (mask & (1 << (i - 1))) {
                for (int j = 0; j < m; j++) {
                    flippedA[i][j] = 1 - flippedA[i][j];
                }
            }
        }

        // Calculate the score for the flipped matrix
        int score = 0;
        for (int j = 0; j < m; j++) {
            int count = 0;
            for (int i = 0; i < n; i++) {
                count += flippedA[i][j];
            }
            score += std::max(count, n - count);
        }

        // Update the maximum score
        maxScore = std::max(maxScore, score);
    }

    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1} \cdot n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns. The dominant term is the generation of all possible combinations of row flips for the remaining rows, which has a time complexity of $O(2^{n-1})$.
> - **Space Complexity:** $O(n \cdot m)$, which is the space required to store the flipped matrix.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of row flips for the remaining rows after fixing the first row, which guarantees the maximum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Generation of all possible combinations of row flips, calculation of the score for each combination, and keeping track of the maximum score.
- Problem-solving patterns identified: Using a binary counter to generate all possible combinations, fixing the first row to reduce the search space, and trying all possible combinations of flips for the remaining rows.
- Optimization techniques learned: Reducing the search space by fixing the first row and using a binary counter to generate all possible combinations.
- Similar problems to practice: Other problems involving generation of all possible combinations, such as subset sum and knapsack problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly generating all possible combinations of row flips, failing to fix the first row, and not keeping track of the maximum score.
- Edge cases to watch for: Handling the case where the input matrix is empty or has only one row.
- Performance pitfalls: Failing to reduce the search space by fixing the first row, which can lead to an exponential time complexity.
- Testing considerations: Testing the implementation with different input matrices, including edge cases, to ensure correctness and performance.