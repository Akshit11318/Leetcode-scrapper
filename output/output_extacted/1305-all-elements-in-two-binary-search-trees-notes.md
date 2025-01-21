## All Elements in Two Binary Search Trees

**Problem Link:** https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description

**Problem Statement:**
- Input format and constraints: Given two binary search trees `root1` and `root2`, return a list containing all the integers from both trees in ascending order.
- Expected output format: A sorted list of integers.
- Key requirements and edge cases to consider: The trees may be empty, and the output list should not contain duplicates.
- Example test cases with explanations: 
    - `root1 = [2,1,4]`, `root2 = [1,0,3]`, output: `[0,1,1,2,3,4]`
    - `root1 = [0,-10,10]`, `root2 = [5,1,7,0,2]`, output: `[-10,0,0,1,2,5,7,10]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse both trees, collect all nodes' values, and then sort them.
- Step-by-step breakdown of the solution:
    1. Perform an in-order traversal of both trees to collect all node values in two separate lists.
    2. Merge the two lists into one.
    3. Sort the merged list in ascending order.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> tree1, tree2;
        inOrder(root1, tree1);
        inOrder(root2, tree2);
        tree1.insert(tree1.end(), tree2.begin(), tree2.end());
        sort(tree1.begin(), tree1.end());
        return tree1;
    }
    
    void inOrder(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inOrder(node->left, values);
        values.push_back(node->val);
        inOrder(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + (n + m) \log(n + m))$, where $n$ and $m$ are the number of nodes in `root1` and `root2`, respectively. The $n + m$ accounts for the in-order traversal, and $(n + m) \log(n + m)$ is for the sorting.
> - **Space Complexity:** $O(n + m)$ for storing the values of all nodes.
> - **Why these complexities occur:** The traversal of both trees is linear with respect to the total number of nodes, and the sorting operation dominates the time complexity due to its logarithmic factor.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since both trees are binary search trees, we can leverage their inherent ordering property to merge the two trees' values in a single pass without needing to sort afterwards.
- Detailed breakdown of the approach:
    1. Perform an in-order traversal of both trees simultaneously, comparing the current node values and adding the smaller one to the result list.
    2. If one tree is exhausted before the other, append the remaining nodes from the non-exhausted tree to the result list.
- Proof of optimality: This approach takes advantage of the BST property, ensuring that the merged list is sorted without the need for an additional sorting step, thus reducing the overall time complexity.

```cpp
class Solution {
public:
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> result;
        stack<TreeNode*> stack1, stack2;
        pushLeft(root1, stack1);
        pushLeft(root2, stack2);
        
        while (!stack1.empty() || !stack2.empty()) {
            if (stack2.empty() || (!stack1.empty() && stack1.top()->val < stack2.top()->val)) {
                TreeNode* node = stack1.top(); stack1.pop();
                result.push_back(node->val);
                pushLeft(node->right, stack1);
            } else {
                TreeNode* node = stack2.top(); stack2.pop();
                result.push_back(node->val);
                pushLeft(node->right, stack2);
            }
        }
        return result;
    }
    
    void pushLeft(TreeNode* node, stack<TreeNode*>& stack) {
        while (node) {
            stack.push(node);
            node = node->left;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the number of nodes in `root1` and `root2`, respectively. This is because we visit each node exactly once.
> - **Space Complexity:** $O(n + m)$ for the stacks used to store nodes and the result vector.
> - **Optimality proof:** This approach is optimal because it leverages the inherent ordering of BSTs to merge the trees in a single pass, avoiding the need for an additional sorting step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal, stack usage for iterative traversal, and leveraging properties of data structures (BSTs) for efficient merging.
- Problem-solving patterns identified: Recognizing the opportunity to use the ordering property of BSTs to simplify the merging process.
- Optimization techniques learned: Avoiding unnecessary sorting by utilizing the inherent ordering of data structures.
- Similar problems to practice: Merging sorted lists, traversing BSTs, and leveraging properties of other data structures for efficient solutions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty trees), failing to consider the properties of BSTs, and inefficiently sorting the merged list.
- Edge cases to watch for: Empty trees, trees with a single node, and trees with duplicate values.
- Performance pitfalls: Using sorting algorithms when the data structure's properties can be leveraged for more efficient solutions.
- Testing considerations: Thoroughly testing with various tree configurations, including empty trees, balanced and unbalanced trees, and trees with duplicate values.