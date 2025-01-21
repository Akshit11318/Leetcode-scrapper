## Greatest Common Divisor Traversal
**Problem Link:** https://leetcode.com/problems/greatest-common-divisor-traversal/description

**Problem Statement:**
- Input format and constraints: Given a binary tree where each node contains an integer, find the greatest common divisor (GCD) of all node values in the tree.
- Expected output format: Return the GCD of all node values in the tree.
- Key requirements and edge cases to consider: 
  - The tree may be empty.
  - The tree may contain duplicate values.
  - The GCD of a single number is the number itself.
- Example test cases with explanations:
  - If the tree is empty, return 0.
  - If the tree contains a single node with value 5, return 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: First, traverse the tree to collect all node values, then calculate the GCD of these values.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) or breadth-first search (BFS) to collect all node values in a vector.
  2. Use the Euclidean algorithm to find the GCD of the first two numbers in the vector.
  3. Iterate through the rest of the vector, updating the GCD with each number using the Euclidean algorithm.
- Why this approach comes to mind first: It is straightforward and ensures that we consider all node values.

```cpp
class Solution {
public:
    int gcdTraversal(TreeNode* root) {
        vector<int> values;
        dfs(root, values);
        if (values.empty()) return 0;
        int gcd = values[0];
        for (int i = 1; i < values.size(); i++) {
            gcd = calculateGCD(gcd, values[i]);
        }
        return gcd;
    }
    
    void dfs(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        values.push_back(node->val);
        dfs(node->left, values);
        dfs(node->right, values);
    }
    
    int calculateGCD(int a, int b) {
        if (b == 0) return a;
        return calculateGCD(b, a % b);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(m))$ where $n$ is the number of nodes in the tree and $m$ is the maximum value in the tree. This is because we perform a DFS traversal ($O(n)$) and then calculate the GCD of each pair of numbers ($O(log(m))$).
> - **Space Complexity:** $O(n)$ for storing the node values in the vector.
> - **Why these complexities occur:** The time complexity is dominated by the GCD calculation, which involves the Euclidean algorithm. The space complexity is due to storing all node values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the GCD of all node values as we traverse the tree, rather than storing all values and calculating the GCD afterwards.
- Detailed breakdown of the approach:
  1. Perform a DFS traversal of the tree, maintaining a running GCD of the node values encountered so far.
  2. At each node, update the running GCD using the Euclidean algorithm.
- Proof of optimality: This approach is optimal because it avoids storing all node values, reducing the space complexity to $O(h)$ where $h$ is the height of the tree.

```cpp
class Solution {
public:
    int gcdTraversal(TreeNode* root) {
        int gcd = 0;
        dfs(root, gcd);
        return gcd;
    }
    
    void dfs(TreeNode* node, int& gcd) {
        if (node == nullptr) return;
        if (gcd == 0) gcd = node->val;
        else gcd = calculateGCD(gcd, node->val);
        dfs(node->left, gcd);
        dfs(node->right, gcd);
    }
    
    int calculateGCD(int a, int b) {
        if (b == 0) return a;
        return calculateGCD(b, a % b);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(m))$ where $n$ is the number of nodes in the tree and $m$ is the maximum value in the tree. This is because we perform a DFS traversal ($O(n)$) and calculate the GCD at each node ($O(log(m))$).
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it minimizes both time and space complexity by calculating the GCD on the fly and avoiding unnecessary storage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, Euclidean algorithm for GCD calculation.
- Problem-solving patterns identified: Optimizing space complexity by calculating results on the fly.
- Optimization techniques learned: Avoiding unnecessary storage, using recursive functions to minimize space usage.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of an empty tree, incorrectly implementing the Euclidean algorithm.
- Edge cases to watch for: Trees with duplicate values, trees with a single node.
- Performance pitfalls: Storing all node values before calculating the GCD, which can lead to high space complexity.
- Testing considerations: Test with trees of varying sizes and structures, including edge cases like empty trees or trees with a single node.