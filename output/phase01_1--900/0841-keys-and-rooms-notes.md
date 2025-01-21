## Keys and Rooms
**Problem Link:** https://leetcode.com/problems/keys-and-rooms/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector `rooms` where each `rooms[i]` is a vector of integers representing the keys in room `i`. The goal is to find if all rooms can be visited.
- Expected output format: Return `true` if all rooms can be visited, otherwise return `false`.
- Key requirements and edge cases to consider: We need to keep track of visited rooms to avoid infinite loops. The number of rooms and keys in each room can vary.
- Example test cases with explanations:
  - Example 1:
    - Input: `rooms = [[1],[2],[3],[]]`
    - Output: `true`
    - Explanation: We start in room 0, and pick up key 1. Then we go to room 1 and pick up key 2. Finally, we go to room 2 and pick up key 3. We can now go to room 3 and visit all rooms.
  - Example 2:
    - Input: `rooms = [[1,3],[3,0,1],[2],[0]]`
    - Output: `false`
    - Explanation: We can't enter room 2 because we don't have key 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try to visit each room and see if we can visit all rooms.
- Step-by-step breakdown of the solution:
  1. Start in room 0.
  2. Visit each room and add its keys to a set.
  3. If we can visit a room, mark it as visited.
  4. If we can't visit a room, return false.
- Why this approach comes to mind first: This approach is simple and straightforward. It's easy to understand and implement.

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        vector<int> keys;
        
        // Start in room 0
        visited[0] = true;
        for (int key : rooms[0]) {
            keys.push_back(key);
        }
        
        // Visit each room and add its keys to the set
        while (!keys.empty()) {
            int key = keys[0];
            keys.erase(keys.begin());
            if (!visited[key]) {
                visited[key] = true;
                for (int newKey : rooms[key]) {
                    keys.push_back(newKey);
                }
            }
        }
        
        // If we can't visit a room, return false
        for (bool visit : visited) {
            if (!visit) {
                return false;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of rooms and $m$ is the total number of keys.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of rooms and $m$ is the total number of keys.
> - **Why these complexities occur:** We visit each room once and add its keys to the set. We also need to store the visited rooms and keys.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a queue to keep track of the rooms to visit and a set to keep track of the visited rooms.
- Detailed breakdown of the approach:
  1. Start in room 0 and add it to the queue.
  2. While the queue is not empty, dequeue a room and visit it.
  3. If we haven't visited the room before, mark it as visited and add its keys to the queue.
- Proof of optimality: This approach is optimal because we visit each room only once and use a queue to keep track of the rooms to visit.
- Why further optimization is impossible: We need to visit each room at least once to determine if we can visit all rooms.

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        queue<int> q;
        
        // Start in room 0
        q.push(0);
        visited[0] = true;
        
        // Visit each room and add its keys to the queue
        while (!q.empty()) {
            int room = q.front();
            q.pop();
            for (int key : rooms[room]) {
                if (!visited[key]) {
                    q.push(key);
                    visited[key] = true;
                }
            }
        }
        
        // If we can't visit a room, return false
        for (bool visit : visited) {
            if (!visit) {
                return false;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of rooms and $m$ is the total number of keys.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of rooms and $m$ is the total number of keys.
> - **Optimality proof:** We visit each room only once and use a queue to keep track of the rooms to visit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph traversal, queue, set.
- Problem-solving patterns identified: Using a queue to keep track of the rooms to visit and a set to keep track of the visited rooms.
- Optimization techniques learned: Using a queue to avoid visiting the same room multiple times.
- Similar problems to practice: Graph traversal problems, such as finding the shortest path between two nodes.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a room has been visited before visiting it.
- Edge cases to watch for: Handling the case where a room has no keys.
- Performance pitfalls: Using a recursive approach instead of an iterative approach.
- Testing considerations: Testing the case where all rooms can be visited and the case where not all rooms can be visited.