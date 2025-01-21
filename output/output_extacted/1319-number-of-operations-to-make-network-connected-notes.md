## Number of Operations to Make Network Connected
**Problem Link:** https://leetcode.com/problems/number-of-operations-to-make-network-connected/description

**Problem Statement:**
- Input: `n` (number of computers) and `connections` (a list of connections between computers)
- Constraints: $1 \leq n \leq 10^5$, $0 \leq connections.length \leq n * (n - 1) / 2$
- Expected Output: The minimum number of operations required to make the network connected
- Key Requirements:
  - A network is considered connected if all computers can communicate with each other.
  - If the network is already connected, return 0.
  - If it's impossible to make the network connected, return -1.
- Edge Cases:
  - If `connections` is empty, the network is not connected.
  - If `n` is 1, the network is always connected.

Example Test Cases:
- `n = 4`, `connections = [[0,1],[0,2],[1,2]]`, Expected Output: `1`
- `n = 5`, `connections = [[0,1],[0,2],[3,4]]`, Expected Output: `2`
- `n = 6`, `connections = [[0,1],[0,2],[0,3],[3,4],[3,5]]`, Expected Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of connections to see if we can make the network connected.
- We can use a depth-first search (DFS) to check if all computers are connected.
- However, this approach is not efficient because it has an exponential time complexity.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int count;

    UnionFind(int n) : parent(n), rank(n, 0), count(n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
            } else if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else {
                parent[rooty] = rootx;
                rank[rootx]++;
            }
            count--;
        }
    }
};

int makeConnected(int n, vector<vector<int>>& connections) {
    UnionFind uf(n);
    for (auto& connection : connections) {
        uf.union_(connection[0], connection[1]);
    }
    if (uf.count == 1) {
        return 0;
    } else if (connections.size() < n - 1) {
        return -1;
    } else {
        return uf.count - 1;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of computers. This is because in the worst case, we might need to try all possible combinations of connections.
> - **Space Complexity:** $O(n)$, where $n$ is the number of computers. This is because we need to store the parent and rank arrays for each computer.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible combinations of connections. The space complexity is relatively low because we only need to store the parent and rank arrays for each computer.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a Union-Find data structure to keep track of the connected components.
- We can iterate through the connections and use the Union-Find data structure to merge the connected components.
- If the number of connected components is greater than 1, we need to add cables to connect them.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int count;

    UnionFind(int n) : parent(n), rank(n, 0), count(n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void union_(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] > rank[rooty]) {
                parent[rooty] = rootx;
            } else if (rank[rootx] < rank[rooty]) {
                parent[rootx] = rooty;
            } else {
                parent[rooty] = rootx;
                rank[rootx]++;
            }
            count--;
        }
    }
};

int makeConnected(int n, vector<vector<int>>& connections) {
    UnionFind uf(n);
    for (auto& connection : connections) {
        uf.union_(connection[0], connection[1]);
    }
    if (uf.count == 1) {
        return 0;
    } else if (connections.size() < n - 1) {
        return -1;
    } else {
        return uf.count - 1;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$, where $n$ is the number of computers and $m$ is the number of connections. The $\alpha(n)$ term represents the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n)$, where $n$ is the number of computers. This is because we need to store the parent and rank arrays for each computer.
> - **Optimality proof:** This approach is optimal because it uses a Union-Find data structure, which has a proven time complexity of $O(n + m \alpha(n))$. Additionally, we only need to iterate through the connections once, making the time complexity linear with respect to the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-Find data structure, connected components.
- Problem-solving patterns identified: using a Union-Find data structure to solve connectivity problems.
- Optimization techniques learned: using a Union-Find data structure to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty list of connections.
- Edge cases to watch for: the number of connections is less than $n-1$, in which case it's impossible to make the network connected.
- Performance pitfalls: using a brute force approach, which has a high time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.