## Convert Sorted Array to Binary Search Tree

**Problem Link:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` where the elements are in ascending order, convert it to a height-balanced binary search tree.
- Expected output format: Return the root of the binary search tree.
- Key requirements and edge cases to consider: 
    - The binary search tree should be height-balanced, meaning the absolute difference between the heights of its left and right subtrees cannot exceed 1 for all nodes in the tree.
    - The input array `nums` is non-empty and contains unique integers.
    - The length of `nums` is less than or equal to 1000.
- Example test cases with explanations:
    - For `nums = [-10,-3,0,5,9]`, the output should be a binary search tree with the following structure:
        ```
        0
       / \
      -3   9
      /   /
     -10  5
        ```
    - For `nums = [1, 3]`, the output should be a binary search tree with the following structure:
        ```
          3
         /
        1
        ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try to create all possible binary search trees and then check which one is height-balanced.
- Step-by-step breakdown of the solution:
    1. Generate all possible binary search trees from the given array.
    2. For each tree, calculate its height and check if it is height-balanced.
    3. If a tree is height-balanced, return its root.
- Why this approach comes to mind first: This approach is straightforward but inefficient because it involves generating all possible trees, which has a high time complexity.

```cpp
// Brute Force Approach
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        // Generate all possible binary search trees
        vector<TreeNode*> trees = generateTrees(nums);
        for (TreeNode* tree : trees) {
            if (isHeightBalanced(tree)) {
                return tree;
            }
        }
        return nullptr;
    }
    
    vector<TreeNode*> generateTrees(vector<int>& nums) {
        if (nums.empty()) {
            return {nullptr};
        }
        vector<TreeNode*> trees;
        for (int i = 0; i < nums.size(); i++) {
            vector<int> leftNums(nums.begin(), nums.begin() + i);
            vector<int> rightNums(nums.begin() + i + 1, nums.end());
            for (TreeNode* left : generateTrees(leftNums)) {
                for (TreeNode* right : generateTrees(rightNums)) {
                    TreeNode* tree = new TreeNode(nums[i]);
                    tree->left = left;
                    tree->right = right;
                    trees.push_back(tree);
                }
            }
        }
        return trees;
    }
    
    bool isHeightBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);
        return abs(leftHeight - rightHeight) <= 1 && isHeightBalanced(root->left) && isHeightBalanced(root->right);
    }
    
    int getHeight(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return max(getHeight(root->left), getHeight(root->right)) + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of `nums`, because we generate all possible binary search trees.
> - **Space Complexity:** $O(2^n)$, because we store all possible binary search trees.
> - **Why these complexities occur:** These complexities occur because we generate all possible trees and store them in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a recursive approach to construct the binary search tree, where the middle element of the array is the root of the tree, and the left and right halves of the array are the left and right subtrees, respectively.
- Detailed breakdown of the approach:
    1. If the input array is empty, return `nullptr`.
    2. Calculate the middle index of the array.
    3. Create a new `TreeNode` with the middle element as its value.
    4. Recursively construct the left and right subtrees using the left and right halves of the array, respectively.
    5. Return the root of the constructed binary search tree.
- Proof of optimality: This approach is optimal because it constructs the binary search tree in $O(n)$ time complexity, where $n$ is the length of `nums`, and $O(log n)$ space complexity, where $n$ is the length of `nums`, because we only need to store the recursive call stack.

```cpp
// Optimal Approach
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size() - 1);
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        int mid = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = sortedArrayToBST(nums, left, mid - 1);
        root->right = sortedArrayToBST(nums, mid + 1, right);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we construct the binary search tree in a single pass.
> - **Space Complexity:** $O(log n)$, where $n$ is the length of `nums`, because we only need to store the recursive call stack.
> - **Optimality proof:** This approach is optimal because it constructs the binary search tree in linear time complexity and logarithmic space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive approach, binary search tree construction, and height-balanced tree properties.
- Problem-solving patterns identified: using the middle element as the root of the tree and recursively constructing the left and right subtrees.
- Optimization techniques learned: using a recursive approach to construct the binary search tree and avoiding unnecessary computations.
- Similar problems to practice: constructing a binary search tree from a sorted linked list, finding the median of two sorted arrays, and constructing a height-balanced binary search tree from a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array, and not handling recursive calls correctly.
- Edge cases to watch for: handling the case where the input array has an odd or even number of elements, and ensuring that the constructed binary search tree is height-balanced.
- Performance pitfalls: using an inefficient approach, such as generating all possible binary search trees, and not optimizing the recursive approach.
- Testing considerations: testing the solution with different input arrays, including edge cases, and verifying that the constructed binary search tree is height-balanced and correct.