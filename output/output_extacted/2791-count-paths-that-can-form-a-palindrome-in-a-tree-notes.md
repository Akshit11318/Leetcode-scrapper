## Count Paths that Can Form a Palindrome in a Tree

**Problem Link:** https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/description

**Problem Statement:**
- Input format: Given the root of a binary tree where each node contains a character, you need to count the number of paths from the root to a leaf node that can form a palindrome when the characters along the path are concatenated.
- Constraints: The tree has at most $10^4$ nodes, and each node contains a lowercase English letter.
- Expected output format: The number of paths that can form a palindrome.
- Key requirements and edge cases to consider: Handling the base case where a node is a leaf, considering all possible paths, and identifying palindromes efficiently.

**Example Test Cases:**
- For the tree with nodes containing characters 'a', 'b', 'a', the path "aba" is a palindrome.
- An empty tree should return 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree, collecting paths from the root to each leaf node, and then check if each path forms a palindrome.
- Step-by-step breakdown:
  1. Define a recursive function to traverse the tree and collect paths.
  2. At each leaf node, concatenate the characters along the path and check if the resulting string is a palindrome.
  3. Count all paths that form palindromes.

```cpp
class Solution {
public:
    int countPaths(TreeNode* root) {
        int count = 0;
        string path;
        countPathsHelper(root, path, count);
        return count;
    }
    
    void countPathsHelper(TreeNode* node, string& path, int& count) {
        if (!node) return;
        
        path += node->val;
        
        if (!node->left && !node->right) {
            // Check if path is a palindrome
            string reversedPath = path;
            reverse(reversedPath.begin(), reversedPath.end());
            if (path == reversedPath) count++;
        } else {
            countPathsHelper(node->left, path, count);
            countPathsHelper(node->right, path, count);
        }
        
        path.pop_back(); // Backtrack
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot H)$ where $N$ is the number of nodes and $H$ is the height of the tree, because in the worst case, we visit each node once and for each leaf node, we potentially reverse a string of length $H$.
> - **Space Complexity:** $O(H)$ for the recursion stack and the string used to build the path, where $H$ is the height of the tree.
> - **Why these complexities occur:** The time complexity is dominated by the traversal and the palindrome check at each leaf node. The space complexity is due to the recursion stack and the storage needed for the path string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking if a path is a palindrome by reversing the string, we can use two pointers, one from the start and one from the end of the path, moving towards the center. This way, we avoid the overhead of string reversal.
- Detailed breakdown:
  1. Modify the recursive function to pass the path as a reference to a string.
  2. At each leaf node, implement the two-pointer technique to check for palindrome.

```cpp
class Solution {
public:
    int countPaths(TreeNode* root) {
        int count = 0;
        string path;
        countPathsHelper(root, path, count);
        return count;
    }
    
    void countPathsHelper(TreeNode* node, string& path, int& count) {
        if (!node) return;
        
        path += node->val;
        
        if (!node->left && !node->right) {
            // Check if path is a palindrome using two pointers
            int left = 0, right = path.size() - 1;
            bool isPalindrome = true;
            while (left < right) {
                if (path[left] != path[right]) {
                    isPalindrome = false;
                    break;
                }
                left++;
                right--;
            }
            if (isPalindrome) count++;
        } else {
            countPathsHelper(node->left, path, count);
            countPathsHelper(node->right, path, count);
        }
        
        path.pop_back(); // Backtrack
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot H)$, where $N$ is the number of nodes and $H$ is the height of the tree, because we still visit each node once and for each leaf node, we check if the path of length $H$ is a palindrome.
> - **Space Complexity:** $O(H)$ for the recursion stack and the string used to build the path.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to check for palindromes without compromising the need to explore all paths in the tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, palindrome checking, and optimization techniques.
- Problem-solving patterns identified: Using recursion for tree problems and optimizing string operations.
- Optimization techniques learned: Avoiding unnecessary string reversals and using two pointers for palindrome checks.
- Similar problems to practice: Other tree traversal problems and string manipulation challenges.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., empty tree, single-node tree).
- Edge cases to watch for: Leaf nodes, nodes with one child, and the root node.
- Performance pitfalls: Inefficient string operations and not optimizing the palindrome check.
- Testing considerations: Thoroughly testing with different tree structures and sizes.