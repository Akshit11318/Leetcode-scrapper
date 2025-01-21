## Number of Provinces

**Problem Link:** https://leetcode.com/problems/number-of-provinces/description

**Problem Statement:**
- Input format: An integer `n` and an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if there is a direct connection between city `i` and city `j`, otherwise `isConnected[i][j] = 0`.
- Constraints: `1 <= n <= 200`, `isConnected[i][j]` is `0` or `1`, `isConnected[i][i] = 1`, `isConnected[i][j] = isConnected[j][i]`.
- Expected output format: The number of provinces (connected components) in the graph.
- Key requirements and edge cases to consider: Handling disconnected graphs, ensuring all nodes are visited, and counting connected components accurately.
- Example test cases with explanations: 
    - For `n = 5` and `isConnected = [[1,1,0],[1,1,0],[0,0,1]]`, the output is `2` because there are two provinces (connected components) in the graph.
    - For `n = 6` and `isConnected = [[1,0,0,1,0],[0,1,0,0,0],[0,0,1,0,0],[1,0,0,1,0],[0,0,0,0,1]]`, the output is `3` because there are three provinces in the graph.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all cities and perform a depth-first search (DFS) from each unvisited city to find all connected components.
- Step-by-step breakdown of the solution:
    1. Initialize a set `visited` to keep track of visited cities.
    2. Initialize a counter `provinces` to count the number of provinces (connected components).
    3. Iterate over all cities. For each unvisited city, perform a DFS to mark all connected cities as visited and increment the `provinces` counter.
- Why this approach comes to mind first: It's a straightforward method to ensure all nodes are visited and to identify connected components by exploring the graph from each node.

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int provinces = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, visited, i);
                provinces++;
            }
        }
        
        return provinces;
    }
    
    void dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int city) {
        visited[city] = true;
        for (int i = 0; i < isConnected.size(); i++) {
            if (isConnected[city][i] == 1 && !visited[i]) {
                dfs(isConnected, visited, i);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cities. This is because in the worst case, we might need to perform DFS from each city, and each DFS could potentially visit every city.
> - **Space Complexity:** $O(n)$, for the `visited` vector and the recursion stack in the worst case.
> - **Why these complexities occur:** The brute force approach involves iterating over all cities and potentially performing DFS from each one, leading to quadratic time complexity. The space complexity is linear due to the need to track visited cities and the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a **Union-Find** (Disjoint-Set) algorithm, which is more efficient for finding connected components in a graph.
- Detailed breakdown of the approach:
    1. Initialize the Union-Find data structure with each city as its own set.
    2. Iterate over the `isConnected` matrix. For each pair of connected cities, union their sets.
    3. Count the number of distinct sets (connected components) in the Union-Find data structure.
- Proof of optimality: Union-Find has an average time complexity of $O(\alpha(n))$ per operation, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly. Thus, it's nearly constant time for practical purposes.

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    unionSets(parent, i, j);
                }
            }
        }
        
        set<int> distinctSets;
        for (int i = 0; i < n; i++) {
            distinctSets.insert(findSet(parent, i));
        }
        
        return distinctSets.size();
    }
    
    int findSet(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = findSet(parent, parent[x]);
        }
        return parent[x];
    }
    
    void unionSets(vector<int>& parent, int x, int y) {
        int rootX = findSet(parent, x);
        int rootY = findSet(parent, y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function. For practical purposes, this is nearly $O(n^2)$, but the $\alpha(n)$ term makes it slightly better than the brute force approach for very large inputs.
> - **Space Complexity:** $O(n)$, for the `parent` vector and the set to store distinct sets.
> - **Optimality proof:** The Union-Find algorithm is highly efficient for this type of problem, especially when dealing with a large number of elements and operations. The use of path compression and union by rank (not implemented here for simplicity) can further optimize the algorithm.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), Union-Find (Disjoint-Set) algorithm.
- Problem-solving patterns identified: Iterating over all elements, using data structures to keep track of visited or connected components.
- Optimization techniques learned: Using more efficient algorithms like Union-Find for finding connected components.
- Similar problems to practice: Finding connected components in a graph, clustering problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as disconnected graphs or self-loops.
- Edge cases to watch for: Empty graphs, graphs with a single node, fully connected graphs.
- Performance pitfalls: Using brute force approaches for large inputs, not optimizing the algorithm for the specific problem constraints.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and performance.