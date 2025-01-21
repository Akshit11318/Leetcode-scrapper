## Minimum Edge Weight Equilibrium Queries in a Tree

**Problem Link:** https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description

**Problem Statement:**
- Input format and constraints: Given an undirected tree with `n` nodes and `n-1` edges, each edge has a weight. The task is to find the minimum edge weight that makes the tree *equilibrium*, which means that for every node, the sum of the weights of the edges going out of the node is greater than or equal to the sum of the weights of the edges going into the node. The input includes the number of nodes `n`, an adjacency list representation of the tree `edges`, and an array of queries `queries`.
- Expected output format: For each query, find the minimum edge weight to make the tree equilibrium.
- Key requirements and edge cases to consider: The tree is connected and undirected, each edge has a unique weight, and the queries are given as node indices.
- Example test cases with explanations: 
    - For example, if we have a tree with 3 nodes and edges [[0,1,1],[1,2,2]], to make the tree equilibrium, we need to find the minimum edge weight for each query.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate through all possible edge weights from the smallest to the largest, and for each edge weight, check if the tree is equilibrium.
- Step-by-step breakdown of the solution:
    1. Iterate through all possible edge weights.
    2. For each edge weight, iterate through all nodes and check if the tree is equilibrium by calculating the sum of the weights of the edges going out of the node and the sum of the weights of the edges going into the node.
    3. If the tree is equilibrium, return the current edge weight.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isEquilibrium(const vector<vector<int>>& edges, int weight, int query) {
    // Function to check if the tree is equilibrium
    vector<int> outDegree(edges.size(), 0);
    vector<int> inDegree(edges.size(), 0);
    
    for (const auto& edge : edges) {
        if (edge[2] >= weight) {
            outDegree[edge[0]]++;
            inDegree[edge[1]]++;
        }
    }
    
    for (int i = 0; i < edges.size(); i++) {
        if (outDegree[i] < inDegree[i]) {
            return false;
        }
    }
    
    return true;
}

vector<int> minEdgeWeight(const vector<vector<int>>& edges, const vector<int>& queries) {
    vector<int> result;
    
    for (int query : queries) {
        int minWeight = INT_MAX;
        
        for (int weight = 1; weight <= 1000; weight++) {
            if (isEquilibrium(edges, weight, query)) {
                minWeight = weight;
                break;
            }
        }
        
        result.push_back(minWeight);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot w)$, where $n$ is the number of nodes, $m$ is the number of edges, and $w$ is the maximum edge weight.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Why these complexities occur:** The time complexity is high because we iterate through all possible edge weights for each query, and for each edge weight, we check if the tree is equilibrium by iterating through all nodes and edges.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the minimum edge weight for each query.
- Detailed breakdown of the approach:
    1. Sort the edge weights in ascending order.
    2. For each query, use binary search to find the minimum edge weight that makes the tree equilibrium.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n \cdot m \cdot w)$ to $O(n \cdot m \cdot \log w)$.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isEquilibrium(const vector<vector<int>>& edges, int weight) {
    // Function to check if the tree is equilibrium
    vector<int> outDegree(edges.size(), 0);
    vector<int> inDegree(edges.size(), 0);
    
    for (const auto& edge : edges) {
        if (edge[2] >= weight) {
            outDegree[edge[0]]++;
            inDegree[edge[1]]++;
        }
    }
    
    for (int i = 0; i < edges.size(); i++) {
        if (outDegree[i] < inDegree[i]) {
            return false;
        }
    }
    
    return true;
}

int binarySearch(const vector<vector<int>>& edges, int low, int high) {
    while (low < high) {
        int mid = low + (high - low) / 2;
        
        if (isEquilibrium(edges, mid)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    
    return low;
}

vector<int> minEdgeWeight(const vector<vector<int>>& edges, const vector<int>& queries) {
    vector<int> result;
    
    for (int query : queries) {
        int minWeight = binarySearch(edges, 1, 1000);
        result.push_back(minWeight);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log w)$, where $n$ is the number of nodes, $m$ is the number of edges, and $w$ is the maximum edge weight.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n \cdot m \cdot w)$ to $O(n \cdot m \cdot \log w)$ using binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, graph traversal.
- Problem-solving patterns identified: reducing time complexity using binary search.
- Optimization techniques learned: using binary search to reduce time complexity.
- Similar problems to practice: finding the minimum edge weight in a graph, finding the maximum flow in a network.

**Mistakes to Avoid:**
- Common implementation errors: incorrect implementation of binary search, incorrect calculation of edge weights.
- Edge cases to watch for: handling cases where the tree is not connected, handling cases where the edge weights are not unique.
- Performance pitfalls: using a brute force approach instead of binary search, not optimizing the implementation for large inputs.
- Testing considerations: testing the implementation with different inputs, testing the implementation with edge cases.