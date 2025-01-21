## Loud and Rich

**Problem Link:** https://leetcode.com/problems/loud-and-rich/description

**Problem Statement:**
- Input format and constraints: Given two integer arrays `richer` and `quiet`, where `richer[i] = [a, b]` and `quiet[i] = [q1, q2, ..., qn]`, find an array `answer` where `answer[x]` is the least quiet person `y` (that may be equal to `x`) such that there is a path from `x` to `y`.
- Expected output format: Return an array of integers, where each integer represents the least quiet person reachable from the corresponding person.
- Key requirements and edge cases to consider: There are `n` people, numbered from `1` to `n`, and there are `m` relations `richer[i] = [a, b]`, which means person `a` is richer than person `b`. The `quiet` array represents the quietness levels of each person.
- Example test cases with explanations:
  - `richer = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 3], [6, 3]]`, `quiet = [3, 2, 5, 4, 6, 1, 7, 0]`, the output should be `[5, 5, 2, 5, 4, 5, 6, 7]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create an adjacency list representation of the graph and then perform a depth-first search (DFS) from each person to find the least quiet person reachable.
- Step-by-step breakdown of the solution:
  1. Build the adjacency list representation of the graph.
  2. Perform DFS from each person to find the least quiet person reachable.
- Why this approach comes to mind first: This is a straightforward approach to solve the problem by exploring all possible paths from each person.

```cpp
vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
    int n = quiet.size();
    vector<vector<int>> graph(n);
    for (auto& r : richer) {
        graph[r[1]].push_back(r[0]);
    }
    vector<int> answer(n);
    for (int i = 0; i < n; i++) {
        answer[i] = i;
        dfs(graph, quiet, answer, i);
    }
    return answer;
}

void dfs(vector<vector<int>>& graph, vector<int>& quiet, vector<int>& answer, int person) {
    for (int neighbor : graph[person]) {
        if (quiet[answer[neighbor]] < quiet[answer[person]]) {
            answer[person] = answer[neighbor];
        }
        dfs(graph, quiet, answer, neighbor);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the number of relations. This is because we are performing DFS from each person, and in the worst case, we might visit all relations.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of relations. This is because we are storing the adjacency list representation of the graph.
> - **Why these complexities occur:** The time complexity occurs because we are performing DFS from each person, and the space complexity occurs because we are storing the adjacency list representation of the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a topological sorting approach to solve the problem more efficiently. The idea is to first build the graph and then perform a topological sorting. During the topological sorting, we update the answer for each person based on the quietness levels of their neighbors.
- Detailed breakdown of the approach:
  1. Build the adjacency list representation of the graph.
  2. Perform a topological sorting on the graph.
  3. During the topological sorting, update the answer for each person based on the quietness levels of their neighbors.
- Proof of optimality: This approach is optimal because we are only visiting each relation once during the topological sorting, and we are updating the answer for each person based on the quietness levels of their neighbors.

```cpp
vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet) {
    int n = quiet.size();
    vector<vector<int>> graph(n);
    vector<int> indegree(n, 0);
    for (auto& r : richer) {
        graph[r[1]].push_back(r[0]);
        indegree[r[0]]++;
    }
    vector<int> answer(n);
    queue<int> q;
    for (int i = 0; i < n; i++) {
        answer[i] = i;
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int person = q.front();
        q.pop();
        for (int neighbor : graph[person]) {
            if (quiet[answer[person]] < quiet[answer[neighbor]]) {
                answer[neighbor] = answer[person];
            }
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of relations. This is because we are only visiting each relation once during the topological sorting.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of relations. This is because we are storing the adjacency list representation of the graph.
> - **Optimality proof:** This approach is optimal because we are only visiting each relation once during the topological sorting, and we are updating the answer for each person based on the quietness levels of their neighbors.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sorting, graph traversal, and dynamic programming.
- Problem-solving patterns identified: Using a topological sorting approach to solve problems that involve graph traversal and dynamic programming.
- Optimization techniques learned: Using a topological sorting approach to reduce the time complexity of the solution.
- Similar problems to practice: Problems that involve graph traversal, dynamic programming, and topological sorting.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the answer for each person based on the quietness levels of their neighbors during the topological sorting.
- Edge cases to watch for: Handling cases where there are multiple people with the same quietness level.
- Performance pitfalls: Not using a topological sorting approach to reduce the time complexity of the solution.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure that it is correct and efficient.