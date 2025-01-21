## Populating Next Right Pointers in Each Node

**Problem Link:** https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description

**Problem Statement:**
- Input: A root node of a tree where each node has `val`, `left`, `right`, and `next` pointers.
- Constraints: The number of nodes in the tree is in the range `[0, 2^12 - 1]`.
- Expected Output: Populate the `next` pointer in each node to point to the next right node at the same level.
- Key Requirements: Handle edge cases where a node may not have a right neighbor.
- Example Test Cases:
  - An empty tree.
  - A tree with a single node.
  - A tree where each level is fully populated.
  - A tree where some levels are not fully populated.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree level by level and populating the `next` pointers based on the node's position in the level.
- This can be achieved by using a queue to store nodes at each level and then iterating through the queue to set the `next` pointers.
- This approach comes to mind first because it's a straightforward way to traverse the tree level by level and update the `next` pointers accordingly.

```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        
        std::queue<Node*> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                Node* node = queue.front();
                queue.pop();
                
                if (i < size - 1) {
                    node->next = queue.front();
                }
                
                if (node->left) queue.push(node->left);
                if (node->right) queue.push(node->right);
            }
        }
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because each node is visited once.
> - **Space Complexity:** $O(n)$ due to the queue used for level-order traversal, where in the worst case, the queue will store all nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is also linear due to the need to store nodes at each level in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use the existing `next` pointers of the previous level to traverse the current level, thus eliminating the need for a queue.
- This approach is optimal because it reduces the space complexity to $O(1)$ by avoiding the use of a queue.
- We start by checking if the root is `nullptr`, and if so, we return `nullptr`.
- Then, we iterate through each level, starting from the root, and for each node, we set the `next` pointer of its right child to the left child of the next node in the current level.
- This process continues until we have traversed all levels of the tree.

```cpp
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        
        Node* leftmost = root;
        
        while (leftmost->left) {
            Node* head = leftmost;
            while (head) {
                head->left->next = head->right;
                
                if (head->next) {
                    head->right->next = head->next->left;
                }
                
                head = head->next;
            }
            
            leftmost = leftmost->left;
        }
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because each node is visited once.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the `leftmost` node and other variables.
> - **Optimality proof:** This is the best possible complexity because we must visit each node at least once to populate the `next` pointers, and we do so in a way that minimizes additional space usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: level-order traversal, using existing pointers to reduce space complexity.
- Problem-solving patterns identified: optimizing space complexity by reusing existing data structures.
- Optimization techniques learned: eliminating unnecessary data structures to reduce space complexity.
- Similar problems to practice: other tree traversal problems, optimizing space complexity in graph algorithms.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: trees with varying levels of population, ensuring that the `next` pointers are correctly set for all nodes.
- Performance pitfalls: using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: thoroughly testing the solution with different types of input trees to ensure correctness.