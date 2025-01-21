## Detonate the Maximum Bombs

**Problem Link:** https://leetcode.com/problems/detonate-the-maximum-bombs/description

**Problem Statement:**
- Input format: `bombs` - a list of pairs representing bomb locations and radii.
- Constraints: Each bomb is represented as a pair of three integers `[x, y, radius]`.
- Expected output format: The maximum number of bombs that can be detonated.
- Key requirements and edge cases to consider:
  - A bomb can detonate if its center is within the radius of another bomb.
  - A bomb can only be detonated once.
- Example test cases with explanations:
  - `[[2,1,3],[6,1,2]]` should return `2` because the first bomb can detonate the second.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every bomb against every other bomb to see if it's within the detonation radius.
- Step-by-step breakdown of the solution:
  1. Iterate through each bomb.
  2. For each bomb, check against all other bombs to see if any can detonate it.
  3. Keep track of the maximum number of bombs that can be detonated.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding the maximum number of detonatable bombs.

```cpp
int maximumDetonation(vector<vector<int>>& bombs) {
    int n = bombs.size();
    int maxDetonations = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> detonated;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                detonated.push_back(i);
            }
        }
        bool valid = true;
        for (int i = 0; i < detonated.size(); i++) {
            bool hasDetonator = false;
            for (int j = 0; j < detonated.size(); j++) {
                if (i != j && isWithinRadius(bombs[detonated[i]], bombs[detonated[j]])) {
                    hasDetonator = true;
                    break;
                }
            }
            if (!hasDetonator) {
                valid = false;
                break;
            }
        }
        if (valid) {
            maxDetonations = max(maxDetonations, (int)detonated.size());
        }
    }
    return maxDetonations;
}

bool isWithinRadius(vector<int>& bomb1, vector<int>& bomb2) {
    int dx = bomb1[0] - bomb2[0];
    int dy = bomb1[1] - bomb2[1];
    int distanceSquared = dx * dx + dy * dy;
    return distanceSquared <= bomb2[2] * bomb2[2];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of bombs. This is because we generate all possible subsets of bombs and for each subset, we check every pair of bombs.
> - **Space Complexity:** $O(n)$, for storing the current subset of detonated bombs.
> - **Why these complexities occur:** The brute force approach involves an exhaustive search through all possible subsets of bombs, leading to exponential time complexity. The space complexity is linear due to the storage needed for the current subset being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all subsets, we can use a graph where each bomb is a node, and two nodes are connected if one bomb can detonate another. Then, we find the maximum clique in this graph, as a clique represents a set of bombs where every bomb can be detonated by another.
- Detailed breakdown of the approach:
  1. Build the graph based on the detonation relationship between bombs.
  2. Find the maximum clique in the graph.
- Proof of optimality: This approach is optimal because it directly addresses the problem by identifying the largest set of bombs where every bomb can be detonated, which corresponds to the maximum clique in the graph.

```cpp
int maximumDetonation(vector<vector<int>>& bombs) {
    int n = bombs.size();
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && isWithinRadius(bombs[i], bombs[j])) {
                graph[i].push_back(j);
            }
        }
    }
    int maxCliqueSize = 0;
    vector<bool> visited(n, false);
    vector<int> currentClique;
    
    function<void(int)> backtrack = [&](int node) {
        visited[node] = true;
        currentClique.push_back(node);
        maxCliqueSize = max(maxCliqueSize, (int)currentClique.size());
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                backtrack(neighbor);
            }
        }
        
        currentClique.pop_back();
        visited[node] = false;
    };
    
    for (int i = 0; i < n; i++) {
        backtrack(i);
    }
    
    return maxCliqueSize;
}

bool isWithinRadius(vector<int>& bomb1, vector<int>& bomb2) {
    int dx = bomb1[0] - bomb2[0];
    int dy = bomb1[1] - bomb2[1];
    int distanceSquared = dx * dx + dy * dy;
    return distanceSquared <= bomb2[2] * bomb2[2];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, due to the recursive nature of the backtrack function exploring all possible cliques.
> - **Space Complexity:** $O(n)$, for the recursion stack and the current clique.
> - **Optimality proof:** This approach directly solves the problem by finding the maximum clique, ensuring that every bomb in the clique can be detonated by another, thus maximizing the number of detonated bombs.

---

### Final Notes

**Learning Points:**
- **Graph Theory:** The problem can be elegantly solved by applying graph theory concepts, specifically finding the maximum clique.
- **Backtracking:** The optimal solution utilizes a backtracking approach to explore all possible cliques in the graph.
- **Problem Reduction:** The key insight of reducing the problem to a maximum clique problem in a graph is crucial for achieving an optimal solution.

**Mistakes to Avoid:**
- **Inefficient Algorithms:** Avoid brute force approaches that lead to exponential time complexity without considering more efficient algorithms based on the problem's structure.
- **Incorrect Graph Construction:** Ensure that the graph is correctly constructed based on the detonation relationship between bombs.
- **Insufficient Testing:** Thoroughly test the solution with various inputs to ensure it handles all edge cases correctly.