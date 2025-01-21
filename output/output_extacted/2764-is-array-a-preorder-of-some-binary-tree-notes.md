## Is Array a Preorder of Some Binary Search Tree
**Problem Link:** https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/description

**Problem Statement:**
- Input format: An array of integers representing a preorder traversal of a binary search tree.
- Constraints: The array can contain unique integers.
- Expected output format: A boolean indicating whether the given array can represent a preorder traversal of some binary search tree.
- Key requirements: The tree must be a binary search tree, meaning for every node, all elements in its left subtree must be less than the node, and all elements in its right subtree must be greater.
- Edge cases: Empty array, array with one element, arrays that cannot form a binary search tree.

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible binary trees and check if any of them match the given preorder traversal when traversed in preorder.
- However, this is highly inefficient due to the exponential number of possible trees.
- A more refined brute force approach would involve trying to construct a binary search tree by iterating through the array and ensuring that at each step, we can add a node to the tree without violating the binary search tree property.

```cpp
bool verifyPreorder(vector<int>& preorder) {
    stack<int> s;
    int lower = INT_MIN;
    for (int x : preorder) {
        if (x < lower) return false;
        while (!s.empty() && x > s.top()) {
            lower = s.top();
            s.pop();
        }
        s.push(x);
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array, because each element is pushed and popped from the stack exactly once.
> - **Space Complexity:** $O(n)$ for the stack in the worst case, when the tree is skewed to one side.
> - **Why these complexities occur:** The time complexity is linear because we process each element in the array once. The space complexity is also linear due to the use of the stack to keep track of the nodes.

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is to use a stack to keep track of the nodes that we have seen so far but have not yet found a right child for.
- We start with the root node and push it onto the stack.
- Then, we iterate through the rest of the array. If the current element is less than the top of the stack, we push it onto the stack (because it could be a left child of the top of the stack).
- If the current element is greater than the top of the stack, we pop the stack until we find a node that is greater than the current element or the stack is empty. This process ensures that we maintain the binary search tree property.
- If at any point we try to add a node to the left of a node that is already in the stack (i.e., the current element is less than the lower bound), we return false.

```cpp
bool verifyPreorder(vector<int>& preorder) {
    stack<int> s;
    int lower = INT_MIN;
    for (int x : preorder) {
        if (x < lower) return false;
        while (!s.empty() && x > s.top()) {
            lower = s.top();
            s.pop();
        }
        s.push(x);
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$ for the stack in the worst case.
> - **Optimality proof:** This is optimal because we must at least look at each element in the array once to determine if it can form a valid preorder traversal of a binary search tree.

### Final Notes

**Learning Points:**
- Using a stack to keep track of nodes that we have seen but not yet found a right child for.
- Maintaining the binary search tree property by ensuring that all elements to the left of a node are less than the node and all elements to the right are greater.
- The importance of considering the lower bound when adding new nodes to the tree.

**Mistakes to Avoid:**
- Not checking for the lower bound when adding new nodes, which can lead to incorrect results.
- Not properly handling the case where the stack is empty, which can cause errors.
- Failing to consider the binary search tree property when constructing the tree.