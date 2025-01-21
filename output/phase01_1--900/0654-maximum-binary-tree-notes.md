## Maximum Binary Tree

**Problem Link:** https://leetcode.com/problems/maximum-binary-tree/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, construct a maximum binary tree by recursively finding the maximum value in the array to be the root of the tree, and the elements on the left and right of the maximum value will be the left and right subtrees, respectively.
- Expected output format: Return the root of the constructed maximum binary tree.
- Key requirements and edge cases to consider: The input array will contain at least one element, and the tree should be constructed in a way that the maximum value is always the root of the tree.
- Example test cases with explanations: 
    - Input: `nums = [3,2,1,6,0,5]`
    - Output: The root of the maximum binary tree with the given array.
    - Explanation: The maximum value in the array is 6, so it will be the root of the tree. The elements on the left of 6 will be the left subtree, and the elements on the right of 6 will be the right subtree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to recursively find the maximum value in the array and construct the tree based on that.
- Step-by-step breakdown of the solution:
    1. Find the maximum value in the array.
    2. Create a new node with the maximum value as the root.
    3. Recursively find the maximum value in the left and right subtrees.
    4. Create new nodes for the left and right subtrees and assign them to the root node.
- Why this approach comes to mind first: It is a straightforward approach that directly follows the problem statement.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        
        int maxIndex = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        
        TreeNode* root = new TreeNode(nums[maxIndex]);
        vector<int> left(nums.begin(), nums.begin() + maxIndex);
        vector<int> right(nums.begin() + maxIndex + 1, nums.end());
        
        root->left = constructMaximumBinaryTree(left);
        root->right = constructMaximumBinaryTree(right);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are finding the maximum value in the array and recursively constructing the tree for each element.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are creating new nodes for each element in the array.
> - **Why these complexities occur:** The time complexity occurs because we are recursively finding the maximum value in the array for each element, and the space complexity occurs because we are creating new nodes for each element.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach as the brute force solution, but instead of finding the maximum value in the entire array for each recursive call, we can pass the start and end indices of the current array to the recursive function.
- Detailed breakdown of the approach:
    1. Define a recursive function that takes the start and end indices of the current array as parameters.
    2. Find the maximum value in the current array and create a new node with that value.
    3. Recursively call the function for the left and right subtrees by passing the start and end indices of the corresponding arrays.
- Proof of optimality: This approach is optimal because we are only finding the maximum value in the current array once for each recursive call, instead of finding it for each element in the array.

```cpp
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return constructMaximumBinaryTree(nums, 0, nums.size() - 1);
    }
    
    TreeNode* constructMaximumBinaryTree(vector<int>& nums, int start, int end) {
        if (start > end) return nullptr;
        
        int maxIndex = start;
        for (int i = start + 1; i <= end; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        
        TreeNode* root = new TreeNode(nums[maxIndex]);
        root->left = constructMaximumBinaryTree(nums, start, maxIndex - 1);
        root->right = constructMaximumBinaryTree(nums, maxIndex + 1, end);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are finding the maximum value in the current array only once for each recursive call.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are creating new nodes for each element in the array.
> - **Optimality proof:** This approach is optimal because we are only finding the maximum value in the current array once for each recursive call, instead of finding it for each element in the array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree construction, finding maximum value in an array.
- Problem-solving patterns identified: Using recursive functions to solve problems that can be broken down into smaller sub-problems.
- Optimization techniques learned: Passing start and end indices to recursive functions to avoid redundant calculations.
- Similar problems to practice: Constructing binary trees from arrays, finding maximum values in arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty arrays.
- Edge cases to watch for: Empty arrays, arrays with only one element.
- Performance pitfalls: Using brute force approaches that have high time complexities.
- Testing considerations: Testing the function with different input arrays, including edge cases.