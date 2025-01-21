## Find Duplicate Subtrees

**Problem Link:** https://leetcode.com/problems/find-duplicate-subtrees/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a unique integer value.
- Constraints: The number of nodes in the tree will be in the range [1, 10^4].
- Expected output: A list of all duplicate subtrees, where a duplicate subtree is a subtree that appears more than once in the tree.
- Key requirements: Each node in the tree has a unique integer value, and a subtree is considered duplicate if it has the same structure and node values as another subtree.
- Example test cases:
  - Example 1:
    - Input: root = [1,2,3,2,2,null,null,4,null,null,null,null,4]
    - Output: [[2,null,4],[2,null,4]]
  - Example 2:
    - Input: root = [2,1,1]
    - Output: [[1]]
  - Example 3:
    - Input: root = [2,2,2,2,2,null,2]
    - Output: [[2],[2],[2]]

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) on the tree and serialize each subtree into a string.
- For each node, we recursively serialize its left and right subtrees and combine them with the current node's value.
- We then store these serialized subtrees in a hash map and count their occurrences.
- Finally, we return the serialized subtrees that appear more than once.

```cpp
class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, int> count;
        vector<TreeNode*> result;
        dfs(root, count, result);
        return result;
    }
    
    string dfs(TreeNode* node, unordered_map<string, int>& count, vector<TreeNode*>& result) {
        if (!node) return "";
        string left = dfs(node->left, count, result);
        string right = dfs(node->right, count, result);
        string subtree = to_string(node->val) + "," + left + "," + right;
        count[subtree]++;
        if (count[subtree] == 2) result.push_back(node);
        return subtree;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(N)$, as we store the serialized subtrees in the hash map and the result vector.
> - **Why these complexities occur:** The DFS traversal allows us to visit each node once, resulting in linear time complexity. The space complexity is also linear due to the storage of serialized subtrees and the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a hash map to store the serialized subtrees and their counts, as well as a vector to store the duplicate subtrees.
- We perform a DFS traversal on the tree, serializing each subtree and updating the count in the hash map.
- If a subtree's count becomes 2, we add it to the result vector.
- This approach is optimal because it only requires a single pass through the tree and uses a hash map for efficient lookup and counting.

```cpp
class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string, pair<int, TreeNode*>> count;
        vector<TreeNode*> result;
        dfs(root, count, result);
        return result;
    }
    
    string dfs(TreeNode* node, unordered_map<string, pair<int, TreeNode*>>& count, vector<TreeNode*>& result) {
        if (!node) return "";
        string left = dfs(node->left, count, result);
        string right = dfs(node->right, count, result);
        string subtree = to_string(node->val) + "," + left + "," + right;
        if (count.find(subtree) != count.end()) {
            count[subtree].first++;
            if (count[subtree].first == 2) result.push_back(count[subtree].second);
        } else {
            count[subtree] = {1, node};
        }
        return subtree;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(N)$, as we store the serialized subtrees in the hash map and the result vector.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree and uses a hash map for efficient lookup and counting, resulting in linear time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, hash map usage, and subtree serialization.
- Problem-solving patterns identified: Using a hash map to count occurrences and a vector to store results.
- Optimization techniques learned: Using a single pass through the tree and a hash map for efficient lookup and counting.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a subtree appears more than twice.
- Edge cases to watch for: Empty trees or trees with a single node.
- Performance pitfalls: Using an inefficient data structure, such as a set or list, instead of a hash map.
- Testing considerations: Testing with different tree structures and sizes to ensure correctness and efficiency.