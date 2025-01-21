## Minimum Operations to Convert Number
**Problem Link:** https://leetcode.com/problems/minimum-operations-to-convert-number/description

**Problem Statement:**
- Input format and constraints: Given two integers `num` and `target`, return the minimum number of operations required to convert `num` to `target`.
- Expected output format: The minimum number of operations required.
- Key requirements and edge cases to consider: The allowed operations are addition and subtraction of `1`, and multiplication and division by `2`.
- Example test cases with explanations: 
    - `num = 2, target = 3` should return `2` because `2 * 2 = 4` then `4 - 1 = 3`.
    - `num = 5, target = 2` should return `4` because `5 / 2 = 2.5` then `2.5 * 2 = 5` then `5 - 3 = 2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible operations at each step and exploring all possible paths until we reach the target.
- Step-by-step breakdown of the solution:
    1. Start with the initial number `num`.
    2. At each step, try all four operations: add `1`, subtract `1`, multiply by `2`, and divide by `2` if possible.
    3. Keep track of the number of operations performed.
    4. If the target is reached, return the number of operations.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities, but it's inefficient due to its exponential time complexity.

```cpp
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minimumOperations(int num, int target) {
        unordered_set<int> visited;
        queue<pair<int, int>> q; // {number, operations}
        q.push({num, 0});
        
        while (!q.empty()) {
            int n = q.front().first;
            int ops = q.front().second;
            q.pop();
            
            if (n == target) return ops;
            if (visited.find(n) != visited.end()) continue;
            visited.insert(n);
            
            // Add 1
            if (n + 1 <= 1000) q.push({n + 1, ops + 1});
            // Subtract 1
            if (n - 1 >= 0) q.push({n - 1, ops + 1});
            // Multiply by 2
            if (n * 2 <= 1000) q.push({n * 2, ops + 1});
            // Divide by 2
            if (n % 2 == 0) q.push({n / 2, ops + 1});
        }
        
        return -1; // Target cannot be reached
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^d)$ where $d$ is the number of operations required to reach the target, because we try all four operations at each step.
> - **Space Complexity:** $O(4^d)$ because we store all possible numbers in the queue.
> - **Why these complexities occur:** The exponential time and space complexities occur because we explore all possible paths without any pruning.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) with a queue to explore all possible numbers level by level.
- Detailed breakdown of the approach:
    1. Start with the initial number `num` and add it to the queue.
    2. At each level, try all four operations for each number in the queue.
    3. Keep track of the number of operations performed.
    4. If the target is reached, return the number of operations.
- Proof of optimality: This approach is optimal because it explores all possible numbers in the shortest number of operations.

```cpp
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minimumOperations(int num, int target) {
        unordered_set<int> visited;
        queue<pair<int, int>> q; // {number, operations}
        q.push({num, 0});
        visited.insert(num);
        
        while (!q.empty()) {
            int n = q.front().first;
            int ops = q.front().second;
            q.pop();
            
            if (n == target) return ops;
            
            // Add 1
            if (n + 1 <= 1000 && visited.find(n + 1) == visited.end()) {
                q.push({n + 1, ops + 1});
                visited.insert(n + 1);
            }
            // Subtract 1
            if (n - 1 >= 0 && visited.find(n - 1) == visited.end()) {
                q.push({n - 1, ops + 1});
                visited.insert(n - 1);
            }
            // Multiply by 2
            if (n * 2 <= 1000 && visited.find(n * 2) == visited.end()) {
                q.push({n * 2, ops + 1});
                visited.insert(n * 2);
            }
            // Divide by 2
            if (n % 2 == 0 && visited.find(n / 2) == visited.end()) {
                q.push({n / 2, ops + 1});
                visited.insert(n / 2);
            }
        }
        
        return -1; // Target cannot be reached
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(b^d)$ where $b$ is the branching factor (4 in this case) and $d$ is the number of operations required to reach the target.
> - **Space Complexity:** $O(b^d)$ because we store all possible numbers in the queue.
> - **Optimality proof:** This approach is optimal because it explores all possible numbers in the shortest number of operations using a BFS.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, and optimal search strategy.
- Problem-solving patterns identified: Using BFS to explore all possible solutions level by level.
- Optimization techniques learned: Pruning the search space by avoiding duplicate numbers.
- Similar problems to practice: Other graph traversal and search problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicate numbers, not handling edge cases correctly.
- Edge cases to watch for: Numbers that are out of range, division by zero.
- Performance pitfalls: Using an inefficient search strategy or data structure.
- Testing considerations: Test the solution with different inputs and edge cases to ensure correctness.