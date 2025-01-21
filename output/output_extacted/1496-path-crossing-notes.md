## Path Crossing
**Problem Link:** https://leetcode.com/problems/path-crossing/description

**Problem Statement:**
- Input format: A string `path` of length `n`, consisting of 'N', 'S', 'E', 'W' characters, representing the directions of the path.
- Constraints: `1 <= path.length <= 10^4`
- Expected output format: `true` if the path crosses itself, `false` otherwise.
- Key requirements and edge cases to consider: 
    - A path crosses itself if, at some point, it visits a cell that it has already visited before.
    - The path can only move in the four main directions (up, down, left, right).
- Example test cases with explanations:
    - Input: "NESW"
      Output: true
      Explanation: The path crosses itself at the starting point.
    - Input: "NES"
      Output: false
      Explanation: The path does not cross itself.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if the path crosses itself, we can simulate the path and keep track of all the cells we have visited.
- Step-by-step breakdown of the solution:
    1. Create a set to store the visited cells.
    2. Initialize the current position to (0, 0).
    3. For each direction in the path:
        - Update the current position based on the direction.
        - If the current position is already in the set, return true.
        - Otherwise, add the current position to the set.
    4. If we have iterated through the entire path and not found any crossing, return false.
- Why this approach comes to mind first: It is a straightforward and intuitive way to simulate the path and check for crossings.

```cpp
#include <iostream>
#include <set>
#include <string>
using namespace std;

bool isPathCrossing(string path) {
    set<pair<int, int>> visited;
    int x = 0, y = 0;
    visited.insert({x, y});
    for (char dir : path) {
        if (dir == 'N') y++;
        else if (dir == 'S') y--;
        else if (dir == 'E') x++;
        else if (dir == 'W') x--;
        if (visited.count({x, y})) return true;
        visited.insert({x, y});
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the path, because we are iterating through the path once and performing constant time operations for each direction.
> - **Space Complexity:** $O(n)$, because in the worst case, we might visit $n$ different cells and store them in the set.
> - **Why these complexities occur:** The time complexity is linear because we are simulating the path and checking for crossings in a single pass. The space complexity is also linear because we are storing the visited cells in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem, as we must simulate the path and check for crossings in a single pass.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: We must check each direction in the path at least once to determine if the path crosses itself, so the time complexity cannot be improved.
- Why further optimization is impossible: We cannot avoid simulating the path and checking for crossings, so the time complexity is already optimal.

```cpp
#include <iostream>
#include <set>
#include <string>
using namespace std;

bool isPathCrossing(string path) {
    set<pair<int, int>> visited;
    int x = 0, y = 0;
    visited.insert({x, y});
    for (char dir : path) {
        if (dir == 'N') y++;
        else if (dir == 'S') y--;
        else if (dir == 'E') x++;
        else if (dir == 'W') x--;
        if (visited.count({x, y})) return true;
        visited.insert({x, y});
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the path.
> - **Space Complexity:** $O(n)$, because in the worst case, we might visit $n$ different cells and store them in the set.
> - **Optimality proof:** We must simulate the path and check for crossings in a single pass, so the time complexity cannot be improved.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulating a path and checking for crossings.
- Problem-solving patterns identified: Using a set to store visited cells and checking for duplicates.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems involving simulating a path and checking for conditions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the set with the starting position, or not checking for duplicates correctly.
- Edge cases to watch for: Empty path, path with only one direction, path with multiple directions that do not cross.
- Performance pitfalls: Using a data structure with slower lookup times, such as a list, instead of a set.
- Testing considerations: Test with different types of paths, including ones that cross and ones that do not cross.