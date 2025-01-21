## Number of Nodes in the Sub-Tree with the Same Label
**Problem Link:** https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description

**Problem Statement:**
- Input format and constraints: The problem is given a tree where each node has a unique id and a label. The task is to find the number of nodes in the sub-tree rooted at each node with the same label.
- Expected output format: Return a list of integers representing the number of nodes in the sub-tree rooted at each node with the same label.
- Key requirements and edge cases to consider: The tree can have up to $n$ nodes, and each node has a unique id and a label.
- Example test cases with explanations: For example, given a tree with nodes labeled as [1, 0, 1, 0, 1, 0, 1], the expected output is [3, 1, 1, 1, 2, 0, 1].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to traverse the tree and for each node, traverse its sub-tree to count the number of nodes with the same label.
- Step-by-step breakdown of the solution:
  1. Create a recursive function to traverse the tree.
  2. For each node, traverse its sub-tree and count the number of nodes with the same label.
  3. Store the count in a list and return it.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is inefficient because it involves multiple traversals of the tree.

```cpp
class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<int> result(n);
        function<void(int, int)> dfs = [&](int node, int parent) {
            int count = 1;
            for (int child : graph[node]) {
                if (child != parent) {
                    count += dfs(child, node);
                }
            }
            result[node] = count;
            return count;
        };
        
        function<void(int, int)> dfs2 = [&](int node, int parent) {
            int count = 0;
            for (int child : graph[node]) {
                if (child != parent) {
                    count += dfs2(child, node);
                }
            }
            if (labels[node] == labels[parent]) {
                result[node] += count;
            }
            return count + 1;
        };
        
        dfs(0, -1);
        dfs2(0, -1);
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we are traversing the tree $n$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing the count of nodes in the sub-tree rooted at each node.
> - **Why these complexities occur:** These complexities occur because we are using a recursive approach to traverse the tree and count the number of nodes in the sub-tree rooted at each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a depth-first search (DFS) approach to traverse the tree and count the number of nodes in the sub-tree rooted at each node with the same label.
- Detailed breakdown of the approach:
  1. Create a recursive function to traverse the tree using DFS.
  2. For each node, traverse its sub-tree and count the number of nodes with the same label.
  3. Use a `map` to store the count of nodes with each label in the sub-tree.
  4. Update the count of nodes in the sub-tree rooted at each node with the same label.
- Proof of optimality: This approach is optimal because it involves a single traversal of the tree, and we are using a `map` to store the count of nodes with each label in the sub-tree.

```cpp
class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<int> result(n);
        function<unordered_map<char, int>(int, int)> dfs = [&](int node, int parent) {
            unordered_map<char, int> count;
            count[labels[node]] = 1;
            for (int child : graph[node]) {
                if (child != parent) {
                    auto childCount = dfs(child, node);
                    for (auto& pair : childCount) {
                        count[pair.first] += pair.second;
                    }
                }
            }
            result[node] = count[labels[node]];
            return count;
        };
        
        dfs(0, -1);
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are traversing the tree once using DFS.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing the count of nodes in the sub-tree rooted at each node.
> - **Optimality proof:** This approach is optimal because it involves a single traversal of the tree, and we are using a `map` to store the count of nodes with each label in the sub-tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), recursive approach, and using a `map` to store the count of nodes with each label in the sub-tree.
- Problem-solving patterns identified: Using a recursive approach to traverse the tree and count the number of nodes in the sub-tree rooted at each node with the same label.
- Optimization techniques learned: Using a `map` to store the count of nodes with each label in the sub-tree to avoid multiple traversals of the tree.
- Similar problems to practice: Problems involving tree traversal and counting the number of nodes in the sub-tree rooted at each node with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly in the recursive approach.
- Edge cases to watch for: Handling the case where the tree is empty or has only one node.
- Performance pitfalls: Using an inefficient approach that involves multiple traversals of the tree.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness and efficiency.