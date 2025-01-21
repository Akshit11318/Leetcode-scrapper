## Number of Good Leaf Nodes Pairs
**Problem Link:** https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description

**Problem Statement:**
- Given a binary tree and an integer `distance`, find the number of pairs of leaf nodes that are within the given distance.
- Input: A binary tree and an integer `distance`.
- Expected Output: The number of pairs of leaf nodes that are within the given distance.
- Key Requirements and Edge Cases:
  - Handle cases where the tree is empty or has only one node.
  - Consider the distance between leaf nodes in both directions (i.e., from left to right and from right to left).
- Example Test Cases:
  - Example 1: Given a binary tree with nodes 1, 2, and 3, and a distance of 2, the output should be 1 because there is one pair of leaf nodes (2 and 3) that are within a distance of 2.
  - Example 2: Given a binary tree with nodes 1, 2, 3, 4, and 5, and a distance of 3, the output should be 2 because there are two pairs of leaf nodes (2 and 4, and 3 and 5) that are within a distance of 3.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the binary tree and find all leaf nodes.
- Then, for each pair of leaf nodes, calculate the distance between them.
- If the distance is within the given limit, increment the count of good leaf node pairs.
- This approach involves calculating the distance between all pairs of leaf nodes, which can be time-consuming.

```cpp
int countPairs(TreeNode* root, int distance) {
    vector<int> leafNodes;
    // Function to find all leaf nodes
    function<void(TreeNode*)> findLeafNodes = [&](TreeNode* node) {
        if (!node) return;
        if (!node->left && !node->right) leafNodes.push_back(node->val);
        findLeafNodes(node->left);
        findLeafNodes(node->right);
    };
    findLeafNodes(root);
    
    int count = 0;
    for (int i = 0; i < leafNodes.size(); i++) {
        for (int j = i + 1; j < leafNodes.size(); j++) {
            // Calculate the distance between two leaf nodes
            int dist = calculateDistance(root, leafNodes[i], leafNodes[j]);
            if (dist <= distance) count++;
        }
    }
    return count;
}

int calculateDistance(TreeNode* root, int node1, int node2) {
    // Function to find the distance between two nodes
    function<int(TreeNode*, int)> findDistance = [&](TreeNode* node, int target) {
        if (!node) return -1;
        if (node->val == target) return 0;
        int left = findDistance(node->left, target);
        if (left != -1) return left + 1;
        int right = findDistance(node->right, target);
        if (right != -1) return right + 1;
        return -1;
    };
    int lca = findLCA(root, node1, node2);
    int dist1 = findDistance(root, node1);
    int dist2 = findDistance(root, node2);
    return dist1 + dist2 - 2 * findDistance(root, lca);
}

int findLCA(TreeNode* root, int node1, int node2) {
    // Function to find the lowest common ancestor of two nodes
    if (!root) return -1;
    if (root->val == node1 || root->val == node2) return root->val;
    int left = findLCA(root->left, node1, node2);
    int right = findLCA(root->right, node1, node2);
    if (left != -1 && right != -1) return root->val;
    return left != -1 ? left : right;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of nodes in the tree. The reason is that we are finding all leaf nodes ($O(n)$), and for each pair of leaf nodes, we are calculating the distance between them ($O(n)$). The distance calculation involves finding the lowest common ancestor ($O(n)$) and the distances from the LCA to each node ($O(n)$).
> - **Space Complexity:** $O(n)$ for storing the leaf nodes.
> - **Why these complexities occur:** The brute force approach involves calculating the distance between all pairs of leaf nodes, which results in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- To optimize the solution, we can use a `HashMap` to store the distance from the root to each node.
- We can also use a `HashSet` to store the leaf nodes.
- Then, for each leaf node, we can calculate the distance to all other leaf nodes using the stored distances.
- This approach reduces the time complexity to $O(n^2)$.

```cpp
int countPairs(TreeNode* root, int distance) {
    unordered_map<int, int> nodeDistances;
    unordered_set<int> leafNodes;
    
    function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int dist) {
        if (!node) return;
        if (!node->left && !node->right) {
            leafNodes.insert(node->val);
            nodeDistances[node->val] = dist;
        }
        dfs(node->left, dist + 1);
        dfs(node->right, dist + 1);
    };
    dfs(root, 0);
    
    int count = 0;
    for (int node1 : leafNodes) {
        for (int node2 : leafNodes) {
            if (node1 == node2) continue;
            if (nodeDistances[node1] + nodeDistances[node2] <= distance) count++;
        }
    }
    return count / 2; // Divide by 2 to avoid counting pairs twice
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of nodes in the tree. The reason is that we are finding all leaf nodes ($O(n)$) and for each leaf node, we are calculating the distance to all other leaf nodes ($O(n)$).
> - **Space Complexity:** $O(n)$ for storing the node distances and leaf nodes.
> - **Optimality proof:** This is the optimal solution because we are using a `HashMap` to store the node distances, which allows us to calculate the distance between two nodes in constant time. We are also using a `HashSet` to store the leaf nodes, which allows us to check if a node is a leaf node in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using a `HashMap` to store node distances and a `HashSet` to store leaf nodes.
- Problem-solving patterns identified: optimizing the solution by reducing the time complexity from $O(n^3)$ to $O(n^2)$.
- Optimization techniques learned: using a `HashMap` to store node distances and a `HashSet` to store leaf nodes.
- Similar problems to practice: finding the closest pair of nodes in a graph, finding the shortest path between two nodes in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty tree or a tree with only one node.
- Edge cases to watch for: handling cases where the distance between two nodes is equal to the given distance.
- Performance pitfalls: using a brute force approach that results in a cubic time complexity.
- Testing considerations: testing the solution with different inputs, such as an empty tree, a tree with only one node, and a tree with multiple nodes.