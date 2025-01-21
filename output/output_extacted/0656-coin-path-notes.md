## Coin Path
**Problem Link:** https://leetcode.com/problems/coin-path/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` representing the coins, where `s[i]` can be either `'H'` or `'T'`, representing heads or tails. The length of `s` is between 1 and 1000.
- Expected output format: The output is a string representing the shortest path to get all heads. If it is impossible, return an empty string.
- Key requirements and edge cases to consider: The path can only consist of `H` and `T`, and we need to find the shortest path.
- Example test cases with explanations: For example, if `s = "HT"`, the output should be `"HT"` because we can get all heads by following the path `"HT"`. If `s = "TH"`, the output should be `"TH"` because we can get all heads by following the path `"TH"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible paths and see which one leads to all heads.
- Step-by-step breakdown of the solution: Generate all possible paths, and for each path, check if it leads to all heads. If it does, update the result if the path is shorter than the current shortest path.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

string coinPath(string s) {
    int n = s.size();
    string shortestPath = "";
    for (int mask = 0; mask < (1 << n); mask++) {
        string path = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                path += 'H';
            } else {
                path += 'T';
            }
        }
        bool allHeads = true;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'H' && path[i] != 'H') {
                allHeads = false;
                break;
            }
        }
        if (allHeads && (shortestPath.empty() || path.size() < shortestPath.size())) {
            shortestPath = path;
        }
    }
    return shortestPath;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we generate all possible paths, which is $2^n$, and for each path, we check if it leads to all heads, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we need to store the current path, which can be at most $n$ characters long.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible paths, and the space complexity occurs because we need to store the current path.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to find the shortest path.
- Detailed breakdown of the approach: We start with an empty path and try to add either `H` or `T` to the path. We use a queue to store the current paths and a set to store the visited paths. We keep trying to add `H` or `T` to the current paths until we find a path that leads to all heads or until we have tried all possible paths.
- Proof of optimality: This approach is optimal because it tries all possible paths in the shortest order, i.e., it tries all paths of length 1 before trying any paths of length 2, and so on.
- Why further optimization is impossible: This approach is already optimal because it tries all possible paths in the shortest order.

```cpp
#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>

string coinPath(string s) {
    int n = s.size();
    std::queue<std::pair<string, int>> q;
    std::unordered_set<string> visited;
    q.push({"", 0});
    while (!q.empty()) {
        string path = q.front().first;
        int idx = q.front().second;
        q.pop();
        if (idx == n) {
            bool allHeads = true;
            for (int i = 0; i < n; i++) {
                if (s[i] == 'H' && path[i] != 'H') {
                    allHeads = false;
                    break;
                }
            }
            if (allHeads) {
                return path;
            }
        } else {
            string newPath = path + 'H';
            if (visited.find(newPath) == visited.end()) {
                q.push({newPath, idx + 1});
                visited.insert(newPath);
            }
            newPath = path + 'T';
            if (visited.find(newPath) == visited.end()) {
                q.push({newPath, idx + 1});
                visited.insert(newPath);
            }
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `s`. This is because we try all possible paths.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the string `s`. This is because we need to store all possible paths.
> - **Optimality proof:** This approach is optimal because it tries all possible paths in the shortest order.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue, and set.
- Problem-solving patterns identified: Trying all possible solutions and optimizing the order in which we try them.
- Optimization techniques learned: Using a queue to store the current paths and a set to store the visited paths.
- Similar problems to practice: Other problems that involve trying all possible solutions and optimizing the order in which we try them.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a path has been visited before trying to add `H` or `T` to it.
- Edge cases to watch for: The case where the input string is empty.
- Performance pitfalls: Trying all possible paths in the wrong order, which can lead to exponential time complexity.
- Testing considerations: Testing the function with different input strings to ensure it works correctly.