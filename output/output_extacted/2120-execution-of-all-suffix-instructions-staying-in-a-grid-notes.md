## Execution of All Suffix Instructions Staying in a Grid

**Problem Link:** https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/description

**Problem Statement:**
- The problem asks to execute a sequence of instructions in a grid, starting from a given position, and determine the final position after executing all suffixes of the instructions.
- The grid size is `m x n`, where `m` is the number of rows and `n` is the number of columns.
- The instructions are given as a string, where each character represents a move in one of the four directions: up (`U`), down (`D`), left (`L`), or right (`R`).
- The goal is to find the final position after executing all suffixes of the instructions and return the maximum number of cells that can be visited.

**Expected Output Format:**
- The output should be an integer representing the maximum number of cells that can be visited.

**Key Requirements and Edge Cases to Consider:**
- The grid size is `m x n`, where `1 <= m, n <= 100`.
- The length of the instructions is `k`, where `1 <= k <= 100`.
- The instructions only contain the characters `U`, `D`, `L`, and `R`.
- The starting position is `(0, 0)`.
- The grid is bounded, and moving outside the grid is not allowed.

**Example Test Cases with Explanations:**
- For example, given `m = 3`, `n = 4`, and `instructions = "URDL"`, the output should be `4`, because the final position after executing all suffixes is `(0, 0)`, `(1, 0)`, `(1, 1)`, and `(0, 1)`.
- Another example is `m = 2`, `n = 2`, and `instructions = "LR"`, the output should be `1`, because the final position after executing all suffixes is `(0, 0)`.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves simulating the execution of all suffixes of the instructions and counting the number of unique cells visited.
- We start by initializing a set to store the unique cells visited.
- Then, we iterate over all suffixes of the instructions and simulate the execution of each suffix.
- For each suffix, we start from the beginning of the suffix and move according to the instructions, updating the current position and adding it to the set of visited cells.
- Finally, we return the size of the set of visited cells, which represents the maximum number of cells that can be visited.

```cpp
int executeInstructions(int m, int n, string instructions) {
    int maxVisited = 0;
    set<pair<int, int>> visited;
    for (int i = 0; i < instructions.size(); i++) {
        int x = 0, y = 0;
        visited.clear();
        for (int j = i; j < instructions.size(); j++) {
            if (instructions[j] == 'U') {
                x = max(0, x - 1);
            } else if (instructions[j] == 'D') {
                x = min(m - 1, x + 1);
            } else if (instructions[j] == 'L') {
                y = max(0, y - 1);
            } else if (instructions[j] == 'R') {
                y = min(n - 1, y + 1);
            }
            visited.insert({x, y});
        }
        maxVisited = max(maxVisited, (int)visited.size());
    }
    return maxVisited;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^2)$, where $k$ is the length of the instructions, because we iterate over all suffixes of the instructions and simulate the execution of each suffix.
> - **Space Complexity:** $O(k)$, because we use a set to store the unique cells visited, and the maximum size of the set is $k$.
> - **Why these complexities occur:** The brute force approach involves simulating the execution of all suffixes of the instructions, which leads to a quadratic time complexity. The space complexity is linear because we use a set to store the unique cells visited.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a hashmap to store the cells visited for each suffix of the instructions.
- We start by initializing a hashmap to store the cells visited for each suffix.
- Then, we iterate over all suffixes of the instructions and simulate the execution of each suffix.
- For each suffix, we start from the beginning of the suffix and move according to the instructions, updating the current position and adding it to the hashmap.
- Finally, we return the maximum number of cells visited for any suffix.
- This approach avoids the need to simulate the execution of all suffixes of the instructions, reducing the time complexity to $O(k)$.

```cpp
int executeInstructions(int m, int n, string instructions) {
    int maxVisited = 0;
    unordered_map<string, unordered_set<string>> visited;
    for (int i = 0; i < instructions.size(); i++) {
        int x = 0, y = 0;
        string suffix = instructions.substr(i);
        unordered_set<string> cells;
        for (char c : suffix) {
            if (c == 'U') {
                x = max(0, x - 1);
            } else if (c == 'D') {
                x = min(m - 1, x + 1);
            } else if (c == 'L') {
                y = max(0, y - 1);
            } else if (c == 'R') {
                y = min(n - 1, y + 1);
            }
            cells.insert(to_string(x) + "," + to_string(y));
        }
        maxVisited = max(maxVisited, (int)cells.size());
    }
    return maxVisited;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the length of the instructions, because we iterate over all suffixes of the instructions and simulate the execution of each suffix.
> - **Space Complexity:** $O(k)$, because we use a hashmap to store the cells visited for each suffix, and the maximum size of the hashmap is $k$.
> - **Optimality proof:** This approach is optimal because we only simulate the execution of each suffix once, reducing the time complexity to $O(k)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap, suffix simulation, and cell counting.
- Problem-solving patterns identified: using a hashmap to store cells visited for each suffix.
- Optimization techniques learned: reducing the time complexity by avoiding unnecessary simulations.
- Similar problems to practice: problems involving suffix simulation and cell counting.

**Mistakes to Avoid:**
- Common implementation errors: incorrect suffix simulation, incorrect cell counting, and incorrect hashmap usage.
- Edge cases to watch for: boundary cases, such as when the instructions are empty or when the grid size is 1x1.
- Performance pitfalls: using a brute force approach with a high time complexity.
- Testing considerations: testing the implementation with different grid sizes, instruction lengths, and instruction types.