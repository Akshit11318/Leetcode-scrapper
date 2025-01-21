## Count Connected Components in LCM Graph
**Problem Link:** https://leetcode.com/problems/count-connected-components-in-lcm-graph/description

**Problem Statement:**
- Input: An integer `n`.
- Output: The number of connected components in the LCM graph.
- Key Requirements: The LCM graph is a graph where two numbers are connected if their least common multiple (`LCM`) is less than or equal to `n`.
- Example Test Cases:
  - Input: `n = 5`
  - Output: `3`
  - Explanation: The LCM graph for `n = 5` contains three connected components: `[1, 2, 4]`, `[3]`, and `[5]`.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Generate all possible pairs of numbers from `1` to `n`, calculate their LCM, and check if it's less than or equal to `n`. Use a `Union-Find` data structure to keep track of connected components.
- Step-by-Step Breakdown:
  1. Initialize a `Union-Find` data structure with `n` elements.
  2. Iterate over all pairs of numbers from `1` to `n`.
  3. For each pair, calculate their LCM and check if it's less than or equal to `n`.
  4. If the LCM is less than or equal to `n`, union the two numbers in the `Union-Find` data structure.
  5. Finally, count the number of connected components in the `Union-Find` data structure.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent.resize(n);
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

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int countConnectedComponents(int n) {
    UnionFind uf(n);
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            int lcm = (i * j) / __gcd(i, j);
            if (lcm <= n) {
                uf.unionNodes(i - 1, j - 1);
            }
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (uf.find(i) == i) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot log(n))$ due to the nested loops and the calculation of LCM using GCD.
> - **Space Complexity:** $O(n)$ for the `Union-Find` data structure.
> - **Why these complexities occur:** The brute force approach checks all pairs of numbers, resulting in a quadratic time complexity. The calculation of LCM using GCD adds a logarithmic factor.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of checking all pairs of numbers, we can iterate over all numbers from `1` to `n` and check if they are connected to any of their multiples.
- Detailed Breakdown:
  1. Initialize a `Union-Find` data structure with `n` elements.
  2. Iterate over all numbers from `1` to `n`.
  3. For each number, check if it's connected to any of its multiples by calculating their LCM.
  4. If the LCM is less than or equal to `n`, union the two numbers in the `Union-Find` data structure.
  5. Finally, count the number of connected components in the `Union-Find` data structure.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) {
        parent.resize(n);
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

    void unionNodes(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

int countConnectedComponents(int n) {
    UnionFind uf(n);
    for (int i = 1; i <= n; i++) {
        for (int j = 2; i * j <= n; j++) {
            int lcm = (i * j) / __gcd(i, j);
            if (lcm <= n) {
                uf.unionNodes(i - 1, i * j - 1);
            }
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (uf.find(i) == i) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ due to the iteration over all numbers and their multiples, and the calculation of LCM using GCD.
> - **Space Complexity:** $O(n)$ for the `Union-Find` data structure.
> - **Optimality proof:** This approach is optimal because it only checks the necessary pairs of numbers, resulting in a linear time complexity with respect to the number of nodes in the LCM graph.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `Union-Find` data structure, LCM calculation using GCD.
- Problem-solving patterns identified: iterating over all numbers and their multiples to find connected components.
- Optimization techniques learned: reducing the number of pairs to check by iterating over multiples instead of all pairs.

**Mistakes to Avoid:**
- Common implementation errors: incorrect implementation of the `Union-Find` data structure, incorrect calculation of LCM using GCD.
- Edge cases to watch for: handling the case where `n` is 1, handling the case where `n` is a prime number.
- Performance pitfalls: using a brute force approach that checks all pairs of numbers, resulting in a quadratic time complexity.
- Testing considerations: testing the implementation with small and large values of `n`, testing the implementation with prime and composite values of `n`.