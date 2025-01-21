## N-ary Tree Preorder Traversal

**Problem Link:** https://leetcode.com/problems/n-ary-tree-preorder-traversal/description

**Problem Statement:**
- Input format: The input is the root of an N-ary tree.
- Constraints: The number of children of each node is between 0 and 10^4.
- Expected output format: A list of node values in preorder traversal order.
- Key requirements and edge cases to consider:
  - The input tree can be empty.
  - Each node has a unique value.
  - The tree can have any number of levels.
- Example test cases with explanations:
  - Example 1:
    - Input: `root = [1, null, 3, 2, 4, null, 5, 6]`
    - Output: `[1, 3, 5, 6, 2, 4]`
    - Explanation: The preorder traversal of the given tree is `[1, 3, 5, 6, 2, 4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to use a recursive approach, where we visit the current node and then recursively visit its children.
- Step-by-step breakdown of the solution:
  1. Start at the root node.
  2. Visit the current node.
  3. Recursively visit each child of the current node.
- Why this approach comes to mind first: This approach is intuitive because it directly follows the definition of a preorder traversal.

```cpp
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        
        // Visit the current node
        result.push_back(root->val);
        
        // Recursively visit each child
        for (Node* child : root->children) {
            vector<int> childResult = preorder(child);
            result.insert(result.end(), childResult.begin(), childResult.end());
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the recursion stack can grow up to the height of the tree, which can be $n$ for an unbalanced tree.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an iterative approach with a stack to avoid the recursion overhead and achieve the same time complexity.
- Detailed breakdown of the approach:
  1. Start at the root node.
  2. Use a stack to keep track of nodes to visit.
  3. While the stack is not empty, pop a node, visit it, and push its children onto the stack.
- Proof of optimality: This approach is optimal because it still visits each node once, resulting in a linear time complexity, and it avoids the recursion overhead.

```cpp
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }
        
        stack<Node*> stack;
        stack.push(root);
        
        while (!stack.empty()) {
            Node* node = stack.top();
            stack.pop();
            result.push_back(node->val);
            
            // Push children in reverse order so they are visited in the correct order
            for (int i = node->children.size() - 1; i >= 0; --i) {
                stack.push(node->children[i]);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the stack can contain all nodes at the last level of the tree, which can be $n$ for a complete tree.
> - **Optimality proof:** This approach is optimal because it achieves the same linear time complexity as the recursive approach but avoids the recursion overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Preorder traversal, recursive and iterative approaches, use of a stack for iterative traversal.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (visiting each node and its children), using a stack to manage the order of visitation.
- Optimization techniques learned: Avoiding recursion overhead by using an iterative approach.
- Similar problems to practice: Inorder and postorder traversal of N-ary trees.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for `nullptr` before accessing node properties, incorrect order of visiting children in the iterative approach.
- Edge cases to watch for: Empty tree, tree with a single node, tree with multiple levels.
- Performance pitfalls: Using recursion for very large trees, which can lead to stack overflow errors.
- Testing considerations: Test with trees of varying sizes and structures to ensure correctness and performance.