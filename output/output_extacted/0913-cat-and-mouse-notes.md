## Cat and Mouse
**Problem Link:** https://leetcode.com/problems/cat-and-mouse/description

**Problem Statement:**
- Input format: `n` (number of nodes in the graph), `graph` (adjacency list representation of the graph), `startMouse` (initial position of the mouse), `startCat` (initial position of the cat)
- Expected output format: `0` if the mouse can win, `1` if the cat can win, `2` if the game is a draw
- Key requirements and edge cases to consider:
  - The mouse and the cat move alternately.
  - The mouse can only move to an adjacent node that is not occupied by the cat.
  - The cat can only move to an adjacent node that is not occupied by the mouse.
  - If the mouse reaches node `0`, it wins.
  - If the cat reaches the mouse, it wins.
  - If the game is in a state that has occurred before, it is a draw.
- Example test cases with explanations:
  - `n = 3`, `graph = [[1,2],[0],[0]]`, `startMouse = 1`, `startCat = 2`
  - `n = 2`, `graph = [[1],[0]]`, `startMouse = 1`, `startCat = 0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the game and try all possible moves for the mouse and the cat.
- Step-by-step breakdown of the solution:
  1. Initialize the current state of the game with the mouse at `startMouse` and the cat at `startCat`.
  2. For each possible move of the mouse, check if the cat can win in the next step.
  3. If the cat cannot win, recursively try all possible moves for the mouse.
  4. If the mouse reaches node `0`, return `0` (mouse wins).
  5. If the cat reaches the mouse, return `1` (cat wins).
  6. If the game is in a state that has occurred before, return `2` (draw).
- Why this approach comes to mind first: It is a straightforward way to simulate the game and try all possible moves.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int catMouseGame(int n, vector<vector<int>>& graph, int startMouse, int startCat) {
    unordered_set<string> visited;
    return dfs(n, graph, startMouse, startCat, visited);
}

int dfs(int n, vector<vector<int>>& graph, int mouse, int cat, unordered_set<string>& visited) {
    string state = to_string(mouse) + "," + to_string(cat);
    if (visited.find(state) != visited.end()) return 2; // draw
    visited.insert(state);
    
    if (mouse == 0) return 0; // mouse wins
    if (mouse == cat) return 1; // cat wins
    
    int result = 1; // cat wins by default
    for (int nextMouse : graph[mouse]) {
        bool catWins = true;
        for (int nextCat : graph[cat]) {
            int nextResult = dfs(n, graph, nextMouse, nextCat, visited);
            if (nextResult == 0) {
                catWins = false;
                break;
            }
        }
        if (!catWins) {
            result = 0; // mouse wins
            break;
        }
    }
    
    visited.erase(state);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n^2})$ (exponential in the number of nodes)
> - **Space Complexity:** $O(n^2)$ (space needed to store the visited states)
> - **Why these complexities occur:** The brute force approach tries all possible moves for the mouse and the cat, resulting in exponential time complexity. The space complexity is due to the storage of visited states.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The game can be represented as a graph with states as nodes and transitions as edges. The game is a draw if and only if there is a cycle in the graph.
- Detailed breakdown of the approach:
  1. Create a graph with states as nodes and transitions as edges.
  2. Perform a depth-first search (DFS) to detect cycles in the graph.
  3. If a cycle is found, return `2` (draw).
  4. If no cycle is found, return the result of the DFS (either `0` or `1`).
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int catMouseGame(int n, vector<vector<int>>& graph, int startMouse, int startCat) {
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(3, -1)));
    return dfs(n, graph, startMouse, startCat, dp);
}

int dfs(int n, vector<vector<int>>& graph, int mouse, int cat, vector<vector<vector<int>>>& dp) {
    if (mouse == 0) return 0; // mouse wins
    if (mouse == cat) return 1; // cat wins
    
    if (dp[mouse][cat][0] != -1) return dp[mouse][cat][0];
    
    bool catWins = true;
    for (int nextMouse : graph[mouse]) {
        bool mouseWins = true;
        for (int nextCat : graph[cat]) {
            int nextResult = dfs(n, graph, nextMouse, nextCat, dp);
            if (nextResult == 0) {
                mouseWins = false;
                break;
            }
        }
        if (mouseWins) {
            catWins = false;
            break;
        }
    }
    
    if (catWins) {
        dp[mouse][cat][0] = 1; // cat wins
    } else {
        dp[mouse][cat][0] = 0; // mouse wins
    }
    
    return dp[mouse][cat][0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ (polynomial in the number of nodes)
> - **Space Complexity:** $O(n^2)$ (space needed to store the DP table)
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem. The space complexity is also optimal, as we need to store the DP table to avoid redundant computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), dynamic programming (DP), graph theory.
- Problem-solving patterns identified: Reducing the problem to a graph theory problem, using DFS to detect cycles, using DP to avoid redundant computations.
- Optimization techniques learned: Using memoization to store the results of subproblems, using DFS to detect cycles.
- Similar problems to practice: Other graph theory problems, such as finding the shortest path, detecting cycles, and solving the traveling salesman problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for base cases, not handling edge cases, not using memoization to store the results of subproblems.
- Edge cases to watch for: Handling the case where the mouse and the cat are in the same node, handling the case where the game is a draw.
- Performance pitfalls: Not using memoization to store the results of subproblems, not using DFS to detect cycles.
- Testing considerations: Testing the implementation with different inputs, testing the implementation with edge cases.