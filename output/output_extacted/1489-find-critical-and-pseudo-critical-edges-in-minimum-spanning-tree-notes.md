## Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
**Problem Link:** https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description

**Problem Statement:**
- Input format: `n` (number of nodes), `edges` (list of edges where each edge is a list of three integers `[u, v, w]` representing a weighted edge between nodes `u` and `v` with weight `w`)
- Constraints: `2 <= n <= 100`, `1 <= edges.length <= min(100, n * (n - 1) / 2)`, `0 <= u < n`, `0 <= v < n`, `0 <= w <= 10^5`, `u != v`
- Expected output format: Two lists of edge indices, one for critical edges and one for pseudo-critical edges
- Key requirements: Find edges in the minimum spanning tree (MST) of the graph that are critical (removing them increases the total weight of the MST) or pseudo-critical (removing them does not increase the total weight of the MST, but adding another edge of the same weight would make it critical)
- Example test cases:
  - Input: `n = 4`, `edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]`
  - Output: `[1, 2]`, `[]`
  - Explanation: Removing edge at index 1 or 2 increases the weight of the MST, but removing edge at index 0 or 3 does not.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each edge, remove it from the graph, calculate the MST without it, and compare the total weight with the original MST.
- Step-by-step breakdown:
  1. Calculate the original MST using Kruskal's algorithm.
  2. For each edge, remove it from the graph and calculate the new MST.
  3. Compare the total weights to determine if the edge is critical or pseudo-critical.
- Why this approach comes to mind first: It directly addresses the problem statement by simulating the removal of each edge and recalculating the MST.

```cpp
class Solution {
public:
    vector<int> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        // Original MST weight
        int originalWeight = kruskal(n, edges, -1, -1);
        
        vector<int> critical, pseudoCritical;
        
        for (int i = 0; i < edges.size(); ++i) {
            // Calculate MST weight without edge i
            int withoutWeight = kruskal(n, edges, -1, i);
            
            if (withoutWeight > originalWeight) {
                critical.push_back(i);
            } else {
                // Calculate MST weight with edge i as the first edge
                int withWeight = kruskal(n, edges, i, -1);
                
                if (withWeight == originalWeight) {
                    pseudoCritical.push_back(i);
                }
            }
        }
        
        return {critical, pseudoCritical};
    }
    
    int kruskal(int n, vector<vector<int>>& edges, int firstEdge, int skipEdge) {
        vector<int> parent(n), rank(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
        
        int weight = 0;
        
        // Add first edge if specified
        if (firstEdge != -1) {
            weight += edges[firstEdge][2];
            unionSet(parent, rank, edges[firstEdge][0], edges[firstEdge][1]);
        }
        
        // Sort edges by weight
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });
        
        for (int i = 0; i < edges.size(); ++i) {
            if (i == skipEdge) continue;
            
            if (!inSameSet(parent, edges[i][0], edges[i][1])) {
                weight += edges[i][2];
                unionSet(parent, rank, edges[i][0], edges[i][1]);
            }
        }
        
        return weight;
    }
    
    int findSet(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = findSet(parent, parent[x]);
        }
        return parent[x];
    }
    
    bool inSameSet(vector<int>& parent, int x, int y) {
        return findSet(parent, x) == findSet(parent, y);
    }
    
    void unionSet(vector<int>& parent, vector<int>& rank, int x, int y) {
        int rootX = findSet(parent, x);
        int rootY = findSet(parent, y);
        
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(E \cdot (E + V \log V))$ due to sorting and iterating over edges for each edge removal
> - **Space Complexity:** $O(V + E)$ for storing the graph and the disjoint set data structure
> - **Why these complexities occur:** The brute force approach involves recalculating the MST for each edge, which requires sorting and iterating over edges. The space complexity comes from storing the graph and the disjoint set data structure.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of recalculating the MST from scratch for each edge removal, we can use the original MST to guide our calculations and reduce the number of edges to consider.
- Detailed breakdown:
  1. Calculate the original MST using Kruskal's algorithm.
  2. For each edge in the original MST, remove it and calculate the MST weight without it.
  3. For each edge not in the original MST, add it to the original MST and calculate the new MST weight.
  4. Compare the weights to determine if an edge is critical or pseudo-critical.
- Proof of optimality: This approach reduces the number of MST calculations from $E$ (number of edges) to $V - 1$ (number of edges in the MST), significantly improving efficiency.

```cpp
class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        // Original MST weight
        int originalWeight = kruskal(n, edges);
        
        vector<int> critical, pseudoCritical;
        
        // Calculate MST weight without each edge in the MST
        for (int i = 0; i < edges.size(); ++i) {
            if (inMST(edges[i])) {
                int withoutWeight = kruskal(n, edges, i);
                
                if (withoutWeight > originalWeight) {
                    critical.push_back(i);
                }
            }
        }
        
        // Calculate MST weight with each edge not in the MST
        for (int i = 0; i < edges.size(); ++i) {
            if (!inMST(edges[i])) {
                int withWeight = kruskal(n, edges, -1, i);
                
                if (withWeight == originalWeight) {
                    pseudoCritical.push_back(i);
                }
            }
        }
        
        return {critical, pseudoCritical};
    }
    
    int kruskal(int n, vector<vector<int>>& edges, int skipEdge = -1, int addEdge = -1) {
        vector<int> parent(n), rank(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
        
        int weight = 0;
        
        // Add edge if specified
        if (addEdge != -1) {
            weight += edges[addEdge][2];
            unionSet(parent, rank, edges[addEdge][0], edges[addEdge][1]);
        }
        
        // Sort edges by weight
        sort(edges.begin(), edges.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });
        
        for (int i = 0; i < edges.size(); ++i) {
            if (i == skipEdge) continue;
            
            if (!inSameSet(parent, edges[i][0], edges[i][1])) {
                weight += edges[i][2];
                unionSet(parent, rank, edges[i][0], edges[i][1]);
            }
        }
        
        return weight;
    }
    
    bool inMST(const vector<vector<int>>& edges, const vector<int>& edge) {
        // Check if edge is in the MST
        for (const auto& e : edges) {
            if (e[0] == edge[0] && e[1] == edge[1] && e[2] == edge[2]) {
                return true;
            }
        }
        return false;
    }
    
    int findSet(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = findSet(parent, parent[x]);
        }
        return parent[x];
    }
    
    bool inSameSet(vector<int>& parent, int x, int y) {
        return findSet(parent, x) == findSet(parent, y);
    }
    
    void unionSet(vector<int>& parent, vector<int>& rank, int x, int y) {
        int rootX = findSet(parent, x);
        int rootY = findSet(parent, y);
        
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(E \log E)$ due to sorting edges
> - **Space Complexity:** $O(V + E)$ for storing the graph and the disjoint set data structure
> - **Optimality proof:** This approach reduces the number of MST calculations, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Kruskal's algorithm, disjoint set data structure
- Problem-solving patterns identified: Reducing the number of calculations by using the original MST as a guide
- Optimization techniques learned: Using the original MST to reduce the number of edges to consider
- Similar problems to practice: Minimum Spanning Tree, Union-Find algorithm

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the disjoint set data structure or Kruskal's algorithm
- Edge cases to watch for: Handling cases where an edge is not in the original MST or where an edge is critical or pseudo-critical
- Performance pitfalls: Not optimizing the number of MST calculations
- Testing considerations: Testing with different graph sizes and edge weights to ensure correctness and efficiency.