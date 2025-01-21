## Merge BSTs to Create Single BST

**Problem Link:** https://leetcode.com/problems/merge-bsts-to-create-single-bst/description

**Problem Statement:**
- Input format and constraints: Given a list of Binary Search Trees (BSTs), merge them into a single BST.
- Expected output format: Return the root node of the merged BST.
- Key requirements and edge cases to consider: 
  - Each input BST is a valid BST.
  - The input list can be empty.
  - The merged BST should also be a valid BST.
- Example test cases with explanations: 
  - Merging two BSTs with non-overlapping ranges.
  - Merging two BSTs with overlapping ranges.
  - Merging an empty list of BSTs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by thinking about how to merge two BSTs. This can be done by performing an in-order traversal of both trees and merging the resulting sorted lists.
- Step-by-step breakdown of the solution:
  1. Perform an in-order traversal of each BST to get a sorted list of nodes.
  2. Merge the sorted lists into a single sorted list.
  3. Construct a new BST from the merged sorted list.
- Why this approach comes to mind first: It is a straightforward way to merge BSTs, leveraging the fact that in-order traversal of a BST yields a sorted list.

```cpp
// Function to perform in-order traversal and get a sorted list
void inOrder(TreeNode* root, vector<int>& sortedList) {
    if (root) {
        inOrder(root->left, sortedList);
        sortedList.push_back(root->val);
        inOrder(root->right, sortedList);
    }
}

// Function to merge two sorted lists
vector<int> mergeLists(vector<int>& list1, vector<int>& list2) {
    vector<int> mergedList;
    int i = 0, j = 0;
    while (i < list1.size() && j < list2.size()) {
        if (list1[i] < list2[j]) {
            mergedList.push_back(list1[i]);
            i++;
        } else {
            mergedList.push_back(list2[j]);
            j++;
        }
    }
    while (i < list1.size()) {
        mergedList.push_back(list1[i]);
        i++;
    }
    while (j < list2.size()) {
        mergedList.push_back(list2[j]);
        j++;
    }
    return mergedList;
}

// Function to construct a BST from a sorted list
TreeNode* sortedListToBST(vector<int>& sortedList) {
    if (sortedList.empty()) return nullptr;
    int mid = sortedList.size() / 2;
    TreeNode* root = new TreeNode(sortedList[mid]);
    vector<int> leftList(sortedList.begin(), sortedList.begin() + mid);
    vector<int> rightList(sortedList.begin() + mid + 1, sortedList.end());
    root->left = sortedListToBST(leftList);
    root->right = sortedListToBST(rightList);
    return root;
}

// Function to merge a list of BSTs
TreeNode* mergeBSTs(vector<TreeNode*>& bstList) {
    if (bstList.empty()) return nullptr;
    vector<int> mergedList;
    for (auto& bst : bstList) {
        vector<int> sortedList;
        inOrder(bst, sortedList);
        mergedList = mergeLists(mergedList, sortedList);
    }
    return sortedListToBST(mergedList);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the total number of nodes across all BSTs. This is because we perform an in-order traversal of each BST (which takes $O(N)$ time), and then merge the sorted lists (which takes $O(N \log N)$ time).
> - **Space Complexity:** $O(N)$, where $N$ is the total number of nodes across all BSTs. This is because we need to store the merged sorted list.
> - **Why these complexities occur:** The time complexity occurs because we need to perform an in-order traversal of each BST and merge the sorted lists. The space complexity occurs because we need to store the merged sorted list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can merge two BSTs by performing an in-order traversal of both trees and merging the resulting sorted lists. However, instead of constructing a new BST from the merged sorted list, we can directly construct the merged BST by recursively merging the left and right subtrees of the two BSTs.
- Detailed breakdown of the approach:
  1. Perform an in-order traversal of both BSTs to get two sorted lists.
  2. Merge the two sorted lists into a single sorted list.
  3. Directly construct the merged BST by recursively merging the left and right subtrees of the two BSTs.
- Proof of optimality: This approach is optimal because it avoids the overhead of constructing a new BST from the merged sorted list. Instead, it directly constructs the merged BST, which reduces the time complexity.

```cpp
// Function to merge two BSTs
TreeNode* mergeTwoBSTs(TreeNode* bst1, TreeNode* bst2) {
    if (!bst1) return bst2;
    if (!bst2) return bst1;
    
    if (bst1->val < bst2->val) {
        bst1->right = mergeTwoBSTs(bst1->right, bst2);
        return bst1;
    } else {
        bst2->left = mergeTwoBSTs(bst1, bst2->left);
        return bst2;
    }
}

// Function to merge a list of BSTs
TreeNode* mergeBSTs(vector<TreeNode*>& bstList) {
    if (bstList.empty()) return nullptr;
    TreeNode* mergedBST = bstList[0];
    for (int i = 1; i < bstList.size(); i++) {
        mergedBST = mergeTwoBSTs(mergedBST, bstList[i]);
    }
    return mergedBST;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of nodes across all BSTs. This is because we perform a constant amount of work for each node.
> - **Space Complexity:** $O(N)$, where $N$ is the total number of nodes across all BSTs. This is because we need to store the merged BST.
> - **Optimality proof:** This approach is optimal because it avoids the overhead of constructing a new BST from the merged sorted list. Instead, it directly constructs the merged BST, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Merging BSTs, in-order traversal, recursive construction of BSTs.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, using recursion to solve the sub-problems.
- Optimization techniques learned: Avoiding unnecessary overhead, using recursive construction to reduce time complexity.
- Similar problems to practice: Merging linked lists, constructing BSTs from sorted lists.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for null pointers.
- Edge cases to watch for: Empty lists of BSTs, BSTs with overlapping ranges.
- Performance pitfalls: Using inefficient algorithms, not optimizing for time complexity.
- Testing considerations: Testing with different inputs, testing for edge cases.