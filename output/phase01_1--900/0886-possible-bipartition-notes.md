## Possible Bipartition
**Problem Link:** https://leetcode.com/problems/possible-bipartition/description

**Problem Statement:**
- Given a list of integers `N` representing the number of people, and a 2D list `dislikes` where `dislikes[i] = [a, b]` indicates that the `a-th` person and the `b-th` person do not like each other.
- The task is to determine if it's possible to partition the people into two groups such that each person in one group does not dislike any person in the other group.
- Input constraints: `1 <= N <= 2000`, `1 <= dislikes.length <= N * (N - 1) / 2`, `dislikes[i].length == 2`, `1 <= dislikes[i][0] <= N`, `1 <= dislikes[i][1] <= N`, `dislikes[i][0] != dislikes[i][1]`.
- Expected output: A boolean value indicating whether a bipartition is possible.
- Key requirements: The solution should handle all possible input cases, including empty `dislikes` lists and cases where a person dislikes multiple others.
- Example test cases:
  - `N = 4`, `dislikes = [[1,2],[1,3],[2,4]]`, Output: `True`
  - `N = 3`, `dislikes = [[1,2],[1,3],[2,3]]`, Output: `False`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of people and checking if each combination satisfies the condition.
- This approach is straightforward but inefficient due to the large number of possible combinations.
- We can use bit manipulation to generate all possible subsets of people.

```cpp
#include <vector>

bool possibleBipartition(int N, std::vector<std::vector<int>>& dislikes) {
    // Generate all possible subsets of people
    for (int mask = 0; mask < (1 << N); mask++) {
        bool valid = true;
        for (const auto& dislike : dislikes) {
            int a = dislike[0] - 1, b = dislike[1] - 1;
            // Check if a and b are in the same subset
            if (((mask >> a) & 1) == ((mask >> b) & 1)) {
                valid = false;
                break;
            }
        }
        if (valid) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^N \cdot M)$, where $N$ is the number of people and $M$ is the number of dislikes. This is because we generate all possible subsets of people and check each subset against all dislikes.
> - **Space Complexity:** $O(1)$, excluding the input, since we only use a constant amount of space to store the current subset and the result.
> - **Why these complexities occur:** The time complexity is exponential due to generating all possible subsets, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a graph coloring approach, where each person is a node, and two nodes are connected if the corresponding people dislike each other.
- We can use a depth-first search (DFS) to assign colors to each node. If we encounter a node that is already colored with the same color as its neighbor, we return false.
- This approach is optimal because it only requires a single pass through the graph.

```cpp
#include <vector>
#include <unordered_map>

bool possibleBipartition(int N, std::vector<std::vector<int>>& dislikes) {
    std::unordered_map<int, std::vector<int>> graph;
    for (const auto& dislike : dislikes) {
        graph[dislike[0]].push_back(dislike[1]);
        graph[dislike[1]].push_back(dislike[0]);
    }

    std::vector<int> colors(N + 1, 0); // 0: uncolored, 1: color 1, -1: color 2
    for (int i = 1; i <= N; i++) {
        if (colors[i] == 0 && !dfs(graph, colors, i, 1)) return false;
    }
    return true;
}

bool dfs(const std::unordered_map<int, std::vector<int>>& graph, std::vector<int>& colors, int node, int color) {
    if (colors[node] != 0) return colors[node] == color;
    colors[node] = color;
    for (const auto& neighbor : graph.at(node)) {
        if (!dfs(graph, colors, neighbor, -color)) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of people and $M$ is the number of dislikes. This is because we perform a single DFS traversal of the graph.
> - **Space Complexity:** $O(N + M)$, since we need to store the graph and the colors of each node.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the graph, and it uses a minimal amount of extra space to store the colors of each node.

---

### Final Notes

**Learning Points:**
- Graph coloring is a useful technique for solving problems that involve partitioning a set of objects into two groups based on certain constraints.
- DFS is a powerful algorithm for traversing graphs and detecting cycles.
- The optimal approach is often more efficient and scalable than the brute force approach.

**Mistakes to Avoid:**
- Not considering the graph structure of the problem, which can lead to inefficient solutions.
- Not using DFS to traverse the graph, which can lead to incorrect results.
- Not handling edge cases, such as empty input or invalid input.