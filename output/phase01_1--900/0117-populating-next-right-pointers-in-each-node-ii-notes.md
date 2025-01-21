## Populating Next Right Pointers in Each Node II

**Problem Link:** https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description

**Problem Statement:**
- Given a binary tree, populate each node's `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to `NULL`.
- Input: The root of the binary tree.
- Expected output: The root of the binary tree with populated `next` pointers.
- Key requirements and edge cases to consider: Handle cases where the tree is empty, or where nodes have no children or only one child.
- Example test cases with explanations:
  - Example 1: Given the binary tree `[1,2,3,4,5,null,7]`, populate the `next` pointers to point to the next right node.
  - Example 2: Given the binary tree `[1]`, populate the `next` pointers to point to `NULL`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform a level-order traversal of the binary tree and populate the `next` pointers for each node.
- Step-by-step breakdown of the solution:
  1. Perform a level-order traversal of the binary tree using a queue.
  2. For each node in the current level, populate the `next` pointer to point to the next node in the queue.
  3. If the node is the last node in the current level, set its `next` pointer to `NULL`.
- Why this approach comes to mind first: It is a straightforward approach that uses a well-known traversal technique.

```cpp
// Definition for a Node.
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int _val, Node *_left, Node *_right) : val(_val), left(_left), right(_right), next(nullptr) {}
};

class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        
        std::queue<Node*> queue;
        queue.push(root);
        
        while (!queue.empty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node* node = queue.front();
                queue.pop();
                
                if (i < size - 1) {
                    node->next = queue.front();
                } else {
                    node->next = nullptr;
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
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, since in the worst case, the queue will contain all nodes at the last level of the binary tree.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because we need to store all nodes at the last level of the binary tree in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a previous node pointer to keep track of the previous node at the current level.
- Detailed breakdown of the approach:
  1. Initialize the previous node pointer to `nullptr`.
  2. Perform a level-order traversal of the binary tree using a queue.
  3. For each node in the current level, if the previous node is not `nullptr`, set the `next` pointer of the previous node to the current node.
  4. Update the previous node pointer to the current node.
- Proof of optimality: This approach is optimal because it only requires a single pass through the binary tree and uses a constant amount of extra space to store the previous node pointer.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is the best possible complexity for this problem.

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
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, since we visit each node once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of extra space to store the previous node pointer.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is constant because we only use a fixed amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal, queue data structure, and pointer manipulation.
- Problem-solving patterns identified: Using a previous node pointer to keep track of the previous node at the current level.
- Optimization techniques learned: Reducing space complexity by using a constant amount of extra space.
- Similar problems to practice: Populating Next Right Pointers in Each Node, Binary Tree Level Order Traversal.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty tree or a tree with only one node.
- Edge cases to watch for: Handling cases where the tree is empty, or where nodes have no children or only one child.
- Performance pitfalls: Using too much extra space, such as storing all nodes in a data structure.
- Testing considerations: Testing the solution with different types of input, such as an empty tree, a tree with only one node, and a tree with multiple levels.