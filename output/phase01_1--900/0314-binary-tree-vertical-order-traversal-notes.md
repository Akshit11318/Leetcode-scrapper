## Binary Tree Vertical Order Traversal

**Problem Link:** https://leetcode.com/problems/binary-tree-vertical-order-traversal/description

**Problem Statement:**
- Given the `root` of a binary tree, return the vertical order traversal of its nodes' values.
- Input format: The input is a binary tree represented by its root node.
- Expected output format: A list of lists, where each inner list contains the node values at a specific vertical level.
- Key requirements and edge cases to consider:
  - The binary tree may be empty.
  - The binary tree may have a single node.
  - The binary tree may have multiple nodes with the same horizontal distance from the root.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [3,9,20,null,null,15,7]`
    - Output: `[[9],[3,15],[20],[7]]`
    - Explanation: The nodes at vertical level -1 are [9], at level 0 are [3,15], and at level 1 are [20,7].

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the binary tree and calculate the horizontal distance of each node from the root.
- We can use a `map` to store the nodes at each vertical level.
- We will perform a level-order traversal of the binary tree and update the horizontal distance of each node based on its parent node.

```cpp
// Brute Force Approach
#include <queue>
#include <map>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

vector<vector<int>> verticalOrder(TreeNode* root) {
    if (!root) return {};
    
    map<int, vector<int>> columnTable;
    int min_column = 0, max_column = 0;
    queue<pair<TreeNode*, int>> q;
    q.push({root, 0});
    
    while (!q.empty()) {
        auto node = q.front().first;
        int column = q.front().second;
        q.pop();
        
        if (node) {
            columnTable[column].push_back(node->val);
            min_column = min(min_column, column);
            max_column = max(max_column, column);
            
            q.push({node->left, column - 1});
            q.push({node->right, column + 1});
        }
    }
    
    vector<vector<int>> result;
    for (int i = min_column; i <= max_column; i++) {
        result.push_back(columnTable[i]);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the number of nodes in the binary tree. This is because we are performing a level-order traversal and updating the horizontal distance of each node.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. This is because we are using a `map` to store the nodes at each vertical level and a `queue` to perform the level-order traversal.
> - **Why these complexities occur:** The time complexity occurs because we are performing a level-order traversal and updating the horizontal distance of each node. The space complexity occurs because we are using a `map` and a `queue` to store the nodes.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `map` to store the nodes at each vertical level and a `queue` to perform the level-order traversal.
- We can calculate the horizontal distance of each node based on its parent node and update the `map` accordingly.
- We can then iterate over the `map` and construct the result.

```cpp
// Optimal Approach
vector<vector<int>> verticalOrder(TreeNode* root) {
    if (!root) return {};
    
    map<int, vector<int>> columnTable;
    int min_column = 0, max_column = 0;
    queue<pair<TreeNode*, int>> q;
    q.push({root, 0});
    
    while (!q.empty()) {
        auto node = q.front().first;
        int column = q.front().second;
        q.pop();
        
        if (node) {
            columnTable[column].push_back(node->val);
            min_column = min(min_column, column);
            max_column = max(max_column, column);
            
            q.push({node->left, column - 1});
            q.push({node->right, column + 1});
        }
    }
    
    vector<vector<int>> result;
    for (int i = min_column; i <= max_column; i++) {
        result.push_back(columnTable[i]);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the number of nodes in the binary tree. This is because we are performing a level-order traversal and updating the horizontal distance of each node.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the binary tree. This is because we are using a `map` to store the nodes at each vertical level and a `queue` to perform the level-order traversal.
> - **Optimality proof:** This is the optimal solution because we are using a `map` to store the nodes at each vertical level and a `queue` to perform the level-order traversal. This allows us to calculate the horizontal distance of each node in $O(1)$ time and update the `map` in $O(\log N)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: level-order traversal, using a `map` to store nodes at each vertical level.
- Problem-solving patterns identified: calculating the horizontal distance of each node based on its parent node.
- Optimization techniques learned: using a `map` to store nodes at each vertical level and a `queue` to perform the level-order traversal.
- Similar problems to practice: binary tree traversal, graph traversal.

**Mistakes to Avoid:**
- Not updating the horizontal distance of each node correctly.
- Not using a `map` to store nodes at each vertical level.
- Not performing the level-order traversal correctly.
- Not handling edge cases such as an empty binary tree or a binary tree with a single node.