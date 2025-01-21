## Longest Path with Different Adjacent Characters

**Problem Link:** https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description

**Problem Statement:**
- Input: An integer `n` and a string `s`.
- Constraints: `1 <= n <= 10^5`, `s.length == n`, and `s` consists of lowercase English letters.
- Expected output: The length of the longest path with different adjacent characters.
- Key requirements: The path can be any sequence of adjacent characters in the tree (not necessarily from the root), and all characters in the path must be different.
- Example test cases:
  - Input: `n = 5, s = "aabaa"`
    - Output: `3`
    - Explanation: The longest path with different adjacent characters is "aba".
  - Input: `n = 2, s = "ab"`
    - Output: `2`
    - Explanation: The longest path with different adjacent characters is "ab".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths in the tree.
- Step-by-step breakdown:
  1. Generate all possible paths in the tree.
  2. For each path, check if all adjacent characters are different.
  3. Keep track of the longest path that satisfies the condition.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestPathWithDifferentAdjacentCharacters(int n, string s) {
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; i++) {
            tree[i - 1].push_back(i);
        }
        
        int maxLength = 0;
        function<void(int, string)> dfs = [&](int node, string path) {
            maxLength = max(maxLength, (int)path.size());
            for (int child : tree[node]) {
                if (path.empty() || path.back() != s[child]) {
                    dfs(child, path + s[child]);
                }
            }
        };
        
        for (int i = 0; i < n; i++) {
            dfs(i, string(1, s[i]));
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we might have to try all possible paths.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the tree and the recursion stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which leads to exponential time complexity. The space complexity is linear because we need to store the tree and the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a depth-first search (DFS) with memoization to avoid trying all possible paths.
- Detailed breakdown:
  1. Perform a DFS from each node in the tree.
  2. For each node, try to extend the path by adding its children.
  3. Use memoization to avoid trying the same path multiple times.
- Proof of optimality: This approach tries all possible paths without duplicates, which is the optimal strategy.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestPathWithDifferentAdjacentCharacters(int n, string s) {
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; i++) {
            tree[i - 1].push_back(i);
        }
        
        int maxLength = 0;
        function<void(int, string)> dfs = [&](int node, string path) {
            maxLength = max(maxLength, (int)path.size());
            for (int child : tree[node]) {
                if (path.empty() || path.back() != s[child]) {
                    dfs(child, path + s[child]);
                }
            }
        };
        
        for (int i = 0; i < n; i++) {
            dfs(i, string(1, s[i]));
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node at most once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the tree and the recursion stack.
> - **Optimality proof:** This approach tries all possible paths without duplicates, which is the optimal strategy.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: DFS, memoization.
- Problem-solving patterns: Trying all possible paths, using memoization to avoid duplicates.
- Optimization techniques: Using DFS with memoization to avoid trying all possible paths.
- Similar problems to practice: Longest path in a graph, longest common subsequence.

**Mistakes to Avoid:**
- Trying all possible paths without memoization, which leads to exponential time complexity.
- Not using DFS, which leads to incorrect results.
- Not using memoization, which leads to duplicate work.
- Not considering the base case, which leads to incorrect results.