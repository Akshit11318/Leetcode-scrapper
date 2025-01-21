## Time Taken to Mark All Nodes

**Problem Link:** https://leetcode.com/problems/time-taken-to-mark-all-nodes/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `edges` where each integer represents the index of the node's parent in a tree. The length of the array is the number of nodes in the tree.
- Expected output format: The output should be an integer representing the minimum time taken to mark all nodes in the tree.
- Key requirements and edge cases to consider: The tree can have any number of nodes, and the parent of each node can be any other node in the tree. If a node has no parent, its value in the `edges` array will be -1.
- Example test cases with explanations:
  - For the input `edges = [1, 1, -1]`, the output should be 1 because we can mark all nodes in one step by starting from the root node (index 2).
  - For the input `edges = [1, -1, -1]`, the output should be 2 because we need to mark the root node (index 1) first, and then mark the node at index 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the minimum time taken to mark all nodes, we can start from each node and simulate the marking process.
- Step-by-step breakdown of the solution:
  1. Create a tree from the given `edges` array.
  2. For each node in the tree, start a depth-first search (DFS) and mark all nodes in the subtree rooted at the current node.
  3. Keep track of the time taken to mark all nodes in each subtree.
  4. Return the minimum time taken across all subtrees.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient because it involves repeated work and has a high time complexity.

```cpp
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    vector<TreeNode*> children;
};

int minTime(vector<int>& edges) {
    int n = edges.size();
    vector<TreeNode*> nodes(n);
    for (int i = 0; i < n; i++) {
        nodes[i] = new TreeNode();
    }
    for (int i = 0; i < n; i++) {
        if (edges[i] != -1) {
            nodes[edges[i]]->children.push_back(nodes[i]);
        }
    }
    int minTime = INT_MAX;
    for (int i = 0; i < n; i++) {
        int time = dfs(nodes[i]);
        minTime = min(minTime, time);
    }
    return minTime;
}

int dfs(TreeNode* node) {
    int time = 0;
    for (TreeNode* child : node->children) {
        time = max(time, dfs(child));
    }
    return time + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of nodes in the tree. This is because in the worst case, we are performing a DFS from each node, and each DFS takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ for storing the tree nodes.
> - **Why these complexities occur:** The high time complexity occurs because of the repeated work involved in performing a DFS from each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing a DFS from each node, we can perform a single DFS from the root node and keep track of the height of each subtree.
- Detailed breakdown of the approach:
  1. Create a tree from the given `edges` array.
  2. Perform a DFS from the root node and calculate the height of each subtree.
  3. Return the maximum height across all subtrees.
- Proof of optimality: This approach is optimal because it involves a single DFS and avoids repeated work.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the minimum required to visit each node in the tree.

```cpp
int minTime(vector<int>& edges) {
    int n = edges.size();
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; i++) {
        if (edges[i] != -1) {
            graph[edges[i]].push_back(i);
        }
    }
    int maxDepth = 0;
    function<void(int, int)> dfs = [&](int node, int depth) {
        maxDepth = max(maxDepth, depth);
        for (int child : graph[node]) {
            dfs(child, depth + 1);
        }
    };
    for (int i = 0; i < n; i++) {
        if (edges[i] == -1) {
            dfs(i, 0);
        }
    }
    return maxDepth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree. This is because we are performing a single DFS and visiting each node once.
> - **Space Complexity:** $O(n)$ for storing the tree nodes and the recursion stack.
> - **Optimality proof:** This approach is optimal because it involves a single DFS and avoids repeated work, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal (DFS), dynamic programming.
- Problem-solving patterns identified: Avoiding repeated work, using a single DFS to calculate the height of each subtree.
- Optimization techniques learned: Using a single DFS to avoid repeated work, keeping track of the height of each subtree.
- Similar problems to practice: Other tree traversal problems, such as finding the diameter of a tree or the maximum path sum.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: Trees with a large number of nodes, trees with a large height.
- Performance pitfalls: Using a brute force approach that involves repeated work, not optimizing the DFS to avoid repeated work.
- Testing considerations: Testing the solution with different types of trees, such as balanced trees, unbalanced trees, and trees with a large number of nodes.