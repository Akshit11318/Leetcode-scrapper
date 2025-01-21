## Binary Tree Cameras
**Problem Link:** https://leetcode.com/problems/binary-tree-cameras/description

**Problem Statement:**
- Input format and constraints: Given a binary tree, we need to determine the minimum number of cameras required to monitor the entire tree. Each node can have a camera, and a camera can monitor its parent, itself, and its children.
- Expected output format: The minimum number of cameras required.
- Key requirements and edge cases to consider: The tree may be empty, or it may have a single node. We also need to consider the case where a node has only one child.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [0,0,null,0,0]`
    - Output: `2`
    - Explanation: We can place cameras at the nodes with values 0 and 0.
  - Example 2: 
    - Input: `root = [0,0,0,null,0,null,0]`
    - Output: `2`
    - Explanation: We can place cameras at the nodes with values 0 and 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of placing cameras in the tree and counting the minimum number of cameras required.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of placing cameras in the tree.
  2. For each combination, count the number of cameras.
  3. Check if the current combination can monitor the entire tree.
  4. Update the minimum number of cameras if the current combination is valid and has fewer cameras.
- Why this approach comes to mind first: This approach is straightforward and guarantees the correct solution, but it is inefficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int minCameraCover(TreeNode* root) {
        int minCameras = INT_MAX;
        vector<bool> cameras;
        vector<bool> monitored;
        
        function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int index) {
            if (!node) return;
            cameras.push_back(false);
            monitored.push_back(false);
            dfs(node->left, 2 * index + 1);
            dfs(node->right, 2 * index + 2);
        };
        
        dfs(root, 0);
        
        function<void(int)> backtrack = [&](int index) {
            if (index >= cameras.size()) {
                int count = 0;
                for (bool camera : cameras) {
                    if (camera) count++;
                }
                if (isMonitored(cameras, monitored)) {
                    minCameras = min(minCameras, count);
                }
                return;
            }
            cameras[index] = false;
            monitored[index] = false;
            backtrack(index + 1);
            cameras[index] = true;
            monitored[index] = true;
            if (index > 0) {
                monitored[(index - 1) / 2] = true;
            }
            if (2 * index + 1 < cameras.size()) {
                monitored[2 * index + 1] = true;
            }
            if (2 * index + 2 < cameras.size()) {
                monitored[2 * index + 2] = true;
            }
            backtrack(index + 1);
        };
        
        backtrack(0);
        
        return minCameras;
    }
    
    bool isMonitored(vector<bool>& cameras, vector<bool>& monitored) {
        for (bool monitor : monitored) {
            if (!monitor) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of nodes in the tree. This is because we are generating all possible combinations of placing cameras.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we need to store the cameras and monitored status for each node.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because we are trying all possible combinations of placing cameras. The space complexity is linear because we need to store the cameras and monitored status for each node.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) approach to solve this problem. The idea is to assign a status to each node: 0 if it has a camera, 1 if it is monitored by its parent, and 2 if it is monitored by its children.
- Detailed breakdown of the approach:
  1. Perform a DFS traversal of the tree.
  2. For each node, calculate its status based on the status of its children.
  3. If a node has a status of 0, it means it has a camera. Increment the count of cameras.
- Proof of optimality: This approach is optimal because it ensures that each node is monitored by either its parent or its children, and it uses the minimum number of cameras required.

```cpp
class Solution {
public:
    int minCameraCover(TreeNode* root) {
        int cameras = 0;
        function<int(TreeNode*)> dfs = [&](TreeNode* node) {
            if (!node) return 1;
            int left = dfs(node->left);
            int right = dfs(node->right);
            if (left == -1 || right == -1) {
                cameras++;
                return 0;
            }
            if (left == 0 || right == 0) {
                return 1;
            }
            return -1;
        };
        if (dfs(root) == -1) cameras++;
        return cameras;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we are performing a DFS traversal of the tree.
> - **Space Complexity:** $O(h)$, where h is the height of the tree. This is because we need to store the recursive call stack.
> - **Optimality proof:** This approach is optimal because it ensures that each node is monitored by either its parent or its children, and it uses the minimum number of cameras required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, dynamic programming.
- Problem-solving patterns identified: using a status system to solve the problem.
- Optimization techniques learned: using a DFS approach to reduce the time complexity.
- Similar problems to practice: other problems that involve monitoring or covering a tree or graph.

**Mistakes to Avoid:**
- Common implementation errors: not handling the base case correctly, not updating the count of cameras correctly.
- Edge cases to watch for: the tree may be empty, or it may have a single node.
- Performance pitfalls: using a brute force approach, not using a DFS approach.
- Testing considerations: test the solution with different types of trees, including empty trees and trees with a single node.