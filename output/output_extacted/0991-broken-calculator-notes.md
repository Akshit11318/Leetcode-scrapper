## Broken Calculator
**Problem Link:** https://leetcode.com/problems/broken-calculator/description

**Problem Statement:**
- Input format: Two integers `X` and `Y`, where `X` is the starting number and `Y` is the target number.
- Constraints: `1 <= X, Y <= 10^6`.
- Expected output format: The minimum number of operations required to reach `Y` from `X` using a broken calculator that can only perform two operations: increment (`+1`) and divide by 2 (`/2`).
- Key requirements: The calculator can only divide by 2 if the current number is even.
- Example test cases:
  - Input: `X = 2, Y = 3`, Output: `2` (Explanation: `2 -> 1 -> 3` or `2 -> 4 -> 2 -> 1 -> 3`).
  - Input: `X = 5, Y = 8`, Output: `2` (Explanation: `5 -> 4 -> 8`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate all possible operations from `X` until we reach `Y`.
- We can use a queue to implement a breadth-first search (BFS), where each state is the current number and the number of operations performed so far.
- We start with the initial state `(X, 0)` and explore all possible next states by applying the increment and divide by 2 operations.

```cpp
#include <queue>
using namespace std;

class Solution {
public:
    int brokenCalc(int X, int Y) {
        queue<pair<int, int>> q;
        q.push({X, 0});
        unordered_set<int> visited;
        visited.insert(X);
        
        while (!q.empty()) {
            int curr = q.front().first;
            int steps = q.front().second;
            q.pop();
            
            if (curr == Y) return steps;
            
            // Increment operation
            if (curr + 1 <= Y && visited.find(curr + 1) == visited.end()) {
                q.push({curr + 1, steps + 1});
                visited.insert(curr + 1);
            }
            
            // Divide by 2 operation
            if (curr % 2 == 0 && curr / 2 > 0 && visited.find(curr / 2) == visited.end()) {
                q.push({curr / 2, steps + 1});
                visited.insert(curr / 2);
            }
        }
        
        return -1; // Should not reach here
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^Y)$, where $Y$ is the target number. This is because in the worst case, we might need to explore all numbers up to $Y$.
> - **Space Complexity:** $O(2^Y)$, where $Y$ is the target number. This is because we need to store all visited numbers to avoid revisiting them.
> - **Why these complexities occur:** The brute force approach explores all possible states, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to work backwards from `Y` to `X`.
- We can use a greedy approach to find the minimum number of operations.
- If `Y` is even, we can always divide it by 2, which reduces the number of operations.
- If `Y` is odd, we need to increment it to the next even number, which increases the number of operations.

```cpp
class Solution {
public:
    int brokenCalc(int X, int Y) {
        int operations = 0;
        while (Y > X) {
            if (Y % 2 == 0) {
                Y /= 2;
            } else {
                Y = (Y + 1) / 2;
                operations++;
            }
            operations++;
        }
        return operations + X - Y;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log Y)$, where $Y$ is the target number. This is because we divide `Y` by 2 in each iteration, which reduces the number of iterations.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we only use a constant amount of space to store the variables.
> - **Optimality proof:** The greedy approach ensures that we always choose the operation that reduces the number of operations, which leads to the minimum number of operations.

---

### Final Notes

**Learning Points:**
- The importance of working backwards in problems with a target value.
- The use of greedy algorithms to find the minimum number of operations.
- The need to consider the parity of numbers when working with division by 2.

**Mistakes to Avoid:**
- Not considering the parity of numbers when working with division by 2.
- Not using a greedy approach to find the minimum number of operations.
- Not working backwards from the target value to the starting value.