## Two Sum BSTs
**Problem Link:** https://leetcode.com/problems/two-sum-bsts/description

**Problem Statement:**
- Input: Two binary search trees `root1` and `root2`, and an integer `target`.
- Output: `true` if there exists a pair of elements, one from each tree, that sums to `target`, otherwise `false`.
- Key requirements: 
  - Both trees are non-empty.
  - All values in the trees are integers.
- Edge cases: 
  - If one or both trees are empty, return `false`.
  - If the target is not achievable by any pair of elements, return `false`.

**Example Test Cases:**
- `root1 = [2,1,4]`, `root2 = [1,0]`, `target = 5`. Return `true` because `4` from the first tree and `1` from the second tree sum to `5`.
- `root1 = [0,-10,10]`, `root2 = [1]`, `target = -1`. Return `false` because no pair sums to `-1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible pair of elements from both trees to see if any pair sums to the target.
- This approach requires traversing both trees to collect all elements, then comparing each element from one tree with every element from the other tree.

```cpp
// Brute Force Approach
class Solution {
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        vector<int> tree1Values, tree2Values;
        
        // Traverse the first tree and store its values
        traverseTree(root1, tree1Values);
        
        // Traverse the second tree and store its values
        traverseTree(root2, tree2Values);
        
        // Compare each element from the first tree with every element from the second tree
        for (int val1 : tree1Values) {
            for (int val2 : tree2Values) {
                if (val1 + val2 == target) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    void traverseTree(TreeNode* root, vector<int>& values) {
        if (root == nullptr) return;
        values.push_back(root->val);
        traverseTree(root->left, values);
        traverseTree(root->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the number of nodes in the first and second trees, respectively. This is because we are potentially comparing each node from the first tree with every node from the second tree.
> - **Space Complexity:** $O(n + m)$, as we need to store the values of both trees. 
> - **Why these complexities occur:** These complexities arise from the need to traverse both trees and compare each pair of elements, leading to a quadratic time complexity in terms of the total number of nodes across both trees.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to traverse one tree and for each node, check if the complement (target minus the current node's value) exists in the other tree. This can be efficiently done by using a `set` to store the values of one tree as we traverse it, and then checking for the existence of the complement in the set as we traverse the other tree.
- However, since we are dealing with BSTs, we can directly search for the complement in the second tree without needing to store its values in a set, thus reducing the space complexity.

```cpp
// Optimal Approach
class Solution {
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        return findComplement(root1, root2, target) || findComplement(root2, root1, target);
    }
    
    bool findComplement(TreeNode* root, TreeNode* otherRoot, int target) {
        if (root == nullptr) return false;
        
        if (search(otherRoot, target - root->val)) {
            return true;
        }
        
        return findComplement(root->left, otherRoot, target) || findComplement(root->right, otherRoot, target);
    }
    
    bool search(TreeNode* root, int target) {
        if (root == nullptr) return false;
        if (root->val == target) return true;
        if (target < root->val) return search(root->left, target);
        return search(root->right, target);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot h)$, where $n$ is the number of nodes in the first tree and $h$ is the height of the second tree. This is because in the worst case, we might need to search for a complement in the second tree for each node in the first tree.
> - **Space Complexity:** $O(h)$, due to the recursive call stack for traversing the trees.
> - **Optimality proof:** This approach is optimal because it leverages the properties of BSTs to efficiently search for complements, reducing the need to compare every pair of elements directly.

---

### Final Notes

**Learning Points:**
- Utilizing the properties of binary search trees (BSTs) to optimize search operations.
- Employing recursive approaches for tree traversals.
- Understanding how to analyze time and space complexities for recursive algorithms.

**Mistakes to Avoid:**
- Not considering the properties of the data structures involved (in this case, BSTs).
- Failing to optimize the search process, leading to unnecessary comparisons.
- Not accounting for edge cases, such as empty trees or non-existent complements.