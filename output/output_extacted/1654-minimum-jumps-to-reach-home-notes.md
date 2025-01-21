## Minimum Jumps to Reach Home
**Problem Link:** https://leetcode.com/problems/minimum-jumps-to-reach-home/description

**Problem Statement:**
- Input format and constraints: Given an integer array `forbidden` and integers `a`, `b`, `x`, and `start`, return the minimum number of jumps required to reach the home position `0` from the start position `start`. The array `forbidden` contains positions that cannot be visited.
- Expected output format: The minimum number of jumps required to reach the home position `0`.
- Key requirements and edge cases to consider: The frog can only jump forward or backward by `a` or `b` steps. The frog cannot visit the same position more than once.
- Example test cases with explanations:
  - Input: `forbidden = [1,2,3,4,5,6,7], a = 4, b = 5, x = 4, start = 0`
    Output: `6`
  - Input: `forbidden = [1,2,3,4,5,6,7], a = 4, b = 5, x = 4, start = 4`
    Output: `3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the minimum number of jumps, we can try all possible jumps from the start position and recursively try all possible jumps from each new position.
- Step-by-step breakdown of the solution:
  1. Create a set of forbidden positions for efficient lookups.
  2. Define a recursive function to try all possible jumps from a given position.
  3. Use a visited set to keep track of visited positions and avoid infinite loops.
  4. Try all possible jumps (forward and backward) by `a` and `b` steps.
  5. If a jump lands on a forbidden position or a visited position, skip it.
  6. If a jump lands on the home position `0`, return the number of jumps.
  7. Otherwise, recursively try all possible jumps from the new position.
- Why this approach comes to mind first: It's a straightforward and intuitive approach to try all possible jumps and see which one leads to the minimum number of jumps.

```cpp
class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x, int start) {
        unordered_set<int> forbiddenSet(forbidden.begin(), forbidden.end());
        unordered_set<int> visited;
        int maxPos = max(x, start) + max(a, b) * 100; // arbitrary large number
        return dfs(forbiddenSet, visited, a, b, x, start, 0, maxPos);
    }
    
    int dfs(unordered_set<int>& forbiddenSet, unordered_set<int>& visited, int a, int b, int x, int pos, int jumps, int maxPos) {
        if (pos == 0) return jumps;
        if (pos < 0 || pos > maxPos || forbiddenSet.count(pos) || visited.count(pos)) return INT_MAX;
        visited.insert(pos);
        int res = INT_MAX;
        res = min(res, dfs(forbiddenSet, visited, a, b, x, pos + a, jumps + 1, maxPos));
        res = min(res, dfs(forbiddenSet, visited, a, b, x, pos - b, jumps + 1, maxPos));
        res = min(res, dfs(forbiddenSet, visited, a, b, x, pos + b, jumps + 1, maxPos));
        visited.erase(pos);
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{\frac{maxPos}{min(a,b)}})$, where $maxPos$ is the maximum possible position and $min(a,b)$ is the minimum jump size. This is because we try all possible jumps from each position, and the number of possible positions is proportional to $maxPos$.
> - **Space Complexity:** $O(maxPos)$, where $maxPos$ is the maximum possible position. This is because we use a set to keep track of visited positions.
> - **Why these complexities occur:** The brute force approach tries all possible jumps from each position, leading to exponential time complexity. The space complexity is linear because we use a set to keep track of visited positions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a queue to perform a breadth-first search (BFS) instead of recursive depth-first search (DFS). This allows us to avoid revisiting the same position and reduces the time complexity.
- Detailed breakdown of the approach:
  1. Create a set of forbidden positions for efficient lookups.
  2. Create a queue to store positions to visit, along with the number of jumps.
  3. Enqueue the start position with 0 jumps.
  4. While the queue is not empty, dequeue a position and try all possible jumps (forward and backward) by `a` and `b` steps.
  5. If a jump lands on a forbidden position or a visited position, skip it.
  6. If a jump lands on the home position `0`, return the number of jumps.
  7. Otherwise, mark the new position as visited and enqueue it with the updated number of jumps.
- Why further optimization is impossible: The optimal approach tries all possible jumps from each position, but uses a queue to avoid revisiting the same position. This is the most efficient way to find the minimum number of jumps.

```cpp
class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x, int start) {
        unordered_set<int> forbiddenSet(forbidden.begin(), forbidden.end());
        unordered_set<int> visited;
        queue<pair<int, int>> q;
        q.push({start, 0});
        int maxPos = max(x, start) + max(a, b) * 100; // arbitrary large number
        while (!q.empty()) {
            int pos = q.front().first;
            int jumps = q.front().second;
            q.pop();
            if (pos == 0) return jumps;
            if (pos < 0 || pos > maxPos || forbiddenSet.count(pos) || visited.count(pos)) continue;
            visited.insert(pos);
            q.push({pos + a, jumps + 1});
            q.push({pos - b, jumps + 1});
            if (pos - a >= 0 && !forbiddenSet.count(pos - a) && !visited.count(pos - a)) {
                q.push({pos - a, jumps + 1});
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(maxPos)$, where $maxPos$ is the maximum possible position. This is because we try all possible jumps from each position, and the number of possible positions is proportional to $maxPos$.
> - **Space Complexity:** $O(maxPos)$, where $maxPos$ is the maximum possible position. This is because we use a set to keep track of visited positions and a queue to store positions to visit.
> - **Optimality proof:** The optimal approach tries all possible jumps from each position, but uses a queue to avoid revisiting the same position. This is the most efficient way to find the minimum number of jumps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue, and set.
- Problem-solving patterns identified: Using a queue to avoid revisiting the same position and reducing time complexity.
- Optimization techniques learned: Avoiding recursive DFS and using a queue instead.
- Similar problems to practice: Other problems involving BFS and queue, such as finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for forbidden positions or visited positions before trying a jump.
- Edge cases to watch for: Handling the case where the start position is the home position `0`.
- Performance pitfalls: Using recursive DFS instead of BFS, leading to exponential time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.