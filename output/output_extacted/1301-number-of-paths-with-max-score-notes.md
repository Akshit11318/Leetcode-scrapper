## Number of Paths with Max Score
**Problem Link:** https://leetcode.com/problems/number-of-paths-with-max-score/description

**Problem Statement:**
- Input format: The input is a `board` which is a 2D vector of strings.
- Constraints: Each string in the board is either "E", "X", or a digit from "1" to "9".
- Expected output format: Return an array where the first element is the maximum score and the second element is the number of paths that achieve this maximum score.
- Key requirements and edge cases to consider:
  - "E" represents an empty cell.
  - "X" represents an obstacle.
  - The maximum score is calculated by summing up the digits in the path.
  - The number of paths is the count of unique paths that achieve the maximum score.

**Example Test Cases:**
- Input: `[["E","E","E"],["3","0","9"],["1","2","F"]]`
  Output: `[12, 1]`
- Explanation: The maximum score is 12, achieved by the path "3 -> 0 -> 9 -> 1 -> 2 -> F". There is only one such path.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves exploring all possible paths from the top-left cell to the bottom-right cell, avoiding obstacles ("X").
- This approach comes to mind first because it directly addresses the requirement to find all possible paths and calculate their scores.
- However, this approach is inefficient due to its exponential time complexity.

```cpp
#include <vector>
#include <string>

using namespace std;

void dfs(vector<vector<string>>& board, int i, int j, int score, vector<pair<int, int>>& paths) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] == "X") return;
    if (board[i][j] == "F") {
        paths.push_back({score, 1});
        return;
    }
    int temp = 0;
    if (isdigit(board[i][j][0])) temp = board[i][j][0] - '0';
    board[i][j] = "X"; // Mark as visited
    dfs(board, i+1, j, score + temp, paths);
    dfs(board, i, j+1, score + temp, paths);
    board[i][j] = to_string(temp); // Backtrack
}

vector<int> pathsWithMaxScore(vector<vector<string>>& board) {
    vector<pair<int, int>> paths;
    dfs(board, 0, 0, 0, paths);
    if (paths.empty()) return {0, 0};
    int maxScore = paths[0].first;
    int count = 0;
    for (auto& path : paths) {
        if (path.first > maxScore) {
            maxScore = path.first;
            count = path.second;
        } else if (path.first == maxScore) {
            count += path.second;
        }
    }
    return {maxScore, count};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ where $m$ and $n$ are the dimensions of the board, because in the worst case, we explore all possible paths.
> - **Space Complexity:** $O(m+n)$ due to the recursion stack.
> - **Why these complexities occur:** The brute force approach leads to exponential time complexity because it explores all possible paths without any optimization.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming (DP) to store the maximum score and the number of paths that achieve this score for each cell.
- We iterate through the board from top to bottom and left to right, updating the DP table based on the values of the adjacent cells.
- This approach is optimal because it avoids redundant calculations and only considers valid paths.

```cpp
#include <vector>
#include <string>

using namespace std;

vector<int> pathsWithMaxScore(vector<vector<string>>& board) {
    int m = board.size(), n = board[0].size();
    vector<vector<pair<int, int>>> dp(m, vector<pair<int, int>>(n, {0, 0}));
    dp[0][0] = {0, 1}; // Initialize the starting point
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == "X") continue;
            int score = 0;
            if (isdigit(board[i][j][0])) score = board[i][j][0] - '0';
            if (i > 0) {
                if (dp[i-1][j].first > dp[i][j].first) {
                    dp[i][j] = {dp[i-1][j].first + score, dp[i-1][j].second};
                } else if (dp[i-1][j].first == dp[i][j].first) {
                    dp[i][j].second += dp[i-1][j].second;
                }
            }
            if (j > 0) {
                if (dp[i][j-1].first > dp[i][j].first) {
                    dp[i][j] = {dp[i][j-1].first + score, dp[i][j-1].second};
                } else if (dp[i][j-1].first == dp[i][j].first) {
                    dp[i][j].second += dp[i][j-1].second;
                }
            }
        }
    }
    if (board[m-1][n-1] == "F") {
        return {dp[m-1][n-1].first, dp[m-1][n-1].second};
    } else {
        return {0, 0};
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the board, because we iterate through each cell once.
> - **Space Complexity:** $O(m \cdot n)$ for the DP table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to efficiently calculate the maximum score and the number of paths for each cell, avoiding redundant calculations.

---

### Final Notes
**Learning Points:**
- The importance of dynamic programming in solving path-finding problems with optimal scores.
- How to represent the state of each cell using a pair of values (score and count of paths).
- The need to handle edge cases, such as obstacles and the final cell.

**Mistakes to Avoid:**
- Not properly initializing the DP table.
- Failing to handle the case where a cell has a higher score than the current maximum.
- Not updating the count of paths correctly when encountering a cell with the same score as the current maximum.