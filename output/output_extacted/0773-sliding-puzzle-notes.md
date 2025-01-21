## Sliding Puzzle
**Problem Link:** https://leetcode.com/problems/sliding-puzzle/description

**Problem Statement:**
- Input format: A 2D array `board` representing the puzzle, where `0` represents the empty space.
- Constraints: The puzzle is a 2x3 grid.
- Expected output format: The minimum number of moves required to solve the puzzle, or `-1` if it's impossible to solve.
- Key requirements and edge cases to consider:
  * The puzzle can be solved by moving the empty space up, down, left, or right.
  * The puzzle is solved when the numbers are in the order `[[1,2,3],[4,5,0]]`.
- Example test cases with explanations:
  * `board = [[1,2,3],[4,0,2]]`: The puzzle can be solved by moving the empty space down, then right.
  * `board = [[1,2,3],[4,5,0]]`: The puzzle is already solved.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible moves from the initial state, and recursively try all possible moves from each new state.
- Step-by-step breakdown of the solution:
  1. Start with the initial state of the puzzle.
  2. Try all possible moves from the current state (up, down, left, right).
  3. For each new state, recursively try all possible moves.
  4. If a solved state is found, return the number of moves.
  5. If all possible moves have been tried and no solved state has been found, return `-1`.
- Why this approach comes to mind first: It's a straightforward way to try all possible solutions, but it's inefficient because it does a lot of repeated work.

```cpp
#include <vector>
using namespace std;

int slidingPuzzle(vector<vector<int>>& board) {
    // Define the possible moves
    vector<pair<int, int>> moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    // Function to check if a state is solved
    bool isSolved(vector<vector<int>>& state) {
        vector<int> flatState;
        for (auto& row : state) {
            for (int num : row) {
                flatState.push_back(num);
            }
        }
        for (int i = 0; i < 5; i++) {
            if (flatState[i] != i + 1) return false;
        }
        return true;
    }
    
    // Function to perform a move
    vector<vector<int>> makeMove(vector<vector<int>>& state, int x, int y, int dx, int dy) {
        vector<vector<int>> newState = state;
        int newX = x + dx;
        int newY = y + dy;
        swap(newState[x][y], newState[newX][newY]);
        return newState;
    }
    
    // Perform the brute force search
    int x, y;
    for (x = 0; x < 2; x++) {
        for (y = 0; y < 3; y++) {
            if (board[x][y] == 0) break;
        }
        if (y < 3) break;
    }
    vector<vector<vector<int>>> queue = {board};
    int movesMade = 0;
    while (!queue.empty()) {
        int queueSize = queue.size();
        for (int i = 0; i < queueSize; i++) {
            vector<vector<int>> currentState = queue[0];
            queue.erase(queue.begin());
            if (isSolved(currentState)) return movesMade;
            for (auto& move : moves) {
                int newX = x + move.first;
                int newY = y + move.second;
                if (newX >= 0 && newX < 2 && newY >= 0 && newY < 3) {
                    vector<vector<int>> newState = makeMove(currentState, x, y, move.first, move.second);
                    queue.push_back(newState);
                }
            }
        }
        movesMade++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of moves. This is because in the worst case, we're trying all possible moves from each state.
> - **Space Complexity:** $O(4^n)$, because we're storing all the states in the queue.
> - **Why these complexities occur:** The brute force approach tries all possible moves from each state, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to try all possible moves in a more efficient way.
- Detailed breakdown of the approach:
  1. Start with the initial state of the puzzle.
  2. Try all possible moves from the current state (up, down, left, right).
  3. For each new state, check if it's been visited before. If not, mark it as visited and add it to the queue.
  4. If a solved state is found, return the number of moves.
  5. If all possible moves have been tried and no solved state has been found, return `-1`.
- Why further optimization is impossible: This approach tries all possible moves in a way that minimizes repeated work, making it optimal.

```cpp
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

int slidingPuzzle(vector<vector<int>>& board) {
    // Define the possible moves
    vector<pair<int, int>> moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    // Function to check if a state is solved
    bool isSolved(vector<vector<int>>& state) {
        vector<int> flatState;
        for (auto& row : state) {
            for (int num : row) {
                flatState.push_back(num);
            }
        }
        for (int i = 0; i < 5; i++) {
            if (flatState[i] != i + 1) return false;
        }
        return true;
    }
    
    // Function to perform a move
    vector<vector<int>> makeMove(vector<vector<int>>& state, int x, int y, int dx, int dy) {
        vector<vector<int>> newState = state;
        int newX = x + dx;
        int newY = y + dy;
        swap(newState[x][y], newState[newX][newY]);
        return newState;
    }
    
    // Perform the BFS
    int x, y;
    for (x = 0; x < 2; x++) {
        for (y = 0; y < 3; y++) {
            if (board[x][y] == 0) break;
        }
        if (y < 3) break;
    }
    queue<pair<vector<vector<int>>, int>> q;
    q.push({board, 0});
    unordered_set<string> visited;
    string boardStr;
    for (auto& row : board) {
        for (int num : row) {
            boardStr += to_string(num);
        }
    }
    visited.insert(boardStr);
    while (!q.empty()) {
        auto [currentState, movesMade] = q.front();
        q.pop();
        if (isSolved(currentState)) return movesMade;
        for (auto& move : moves) {
            int newX = x + move.first;
            int newY = y + move.second;
            if (newX >= 0 && newX < 2 && newY >= 0 && newY < 3) {
                vector<vector<int>> newState = makeMove(currentState, x, y, move.first, move.second);
                string newStateStr;
                for (auto& row : newState) {
                    for (int num : row) {
                        newStateStr += to_string(num);
                    }
                }
                if (visited.find(newStateStr) == visited.end()) {
                    visited.insert(newStateStr);
                    q.push({newState, movesMade + 1});
                }
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(b^d)$, where $b$ is the branching factor (the number of possible moves) and $d$ is the depth of the search (the number of moves required to solve the puzzle).
> - **Space Complexity:** $O(b^d)$, because we're storing all the states in the queue and the visited set.
> - **Optimality proof:** This approach tries all possible moves in a way that minimizes repeated work, making it optimal. The use of a queue and a visited set ensures that we don't visit the same state twice, which reduces the number of states we need to visit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue, visited set.
- Problem-solving patterns identified: trying all possible moves, using a queue and a visited set to minimize repeated work.
- Optimization techniques learned: using a queue and a visited set to reduce the number of states to visit.
- Similar problems to practice: other sliding puzzle problems, such as the 8-puzzle or the 15-puzzle.

**Mistakes to Avoid:**
- Common implementation errors: not checking if a state has been visited before, not using a queue to try all possible moves.
- Edge cases to watch for: the puzzle is already solved, the puzzle is impossible to solve.
- Performance pitfalls: trying all possible moves without using a queue and a visited set, which can lead to exponential time complexity.
- Testing considerations: test the function with different inputs, including the base case (the puzzle is already solved) and the edge case (the puzzle is impossible to solve).