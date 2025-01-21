## Open the Lock

**Problem Link:** https://leetcode.com/problems/open-the-lock/description

**Problem Statement:**
- Input format: `deadends` - a list of strings representing dead end combinations, and `target` - a string representing the target combination.
- Constraints: Each combination is a string of four digits from '0' to '9'. The lock has 10,000 possible combinations.
- Expected output format: The minimum number of turns to open the lock, or `-1` if it's impossible.
- Key requirements and edge cases to consider: 
    - If the `target` is already the initial state `"0000"`, return `0`.
    - If the `target` is in `deadends`, return `-1`.
    - The lock can only be turned in one direction (i.e., increasing or decreasing the digit).
- Example test cases with explanations:
    - If `deadends = ["0201","0101","0102","1212","2002"]` and `target = "0202"`, the function should return `6`.
    - If `deadends = ["8888"]` and `target = "0009"`, the function should return `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of turns and check if we reach the target combination.
- Step-by-step breakdown of the solution:
    1. Start from the initial combination `"0000"`.
    2. Try all possible turns (increasing or decreasing each digit).
    3. Check if the new combination is the target combination.
    4. If not, try all possible turns from the new combination.
    5. Repeat this process until we find the target combination or we've tried all possible combinations.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

int openLock(std::vector<std::string>& deadends, std::string target) {
    std::unordered_set<std::string> dead(deadends.begin(), deadends.end());
    if (dead.find("0000") != dead.end()) return -1;
    if (target == "0000") return 0;

    std::unordered_set<std::string> visited;
    std::queue<std::pair<std::string, int>> q;
    q.push({"0000", 0});

    while (!q.empty()) {
        std::string current = q.front().first;
        int turns = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            for (int j = -1; j <= 1; j += 2) {
                std::string next = current;
                next[i] = (next[i] - '0' + j + 10) % 10 + '0';
                if (next == target) return turns + 1;
                if (dead.find(next) == dead.end() && visited.find(next) == visited.end()) {
                    q.push({next, turns + 1});
                    visited.insert(next);
                }
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^4 \times 4 \times 2)$, where $10^4$ is the number of possible combinations and $4 \times 2$ is the number of possible turns for each combination.
> - **Space Complexity:** $O(10^4)$, where we store all possible combinations in the `visited` set.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a **Breadth-First Search (BFS)** algorithm to try all possible combinations in a more efficient way.
- Detailed breakdown of the approach:
    1. Start from the initial combination `"0000"`.
    2. Try all possible turns (increasing or decreasing each digit).
    3. Check if the new combination is the target combination.
    4. If not, add the new combination to a queue and mark it as visited.
    5. Repeat this process until we find the target combination or the queue is empty.
- Proof of optimality: The BFS algorithm ensures that we try all possible combinations in the shortest possible order, resulting in the minimum number of turns.

```cpp
int openLock(std::vector<std::string>& deadends, std::string target) {
    std::unordered_set<std::string> dead(deadends.begin(), deadends.end());
    if (dead.find("0000") != dead.end()) return -1;
    if (target == "0000") return 0;

    std::unordered_set<std::string> visited;
    std::queue<std::pair<std::string, int>> q;
    q.push({"0000", 0});
    visited.insert("0000");

    while (!q.empty()) {
        std::string current = q.front().first;
        int turns = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            for (int j = -1; j <= 1; j += 2) {
                std::string next = current;
                next[i] = (next[i] - '0' + j + 10) % 10 + '0';
                if (next == target) return turns + 1;
                if (dead.find(next) == dead.end() && visited.find(next) == visited.end()) {
                    q.push({next, turns + 1});
                    visited.insert(next);
                }
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^4)$, where we try all possible combinations.
> - **Space Complexity:** $O(10^4)$, where we store all possible combinations in the `visited` set.
> - **Optimality proof:** The BFS algorithm ensures that we try all possible combinations in the shortest possible order, resulting in the minimum number of turns.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, queue data structure, and `unordered_set` data structure.
- Problem-solving patterns identified: Using BFS to try all possible combinations in a more efficient way.
- Optimization techniques learned: Using a `visited` set to avoid trying the same combination multiple times.
- Similar problems to practice: Other problems that involve trying all possible combinations, such as the "Letter Combinations of a Phone Number" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a combination is already visited before adding it to the queue.
- Edge cases to watch for: When the target combination is already the initial combination, or when the target combination is in the `deadends` list.
- Performance pitfalls: Trying all possible combinations without using a `visited` set, resulting in high time complexity.
- Testing considerations: Testing the function with different input combinations, including edge cases.