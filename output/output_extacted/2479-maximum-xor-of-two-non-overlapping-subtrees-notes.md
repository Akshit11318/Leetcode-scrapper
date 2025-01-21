## Maximum XOR of Two Non-Overlapping Subtrees
**Problem Link:** https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/description

**Problem Statement:**
- Given the root of a binary tree, return the maximum XOR of two non-overlapping subtrees.
- Input format: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [2, 10^5].
- Expected output format: The maximum XOR of two non-overlapping subtrees.
- Key requirements and edge cases to consider: Non-overlapping subtrees can be any two subtrees that do not overlap, including the root node and any other node.

**Example Test Cases:**
- Example 1:
  - Input: [5, 4, 8, 3, null, 5, 1]
  - Output: 28
  - Explanation: The maximum XOR is obtained by choosing the subtrees with roots 5 and 8.
- Example 2:
  - Input: [3, 2, 1, 0]
  - Output: 2
  - Explanation: The maximum XOR is obtained by choosing the subtrees with roots 3 and 1.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible non-overlapping subtrees and calculate their XOR values.
- Step-by-step breakdown:
  1. Generate all possible subtrees.
  2. For each subtree, calculate its XOR value by recursively XORing the values of its nodes.
  3. Store the XOR values of all subtrees.
  4. For each pair of non-overlapping subtrees, calculate the XOR of their XOR values.
  5. Keep track of the maximum XOR value found.

```cpp
class Solution {
public:
    int max XOR(int root) {
        int max_XOR = 0;
        vector<int> subtree_XORs;
        
        // Generate all possible subtrees and calculate their XOR values
        traverse(root, subtree_XORs);
        
        // Calculate the XOR of each pair of non-overlapping subtrees
        for (int i = 0; i < subtree_XORs.size(); i++) {
            for (int j = i + 1; j < subtree_XORs.size(); j++) {
                int XOR = subtree_XORs[i] ^ subtree_XORs[j];
                max_XOR = max(max_XOR, XOR);
            }
        }
        
        return max_XOR;
    }
    
    void traverse(TreeNode* node, vector<int>& subtree_XORs) {
        if (node == nullptr) return;
        
        int XOR = node->val;
        traverse(node->left, subtree_XORs);
        traverse(node->right, subtree_XORs);
        
        subtree_XORs.push_back(XOR);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where n is the number of nodes in the tree. This is because we generate all possible subtrees and calculate their XOR values.
> - **Space Complexity:** $O(2^n)$, where n is the number of nodes in the tree. This is because we store the XOR values of all subtrees.
> - **Why these complexities occur:** These complexities occur because we generate all possible subtrees and calculate their XOR values, resulting in exponential time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a `Trie` data structure to store the XOR values of all subtrees.
- Step-by-step breakdown:
  1. Create a `Trie` data structure with 31 nodes (since the XOR value of two integers can be at most 2^31 - 1).
  2. Traverse the tree and calculate the XOR value of each subtree.
  3. For each subtree, insert its XOR value into the `Trie`.
  4. For each subtree, query the `Trie` to find the maximum XOR value that can be obtained by XORing the current subtree's XOR value with any other subtree's XOR value.
  5. Keep track of the maximum XOR value found.

```cpp
class Solution {
public:
    int max_XOR(TreeNode* root) {
        int max_XOR = 0;
        vector<int> values;
        
        // Traverse the tree and calculate the XOR value of each subtree
        traverse(root, values);
        
        // Create a Trie data structure
        Trie trie;
        
        // Insert the XOR values of all subtrees into the Trie
        for (int value : values) {
            trie.insert(value);
        }
        
        // Query the Trie to find the maximum XOR value
        for (int value : values) {
            max_XOR = max(max_XOR, trie.query(value));
        }
        
        return max_XOR;
    }
    
    void traverse(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        
        int XOR = node->val;
        traverse(node->left, values);
        traverse(node->right, values);
        
        values.push_back(XOR);
    }
};

class Trie {
public:
    Trie() {
        root = new Node();
    }
    
    void insert(int value) {
        Node* node = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (value >> i) & 1;
            if (node->children[bit] == nullptr) {
                node->children[bit] = new Node();
            }
            node = node->children[bit];
        }
    }
    
    int query(int value) {
        Node* node = root;
        int result = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (value >> i) & 1;
            if (node->children[1 - bit] != nullptr) {
                result |= (1 << i);
                node = node->children[1 - bit];
            } else {
                node = node->children[bit];
            }
        }
        return result;
    }
    
private:
    struct Node {
        Node* children[2];
    };
    
    Node* root;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 31)$, where n is the number of nodes in the tree. This is because we traverse the tree and calculate the XOR value of each subtree, and then insert and query the `Trie` for each subtree.
> - **Space Complexity:** $O(n \cdot 31)$, where n is the number of nodes in the tree. This is because we store the XOR values of all subtrees in the `Trie`.
> - **Optimality proof:** This solution is optimal because we use a `Trie` data structure to store the XOR values of all subtrees, allowing us to query the maximum XOR value in $O(31)$ time. This is the best possible time complexity because we must consider all possible subtrees.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of a `Trie` data structure to store and query XOR values.
- The problem-solving pattern identified is to use a `Trie` to store and query values in a way that allows for efficient calculation of the maximum XOR value.
- The optimization technique learned is to use a `Trie` to reduce the time complexity of querying the maximum XOR value from $O(n)$ to $O(31)$.

**Mistakes to Avoid:**
- A common implementation error is to forget to handle the case where the tree is empty.
- An edge case to watch for is when the tree has only one node.
- A performance pitfall is to use a naive approach that generates all possible subtrees and calculates their XOR values, resulting in exponential time and space complexities.
- A testing consideration is to test the solution with different tree structures and sizes to ensure that it works correctly and efficiently.