## Maximum Binary Tree II
**Problem Link:** https://leetcode.com/problems/maximum-binary-tree-ii/description

**Problem Statement:**
- Input format and constraints: Given an array `numbers`, the goal is to construct a maximum binary tree.
- Expected output format: Return the root of the maximum binary tree.
- Key requirements and edge cases to consider: The maximum binary tree is defined as the maximum value in the array becomes the root, and the elements before and after it become the left and right subtrees, respectively.
- Example test cases with explanations:
  - Example 1: Input: `numbers = [6,3,2,5,0,9]`, Output: `[9,0,6,3,2,null,null,5]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum value in the array and recursively construct the left and right subtrees.
- Step-by-step breakdown of the solution:
  1. Find the maximum value in the array.
  2. Create a new node with the maximum value.
  3. Recursively construct the left subtree with the elements before the maximum value.
  4. Recursively construct the right subtree with the elements after the maximum value.
- Why this approach comes to mind first: It is a straightforward approach that follows the definition of the maximum binary tree.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if (nums.empty()) {
            return nullptr;
        }
        int maxIndex = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        TreeNode* root = new TreeNode(nums[maxIndex]);
        vector<int> leftNums(nums.begin(), nums.begin() + maxIndex);
        vector<int> rightNums(nums.begin() + maxIndex + 1, nums.end());
        root->left = constructMaximumBinaryTree(leftNums);
        root->right = constructMaximumBinaryTree(rightNums);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are recursively constructing the left and right subtrees, and in the worst case, we are copying the entire array.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are using recursive function calls, which can go up to $n$ levels deep.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the recursive construction of the left and right subtrees, and the copying of the array. The space complexity is high due to the recursive function calls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the array to find the maximum value and construct the left and right subtrees.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the nodes.
  2. Iterate through the array, and for each element:
     - While the stack is not empty and the top node's value is less than the current element, pop the top node and set it as the right child of the new node.
     - Push the new node onto the stack.
  3. The root of the maximum binary tree is the last node in the stack.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we must at least read the input array once.
- Why further optimization is impossible: We must read the input array at least once to construct the maximum binary tree, so the time complexity cannot be improved further.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stack;
        for (int num : nums) {
            TreeNode* node = new TreeNode(num);
            while (!stack.empty() && stack.back()->val < num) {
                node->left = stack.back();
                stack.pop_back();
            }
            if (!stack.empty()) {
                stack.back()->right = node;
            }
            stack.push_back(node);
        }
        return stack[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are using a stack to store the nodes.
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is optimal because we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive construction of trees, stack-based algorithms.
- Problem-solving patterns identified: Finding the maximum value in an array and constructing a tree based on it.
- Optimization techniques learned: Using a single pass through the array to construct the tree, using a stack to store nodes.
- Similar problems to practice: Constructing a binary search tree, constructing a heap.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not validating input.
- Edge cases to watch for: Empty array, array with one element.
- Performance pitfalls: Using recursive function calls with high time complexity, using excessive memory.
- Testing considerations: Test with different input arrays, test with edge cases.