## Count Distinct Numbers on Board
**Problem Link:** https://leetcode.com/problems/count-distinct-numbers-on-board/description

**Problem Statement:**
- Input format and constraints: Given a `n x n` board, where each cell can have a value from 1 to n^2. 
- Expected output format: Return the number of distinct numbers on the board.
- Key requirements and edge cases to consider: The board can contain duplicate numbers, and we need to count each distinct number only once.
- Example test cases with explanations: 
  - For a 3x3 board with numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, the output should be 9.
  - For a 2x2 board with numbers 1, 1, 1, 1, the output should be 1.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To count distinct numbers, we can iterate over each cell in the board and add the number to a set if it's not already present.
- Step-by-step breakdown of the solution:
  1. Create an empty set to store unique numbers.
  2. Iterate over each cell in the board.
  3. For each cell, check if the number is already in the set. If not, add it to the set.
  4. After iterating over all cells, return the size of the set, which represents the count of distinct numbers.
- Why this approach comes to mind first: It's straightforward and easy to implement, as it directly addresses the problem statement.

```cpp
#include <iostream>
#include <set>

int distinctNumbers(vector<vector<int>>& board) {
    set<int> uniqueNumbers;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            uniqueNumbers.insert(board[i][j]);
        }
    }
    return uniqueNumbers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we iterate over each cell in the board once.
> - **Space Complexity:** $O(n^2)$, as in the worst case (all numbers are distinct), the size of the set will be equal to the number of cells in the board.
> - **Why these complexities occur:** The time complexity is due to the nested loop iterating over the board, and the space complexity is due to storing unique numbers in a set.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity because we must examine each cell at least once to count distinct numbers.
- Detailed breakdown of the approach: The same as the brute force approach, as it is already optimal.
- Proof of optimality: Any algorithm must at least read the input, which takes $O(n^2)$ time for an $n \times n$ board. Thus, the brute force approach is optimal.
- Why further optimization is impossible: We cannot do better than $O(n^2)$ time because we must look at each cell.

```cpp
#include <iostream>
#include <set>

int distinctNumbers(vector<vector<int>>& board) {
    set<int> uniqueNumbers;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            uniqueNumbers.insert(board[i][j]);
        }
    }
    return uniqueNumbers.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the board.
> - **Space Complexity:** $O(n^2)$, as in the worst case, the size of the set will be equal to the number of cells in the board.
> - **Optimality proof:** As explained, any algorithm must at least read the input, which takes $O(n^2)$ time for an $n \times n$ board.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Use of sets for efficient storage and lookup of unique elements.
- Problem-solving patterns identified: The importance of examining each element in the input at least once to solve the problem.
- Optimization techniques learned: Recognizing when the brute force approach is already optimal due to the inherent complexity of the problem.
- Similar problems to practice: Other problems involving counting distinct elements or finding unique values in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty board or a board with all identical numbers.
- Edge cases to watch for: Boards with duplicate numbers, boards with numbers outside the range of 1 to n^2, and boards of different sizes.
- Performance pitfalls: Using data structures that are inefficient for storing and looking up unique elements, such as lists or arrays.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large boards, to ensure correctness and efficiency.