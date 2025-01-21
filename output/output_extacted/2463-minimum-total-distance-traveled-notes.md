## Minimum Total Distance Traveled
**Problem Link:** https://leetcode.com/problems/minimum-total-distance-traveled/description

**Problem Statement:**
- Input format and constraints: The problem involves a list of `n` robots and a list of `m` factories. Each robot has a position, and each factory has a position. The goal is to assign each robot to a factory such that the total distance traveled by all robots is minimized.
- Expected output format: The minimum total distance traveled by all robots.
- Key requirements and edge cases to consider: The distance between two points is calculated using the Manhattan distance (L1 distance), and each robot can be assigned to any factory.
- Example test cases with explanations:
  - For example, if we have two robots at positions `(0, 0)` and `(1, 1)`, and two factories at positions `(0, 0)` and `(1, 1)`, the minimum total distance traveled would be `0` because we can assign the first robot to the first factory and the second robot to the second factory.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to try all possible assignments of robots to factories and calculate the total distance traveled for each assignment.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of assigning `n` robots to `m` factories.
  2. For each permutation, calculate the total distance traveled by all robots.
  3. Keep track of the minimum total distance traveled.
- Why this approach comes to mind first: This approach is intuitive because it tries all possible solutions and selects the best one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minDistanceTraveled(vector<vector<int>>& robot, vector<vector<int>>& factory) {
    int n = robot.size();
    int m = factory.size();
    vector<int> permutation(n);
    for (int i = 0; i < n; i++) permutation[i] = i;

    int minDistance = INT_MAX;
    do {
        int distance = 0;
        for (int i = 0; i < n; i++) {
            distance += abs(robot[i][0] - factory[permutation[i]][0]) + abs(robot[i][1] - factory[permutation[i]][1]);
        }
        minDistance = min(minDistance, distance);
    } while (next_permutation(permutation.begin(), permutation.end()));

    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of robots and $m$ is the number of factories. The reason is that we generate all permutations of assigning $n$ robots to $m$ factories, which takes $O(n!)$ time, and for each permutation, we calculate the total distance traveled, which takes $O(n \cdot m)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of robots. The reason is that we need to store the permutation of robots, which takes $O(n)$ space.
> - **Why these complexities occur:** The time complexity is high because we try all possible assignments of robots to factories, and the space complexity is relatively low because we only need to store the current permutation of robots.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using the Hungarian algorithm, which is a combinatorial optimization algorithm that solves the assignment problem in polynomial time.
- Detailed breakdown of the approach:
  1. Create a cost matrix where the entry at row $i$ and column $j$ represents the distance between the $i$th robot and the $j$th factory.
  2. Apply the Hungarian algorithm to the cost matrix to find the optimal assignment of robots to factories.
- Proof of optimality: The Hungarian algorithm is guaranteed to find the optimal solution to the assignment problem, which is equivalent to the minimum total distance traveled problem.
- Why further optimization is impossible: The Hungarian algorithm has a time complexity of $O(n^3)$, which is the best known time complexity for the assignment problem.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = INT_MAX / 2;

int minDistanceTraveled(vector<vector<int>>& robot, vector<vector<int>>& factory) {
    int n = robot.size();
    int m = factory.size();
    vector<vector<int>> cost(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cost[i][j] = abs(robot[i][0] - factory[j][0]) + abs(robot[i][1] - factory[j][1]);
        }
    }

    vector<int> u(n, 0);
    vector<int> v(m, 0);
    vector<int> p(m, 0);
    vector<bool> way(m, false);

    for (int i = 0; i < n; i++) {
        p[0] = i;
        int j0 = 0;
        vector<int> minv(m, INF);
        do {
            way[j0] = true;
            int i0 = p[j0];
            int delta = INF;
            int j1;
            for (int j = 0; j < m; j++) {
                if (!way[j]) {
                    int cur = cost[i0][j] - u[i0] - v[j];
                    if (cur < minv[j]) {
                        minv[j] = cur;
                        p[j] = i0;
                    }
                    if (minv[j] < delta) {
                        delta = minv[j];
                        j1 = j;
                    }
                }
            }
            for (int j = 0; j < m; j++) {
                if (way[j]) {
                    u[p[j]] += delta;
                    v[j] -= delta;
                } else {
                    minv[j] -= delta;
                }
            }
            j0 = j1;
        } while (p[j0] != i);
        do {
            int j1 = j0;
            j0 = p[j1];
            p[j1] = i;
        } while (j0 != i);
    }

    int minDistance = 0;
    for (int i = 0; i < n; i++) {
        minDistance += cost[i][p[i]];
    }

    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of robots. The reason is that we use the Hungarian algorithm, which has a time complexity of $O(n^3)$.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of robots. The reason is that we need to store the cost matrix, which takes $O(n^2)$ space.
> - **Optimality proof:** The Hungarian algorithm is guaranteed to find the optimal solution to the assignment problem, which is equivalent to the minimum total distance traveled problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Hungarian algorithm, which is a combinatorial optimization algorithm that solves the assignment problem in polynomial time.
- Problem-solving patterns identified: The problem can be solved by creating a cost matrix and applying the Hungarian algorithm to find the optimal assignment of robots to factories.
- Optimization techniques learned: The Hungarian algorithm is an example of a polynomial-time algorithm for solving the assignment problem.
- Similar problems to practice: The assignment problem, the stable marriage problem, and other combinatorial optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the cost matrix correctly, not applying the Hungarian algorithm correctly, and not handling edge cases correctly.
- Edge cases to watch for: The number of robots and factories can be different, and the cost matrix can have different values.
- Performance pitfalls: The Hungarian algorithm has a time complexity of $O(n^3)$, which can be slow for large inputs.
- Testing considerations: Test the implementation with different inputs, including edge cases, to ensure that it works correctly.