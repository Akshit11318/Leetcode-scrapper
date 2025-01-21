## Check If Point Is Reachable
**Problem Link:** https://leetcode.com/problems/check-if-point-is-reachable/description

**Problem Statement:**
- Input: `x`, `y`, `maxMove`, `start`, `end`
- Constraints: `1 <= x, y, maxMove <= 10^9`, `1 <= start.length == end.length <= 2`, `0 <= start[i], end[i] <= 10^9`
- Expected Output: `true` if the point `end` is reachable from `start` within `maxMove` moves, `false` otherwise
- Key requirements and edge cases to consider: The movement is restricted to the `x` and `y` axes, and a move consists of either incrementing or decrementing the `x` coordinate or the `y` coordinate by 1.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible moves from the `start` point and see if we can reach the `end` point within `maxMove` moves.
- This approach involves using a queue to perform a breadth-first search (BFS) from the `start` point.
- We keep track of the visited points to avoid revisiting them.

```cpp
class Solution {
public:
    bool isReachable(vector<int>& start, vector<int>& end, int maxMove) {
        queue<vector<int>> q;
        q.push(start);
        set<string> visited;
        visited.insert(to_string(start[0]) + "," + to_string(start[1]));
        
        int moves = 0;
        while (!q.empty() && moves <= maxMove) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                vector<int> current = q.front();
                q.pop();
                
                if (current[0] == end[0] && current[1] == end[1]) {
                    return true;
                }
                
                vector<int> next = {current[0] + 1, current[1]};
                if (next[0] <= end[0] + maxMove - moves && next[1] <= end[1] + maxMove - moves && visited.find(to_string(next[0]) + "," + to_string(next[1])) == visited.end()) {
                    q.push(next);
                    visited.insert(to_string(next[0]) + "," + to_string(next[1]));
                }
                
                next = {current[0] - 1, current[1]};
                if (next[0] >= end[0] - maxMove + moves && next[1] <= end[1] + maxMove - moves && visited.find(to_string(next[0]) + "," + to_string(next[1])) == visited.end()) {
                    q.push(next);
                    visited.insert(to_string(next[0]) + "," + to_string(next[1]));
                }
                
                next = {current[0], current[1] + 1};
                if (next[0] <= end[0] + maxMove - moves && next[1] <= end[1] + maxMove - moves && visited.find(to_string(next[0]) + "," + to_string(next[1])) == visited.end()) {
                    q.push(next);
                    visited.insert(to_string(next[0]) + "," + to_string(next[1]));
                }
                
                next = {current[0], current[1] - 1};
                if (next[0] <= end[0] + maxMove - moves && next[1] >= end[1] - maxMove + moves && visited.find(to_string(next[0]) + "," + to_string(next[1])) == visited.end()) {
                    q.push(next);
                    visited.insert(to_string(next[0]) + "," + to_string(next[1]));
                }
            }
            moves++;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(maxMove^2)$, because in the worst case, we need to explore all points within a square of side length `maxMove`.
> - **Space Complexity:** $O(maxMove^2)$, because we need to store all visited points.
> - **Why these complexities occur:** The brute force approach involves exploring all possible moves, which leads to a quadratic time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to consider the difference in `x` and `y` coordinates between the `start` and `end` points.
- We can calculate the minimum number of moves required to reach the `end` point from the `start` point by taking the sum of the absolute differences in `x` and `y` coordinates.
- If the minimum number of moves is less than or equal to `maxMove`, we can reach the `end` point.

```cpp
class Solution {
public:
    bool isReachable(vector<int>& start, vector<int>& end, int maxMove) {
        int dx = abs(end[0] - start[0]);
        int dy = abs(end[1] - start[1]);
        return (dx + dy) <= maxMove && (dx + dy) % 2 == maxMove % 2;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only need to perform a constant number of operations.
> - **Space Complexity:** $O(1)$, because we only need to use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum number of moves required to reach the `end` point, and checks if it is within the allowed `maxMove`.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, optimal solution using mathematical insights.
- Problem-solving patterns identified: reducing the problem to a simpler form by considering the differences in coordinates.
- Optimization techniques learned: avoiding unnecessary exploration by using mathematical insights.
- Similar problems to practice: other problems involving movement restrictions and optimal paths.

**Mistakes to Avoid:**
- Common implementation errors: not considering the absolute differences in coordinates, not checking the parity of the sum of differences and `maxMove`.
- Edge cases to watch for: when `start` and `end` points are the same, when `maxMove` is 0.
- Performance pitfalls: using a brute force approach without considering the optimal solution.
- Testing considerations: testing with different inputs, including edge cases and large inputs.