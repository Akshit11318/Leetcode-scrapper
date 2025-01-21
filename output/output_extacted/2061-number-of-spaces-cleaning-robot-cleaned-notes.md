## Number of Spaces Cleaning Robot Cleaned
**Problem Link:** https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/description

**Problem Statement:**
- The problem requires calculating the number of spaces cleaned by a robot in a grid. The robot moves according to the given instructions.
- Input format: A 2D grid and a string of instructions (e.g., "L", "R", "U", "D").
- Expected output format: The total number of unique cells visited by the robot.
- Key requirements and edge cases to consider:
  - The robot starts at the origin (0, 0).
  - The robot can move in four directions: up, down, left, right.
  - The grid is unbounded, but the robot's movement is constrained by the given instructions.
- Example test cases with explanations:
  - For a grid with no obstacles and instructions "LL", the robot moves to the left twice, visiting two cells.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves simulating the robot's movement step by step.
- We can use a set to keep track of visited cells.
- We iterate through the instructions and update the robot's position accordingly.

```cpp
int robotCleaned(vector<vector<int>>& room, string path) {
    // Initialize the set to store visited cells
    set<pair<int, int>> visited;
    // Initialize the robot's position
    pair<int, int> pos(0, 0);
    // Add the initial position to the set
    visited.insert(pos);
    // Define the possible movements
    map<char, pair<int, int>> movements = {{'U', {0, 1}}, {'D', {0, -1}}, {'L', {-1, 0}}, {'R', {1, 0}}};
    // Iterate through the instructions
    for (char c : path) {
        // Update the robot's position
        pos.first += movements[c].first;
        pos.second += movements[c].second;
        // Add the new position to the set
        visited.insert(pos);
    }
    // Return the number of unique cells visited
    return visited.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the instruction string, because we iterate through the instructions once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might visit a new cell for each instruction.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each instruction. The space complexity is also linear because we store each visited cell in the set.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is similar to the brute force approach, but we can optimize the code by using a more efficient data structure to store visited cells.
- We can use an unordered set to reduce the lookup time.
- The key insight is that we don't need to store the entire grid, just the visited cells.

```cpp
int robotCleaned(vector<vector<int>>& room, string path) {
    // Initialize the set to store visited cells
    unordered_set<string> visited;
    // Initialize the robot's position
    pair<int, int> pos(0, 0);
    // Add the initial position to the set
    visited.insert(to_string(pos.first) + "," + to_string(pos.second));
    // Define the possible movements
    map<char, pair<int, int>> movements = {{'U', {0, 1}}, {'D', {0, -1}}, {'L', {-1, 0}}, {'R', {1, 0}}};
    // Iterate through the instructions
    for (char c : path) {
        // Update the robot's position
        pos.first += movements[c].first;
        pos.second += movements[c].second;
        // Add the new position to the set
        visited.insert(to_string(pos.first) + "," + to_string(pos.second));
    }
    // Return the number of unique cells visited
    return visited.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the instruction string, because we iterate through the instructions once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might visit a new cell for each instruction.
> - **Optimality proof:** This is the optimal solution because we only store the visited cells, and we use an efficient data structure to store them.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a set to keep track of visited cells.
- The problem-solving pattern identified is the simulation of the robot's movement step by step.
- The optimization technique learned is the use of an efficient data structure to store visited cells.
- Similar problems to practice include other simulation problems, such as simulating a game or a process.

**Mistakes to Avoid:**
- A common implementation error is not handling the edge cases correctly, such as the robot moving out of the grid.
- A performance pitfall is using an inefficient data structure to store visited cells, such as a vector or a list.
- A testing consideration is to test the solution with different inputs, including edge cases and corner cases.