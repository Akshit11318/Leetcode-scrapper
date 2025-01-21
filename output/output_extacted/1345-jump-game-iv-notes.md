## Jump Game IV
**Problem Link:** https://leetcode.com/problems/jump-game-iv/description

**Problem Statement:**
- Input format: An array of integers `arr` where `arr[i]` represents the maximum jump length from index `i`.
- Constraints: The length of `arr` is between 1 and 10,000. Each element in `arr` is between 1 and 10,000.
- Expected output format: The minimum number of operations to reach the end of the array.
- Key requirements and edge cases to consider: The end of the array is considered reachable if there exists a sequence of jumps that lands on the last index. The array is 0-indexed.
- Example test cases with explanations:
  - Input: `arr = [100,-23,-23,404,1001,93,0,1,92,92,-23]`
    Output: `3`
    Explanation: From the start, we can jump to index 1 (arr[0] = 100), then to index 4 (arr[1] = -23, but we can jump from index 1 to index 4 because arr[4] = 1001 which is greater than the distance between index 1 and 4), then to the end (arr[4] = 1001 which is greater than the distance between index 4 and the end).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible jumps from each position and use a depth-first search (DFS) or breadth-first search (BFS) to explore all reachable positions.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the starting position (index 0) and the number of operations (0).
  2. For each position in the queue, try all possible jumps and add the new positions to the queue if they have not been visited before.
  3. If the end of the array is reached, return the number of operations.
- Why this approach comes to mind first: It is a straightforward way to explore all possible solutions, but it can be inefficient due to the large number of possible jumps.

```cpp
#include <queue>
#include <unordered_set>

int minOperations(vector<int>& arr) {
    int n = arr.size();
    std::queue<std::pair<int, int>> q; // position, operations
    std::unordered_set<int> visited;
    q.push({0, 0});
    while (!q.empty()) {
        int pos = q.front().first;
        int ops = q.front().second;
        q.pop();
        if (pos == n - 1) return ops;
        if (visited.find(pos) != visited.end()) continue;
        visited.insert(pos);
        for (int i = 1; i <= arr[pos]; i++) {
            if (pos + i < n) {
                q.push({pos + i, ops + 1});
            }
        }
    }
    return -1; // unreachable
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot max(arr))$ where $n$ is the length of the array and $max(arr)$ is the maximum value in the array. This is because in the worst case, we need to try all possible jumps from each position.
> - **Space Complexity:** $O(n)$ for the queue and the visited set.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible jumps, and the space complexity is moderate because we need to store the visited positions and the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a BFS with a priority queue to explore the positions with the minimum number of operations first.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the starting position (index 0) and the number of operations (0).
  2. For each position in the queue, try all possible jumps and add the new positions to the queue if they have not been visited before.
  3. If the end of the array is reached, return the number of operations.
- Proof of optimality: This approach is optimal because it explores the positions with the minimum number of operations first, which guarantees that we find the minimum number of operations to reach the end of the array.

```cpp
#include <queue>
#include <unordered_set>

int minOperations(vector<int>& arr) {
    int n = arr.size();
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> q; // operations, position
    std::unordered_set<int> visited;
    q.push({0, 0});
    while (!q.empty()) {
        int ops = q.top().first;
        int pos = q.top().second;
        q.pop();
        if (pos == n - 1) return ops;
        if (visited.find(pos) != visited.end()) continue;
        visited.insert(pos);
        for (int i = 1; i <= arr[pos]; i++) {
            if (pos + i < n) {
                q.push({ops + 1, pos + i});
            }
        }
    }
    return -1; // unreachable
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ where $n$ is the length of the array. This is because we use a priority queue to explore the positions with the minimum number of operations first.
> - **Space Complexity:** $O(n)$ for the queue and the visited set.
> - **Optimality proof:** This approach is optimal because it explores the positions with the minimum number of operations first, which guarantees that we find the minimum number of operations to reach the end of the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, priority queue, and dynamic programming.
- Problem-solving patterns identified: exploring all possible solutions and using a priority queue to optimize the search.
- Optimization techniques learned: using a priority queue to explore the positions with the minimum number of operations first.
- Similar problems to practice: Jump Game, Jump Game II, and other problems that involve exploring all possible solutions and optimizing the search.

**Mistakes to Avoid:**
- Common implementation errors: not checking for visited positions, not using a priority queue to optimize the search.
- Edge cases to watch for: the end of the array is not reachable, the array is empty.
- Performance pitfalls: using a brute force approach that tries all possible jumps, not using a priority queue to optimize the search.
- Testing considerations: test the function with different inputs, including edge cases and large inputs.