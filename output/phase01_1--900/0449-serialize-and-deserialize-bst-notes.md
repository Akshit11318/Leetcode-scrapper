## Serialize and Deserialize BST
**Problem Link:** https://leetcode.com/problems/serialize-and-deserialize-bst/description

**Problem Statement:**
- Input: A binary search tree (`BST`) represented as a `TreeNode*` root.
- Output: A class with two methods: `serialize` to convert the `BST` into a string, and `deserialize` to reconstruct the `BST` from the string.
- Key requirements: The serialization and deserialization should be efficient and able to handle large inputs.
- Edge cases: Empty tree, tree with one node, tree with multiple levels.

**Example Test Cases:**
- Test with an empty tree to ensure correct handling of edge case.
- Test with a tree containing a single node to verify serialization and deserialization of a simple case.
- Test with a multi-level tree to ensure the approach can handle complex structures.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves a straightforward, recursive approach to serialize and deserialize the `BST`. This involves traversing the tree, storing node values in a string during serialization, and reconstructing the tree based on the stored values during deserialization.
- However, a brute force approach may not consider the `BST` properties and could lead to inefficient solutions, such as not leveraging the ordered nature of the tree.

```cpp
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        string data = to_string(root->val);
        if (root->left) data += "," + serialize(root->left);
        if (root->right) data += "," + serialize(root->right);
        return data;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        vector<int> values;
        stringstream ss(data);
        string val;
        while (getline(ss, val, ',')) {
            values.push_back(stoi(val));
        }
        return constructTree(values, 0, values.size() - 1);
    }

    TreeNode* constructTree(vector<int>& values, int start, int end) {
        if (start > end) return nullptr;
        TreeNode* node = new TreeNode(values[start]);
        int mid = start + 1;
        node->left = constructTree(values, start + 1, end);
        node->right = constructTree(values, mid, end);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once during both serialization and deserialization.
> - **Space Complexity:** $O(n)$, for storing the serialized string and the recursive call stack.
> - **Why these complexities occur:** The brute force approach leads to these complexities due to the recursive nature of the solution and the need to store all node values in the serialized string.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach leverages the properties of a `BST` to improve the efficiency of serialization and deserialization. Specifically, it uses a pre-order traversal to serialize the tree, which allows for efficient deserialization by ensuring that the root node is always processed first, followed by its left and right subtrees.
- This approach ensures that the deserialization process can correctly reconstruct the `BST` without needing to sort the node values or perform additional operations.

```cpp
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "X,";
        return to_string(root->val) + "," + serialize(root->left) + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream ss(data);
        string val;
        vector<string> values;
        while (getline(ss, val, ',')) {
            values.push_back(val);
        }
        int idx = 0;
        return constructTree(values, idx);
    }

    TreeNode* constructTree(vector<string>& values, int& idx) {
        if (idx >= values.size() || values[idx] == "X") {
            idx++;
            return nullptr;
        }
        TreeNode* node = new TreeNode(stoi(values[idx++]));
        node->left = constructTree(values, idx);
        node->right = constructTree(values, idx);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once during both serialization and deserialization.
> - **Space Complexity:** $O(n)$, for storing the serialized string and the recursive call stack.
> - **Optimality proof:** This approach is optimal because it leverages the `BST` properties to minimize the number of operations required for serialization and deserialization, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: pre-order traversal, recursive tree construction, and leveraging the properties of a `BST` for efficient serialization and deserialization.
- Problem-solving patterns identified: using a recursive approach to solve tree-related problems and considering the properties of the data structure to optimize the solution.
- Optimization techniques learned: leveraging the ordered nature of a `BST` to simplify the deserialization process.

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of edge cases (e.g., empty tree, single-node tree), failing to consider the properties of the `BST` during serialization and deserialization.
- Edge cases to watch for: empty input, single-node tree, and multi-level trees with varying structures.
- Performance pitfalls: using an inefficient traversal method or failing to optimize the deserialization process based on the `BST` properties.