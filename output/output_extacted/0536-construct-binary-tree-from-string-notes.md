## Construct Binary Tree from String
**Problem Link:** https://leetcode.com/problems/construct-binary-tree-from-string/description

**Problem Statement:**
- Input format: a string `s` representing a binary tree where each node's value is given in parentheses.
- Constraints: `1 <= s.length <= 105`, and the given string `s` is valid.
- Expected output format: the root node of the reconstructed binary tree.
- Key requirements: construct a binary tree from the given string representation.
- Edge cases to consider: empty string, single node tree, balanced and unbalanced trees.

**Example Test Cases:**
- `s = "4(2(3)(1))(6(5))"` should return a binary tree with the given structure.
- `s = "4(2(3)(1))(6(5)(7))"` should return a binary tree with the given structure.
- `s = "1()"` should return a binary tree with a single node and an empty left and right child.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to parse the string and construct the tree by iterating through the string and creating nodes as we encounter them.
- We will use a stack to keep track of the nodes as we construct the tree.

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
    TreeNode* str2tree(string s) {
        if (s.empty()) return NULL;
        int start = 0, end = 0;
        while (end < s.size() && s[end] != '(') end++;
        TreeNode* root = new TreeNode(stoi(s.substr(start, end - start)));
        if (end == s.size()) return root;
        stack<TreeNode*> st;
        st.push(root);
        start = end + 1;
        while (end < s.size()) {
            if (s[end] == '(') {
                end++;
                start = end;
                while (end < s.size() && s[end] != ')') end++;
                TreeNode* newNode = new TreeNode(stoi(s.substr(start, end - start)));
                if (st.top()->left == NULL) st.top()->left = newNode;
                else st.top()->right = newNode;
                st.push(newNode);
            } else if (s[end] == ')') {
                st.pop();
            }
            end++;
        }
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. We iterate through the string once to construct the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. We use a stack to keep track of the nodes as we construct the tree.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the string once, and the space complexity is also linear because in the worst case, the stack can contain $n$ nodes.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a recursive approach to construct the tree.
- We will use a recursive function to construct the tree by parsing the string and creating nodes as we encounter them.

```cpp
class Solution {
public:
    TreeNode* str2tree(string s) {
        if (s.empty()) return NULL;
        int start = 0, end = 0;
        while (end < s.size() && s[end] != '(') end++;
        TreeNode* root = new TreeNode(stoi(s.substr(start, end - start)));
        if (end == s.size()) return root;
        start = end + 1;
        int count = 0;
        end = start;
        while (end < s.size()) {
            if (s[end] == '(') count++;
            if (s[end] == ')') count--;
            if (count == 0) break;
            end++;
        }
        if (start < end) root->left = str2tree(s.substr(start, end - start));
        start = end + 2;
        end = s.size() - 1;
        if (start < end) root->right = str2tree(s.substr(start, end - start + 1));
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. We iterate through the string once to construct the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. We use recursive calls to construct the tree.
> - **Optimality proof:** The time complexity is optimal because we must iterate through the string at least once to construct the tree. The space complexity is also optimal because we must use at least $n$ space to store the nodes of the tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: tree construction, recursive parsing, and stack-based parsing.
- Problem-solving patterns identified: parsing a string to construct a data structure.
- Optimization techniques learned: using recursive calls to reduce the space complexity.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not checking for invalid input.
- Edge cases to watch for: empty string, single node tree, balanced and unbalanced trees.
- Performance pitfalls: using excessive space or time complexity.
- Testing considerations: testing with different input sizes, testing with different tree structures.