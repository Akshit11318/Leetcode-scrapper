## N-ary Tree Postorder Traversal

**Problem Link:** https://leetcode.com/problems/n-ary-tree-postorder-traversal/description

**Problem Statement:**
- Input: A root node of an N-ary tree, where each node has a value and a list of its children.
- Constraints: The number of children of each node is in the range $[0, N]$, where $N$ is the maximum number of children for any node.
- Expected Output: A list of node values in postorder traversal order.
- Key Requirements:
  - Traverse the tree in postorder, meaning visit the children before the parent.
  - Handle edge cases, such as an empty tree or a tree with a single node.
- Example Test Cases:
  - Example 1: Given a tree with a root node having value 1 and three children with values 3, 2, and 4, the output should be [3, 2, 4, 1].
  - Example 2: Given an empty tree, the output should be an empty list.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform a recursive depth-first search (DFS) on the tree, visiting each child before its parent.
- However, a brute force approach would involve using a recursive function to visit each node and its children, without considering any optimizations.

```cpp
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        if (root == nullptr) return result;
        
        function<void(Node*)> dfs = [&](Node* node) {
            for (Node* child : node->children) {
                dfs(child);
            }
            result.push_back(node->val);
        };
        
        dfs(root);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, since in the worst case, the recursive call stack can go up to $N$ levels deep.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use an iterative approach instead of recursive, which can help avoid the overhead of recursive function calls.
- We can use a stack to store nodes to be visited, and iterate through the stack to perform the postorder traversal.
- This approach is optimal because it achieves the same time complexity as the brute force approach but with improved space complexity.

```cpp
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        if (root == nullptr) return result;
        
        stack<Node*> stack;
        stack.push(root);
        stack<Node*> output;
        
        while (!stack.empty()) {
            Node* node = stack.top();
            stack.pop();
            output.push(node);
            
            for (Node* child : node->children) {
                stack.push(child);
            }
        }
        
        while (!output.empty()) {
            result.push_back(output.top()->val);
            output.pop();
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, since we use two stacks to store nodes, but the space complexity is still linear.
> - **Optimality proof:** This approach is optimal because it achieves the same time complexity as the brute force approach but with improved code structure and no recursive function calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: postorder traversal, recursive and iterative DFS.
- Problem-solving patterns identified: using a stack to perform iterative DFS.
- Optimization techniques learned: avoiding recursive function calls to improve space complexity.
- Similar problems to practice: binary tree traversal, graph traversal.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: trees with a large number of nodes, trees with a deep hierarchy.
- Performance pitfalls: using recursive function calls for large inputs, not considering the space complexity of the solution.
- Testing considerations: testing the solution with different tree structures, testing the solution with large inputs.