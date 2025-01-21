## Queens That Can Attack the King
**Problem Link:** https://leetcode.com/problems/queens-that-can-attack-the-king/description

**Problem Statement:**
- Input format: An 8x8 chessboard represented as a 2D array, where `queen` represents a queen and `king` represents the king.
- Constraints: The input array will contain exactly one `king` and any number of `queen`s.
- Expected output format: A list of coordinates of queens that can attack the king.
- Key requirements and edge cases to consider: 
  - A queen can attack the king if they are in the same row, column, or diagonal.
  - There might be other queens blocking the path.
- Example test cases with explanations:
  - Example 1: If the king is at position (0,0) and there are queens at positions (0,1), (1,1), and (2,0), the queens at (0,1) and (2,0) can attack the king.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each cell in the chessboard, and for each cell, check if it's a queen. If it's a queen, check if it can attack the king by checking all possible paths (up, down, left, right, and diagonals).
- Step-by-step breakdown of the solution:
  1. Find the position of the king.
  2. Iterate over each cell in the chessboard.
  3. If the cell is a queen, check if it can attack the king.
  4. To check if a queen can attack the king, iterate over all possible paths from the queen to the king.
  5. If there's no other queen or obstacle in the path, add the queen's position to the result list.
- Why this approach comes to mind first: It's a straightforward and intuitive approach that checks all possible scenarios.

```cpp
vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
    vector<vector<int>> result;
    int row = king[0];
    int col = king[1];
    vector<int> directions = {-1, -1, 0, -1, 1, -1, 1, 0, 1, 1, 0, 1};
    
    for (int i = 0; i < 8; i += 2) {
        int r = row + directions[i];
        int c = col + directions[i + 1];
        
        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            bool found = false;
            for (auto& q : queens) {
                if (q[0] == r && q[1] == c) {
                    result.push_back(q);
                    found = true;
                    break;
                }
            }
            if (found) break;
            r += directions[i];
            c += directions[i + 1];
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of queens and $m$ is the number of directions (8 in this case).
> - **Space Complexity:** $O(n)$, where $n$ is the number of queens that can attack the king.
> - **Why these complexities occur:** The brute force approach checks all possible paths from each queen to the king, resulting in a time complexity of $O(n \times m)$. The space complexity is $O(n)$ because we store the positions of queens that can attack the king.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible paths from each queen to the king, we can iterate over all possible paths from the king and stop as soon as we find a queen.
- Detailed breakdown of the approach:
  1. Find the position of the king.
  2. Iterate over all possible paths from the king (up, down, left, right, and diagonals).
  3. For each path, stop as soon as we find a queen and add its position to the result list.
- Proof of optimality: This approach is optimal because it only checks the necessary paths and stops as soon as it finds a queen, resulting in a time complexity of $O(8 \times n)$, where $n$ is the number of queens.

```cpp
vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
    vector<vector<int>> result;
    int row = king[0];
    int col = king[1];
    set<string> queenSet;
    for (auto& q : queens) {
        queenSet.insert(to_string(q[0]) + "," + to_string(q[1]));
    }
    vector<int> directions = {-1, -1, 0, -1, 1, -1, 1, 0, 1, 1, 0, 1};
    
    for (int i = 0; i < 8; i += 2) {
        int r = row + directions[i];
        int c = col + directions[i + 1];
        
        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            string pos = to_string(r) + "," + to_string(c);
            if (queenSet.find(pos) != queenSet.end()) {
                result.push_back({r, c});
                break;
            }
            r += directions[i];
            c += directions[i + 1];
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8 \times n)$, where $n$ is the number of queens.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queens.
> - **Optimality proof:** This approach is optimal because it only checks the necessary paths and stops as soon as it finds a queen, resulting in a time complexity of $O(8 \times n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over all possible paths, use of sets for efficient lookup.
- Problem-solving patterns identified: Checking all possible scenarios, optimizing by stopping as soon as a solution is found.
- Optimization techniques learned: Reducing the number of iterations, using data structures for efficient lookup.
- Similar problems to practice: Problems involving iteration over all possible paths, optimization by stopping as soon as a solution is found.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for boundary conditions, not stopping as soon as a solution is found.
- Edge cases to watch for: Queens that are not in the same row, column, or diagonal as the king.
- Performance pitfalls: Checking all possible paths from each queen to the king, resulting in a high time complexity.
- Testing considerations: Test cases with different numbers of queens, test cases with queens in different positions.