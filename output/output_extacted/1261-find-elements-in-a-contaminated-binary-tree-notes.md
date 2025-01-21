## Find Elements in a Contaminated Binary Tree

**Problem Link:** https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description

**Problem Statement:**
- Input format: A binary tree with unique values and a recovery array.
- Constraints: The binary tree has at most $10^4$ nodes.
- Expected output format: A boolean array indicating whether each value in the recovery array is present in the binary tree.
- Key requirements and edge cases to consider:
  - The binary tree may be empty.
  - The recovery array may be empty.
  - The values in the binary tree and recovery array are integers.
- Example test cases with explanations:
  - If the binary tree is empty, return an array of zeros for the recovery array.
  - If the recovery array is empty, return an empty array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the binary tree and check if each value in the recovery array is present.
- Step-by-step breakdown of the solution:
  1. Traverse the binary tree using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
  2. For each node in the tree, check if its value is present in the recovery array.
  3. If a value is found, mark the corresponding index in the output array as true.
- Why this approach comes to mind first: It is straightforward and easy to implement.

```cpp
class FindElements {
public:
    unordered_set<int> values;
    FindElements(TreeNode* root, vector<int>& recovery) {
        recoverTree(root, 0, recovery);
    }
    int recoverTree(TreeNode* node, int val, vector<int>& recovery) {
        if (!node) return 0;
        int left = recoverTree(node->left, val * 2 + 1, recovery);
        int right = recoverTree(node->right, val * 2 + 2, recovery);
        if (val == 0) {
            for (int i = 0; i < recovery.size(); i++) {
                values.insert(recovery[i]);
            }
        }
        return val;
    }
    bool find(int target) {
        return values.find(target) != values.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the tree and $m$ is the size of the recovery array. The reason for this is that we are doing a depth-first search of the tree, which takes $O(n)$ time, and then we are checking each value in the recovery array, which takes $O(m)$ time.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes in the tree and $m$ is the size of the recovery array. The reason for this is that in the worst case, we are storing all values from the tree and the recovery array in the `values` set.
> - **Why these complexities occur:** The time complexity occurs because we are doing a depth-first search of the tree and checking each value in the recovery array. The space complexity occurs because we are storing all values from the tree and the recovery array in the `values` set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using an unordered set to store the values, we can use a hash map to store the values and their corresponding indices in the recovery array.
- Detailed breakdown of the approach:
  1. Create a hash map to store the values and their corresponding indices.
  2. Traverse the binary tree using a depth-first search (DFS) algorithm.
  3. For each node in the tree, calculate its value and store it in the hash map.
  4. Create a boolean array to store the results.
  5. Iterate over the recovery array and check if each value is present in the hash map. If it is, mark the corresponding index in the boolean array as true.
- Proof of optimality: This solution has a time complexity of $O(n + m)$ and a space complexity of $O(n + m)$, which is optimal because we must traverse the tree and check each value in the recovery array.

```cpp
class FindElements {
public:
    unordered_map<int, bool> values;
    FindElements(TreeNode* root, vector<int>& recovery) {
        recoverTree(root, 0);
    }
    void recoverTree(TreeNode* node, int val) {
        if (!node) return;
        values[val] = true;
        recoverTree(node->left, val * 2 + 1);
        recoverTree(node->right, val * 2 + 2);
    }
    bool find(int target) {
        return values.find(target) != values.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the tree and $m$ is the size of the recovery array. The reason for this is that we are doing a depth-first search of the tree, which takes $O(n)$ time, and then we are checking each value in the recovery array, which takes $O(m)$ time.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes in the tree and $m$ is the size of the recovery array. The reason for this is that in the worst case, we are storing all values from the tree and the recovery array in the `values` map.
> - **Optimality proof:** This solution is optimal because we must traverse the tree and check each value in the recovery array, and we are doing so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), hash maps, and unordered sets.
- Problem-solving patterns identified: Using a hash map to store values and their corresponding indices, and using a boolean array to store the results.
- Optimization techniques learned: Using a hash map instead of an unordered set to store values, and using a boolean array instead of a hash map to store the results.
- Similar problems to practice: Problems that involve traversing a tree and checking values in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null pointers, not handling edge cases, and not using the correct data structures.
- Edge cases to watch for: Empty trees, empty recovery arrays, and duplicate values.
- Performance pitfalls: Using the wrong data structures, not optimizing the solution, and not handling edge cases correctly.
- Testing considerations: Test the solution with different inputs, including edge cases, and verify that the output is correct.