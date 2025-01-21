## Frog Position After T Seconds
**Problem Link:** https://leetcode.com/problems/frog-position-after-t-seconds/description

**Problem Statement:**
- Given a tree where each node represents a city and each edge represents a road, find the probability that a frog starts at a given city and jumps to a neighboring city after `t` seconds.
- Input format: `n` (number of cities), `edges` (list of roads), `t` (time), and `target` (target city).
- Expected output format: The probability that the frog is at the target city after `t` seconds.
- Key requirements and edge cases to consider:
  - The tree is undirected and connected.
  - The frog can only jump to a neighboring city.
  - If the frog is at a city with only one neighboring city, it will jump to that city with probability 1.
  - If the frog is at a city with multiple neighboring cities, it will jump to each city with equal probability.
- Example test cases:
  - `n = 7`, `edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]`, `t = 2`, `target = 4`. The output should be `0.16666666666666666`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Simulate the frog's jumps for `t` seconds and calculate the probability of the frog being at the target city.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the tree.
  2. Initialize a probability array with the initial probability of the frog being at each city.
  3. Simulate the frog's jumps for `t` seconds.
  4. Calculate the probability of the frog being at the target city after `t` seconds.
- Why this approach comes to mind first: It is a straightforward simulation of the problem.

```cpp
#include <iostream>
#include <vector>

using namespace std;

double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
    vector<vector<int>> graph(n + 1);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<double> prob(n + 1, 0.0);
    prob[1] = 1.0;

    for (int i = 0; i < t; ++i) {
        vector<double> newProb(n + 1, 0.0);
        for (int j = 1; j <= n; ++j) {
            if (prob[j] > 0) {
                double p = prob[j] / graph[j].size();
                for (int neighbor : graph[j]) {
                    newProb[neighbor] += p;
                }
            }
        }
        prob = newProb;
    }

    return prob[target];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(t \cdot n \cdot \bar{d})$, where $\bar{d}$ is the average degree of the tree.
> - **Space Complexity:** $O(n)$.
> - **Why these complexities occur:** The time complexity occurs because we simulate the frog's jumps for `t` seconds, and in each second, we update the probabilities of the frog being at each city. The space complexity occurs because we need to store the probabilities of the frog being at each city.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The frog's position after `t` seconds can be calculated using a depth-first search (DFS) approach.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the tree.
  2. Perform a DFS from the starting city to calculate the probability of the frog being at each city after `t` seconds.
- Proof of optimality: The DFS approach is optimal because it only visits each city once, resulting in a time complexity of $O(n)$.

```cpp
#include <iostream>
#include <vector>

using namespace std;

double frogPosition(int n, vector<vector<int>>& edges, int t, int target) {
    vector<vector<int>> graph(n + 1);
    for (const auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    vector<bool> visited(n + 1, false);
    vector<double> prob(n + 1, 0.0);
    prob[1] = 1.0;

    function<void(int, int, double)> dfs = [&](int city, int time, double probability) {
        if (time == t) {
            if (city == target) {
                prob[city] = probability;
            }
            return;
        }

        if (visited[city]) {
            return;
        }

        visited[city] = true;

        for (int neighbor : graph[city]) {
            if (!visited[neighbor]) {
                dfs(neighbor, time + 1, probability / graph[city].size());
            }
        }

        visited[city] = false;
    };

    dfs(1, 0, 1.0);

    return prob[target];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$.
> - **Space Complexity:** $O(n)$.
> - **Optimality proof:** The DFS approach is optimal because it only visits each city once, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, probability calculation.
- Problem-solving patterns identified: Using DFS to calculate probabilities in a tree.
- Optimization techniques learned: Avoiding redundant calculations by using a visited array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree or a target city that is not in the tree.
- Edge cases to watch for: The frog starting at a city with no neighbors, or the target city being the starting city.
- Performance pitfalls: Using a brute force approach that simulates the frog's jumps for `t` seconds, resulting in a high time complexity.
- Testing considerations: Testing the function with different inputs, such as different tree structures and target cities.