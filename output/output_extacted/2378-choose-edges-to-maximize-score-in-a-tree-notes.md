## Choose Edges to Maximize Score in a Tree

**Problem Link:** https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/description

**Problem Statement:**
- Given a tree with `n` nodes and a list of edges with their corresponding scores, choose a subset of edges to include in the tree to maximize the total score.
- The input format includes the number of nodes `n` and a list of edges `edges`, where each edge is represented as a tuple `(u, v, score)`.
- The expected output is the maximum total score that can be achieved by choosing a subset of edges.
- Key requirements and edge cases to consider include handling the case where the input tree is empty or has only one node, and ensuring that the chosen subset of edges forms a connected tree.

**Example Test Cases:**
- For `n = 5` and `edges = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (1, 4, 5)]`, the maximum total score is `14`, achieved by choosing edges `(0, 1, 2)`, `(0, 2, 3)`, and `(1, 4, 5)`.
- For `n = 4` and `edges = [(0, 1, 1), (0, 2, 2), (0, 3, 3)]`, the maximum total score is `6`, achieved by choosing edges `(0, 1, 1)`, `(0, 2, 2)`, and `(0, 3, 3)`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible subsets of edges to find the one that maximizes the total score.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of edges.
  2. For each subset, check if the subset of edges forms a connected tree.
  3. If it does, calculate the total score for the subset.
  4. Keep track of the maximum total score found so far.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions, but it has an exponential time complexity due to generating all possible subsets.

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& edges, int n) {
        // Generate all possible subsets of edges
        int numEdges = edges.size();
        int maxScore = 0;
        for (int mask = 0; mask < (1 << numEdges); mask++) {
            vector<vector<int>> subset;
            for (int i = 0; i < numEdges; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.push_back(edges[i]);
                }
            }
            // Check if the subset of edges forms a connected tree
            if (isConnected(subset, n)) {
                int score = calculateScore(subset);
                maxScore = max(maxScore, score);
            }
        }
        return maxScore;
    }
    
    bool isConnected(vector<vector<int>>& subset, int n) {
        // Check if the subset of edges forms a connected tree
        vector<int> parent(n, -1);
        for (auto& edge : subset) {
            int u = edge[0], v = edge[1];
            if (find(parent, u) == find(parent, v)) {
                return false; // Cycle detected
            }
            unionSets(parent, u, v);
        }
        // Check if all nodes are connected
        for (int i = 0; i < n; i++) {
            if (find(parent, i) != find(parent, 0)) {
                return false;
            }
        }
        return true;
    }
    
    int calculateScore(vector<vector<int>>& subset) {
        int score = 0;
        for (auto& edge : subset) {
            score += edge[2];
        }
        return score;
    }
    
    int find(vector<int>& parent, int x) {
        if (parent[x] == -1) {
            return x;
        }
        return find(parent, parent[x]);
    }
    
    void unionSets(vector<int>& parent, int u, int v) {
        int rootU = find(parent, u);
        int rootV = find(parent, v);
        parent[rootU] = rootV;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{numEdges} \cdot n)$, where $numEdges$ is the number of edges and $n$ is the number of nodes.
> - **Space Complexity:** $O(n + numEdges)$, for storing the subset of edges and the parent array.
> - **Why these complexities occur:** The time complexity is exponential due to generating all possible subsets of edges, and the space complexity is linear due to storing the subset of edges and the parent array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a greedy approach with a priority queue to choose the edges with the highest scores first.
- Detailed breakdown of the approach:
  1. Sort the edges in non-increasing order of their scores.
  2. Initialize a disjoint-set data structure to keep track of the connected components.
  3. Iterate over the sorted edges and add each edge to the result if it does not form a cycle.
- Proof of optimality: The greedy approach ensures that the maximum total score is achieved by choosing the edges with the highest scores first.
- Why further optimization is impossible: The time complexity of the optimal approach is $O(numEdges \log numEdges + numEdges \alpha(n))$, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& edges, int n) {
        // Sort the edges in non-increasing order of their scores
        sort(edges.begin(), edges.end(), [](vector<int>& a, vector<int>& b) {
            return a[2] > b[2];
        });
        
        // Initialize a disjoint-set data structure
        vector<int> parent(n, -1);
        
        int score = 0;
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            if (find(parent, u) != find(parent, v)) {
                unionSets(parent, u, v);
                score += edge[2];
            }
        }
        return score;
    }
    
    int find(vector<int>& parent, int x) {
        if (parent[x] == -1) {
            return x;
        }
        return find(parent, parent[x]);
    }
    
    void unionSets(vector<int>& parent, int u, int v) {
        int rootU = find(parent, u);
        int rootV = find(parent, v);
        parent[rootU] = rootV;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(numEdges \log numEdges + numEdges \alpha(n))$, where $numEdges$ is the number of edges and $n$ is the number of nodes.
> - **Space Complexity:** $O(n + numEdges)$, for storing the disjoint-set data structure and the edges.
> - **Optimality proof:** The greedy approach ensures that the maximum total score is achieved by choosing the edges with the highest scores first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy approach, disjoint-set data structure, sorting.
- Problem-solving patterns identified: using a priority queue to choose the edges with the highest scores first.
- Optimization techniques learned: using a disjoint-set data structure to keep track of the connected components.
- Similar problems to practice: minimum spanning tree, maximum flow.

**Mistakes to Avoid:**
- Common implementation errors: not checking for cycles when adding edges to the result.
- Edge cases to watch for: handling the case where the input tree is empty or has only one node.
- Performance pitfalls: using an exponential-time algorithm to generate all possible subsets of edges.
- Testing considerations: testing the algorithm with different input sizes and edge cases to ensure correctness and efficiency.