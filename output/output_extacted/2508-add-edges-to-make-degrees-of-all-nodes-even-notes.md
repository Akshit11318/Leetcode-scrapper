## Add Edges to Make Degrees of All Nodes Even
**Problem Link:** https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/description

**Problem Statement:**
- Input: `n` (number of nodes), `edges` (list of edges)
- Constraints: `1 <= n <= 10^5`, `0 <= edges.length <= 10^5`, `edges[i].length == 2`, `0 <= edges[i][0] <= edges[i][1] < n`, no self-loops or parallel edges
- Expected output: A list of edges to add to make all node degrees even, or an empty list if it's impossible
- Key requirements: All node degrees must be even after adding edges
- Example test cases:
  - `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4]]`: Return `[[0,4]]` or `[[1,3]]` or `[[1,4]]`
  - `n = 4`, `edges = [[1,0],[3,1]]`: Return `[]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible edges and check if adding them makes all node degrees even
- Step-by-step breakdown:
  1. Initialize a list to store the edges to add
  2. Iterate over all possible edges
  3. For each edge, check if adding it makes all node degrees even
  4. If it does, add it to the list
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient

```cpp
vector<vector<int>> addEdgesToMakeDegreesEven(int n, vector<vector<int>>& edges) {
    vector<vector<int>> result;
    vector<int> degrees(n, 0);
    
    // Calculate initial degrees
    for (auto& edge : edges) {
        degrees[edge[0]]++;
        degrees[edge[1]]++;
    }
    
    // Try all possible edges
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            // Create a copy of the degrees array
            vector<int> newDegrees = degrees;
            
            // Add the edge
            newDegrees[i]++;
            newDegrees[j]++;
            
            // Check if all degrees are even
            bool allEven = true;
            for (int k = 0; k < n; k++) {
                if (newDegrees[k] % 2 != 0) {
                    allEven = false;
                    break;
                }
            }
            
            // If all degrees are even, add the edge to the result
            if (allEven) {
                result.push_back({i, j});
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ (iterating over all possible edges and checking if all degrees are even)
> - **Space Complexity:** $O(n)$ (storing the degrees array)
> - **Why these complexities occur:** The brute force approach tries all possible edges, which leads to a high time complexity. The space complexity is relatively low since we only need to store the degrees array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a graph theory concept called "odd-degree nodes". A graph has an even number of odd-degree nodes. We can pair these nodes and add edges between them to make all degrees even.
- Detailed breakdown:
  1. Calculate the initial degrees of all nodes
  2. Identify the odd-degree nodes
  3. Pair these nodes and add edges between them
- Proof of optimality: This approach is optimal because it directly addresses the problem by identifying and pairing odd-degree nodes, which is the minimum number of edges needed to make all degrees even.

```cpp
vector<vector<int>> addEdgesToMakeDegreesEven(int n, vector<vector<int>>& edges) {
    vector<vector<int>> result;
    vector<int> degrees(n, 0);
    
    // Calculate initial degrees
    for (auto& edge : edges) {
        degrees[edge[0]]++;
        degrees[edge[1]]++;
    }
    
    // Identify odd-degree nodes
    vector<int> oddNodes;
    for (int i = 0; i < n; i++) {
        if (degrees[i] % 2 != 0) {
            oddNodes.push_back(i);
        }
    }
    
    // Pair odd-degree nodes and add edges
    for (int i = 0; i < oddNodes.size(); i += 2) {
        if (i + 1 < oddNodes.size()) {
            result.push_back({oddNodes[i], oddNodes[i + 1]});
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ (calculating degrees and identifying odd-degree nodes)
> - **Space Complexity:** $O(n)$ (storing the degrees array and odd-degree nodes)
> - **Optimality proof:** This approach is optimal because it directly addresses the problem by identifying and pairing odd-degree nodes, which is the minimum number of edges needed to make all degrees even.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph theory, odd-degree nodes
- Problem-solving patterns identified: Identifying and pairing odd-degree nodes
- Optimization techniques learned: Directly addressing the problem by identifying and pairing odd-degree nodes
- Similar problems to practice: Other graph theory problems involving degree sequences

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty graph or a graph with no odd-degree nodes
- Edge cases to watch for: An empty graph or a graph with no odd-degree nodes
- Performance pitfalls: Using a brute force approach, which can lead to high time complexity
- Testing considerations: Testing the implementation with different graph structures and edge cases.