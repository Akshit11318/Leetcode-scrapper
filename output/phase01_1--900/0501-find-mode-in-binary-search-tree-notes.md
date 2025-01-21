## Find Mode in Binary Search Tree

**Problem Link:** https://leetcode.com/problems/find-mode-in-binary-search-tree/description

**Problem Statement:**
- Input format and constraints: The input is the root of a binary search tree.
- Expected output format: The output should be a vector of integers representing the mode(s) in the binary search tree.
- Key requirements and edge cases to consider: 
  - The mode is the value that appears most frequently in the tree.
  - If there are multiple modes, return all of them in any order.
  - The input tree is not guaranteed to be balanced.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [1, null, 2, 2]`
    - Output: `[2]`
  - Example 2: 
    - Input: `root = [0]`
    - Output: `[0]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform an in-order traversal of the binary search tree to get the values in ascending order, then count the frequency of each value.
- Step-by-step breakdown of the solution:
  1. Perform an in-order traversal of the binary search tree and store the values in a vector.
  2. Use a `map` to count the frequency of each value in the vector.
  3. Find the maximum frequency.
  4. Return all values with the maximum frequency.
- Why this approach comes to mind first: It is straightforward and easy to implement.

```cpp
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> values;
        // In-order traversal to get values in ascending order
        inOrderTraversal(root, values);
        
        map<int, int> frequency;
        for (int value : values) {
            frequency[value]++;
        }
        
        int maxFrequency = 0;
        for (auto& pair : frequency) {
            maxFrequency = max(maxFrequency, pair.second);
        }
        
        vector<int> modes;
        for (auto& pair : frequency) {
            if (pair.second == maxFrequency) {
                modes.push_back(pair.first);
            }
        }
        
        return modes;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, values);
        values.push_back(node->val);
        inOrderTraversal(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform an in-order traversal of the tree, which visits each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store all values in a vector.
> - **Why these complexities occur:** The time complexity occurs because we visit each node once during the in-order traversal. The space complexity occurs because we store all values in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can count the frequency of each value and keep track of the maximum frequency during the in-order traversal, eliminating the need to store all values.
- Detailed breakdown of the approach:
  1. Initialize a `map` to count the frequency of each value and a variable to keep track of the maximum frequency.
  2. Perform an in-order traversal of the binary search tree. During the traversal, increment the frequency of each value in the `map`.
  3. If the frequency of the current value is greater than the maximum frequency, update the maximum frequency and reset the modes vector to contain only the current value.
  4. If the frequency of the current value is equal to the maximum frequency, add the current value to the modes vector.
- Proof of optimality: This solution is optimal because it only visits each node once, resulting in a time complexity of $O(n)$.

```cpp
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> modes;
        int maxFrequency = 0;
        map<int, int> frequency;
        
        inOrderTraversal(root, modes, maxFrequency, frequency);
        
        return modes;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& modes, int& maxFrequency, map<int, int>& frequency) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, modes, maxFrequency, frequency);
        
        frequency[node->val]++;
        if (frequency[node->val] > maxFrequency) {
            maxFrequency = frequency[node->val];
            modes.clear();
            modes.push_back(node->val);
        } else if (frequency[node->val] == maxFrequency) {
            modes.push_back(node->val);
        }
        
        inOrderTraversal(node->right, modes, maxFrequency, frequency);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform an in-order traversal of the tree, which visits each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we might store all values in the `map` and the modes vector.
> - **Optimality proof:** The time complexity occurs because we visit each node once during the in-order traversal. The space complexity occurs because we store the frequency of each value in the `map` and the modes in the vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal, frequency counting, and mode finding.
- Problem-solving patterns identified: Using a `map` to count frequency and keeping track of the maximum frequency during traversal.
- Optimization techniques learned: Eliminating unnecessary storage by counting frequency and keeping track of the maximum frequency during traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `nullptr` during traversal, not updating the maximum frequency correctly.
- Edge cases to watch for: Empty tree, tree with a single node, tree with multiple modes.
- Performance pitfalls: Storing all values in a vector before counting frequency, not using a `map` to count frequency.
- Testing considerations: Test with different tree structures, including empty tree, tree with a single node, and tree with multiple modes.