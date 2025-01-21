## K-Similar Strings

**Problem Link:** https://leetcode.com/problems/k-similar-strings/description

**Problem Statement:**
- Input format: Two strings `A` and `B` of the same length, and an integer `K`.
- Constraints: `1 <= A.length == B.length <= 12`, `A` and `B` contain only lowercase letters, `0 <= K <= 12`.
- Expected output format: The minimum number of steps required to make string `A` the same as string `B` by swapping two adjacent characters in `A`, or `-1` if it is impossible to make `A` the same as `B` within `K` steps.
- Key requirements and edge cases to consider: Handling cases where `A` and `B` are already the same, or when `K` is 0, or when the length of `A` and `B` is 1.
- Example test cases with explanations:
  - `A = "ab", B = "ba", K = 2` should return `2`.
  - `A = "abc", B = "bca", K = 2` should return `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to try all possible swaps and see if we can transform `A` into `B` within `K` steps.
- Step-by-step breakdown of the solution:
  1. Generate all possible next states by swapping two adjacent characters in `A`.
  2. Use a queue to store the current state and the number of steps taken so far.
  3. Use a set to store the visited states to avoid duplicates.
- Why this approach comes to mind first: It is the most intuitive way to solve the problem, but it has a high time complexity due to the large number of possible states.

```cpp
#include <queue>
#include <set>
#include <string>

class Solution {
public:
    int kSimilarity(std::string A, std::string B) {
        if (A == B) return 0;
        std::queue<std::pair<std::string, int>> q;
        std::set<std::string> visited;
        q.push({A, 0});
        visited.insert(A);
        while (!q.empty()) {
            auto [curr, steps] = q.front();
            q.pop();
            for (int i = 0; i < curr.size(); i++) {
                if (curr[i] != B[i]) {
                    for (int j = i + 1; j < curr.size(); j++) {
                        if (curr[j] == B[i]) {
                            std::string next = curr;
                            std::swap(next[i], next[j]);
                            if (next == B) return steps + 1;
                            if (visited.find(next) == visited.end()) {
                                q.push({next, steps + 1});
                                visited.insert(next);
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N!)$ where $N$ is the length of the string, because in the worst case, we need to try all possible permutations of the string.
> - **Space Complexity:** $O(N!)$ because we need to store all possible states in the queue and the set.
> - **Why these complexities occur:** The brute force approach tries all possible swaps, which results in a large number of possible states.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bidirectional BFS to reduce the search space.
- Detailed breakdown of the approach:
  1. Use two queues to store the states from both sides (i.e., from `A` to `B` and from `B` to `A`).
  2. Use two sets to store the visited states from both sides.
  3. In each iteration, try all possible swaps for the current state and add the next state to the queue if it has not been visited before.
- Proof of optimality: The bidirectional BFS approach reduces the search space by half, making it more efficient than the brute force approach.

```cpp
#include <queue>
#include <set>
#include <string>

class Solution {
public:
    int kSimilarity(std::string A, std::string B) {
        if (A == B) return 0;
        std::queue<std::pair<std::string, int>> q1, q2;
        std::set<std::string> visited1, visited2;
        q1.push({A, 0});
        q2.push({B, 0});
        visited1.insert(A);
        visited2.insert(B);
        while (!q1.empty() || !q2.empty()) {
            if (!q1.empty()) {
                auto [curr, steps] = q1.front();
                q1.pop();
                for (int i = 0; i < curr.size(); i++) {
                    if (curr[i] != B[i]) {
                        for (int j = i + 1; j < curr.size(); j++) {
                            if (curr[j] == B[i]) {
                                std::string next = curr;
                                std::swap(next[i], next[j]);
                                if (visited2.find(next) != visited2.end()) return steps + 1;
                                if (visited1.find(next) == visited1.end()) {
                                    q1.push({next, steps + 1});
                                    visited1.insert(next);
                                }
                            }
                        }
                    }
                }
            }
            if (!q2.empty()) {
                auto [curr, steps] = q2.front();
                q2.pop();
                for (int i = 0; i < curr.size(); i++) {
                    if (curr[i] != A[i]) {
                        for (int j = i + 1; j < curr.size(); j++) {
                            if (curr[j] == A[i]) {
                                std::string next = curr;
                                std::swap(next[i], next[j]);
                                if (visited1.find(next) != visited1.end()) return steps + 1;
                                if (visited2.find(next) == visited2.end()) {
                                    q2.push({next, steps + 1});
                                    visited2.insert(next);
                                }
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{N/2})$ where $N$ is the length of the string, because we use a bidirectional BFS to reduce the search space.
> - **Space Complexity:** $O(2^{N/2})$ because we need to store the visited states from both sides.
> - **Optimality proof:** The bidirectional BFS approach reduces the search space by half, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bidirectional BFS, string manipulation.
- Problem-solving patterns identified: Reducing the search space by using a bidirectional approach.
- Optimization techniques learned: Using a bidirectional BFS to reduce the search space.
- Similar problems to practice: Other string manipulation problems, such as finding the minimum number of operations to transform one string into another.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited states, not handling edge cases correctly.
- Edge cases to watch for: Handling cases where `A` and `B` are already the same, or when `K` is 0, or when the length of `A` and `B` is 1.
- Performance pitfalls: Using a brute force approach, not optimizing the search space.
- Testing considerations: Testing the code with different inputs, including edge cases and large inputs.