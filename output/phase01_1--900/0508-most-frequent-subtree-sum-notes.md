## Most Frequent Subtree Sum

**Problem Link:** https://leetcode.com/problems/most-frequent-subtree-sum/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a unique integer value.
- Output: The most frequent subtree sum. If there are multiple sums with the same highest frequency, return all of them.
- Key Requirements: Calculate the sum of each subtree and find the sum(s) with the highest frequency.
- Edge Cases: Empty tree, tree with a single node, trees with multiple nodes but no repeated sums, trees with multiple repeated sums.

**Example Test Cases:**
- Test Case 1: A tree with nodes [5, 2, -3]. The subtree sums are [2], [5], [5 + 2 + -3] = [5, 2, 4]. The most frequent sum is [2, 4, 5] as each occurs once, and there are no more frequent sums.
- Test Case 2: A tree with nodes [5, 2, -5]. The subtree sums are [2], [-5], [5 + 2 + -5] = [2, -5, 2]. The most frequent sum is [2] since it occurs twice, which is more than any other sum.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the sum of each subtree and store these sums in a `map` or a frequency table to track how often each sum occurs.
- Then, iterate through the tree to calculate the sum of each subtree by recursively summing the values of the current node and its children.
- Finally, update the frequency table with each calculated sum and find the maximum frequency.

```cpp
#include <iostream>
#include <map>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        map<int, int> sumFrequency;
        int maxFrequency = 0;
        
        // Function to calculate subtree sum and update frequency
        function<void(TreeNode*)> calculateSubtreeSum = [&](TreeNode* node) {
            if (!node) return;
            
            int sum = node->val;
            if (node->left) {
                calculateSubtreeSum(node->left);
                sum += leftSum;
            }
            if (node->right) {
                calculateSubtreeSum(node->right);
                sum += rightSum;
            }
            
            sumFrequency[sum]++;
            maxFrequency = max(maxFrequency, sumFrequency[sum]);
        };
        
        // Initialize leftSum and rightSum for calculation
        int leftSum = 0, rightSum = 0;
        
        calculateSubtreeSum(root);
        
        vector<int> result;
        for (auto& pair : sumFrequency) {
            if (pair.second == maxFrequency) {
                result.push_back(pair.first);
            }
        }
        
        return result;
    }
    
private:
    int leftSum = 0, rightSum = 0;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree because we visit each node once to calculate its subtree sum.
> - **Space Complexity:** $O(n)$ for storing the frequency of each sum in the `map`.
> - **Why these complexities occur:** The time complexity is linear because we recursively visit each node once. The space complexity is also linear because in the worst case, every node could have a unique sum, requiring space to store each unique sum in the frequency table.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using a depth-first search (DFS) to calculate the sum of each subtree and update a frequency map simultaneously.
- We use a recursive function to calculate the sum of each subtree and update the frequency map.
- After calculating all subtree sums, we find the maximum frequency and return all sums that have this maximum frequency.

```cpp
class Solution {
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        map<int, int> sumFrequency;
        int maxFrequency = 0;
        
        function<int(TreeNode*)> dfs = [&](TreeNode* node) {
            if (!node) return 0;
            
            int sum = node->val + dfs(node->left) + dfs(node->right);
            sumFrequency[sum]++;
            maxFrequency = max(maxFrequency, sumFrequency[sum]);
            return sum;
        };
        
        dfs(root);
        
        vector<int> result;
        for (auto& pair : sumFrequency) {
            if (pair.second == maxFrequency) {
                result.push_back(pair.first);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree because we visit each node once during the DFS.
> - **Space Complexity:** $O(n)$ for storing the frequency of each sum in the `map` and the recursive call stack.
> - **Optimality proof:** This approach is optimal because we only visit each node once and use a single pass through the tree to calculate all subtree sums and their frequencies, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), recursive tree traversal, frequency counting.
- Problem-solving patterns identified: Calculating subtree sums, tracking frequencies, finding maximum frequency.
- Optimization techniques learned: Minimizing the number of tree traversals, using a single pass to calculate subtree sums and their frequencies.

**Mistakes to Avoid:**
- Not correctly handling the base case for recursive functions (e.g., returning 0 for empty trees).
- Failing to update the maximum frequency as new sums are calculated.
- Not considering all possible subtree sums, especially when a node has no children.