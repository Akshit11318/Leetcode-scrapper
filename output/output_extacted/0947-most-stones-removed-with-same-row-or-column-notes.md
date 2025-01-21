## Most Stones Removed with Same Row or Column
**Problem Link:** https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description

**Problem Statement:**
- Input format and constraints: Given a set of stones where each stone is represented as an array `[row, column]`, find the maximum number of stones that can be removed if a stone can be removed if it shares the same row or column with another stone.
- Expected output format: The number of stones that can be removed.
- Key requirements and edge cases to consider: Stones can only be removed if they share a row or column with another stone. The input list of stones will not be empty.
- Example test cases with explanations:
    - Input: `stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]`
      Output: `5`
      Explanation: We can remove 5 stones by removing the stones at positions (0,1), (1,0), (1,2), (2,1), and (2,2).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over all pairs of stones and check if they share the same row or column. If they do, we can remove one of the stones.
- Step-by-step breakdown of the solution:
  1. Create a set to store the removed stones.
  2. Iterate over all pairs of stones.
  3. For each pair, check if they share the same row or column.
  4. If they do, add one of the stones to the set of removed stones.
  5. Return the number of removed stones.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        set<pair<int, int>> removed;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    removed.insert(stones[i]);
                    break;
                }
            }
        }
        return removed.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of stones, because we have nested loops that iterate over all pairs of stones.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all stones in the `removed` set.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, and the space complexity is due to the `removed` set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find algorithm to group the stones that share the same row or column. Then, we can remove all stones in each group except one.
- Detailed breakdown of the approach:
  1. Create a union-find data structure with `n` groups, where each group represents a stone.
  2. Iterate over all stones and union the groups of stones that share the same row or column.
  3. Count the number of groups.
  4. Return `n - count`, where `count` is the number of groups.
- Proof of optimality: This approach is optimal because it uses a union-find algorithm, which has a time complexity of $O(n \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.

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
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            count--;
        }
    }
};

class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        UnionFind uf(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    uf.union_(i, j);
                }
            }
        }
        return n - uf.count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because we have nested loops that iterate over all pairs of stones. However, the union-find operation has a very low time complexity, so the overall time complexity is dominated by the nested loops.
> - **Space Complexity:** $O(n)$, because we need to store the `parent` and `rank` arrays in the union-find data structure.
> - **Optimality proof:** The optimal approach is optimal because it uses a union-find algorithm, which has a very low time complexity. The overall time complexity is dominated by the nested loops, but the union-find operation reduces the number of groups, which reduces the number of stones that need to be removed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find algorithm, graph traversal.
- Problem-solving patterns identified: Using a union-find algorithm to group objects that share a common property.
- Optimization techniques learned: Using a union-find algorithm to reduce the number of groups.
- Similar problems to practice: Other problems that involve grouping objects that share a common property.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where two stones share the same row and column.
- Edge cases to watch for: The case where there is only one stone, the case where all stones share the same row or column.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases.