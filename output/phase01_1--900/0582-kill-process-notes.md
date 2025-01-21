## Kill Process
**Problem Link:** https://leetcode.com/problems/kill-process/description

**Problem Statement:**
- Input format and constraints: The problem takes in a list of `pid` (process IDs), a list of `ppid` (parent process IDs), a list of `time` (timestamp of each process), and a `kill` process ID. 
- Expected output format: Return a list of process IDs that will be killed.
- Key requirements and edge cases to consider: A process will be killed if it is the process to be killed or if it is a child of a process that will be killed.
- Example test cases with explanations:
  - Example 1: `pid = [1,3,10,5]`, `ppid = [3,0,5,3]`, `time = [0,0,0,0]`, `kill = 5`, the output should be `[5,10]`.
  - Example 2: `pid = [1,2,3]`, `ppid = [0,0,0]`, `time = [0,0,0]`, `kill = 1`, the output should be `[1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by identifying the process to be killed and then recursively find all its children.
- Step-by-step breakdown of the solution:
  1. Create a map to store the parent-child relationships.
  2. Iterate through the `pid` and `ppid` lists to populate the map.
  3. Start a depth-first search (DFS) from the process to be killed.
  4. During the DFS, add each visited process to the result list.
- Why this approach comes to mind first: The problem requires finding all processes that will be killed, which naturally leads to a recursive or DFS approach.

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, vector<int>& time, int kill) {
        unordered_map<int, vector<int>> graph;
        for (int i = 0; i < pid.size(); i++) {
            if (ppid[i] != 0) {
                graph[ppid[i]].push_back(pid[i]);
            }
        }
        
        vector<int> result;
        dfs(graph, kill, result);
        return result;
    }
    
    void dfs(unordered_map<int, vector<int>>& graph, int node, vector<int>& result) {
        result.push_back(node);
        if (graph.find(node) != graph.end()) {
            for (int child : graph[node]) {
                dfs(graph, child, result);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of processes and $m$ is the number of edges in the graph. This is because we visit each process and edge once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of processes and $m$ is the number of edges in the graph. This is because we store the graph and the result list.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS traversal of the graph, and the space complexity occurs because we store the graph and the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a topological sorting approach, but since we only need to find the processes that will be killed, a simple DFS from the process to be killed is sufficient.
- Detailed breakdown of the approach:
  1. Create a map to store the parent-child relationships.
  2. Iterate through the `pid` and `ppid` lists to populate the map.
  3. Start a DFS from the process to be killed.
  4. During the DFS, add each visited process to the result list.
- Proof of optimality: The DFS approach is optimal because it visits each process and edge only once, resulting in a linear time complexity.

```cpp
#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, vector<int>& time, int kill) {
        unordered_map<int, vector<int>> graph;
        for (int i = 0; i < pid.size(); i++) {
            if (ppid[i] != 0) {
                graph[ppid[i]].push_back(pid[i]);
            }
        }
        
        vector<int> result;
        dfs(graph, kill, result);
        return result;
    }
    
    void dfs(unordered_map<int, vector<int>>& graph, int node, vector<int>& result) {
        result.push_back(node);
        if (graph.find(node) != graph.end()) {
            for (int child : graph[node]) {
                dfs(graph, child, result);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of processes and $m$ is the number of edges in the graph. This is because we visit each process and edge once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of processes and $m$ is the number of edges in the graph. This is because we store the graph and the result list.
> - **Optimality proof:** The DFS approach is optimal because it visits each process and edge only once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, and recursive algorithms.
- Problem-solving patterns identified: Identifying the process to be killed and recursively finding its children.
- Optimization techniques learned: Using a DFS approach to reduce the time complexity.
- Similar problems to practice: Problems involving graph traversal, DFS, and recursive algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input list.
- Edge cases to watch for: Processes with no children, processes with multiple parents.
- Performance pitfalls: Using an inefficient algorithm, such as a brute force approach.
- Testing considerations: Testing with different input sizes, testing with different graph structures.