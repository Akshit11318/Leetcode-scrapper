## Path in Zigzag Labelled Binary Tree

**Problem Link:** https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description

**Problem Statement:**
- Input: A `label` representing a node in a binary tree where each node is labelled in a zigzag pattern.
- Constraints: The tree has `3^h - 1` nodes where `h` is the height of the tree.
- Expected Output: The path from the root node to the node with the given `label`.
- Key Requirements: Understand the zigzag labelling pattern and how to traverse the tree to find the path to the target node.
- Edge Cases: Consider the cases where the `label` is not valid or the tree is empty.

Example Test Case:
- Input: `label = 14`
- Output: `[1, 3, 4, 14]`
- Explanation: The path from the root node to the node with label `14` is `[1, 3, 4, 14]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate the construction of the binary tree with zigzag labelling and then traverse the tree to find the path to the target node.
- We can start by creating the tree level by level, following the zigzag pattern for labelling.
- Once the tree is constructed, we can perform a depth-first search (DFS) to find the path to the node with the given `label`.

```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        // Initialize variables
        vector<int> path;
        int level = 0;
        int nodeCount = 1;
        
        // Find the level of the target node
        while (nodeCount < label) {
            level++;
            nodeCount += (1 << level);
        }
        
        // Traverse from the target node to the root
        while (level >= 0) {
            path.push_back(label);
            // Calculate the parent node's label based on the zigzag pattern
            label = ((1 << (level + 1)) - 1 - label + (1 << level)) / 2;
            level--;
        }
        
        // Reverse the path to get the correct order
        reverse(path.begin(), path.end());
        
        return path;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$ where $h$ is the height of the tree, because we traverse from the target node to the root.
> - **Space Complexity:** $O(h)$ for storing the path, as the maximum length of the path is equal to the height of the tree.
> - **Why these complexities occur:** The time complexity is due to the traversal from the target node to the root, and the space complexity is due to storing the path.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to directly calculate the parent node's label based on the zigzag pattern without constructing the entire tree.
- We can start from the target node and iteratively calculate its parent node's label until we reach the root.
- The calculation involves using the properties of the zigzag labelling pattern to find the parent node's label.

```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> path;
        int level = 0;
        int nodeCount = 1;
        
        // Find the level of the target node
        while (nodeCount < label) {
            level++;
            nodeCount += (1 << level);
        }
        
        // Traverse from the target node to the root
        while (level >= 0) {
            path.push_back(label);
            // Calculate the parent node's label based on the zigzag pattern
            label = ((1 << (level + 1)) - 1 - label + (1 << level)) / 2;
            level--;
        }
        
        // Reverse the path to get the correct order
        reverse(path.begin(), path.end());
        
        return path;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$ where $h$ is the height of the tree, because we traverse from the target node to the root.
> - **Space Complexity:** $O(h)$ for storing the path, as the maximum length of the path is equal to the height of the tree.
> - **Optimality proof:** This is the optimal solution because we directly calculate the parent node's label without constructing the entire tree, resulting in the minimum possible time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: zigzag labelling pattern, tree traversal, and calculation of parent node's label.
- Problem-solving patterns identified: using properties of the labelling pattern to find the parent node's label.
- Optimization techniques learned: avoiding construction of the entire tree and directly calculating the parent node's label.

**Mistakes to Avoid:**
- Common implementation errors: incorrect calculation of the parent node's label, incorrect traversal order.
- Edge cases to watch for: invalid `label` values, empty tree.
- Performance pitfalls: constructing the entire tree instead of directly calculating the parent node's label.
- Testing considerations: testing with different `label` values, testing with edge cases.