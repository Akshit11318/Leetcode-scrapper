## Find the Minimum and Maximum Number of Nodes Between Critical Points

**Problem Link:** https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description

**Problem Statement:**
- Given a binary tree where each node has a unique integer value, find the minimum and maximum number of nodes between critical points. A critical point is a node with a value that is either the minimum or maximum in its subtree.
- Input: `root` of the binary tree
- Expected output: An array `[min, max]` where `min` is the minimum number of nodes between critical points and `max` is the maximum number of nodes between critical points.
- Key requirements:
  - Each node has a unique integer value.
  - A critical point is a node that is either the minimum or maximum in its subtree.
- Edge cases:
  - An empty tree.
  - A tree with a single node.
  - A tree with multiple critical points.

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree for each node to find its minimum and maximum subtrees, then checking if it's a critical point. If it is, we calculate the distance to the next critical point.
- Step-by-step breakdown:
  1. Traverse the tree to find all critical points.
  2. For each critical point, traverse the tree again to find the next critical point and calculate the distance.
- Why this approach comes to mind first: It's straightforward but inefficient because it involves multiple traversals of the tree.

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void findCriticalPoints(TreeNode* root, vector<TreeNode*>& criticalPoints) {
    if (!root) return;
    if (isCriticalPoint(root)) criticalPoints.push_back(root);
    findCriticalPoints(root->left, criticalPoints);
    findCriticalPoints(root->right, criticalPoints);
}

bool isCriticalPoint(TreeNode* node) {
    if (!node) return false;
    int min = node->val, max = node->val;
    findMinMax(node, min, max);
    return node->val == min || node->val == max;
}

void findMinMax(TreeNode* node, int& min, int& max) {
    if (!node) return;
    min = std::min(min, node->val);
    max = std::max(max, node->val);
    findMinMax(node->left, min, max);
    findMinMax(node->right, min, max);
}

int findDistance(TreeNode* start, TreeNode* end) {
    if (!start || !end) return -1; // Not found
    if (start == end) return 0;
    queue<TreeNode*> q;
    q.push(start);
    int level = 0;
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front(); q.pop();
            if (node == end) return level;
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        level++;
    }
    return -1; // Not found
}

vector<int> nodesBetweenCriticalPoints(TreeNode* root) {
    vector<TreeNode*> criticalPoints;
    findCriticalPoints(root, criticalPoints);
    if (criticalPoints.size() < 2) return {-1, -1};
    int minDist = INT_MAX, maxDist = 0;
    for (int i = 0; i < criticalPoints.size() - 1; i++) {
        int dist = findDistance(criticalPoints[i], criticalPoints[i+1]);
        minDist = std::min(minDist, dist);
        maxDist = std::max(maxDist, dist);
    }
    return {minDist, maxDist};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of nodes in the tree, because for each node, we potentially traverse the tree again.
> - **Space Complexity:** $O(n)$ for storing critical points and the queue.
> - **Why these complexities occur:** The multiple traversals of the tree for finding critical points and then finding distances between them lead to high time complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to perform a single traversal of the tree, keeping track of the minimum and maximum values seen so far and marking critical points.
- We use a depth-first search (DFS) approach to efficiently find all critical points and calculate distances between them in a single pass.
- Proof of optimality: This approach visits each node exactly once, resulting in linear time complexity.

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void dfs(TreeNode* node, int& min, int& max, vector<TreeNode*>& criticalPoints, unordered_map<TreeNode*, int>& distanceMap, int& index) {
    if (!node) return;
    if (node->val == min || node->val == max) {
        criticalPoints.push_back(node);
        distanceMap[node] = index++;
    }
    dfs(node->left, min, max, criticalPoints, distanceMap, index);
    dfs(node->right, min, max, criticalPoints, distanceMap, index);
}

vector<int> nodesBetweenCriticalPoints(TreeNode* root) {
    if (!root) return {-1, -1};
    vector<TreeNode*> criticalPoints;
    unordered_map<TreeNode*, int> distanceMap;
    int min = root->val, max = root->val;
    int index = 0;
    dfs(root, min, max, criticalPoints, distanceMap, index);
    if (criticalPoints.size() < 2) return {-1, -1};
    int minDist = INT_MAX, maxDist = 0;
    for (int i = 0; i < criticalPoints.size() - 1; i++) {
        int dist = abs(distanceMap[criticalPoints[i]] - distanceMap[criticalPoints[i+1]]);
        minDist = std::min(minDist, dist);
        maxDist = std::max(maxDist, dist);
    }
    return {minDist, maxDist};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, as we visit each node exactly once.
> - **Space Complexity:** $O(n)$ for storing critical points and the distance map.
> - **Optimality proof:** This approach achieves linear time complexity by visiting each node once, making it optimal for this problem.

### Final Notes

**Learning Points:**
- **_Depth-First Search (DFS)_**: Useful for traversing trees and finding specific nodes or patterns.
- **_Critical Point Identification_**: Involves comparing node values with their subtrees' minimum and maximum values.
- **_Distance Calculation_**: Can be efficiently done by maintaining a distance map during the DFS traversal.

**Mistakes to Avoid:**
- **_Multiple Traversals_**: Avoid traversing the tree multiple times for each node, as it leads to high time complexity.
- **_Incorrect Critical Point Identification_**: Ensure that critical points are correctly identified based on their values and subtree minimum and maximum values.
- **_Inaccurate Distance Calculation_**: Be careful when calculating distances between critical points to ensure accuracy.