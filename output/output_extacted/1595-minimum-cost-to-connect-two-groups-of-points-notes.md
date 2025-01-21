## Minimum Cost to Connect Two Groups of Points
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/description

**Problem Statement:**
- Input format and constraints: The problem involves connecting two groups of points, `points1` and `points2`, where each point is represented as an array of two integers. The goal is to find the minimum cost to connect each point in `points1` to exactly one point in `points2`.
- Expected output format: The function should return the minimum cost to connect all points.
- Key requirements and edge cases to consider: The cost to connect two points is the Manhattan distance between them. Each point in `points1` must be connected to exactly one point in `points2`, and vice versa.
- Example test cases with explanations: For example, given `points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]` and `points2 = [[0,0],[1,1],[1,1],[2,1],[3,4]]`, the function should return the minimum cost to connect all points.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to try all possible connections between points in `points1` and `points2` and calculate the total cost for each possible connection.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of points in `points2`.
  2. For each permutation, calculate the total cost by summing the Manhattan distances between corresponding points in `points1` and the permutation.
  3. Keep track of the minimum total cost found.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible connections are considered.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int bruteForce(const std::vector<std::vector<int>>& points1, const std::vector<std::vector<int>>& points2) {
    int minCost = INT_MAX;
    std::vector<int> permutation(points2.size());
    std::iota(permutation.begin(), permutation.end(), 0);

    do {
        int cost = 0;
        for (int i = 0; i < points1.size(); ++i) {
            cost += abs(points1[i][0] - points2[permutation[i]][0]) + abs(points1[i][1] - points2[permutation[i]][1]);
        }
        minCost = std::min(minCost, cost);
    } while (std::next_permutation(permutation.begin(), permutation.end()));

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of points in `points1` (or `points2`), because there are $n!$ permutations of points in `points2`.
> - **Space Complexity:** $O(n)$, for storing the permutation.
> - **Why these complexities occur:** The brute force approach tries all possible permutations, leading to an exponential time complexity. The space complexity is linear because only one permutation is stored at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using the Hungarian Algorithm, which is an efficient method for solving the Assignment Problem.
- Detailed breakdown of the approach:
  1. Create a cost matrix where the entry at row $i$ and column $j$ represents the cost of connecting the $i$-th point in `points1` to the $j$-th point in `points2`.
  2. Apply the Hungarian Algorithm to find the optimal assignment that minimizes the total cost.
- Proof of optimality: The Hungarian Algorithm is guaranteed to find the optimal solution for the Assignment Problem, which is a well-known problem in combinatorial optimization.
- Why further optimization is impossible: The Hungarian Algorithm has a time complexity of $O(n^3)$, which is much better than the brute force approach.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int optimal(const std::vector<std::vector<int>>& points1, const std::vector<std::vector<int>>& points2) {
    int n = points1.size();
    std::vector<std::vector<int>> costMatrix(n, std::vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            costMatrix[i][j] = abs(points1[i][0] - points2[j][0]) + abs(points1[i][1] - points2[j][1]);
        }
    }

    std::vector<int> u(n), v(n), p(n);
    std::vector<bool> way(n);

    for (int i = 0; i < n; ++i) {
        p[0] = i;
        int j0 = 0;
        std::fill(way.begin(), way.end(), false);
        do {
            way[j0] = true;
            int i0 = p[j0], j1 = 0;
            int delta = INT_MAX;
            for (int j = 0; j < n; ++j) {
                if (!way[j]) {
                    int cur = costMatrix[i0][j] - u[i0] - v[j];
                    if (cur < delta) {
                        delta = cur;
                        j1 = j;
                    }
                }
            }
            for (int j = 0; j < n; ++j) {
                if (way[j]) {
                    u[p[j]] += delta;
                    v[j] -= delta;
                }
            }
            j0 = j1;
        } while (p[j0] != -1);
        do {
            int j1 = p[j0];
            p[j0] = p[j1];
            j0 = j1;
        } while (j0 != -1);
    }

    int minCost = 0;
    for (int i = 0; i < n; ++i) {
        minCost += costMatrix[i][p[i]];
    }

    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of points in `points1` (or `points2`), because the Hungarian Algorithm has a cubic time complexity.
> - **Space Complexity:** $O(n^2)$, for storing the cost matrix and other auxiliary arrays.
> - **Optimality proof:** The Hungarian Algorithm is guaranteed to find the optimal solution for the Assignment Problem, which is a well-known problem in combinatorial optimization.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Hungarian Algorithm, which is an efficient method for solving the Assignment Problem.
- Problem-solving patterns identified: The problem can be solved by reducing it to the Assignment Problem and applying the Hungarian Algorithm.
- Optimization techniques learned: The Hungarian Algorithm is an example of a combinatorial optimization technique that can be used to solve complex problems efficiently.
- Similar problems to practice: Other problems that can be solved using the Hungarian Algorithm, such as the Assignment Problem, the Stable Marriage Problem, and the Traveling Salesman Problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the cost matrix correctly, not applying the Hungarian Algorithm correctly, and not handling edge cases properly.
- Edge cases to watch for: The problem assumes that the input points are valid and that the cost matrix can be computed correctly. However, in practice, it is important to handle edge cases such as invalid input points, non-square cost matrices, and non-integer costs.
- Performance pitfalls: The Hungarian Algorithm has a cubic time complexity, which can be slow for large inputs. However, it is generally much faster than the brute force approach, which has an exponential time complexity.
- Testing considerations: The problem can be tested using a variety of test cases, including small inputs, large inputs, and edge cases. It is also important to test the implementation of the Hungarian Algorithm to ensure that it is correct and efficient.