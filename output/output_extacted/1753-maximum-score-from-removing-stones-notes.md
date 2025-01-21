## Maximum Score from Removing Stones

**Problem Link:** https://leetcode.com/problems/maximum-score-from-removing-stones/description

**Problem Statement:**
- Input: Three integers `a`, `b`, and `c`, representing the number of stones in three piles.
- Constraints: `1 <= a, b, c <= 100`.
- Expected Output: The maximum score that can be achieved by removing stones from the piles.
- Key Requirements: The score is calculated by removing two stones from the same pile or one stone from each of two different piles.
- Edge Cases: When all piles have only one stone, no more moves can be made.

**Example Test Cases:**
- `a = 2, b = 4, c = 6`, expected output: `6`.
- `a = 4, b = 4, c = 6`, expected output: `5`.
- `a = 1, b = 1, c = 1`, expected output: `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing stones and calculate the score for each combination.
- Step-by-step breakdown:
  1. Initialize a queue with the initial state of the piles.
  2. Initialize a set to keep track of visited states.
  3. Dequeue a state and check if it has been visited before.
  4. If not, mark it as visited and generate all possible next states by removing stones.
  5. Enqueue the next states and repeat the process until the queue is empty.
  6. Keep track of the maximum score achieved during the process.

```cpp
#include <queue>
#include <unordered_set>

class Solution {
public:
    int maximumScore(int a, int b, int c) {
        std::queue<std::tuple<int, int, int>> q;
        std::unordered_set<std::tuple<int, int, int>> visited;
        q.push({a, b, c});
        visited.insert({a, b, c});
        int maxScore = 0;
        
        while (!q.empty()) {
            auto [x, y, z] = q.front();
            q.pop();
            maxScore = std::max(maxScore, x + y + z);
            
            if (x > 0 && y > 0) {
                int newX = x - 1;
                int newY = y - 1;
                if (visited.find({newX, newY, z}) == visited.end()) {
                    q.push({newX, newY, z});
                    visited.insert({newX, newY, z});
                }
            }
            
            if (x > 0 && z > 0) {
                int newX = x - 1;
                int newZ = z - 1;
                if (visited.find({newX, y, newZ}) == visited.end()) {
                    q.push({newX, y, newZ});
                    visited.insert({newX, y, newZ});
                }
            }
            
            if (y > 0 && z > 0) {
                int newY = y - 1;
                int newZ = z - 1;
                if (visited.find({x, newY, newZ}) == visited.end()) {
                    q.push({x, newY, newZ});
                    visited.insert({x, newY, newZ});
                }
            }
        }
        
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{a+b+c})$, because in the worst case, we have to explore all possible combinations of removing stones.
> - **Space Complexity:** $O(3^{a+b+c})$, because we need to store all visited states in the set.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of removing stones, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a greedy approach. We always try to remove stones from the pile with the most stones.
- Detailed breakdown:
  1. Initialize the score to 0.
  2. While there are at least two stones in any pile, remove stones from the pile with the most stones.
  3. Update the score accordingly.
  4. Repeat the process until no more moves can be made.

```cpp
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        int score = 0;
        
        while ((a > 0 && b > 0) || (a > 0 && c > 0) || (b > 0 && c > 0)) {
            if (a >= b && a >= c) {
                if (b > 0) {
                    a--;
                    b--;
                } else {
                    a--;
                    c--;
                }
            } else if (b >= a && b >= c) {
                if (a > 0) {
                    a--;
                    b--;
                } else {
                    b--;
                    c--;
                }
            } else {
                if (a > 0) {
                    a--;
                    c--;
                } else {
                    b--;
                    c--;
                }
            }
            score++;
        }
        
        return score;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(a + b + c)$, because we remove stones from the piles until no more moves can be made.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the score and the piles.
> - **Optimality proof:** The greedy approach always tries to remove stones from the pile with the most stones, ensuring that we maximize the score.

---

### Final Notes

**Learning Points:**
- The importance of exploring different approaches to a problem, including brute force and greedy algorithms.
- How to analyze the time and space complexity of an algorithm.
- The trade-offs between different approaches, including the balance between time and space complexity.

**Mistakes to Avoid:**
- Failing to consider the constraints and edge cases of the problem.
- Not analyzing the time and space complexity of the algorithm.
- Not considering alternative approaches to the problem.

By following this approach, you can develop a deep understanding of the problem and its solution, and improve your skills in algorithmic problem-solving.