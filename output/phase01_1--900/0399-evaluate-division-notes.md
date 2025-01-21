## Evaluate Division
**Problem Link:** [https://leetcode.com/problems/evaluate-division/description](https://leetcode.com/problems/evaluate-division/description)

**Problem Statement:**
- Input format: `equations`: a list of pairs of strings representing equations, `values`: a list of floating point numbers representing the values of the equations, `queries`: a list of pairs of strings representing the queries to be evaluated.
- Constraints: The length of `equations` and `values` will be equal, and the length of `queries` will be greater than or equal to 0. The equations will be in the form `a/b`, where `a` and `b` are lowercase letters.
- Expected output format: A list of floating point numbers representing the values of the queries.
- Key requirements and edge cases to consider: The equations may not be consistent, and some queries may not be evaluable.
- Example test cases with explanations:
  - Example 1: `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
    - The equations can be represented as a graph, where each node is a variable and each edge is an equation.
    - The queries can be evaluated by finding the path between the nodes in the graph.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a graph to represent the equations, where each node is a variable and each edge is an equation.
- Step-by-step breakdown of the solution:
  1. Create a graph to represent the equations.
  2. For each query, find the path between the nodes in the graph.
  3. If a path is found, calculate the value of the query by multiplying the values of the edges in the path.
- Why this approach comes to mind first: It is a straightforward way to represent the equations and queries as a graph.

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    unordered_map<string, unordered_map<string, double>> graph;
    for (int i = 0; i < equations.size(); i++) {
        string u = equations[i][0], v = equations[i][1];
        double val = values[i];
        graph[u][v] = val;
        graph[v][u] = 1 / val;
    }

    vector<double> res;
    for (auto& query : queries) {
        string u = query[0], v = query[1];
        if (graph.find(u) == graph.end() || graph.find(v) == graph.end()) {
            res.push_back(-1.0);
            continue;
        }
        unordered_set<string> visited;
        double val = dfs(graph, u, v, visited);
        res.push_back(val);
    }
    return res;
}

double dfs(unordered_map<string, unordered_map<string, double>>& graph, string u, string v, unordered_set<string>& visited) {
    if (graph[u].find(v) != graph[u].end()) {
        return graph[u][v];
    }
    visited.insert(u);
    for (auto& neighbor : graph[u]) {
        if (visited.find(neighbor.first) == visited.end()) {
            double val = dfs(graph, neighbor.first, v, visited);
            if (val != -1.0) {
                return val * neighbor.second;
            }
        }
    }
    return -1.0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queries and $m$ is the number of equations. This is because for each query, we may need to traverse all the equations in the worst case.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of variables and $m$ is the number of equations. This is because we need to store all the variables and equations in the graph.
> - **Why these complexities occur:** The time complexity occurs because we may need to traverse all the equations for each query, and the space complexity occurs because we need to store all the variables and equations in the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to group the variables that are connected by the equations.
- Detailed breakdown of the approach:
  1. Create a union-find data structure to group the variables.
  2. For each equation, union the variables in the equation.
  3. For each query, find the group of the variables in the query.
  4. If the variables are in the same group, calculate the value of the query by multiplying the values of the edges in the path.
- Proof of optimality: This approach is optimal because it reduces the time complexity of finding the path between the variables in the graph from $O(n \cdot m)$ to $O(n + m)$.

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

class UnionFind {
public:
    unordered_map<string, string> parent;
    unordered_map<string, double> rank;

    string find(string x) {
        if (parent.find(x) == parent.end()) {
            parent[x] = x;
            rank[x] = 1.0;
            return x;
        }
        if (parent[x] != x) {
            string p = find(parent[x]);
            rank[x] *= rank[parent[x]];
            parent[x] = p;
        }
        return parent[x];
    }

    void union_(string x, string y, double val) {
        string px = find(x), py = find(y);
        if (px != py) {
            parent[px] = py;
            rank[px] = rank[x] * val / rank[y];
        }
    }
};

vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
    UnionFind uf;
    for (int i = 0; i < equations.size(); i++) {
        string u = equations[i][0], v = equations[i][1];
        double val = values[i];
        uf.union_(u, v, val);
    }

    vector<double> res;
    for (auto& query : queries) {
        string u = query[0], v = query[1];
        if (uf.parent.find(u) == uf.parent.end() || uf.parent.find(v) == uf.parent.end()) {
            res.push_back(-1.0);
            continue;
        }
        string pu = uf.find(u), pv = uf.find(v);
        if (pu != pv) {
            res.push_back(-1.0);
            continue;
        }
        res.push_back(uf.rank[u] / uf.rank[v]);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of queries and $m$ is the number of equations. This is because we only need to traverse the equations once to build the union-find data structure.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of variables and $m$ is the number of equations. This is because we need to store all the variables and equations in the union-find data structure.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of finding the path between the variables in the graph from $O(n \cdot m)$ to $O(n + m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: union-find data structure, graph traversal.
- Problem-solving patterns identified: reducing time complexity by using a union-find data structure.
- Optimization techniques learned: using a union-find data structure to group connected variables.
- Similar problems to practice: problems involving graph traversal and union-find data structure.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where a variable is not present in the graph.
- Edge cases to watch for: the case where the equations are not consistent, the case where a query is not evaluable.
- Performance pitfalls: using a naive approach that has a high time complexity.
- Testing considerations: testing the implementation with different inputs, including edge cases.