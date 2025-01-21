## K-th Symbol in Grammar
**Problem Link:** https://leetcode.com/problems/k-th-symbol-in-grammar/description

**Problem Statement:**
- Input: Two integers `N` and `K`.
- Output: The K-th symbol in the N-th row of a grammar system where each row is generated based on the previous row.
- Key requirements and edge cases:
  - `1 <= N <= 30`
  - `1 <= K <= 2^N`
- Example test cases with explanations:
  - For `N = 1` and `K = 1`, the output is `0`.
  - For `N = 2` and `K = 1`, the output is `0`.
  - For `N = 2` and `K = 2`, the output is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate each row of the grammar system sequentially until we reach the N-th row, then find the K-th symbol in that row.
- Step-by-step breakdown:
  1. Start with the first row as `"0"`.
  2. For each subsequent row, apply the transformation rule to the previous row: replace each `0` with `01` and each `1` with `10`.
  3. Repeat step 2 until we have generated the N-th row.
  4. Find the K-th symbol in the N-th row.
- Why this approach comes to mind first: It directly follows the problem description and applies the given transformation rules.

```cpp
class Solution {
public:
    char kthGrammar(int N, int K) {
        string row = "0";
        for (int i = 1; i < N; i++) {
            string newRow = "";
            for (char c : row) {
                if (c == '0') {
                    newRow += "01";
                } else {
                    newRow += "10";
                }
            }
            row = newRow;
        }
        return row[K - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^N)$, because in the worst case, we generate strings of lengths up to $2^{N-1}$.
> - **Space Complexity:** $O(2^N)$, because we need to store the last generated row which can have up to $2^{N-1}$ characters.
> - **Why these complexities occur:** The exponential growth in time and space is due to the nature of the transformation rule, which doubles the length of the string in each step.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Recognize that the K-th symbol in the N-th row can be determined without generating the entire row. This can be done by analyzing the pattern of how symbols are generated.
- Detailed breakdown:
  - Notice that each symbol in a row is determined by the corresponding symbol in the previous row (if it exists) and its position.
  - Specifically, if the position of the symbol is odd, it is the same as the symbol in the previous row (if the previous row has a symbol at that position). If the position is even, it is the opposite of the symbol in the previous row (if it exists) at the position divided by 2.
  - This insight allows us to compute the K-th symbol directly without generating the entire N-th row.
- Proof of optimality: This approach is optimal because it reduces the problem to a simple recursive relationship without the need to generate and store the entire row.

```cpp
class Solution {
public:
    char kthGrammar(int N, int K) {
        return findKthSymbol(N, K - 1);
    }
    
    char findKthSymbol(int n, int k) {
        if (n == 0) return '0';
        if (n == 1) {
            if (k == 0) return '0';
            else return '1';
        }
        
        // Determine the symbol based on the position in the previous row
        if (k % 2 == 0) {
            return findKthSymbol(n - 1, k / 2);
        } else {
            // The opposite of the symbol in the previous row at k/2
            char symbol = findKthSymbol(n - 1, k / 2);
            return symbol == '0' ? '1' : '0';
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, because in the worst case, we recursively call the function up to N times.
> - **Space Complexity:** $O(N)$, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it avoids generating unnecessary parts of the row, focusing only on the K-th symbol and utilizing the pattern of the grammar system to minimize computational and memory usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Pattern recognition, recursive relationships, and optimization by avoiding unnecessary computations.
- Problem-solving patterns identified: Looking for patterns or rules that can simplify the problem, and using recursive relationships to solve problems that have a tree-like or hierarchical structure.
- Optimization techniques learned: Identifying and exploiting patterns in the problem to reduce computational complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling base cases in recursive functions, and not considering the implications of exponential growth in time and space complexity.
- Edge cases to watch for: The boundary conditions of the problem, such as when `N` or `K` is at its minimum or maximum allowed value.
- Performance pitfalls: Failing to recognize patterns or relationships that could simplify the computation, leading to inefficient algorithms.