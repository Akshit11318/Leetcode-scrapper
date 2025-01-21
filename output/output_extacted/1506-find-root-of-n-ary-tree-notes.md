## Find Root of N-ary Tree

**Problem Link:** https://leetcode.com/problems/find-root-of-n-ary-tree/description

**Problem Statement:**
- Input: A list of `Node` objects representing an N-ary tree.
- Constraints: The N-ary tree has `n` nodes, and each node has a unique value.
- Expected Output: The root of the N-ary tree.
- Key Requirements: The input tree is guaranteed to have a root node.
- Edge Cases: The input list may be empty.

Example:
- Input: `tree = [1,2,3,4,5,6,7,8,9,10,11,12,13]`
- Output: The root of the N-ary tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each node in the tree and check if it has any children. If a node has no parent, it is the root.
- Step-by-step breakdown of the solution:
  1. Create a `set` to store the values of all child nodes.
  2. Iterate over each node in the tree and add its children to the set.
  3. Iterate over each node in the tree again and check if its value is in the set. If not, it is the root.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    Node* findRoot(vector<Node*>& tree) {
        unordered_set<int> children;
        for (auto node : tree) {
            for (auto child : node->children) {
                children.insert(child->val);
            }
        }
        for (auto node : tree) {
            if (children.find(node->val) == children.end()) {
                return node;
            }
        }
        return nullptr; // Return nullptr if no root is found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes and $m$ is the average number of children per node. This is because we iterate over each node and its children twice.
> - **Space Complexity:** $O(n \cdot m)$, as we store all child node values in the set.
> - **Why these complexities occur:** The brute force approach requires iterating over each node and its children multiple times, resulting in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can find the root by counting the number of times each node value appears as a child. The node that appears least often as a child is the root.
- Detailed breakdown of the approach:
  1. Create a `map` to store the count of each node value as a child.
  2. Iterate over each node in the tree and increment the count of its children in the map.
  3. Find the node with the minimum count in the map. This node is the root.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it only requires a single pass over the tree.

```cpp
class Solution {
public:
    Node* findRoot(vector<Node*>& tree) {
        unordered_map<int, int> count;
        for (auto node : tree) {
            for (auto child : node->children) {
                count[child->val]++;
            }
        }
        int minCount = INT_MAX;
        Node* root = nullptr;
        for (auto node : tree) {
            if (count[node->val] < minCount) {
                minCount = count[node->val];
                root = node;
            }
        }
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes and $m$ is the average number of children per node. This is because we iterate over each node and its children once.
> - **Space Complexity:** $O(n)$, as we store the count of each node value in the map.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the tree, resulting in the lowest possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, counting, and iteration.
- Problem-solving patterns identified: Finding the minimum or maximum value in a dataset.
- Optimization techniques learned: Reducing the number of iterations and using efficient data structures.
- Similar problems to practice: Finding the root of a binary tree, counting the number of nodes in a tree, and finding the minimum or maximum value in a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty input, not handling edge cases, and not using efficient data structures.
- Edge cases to watch for: Empty input, single-node tree, and tree with multiple roots.
- Performance pitfalls: Using inefficient data structures, iterating over the tree multiple times, and not optimizing the solution.
- Testing considerations: Testing the solution with different input sizes, testing edge cases, and testing performance.