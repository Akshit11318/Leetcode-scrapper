## Minimum Moves to Reach Target Score
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-reach-target-score/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the minimum number of moves required to reach a target score, given the initial score and the increment and decrement values.
- Expected output format: The function should return the minimum number of moves to reach the target score.
- Key requirements and edge cases to consider: The function should handle cases where the target score is not reachable, and it should also handle cases where the increment and decrement values are not coprime.
- Example test cases with explanations:
  - For example, if the initial score is 5, the increment is 2, and the decrement is 3, and the target score is 10, the function should return 3 (5 + 2 + 2 + 1 = 10).
  - If the target score is not reachable, the function should return -1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of increments and decrements to reach the target score.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the initial score and the number of moves (0).
  2. Dequeue the current score and the number of moves.
  3. If the current score is equal to the target score, return the number of moves.
  4. If the current score is greater than the target score, decrement the score by the decrement value and enqueue the new score and the number of moves + 1.
  5. If the current score is less than the target score, increment the score by the increment value and enqueue the new score and the number of moves + 1.
- Why this approach comes to mind first: The brute force approach is the most straightforward solution and is often the first approach that comes to mind.

```cpp
#include <queue>
#include <unordered_set>

int minMoves(int x, int y, int z) {
    std::queue<std::pair<int, int>> q;
    std::unordered_set<int> visited;
    q.push({x, 0});
    visited.insert(x);
    
    while (!q.empty()) {
        int currScore = q.front().first;
        int moves = q.front().second;
        q.pop();
        
        if (currScore == z) {
            return moves;
        }
        
        int incScore = currScore + y;
        if (visited.find(incScore) == visited.end()) {
            q.push({incScore, moves + 1});
            visited.insert(incScore);
        }
        
        int decScore = currScore - x;
        if (decScore >= 0 && visited.find(decScore) == visited.end()) {
            q.push({decScore, moves + 1});
            visited.insert(decScore);
        }
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(b^d)$ where $b$ is the branching factor (2 in this case) and $d$ is the depth of the search tree. In this case, $d$ is the minimum number of moves required to reach the target score.
> - **Space Complexity:** $O(b^d)$ for storing the visited scores.
> - **Why these complexities occur:** The brute force approach has exponential time and space complexities because it tries all possible combinations of increments and decrements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a breadth-first search (BFS) algorithm with a visited set to avoid revisiting the same scores.
- Detailed breakdown of the approach:
  1. Initialize a queue with the initial score and the number of moves (0).
  2. Dequeue the current score and the number of moves.
  3. If the current score is equal to the target score, return the number of moves.
  4. If the current score is greater than the target score, decrement the score by the decrement value and enqueue the new score and the number of moves + 1.
  5. If the current score is less than the target score, increment the score by the increment value and enqueue the new score and the number of moves + 1.
- Proof of optimality: The BFS algorithm is optimal because it explores all possible scores in the shortest number of moves.

```cpp
#include <queue>
#include <unordered_set>

int minMoves(int x, int y, int z) {
    std::queue<std::pair<int, int>> q;
    std::unordered_set<int> visited;
    q.push({x, 0});
    visited.insert(x);
    
    while (!q.empty()) {
        int currScore = q.front().first;
        int moves = q.front().second;
        q.pop();
        
        if (currScore == z) {
            return moves;
        }
        
        int incScore = currScore + y;
        if (visited.find(incScore) == visited.end()) {
            q.push({incScore, moves + 1});
            visited.insert(incScore);
        }
        
        int decScore = currScore - x;
        if (decScore >= 0 && visited.find(decScore) == visited.end()) {
            q.push({decScore, moves + 1});
            visited.insert(decScore);
        }
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(b^d)$ where $b$ is the branching factor (2 in this case) and $d$ is the depth of the search tree. In this case, $d$ is the minimum number of moves required to reach the target score.
> - **Space Complexity:** $O(b^d)$ for storing the visited scores.
> - **Optimality proof:** The BFS algorithm is optimal because it explores all possible scores in the shortest number of moves.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, visited set.
- Problem-solving patterns identified: using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: using a visited set to avoid revisiting the same scores.
- Similar problems to practice: finding the shortest path in a weighted graph, finding the minimum number of moves to reach a target position in a grid.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the base case (target score reached), not using a visited set to avoid revisiting the same scores.
- Edge cases to watch for: target score not reachable, increment and decrement values not coprime.
- Performance pitfalls: using a recursive approach instead of an iterative approach, not using a visited set to avoid revisiting the same scores.
- Testing considerations: testing the function with different input values, testing the function with edge cases.