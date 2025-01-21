## Smallest Missing Genetic Value in Each Subtree

**Problem Link:** https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/description

**Problem Statement:**
- Input format and constraints: Given a tree with `n` nodes, where each node `i` has a genetic value `genetic[i]`.
- Expected output format: Return an array `ans` of length `n`, where `ans[i]` is the smallest missing genetic value in the subtree rooted at node `i`.
- Key requirements and edge cases to consider: 
    * The tree is represented as a graph where `edges` is a list of edges, where `edges[i] = [ai, bi]` means there is an edge between nodes `ai` and `bi`.
    * The tree is connected and undirected.
    * Genetic values are in the range `[1, n]`.
- Example test cases with explanations: 
    * Example 1:
        + Input: `n = 5`, `edges = [[0,1],[0,2],[3,4]]`, `genetic = [1,2,3,4,5]`
        + Output: `[1,1,2,1,1]`
        + Explanation: The smallest missing genetic value in each subtree is 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each node, iterate through all possible genetic values and check if it is present in the subtree.
- Step-by-step breakdown of the solution:
    1. Create a function to perform DFS and find the smallest missing genetic value in a subtree.
    2. For each node, perform DFS and keep track of the genetic values present in the subtree.
    3. Iterate through all possible genetic values and return the smallest one that is not present in the subtree.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has high time complexity due to the nested loops.

```cpp
class Solution {
public:
    vector<int> smallestMissingValueSubtree(vector<vector<int>>& edges, vector<int>& genetic) {
        int n = genetic.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            vector<bool> present(n + 1);
            dfs(i, -1, graph, genetic, present);
            for (int j = 1; j <= n; j++) {
                if (!present[j]) {
                    ans[i] = j;
                    break;
                }
            }
        }
        return ans;
    }
    
    void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& genetic, vector<bool>& present) {
        present[genetic[node]] = true;
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(child, node, graph, genetic, present);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because for each node, we are performing DFS and iterating through all possible genetic values.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the present genetic values for each node.
> - **Why these complexities occur:** The high time complexity occurs due to the nested loops, and the space complexity occurs due to the storage of present genetic values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a set to store the genetic values present in the subtree, and then find the smallest missing genetic value by iterating through the set.
- Detailed breakdown of the approach:
    1. Create a function to perform DFS and find the smallest missing genetic value in a subtree.
    2. For each node, perform DFS and keep track of the genetic values present in the subtree using a set.
    3. Find the smallest missing genetic value by iterating through the set.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we need to visit each node at least once to find the smallest missing genetic value.
- Why further optimization is impossible: We cannot do better than $O(n)$ time complexity because we need to visit each node at least once.

```cpp
class Solution {
public:
    vector<int> smallestMissingValueSubtree(vector<vector<int>>& edges, vector<int>& genetic) {
        int n = genetic.size();
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            unordered_set<int> present;
            dfs(i, -1, graph, genetic, present);
            int missing = 1;
            while (present.count(missing)) {
                missing++;
            }
            ans[i] = missing;
        }
        return ans;
    }
    
    void dfs(int node, int parent, vector<vector<int>>& graph, vector<int>& genetic, unordered_set<int>& present) {
        present.insert(genetic[node]);
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(child, node, graph, genetic, present);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are performing DFS and iterating through the set of genetic values.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we need to store the present genetic values for each node.
> - **Optimality proof:** This approach is optimal because we need to visit each node at least once to find the smallest missing genetic value.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, set operations.
- Problem-solving patterns identified: Using a set to store present genetic values and finding the smallest missing genetic value.
- Optimization techniques learned: Using a set instead of a vector to store present genetic values.
- Similar problems to practice: Other problems that involve finding the smallest missing value in a set.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the smallest missing genetic value is greater than the number of nodes.
- Edge cases to watch for: The case where the input tree is empty.
- Performance pitfalls: Using a vector instead of a set to store present genetic values.
- Testing considerations: Testing the function with different input trees and genetic values.