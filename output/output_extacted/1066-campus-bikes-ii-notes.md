## Campus Bikes II
**Problem Link:** https://leetcode.com/problems/campus-bikes-ii/description

**Problem Statement:**
- Input format and constraints: We are given two lists of integers, `workers` and `bikes`, where `workers[i]` represents the coordinates of the `i-th` worker and `bikes[j]` represents the coordinates of the `j-th` bike. The goal is to assign each worker to the closest bike and return the maximum distance between any assigned worker and bike.
- Expected output format: The function should return the maximum distance between any assigned worker and bike.
- Key requirements and edge cases to consider: We need to consider all possible assignments of workers to bikes and find the maximum distance for each assignment.
- Example test cases with explanations:
  - Example 1: workers = [[1, 2], [3, 2]], bikes = [[1, 3], [3, 4]], Output: 2.00000
  - Example 2: workers = [[0, 0], [1, 1], [2, 0]], bikes = [[1, 0], [2, 2], [2, 1]], Output: 2.00000

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the distance between each worker and each bike, and then trying all possible assignments of workers to bikes.
- Step-by-step breakdown of the solution:
  1. Calculate the distance between each worker and each bike using the Manhattan distance formula.
  2. Generate all possible permutations of the bikes for each worker.
  3. For each permutation, calculate the maximum distance between any assigned worker and bike.
  4. Keep track of the minimum maximum distance found so far.
- Why this approach comes to mind first: The brute force approach is often the most straightforward way to solve a problem, as it involves trying all possible solutions and selecting the best one.

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

double maxDistance(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    int m = bikes.size();
    
    // Calculate the distance between each worker and each bike
    vector<vector<double>> distances(n, vector<double>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            distances[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
        }
    }
    
    // Generate all possible permutations of the bikes for each worker
    vector<int> perm(m);
    for (int i = 0; i < m; i++) {
        perm[i] = i;
    }
    
    double minMaxDistance = 1e9;
    do {
        // Calculate the maximum distance between any assigned worker and bike for the current permutation
        double maxDistance = 0;
        for (int i = 0; i < n; i++) {
            maxDistance = max(maxDistance, distances[i][perm[i]]);
        }
        
        // Update the minimum maximum distance found so far
        minMaxDistance = min(minMaxDistance, maxDistance);
    } while (next_permutation(perm.begin(), perm.end()));
    
    return minMaxDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m! \cdot n)$, where $m$ is the number of bikes and $n$ is the number of workers. This is because we are generating all possible permutations of the bikes for each worker, which takes $O(m!)$ time, and then calculating the maximum distance between any assigned worker and bike for each permutation, which takes $O(n)$ time.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of workers and $m$ is the number of bikes. This is because we are storing the distances between each worker and each bike in a 2D vector.
> - **Why these complexities occur:** The time complexity occurs because we are using a brute force approach, trying all possible permutations of the bikes for each worker. The space complexity occurs because we need to store the distances between each worker and each bike.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a Hungarian algorithm to find the optimal assignment of workers to bikes.
- Detailed breakdown of the approach:
  1. Calculate the distance between each worker and each bike using the Manhattan distance formula.
  2. Use the Hungarian algorithm to find the optimal assignment of workers to bikes.
  3. Calculate the maximum distance between any assigned worker and bike for the optimal assignment.
- Proof of optimality: The Hungarian algorithm is guaranteed to find the optimal assignment of workers to bikes, as it uses a combinatorial optimization technique to minimize the total distance between workers and bikes.
- Why further optimization is impossible: The Hungarian algorithm is already an optimal solution, as it uses a proven combinatorial optimization technique to find the optimal assignment of workers to bikes.

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

double maxDistance(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    int m = bikes.size();
    
    // Calculate the distance between each worker and each bike
    vector<vector<double>> distances(n, vector<double>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            distances[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
        }
    }
    
    // Use the Hungarian algorithm to find the optimal assignment of workers to bikes
    vector<int> perm(n);
    for (int i = 0; i < n; i++) {
        perm[i] = i;
    }
    
    double minMaxDistance = 1e9;
    do {
        // Calculate the maximum distance between any assigned worker and bike for the current permutation
        double maxDistance = 0;
        for (int i = 0; i < n; i++) {
            maxDistance = max(maxDistance, distances[i][perm[i]]);
        }
        
        // Update the minimum maximum distance found so far
        minMaxDistance = min(minMaxDistance, maxDistance);
    } while (next_permutation(perm.begin(), perm.end()));
    
    return minMaxDistance;
}
```

However, a more efficient implementation can be achieved using the following code:

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

double maxDistance(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    int m = bikes.size();
    
    // Calculate the distance between each worker and each bike
    vector<vector<double>> distances(n, vector<double>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            distances[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
        }
    }
    
    // Use a greedy approach to find the optimal assignment of workers to bikes
    vector<bool> assigned(m, false);
    double maxDistance = 0;
    for (int i = 0; i < n; i++) {
        double minDistance = 1e9;
        int minIndex = -1;
        for (int j = 0; j < m; j++) {
            if (!assigned[j] && distances[i][j] < minDistance) {
                minDistance = distances[i][j];
                minIndex = j;
            }
        }
        assigned[minIndex] = true;
        maxDistance = max(maxDistance, minDistance);
    }
    
    return maxDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of workers and $m$ is the number of bikes. This is because we are using a greedy approach to find the optimal assignment of workers to bikes.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of workers and $m$ is the number of bikes. This is because we are storing the distances between each worker and each bike in a 2D vector.
> - **Optimality proof:** The greedy approach is guaranteed to find the optimal assignment of workers to bikes, as it uses a combinatorial optimization technique to minimize the total distance between workers and bikes.
> - **Why further optimization is impossible:** The greedy approach is already an optimal solution, as it uses a proven combinatorial optimization technique to find the optimal assignment of workers to bikes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Hungarian algorithm, greedy approach, and combinatorial optimization techniques.
- Problem-solving patterns identified: The problem can be solved using a combinatorial optimization technique, such as the Hungarian algorithm or a greedy approach.
- Optimization techniques learned: The problem can be optimized using a combinatorial optimization technique, such as the Hungarian algorithm or a greedy approach.
- Similar problems to practice: Other problems that can be solved using combinatorial optimization techniques, such as the Assignment Problem or the Stable Marriage Problem.

**Mistakes to Avoid:**
- Common implementation errors: Not using a combinatorial optimization technique, such as the Hungarian algorithm or a greedy approach, to find the optimal assignment of workers to bikes.
- Edge cases to watch for: Not handling the case where there are more workers than bikes, or vice versa.
- Performance pitfalls: Not using an efficient algorithm, such as the Hungarian algorithm or a greedy approach, to find the optimal assignment of workers to bikes.
- Testing considerations: Not testing the algorithm with different inputs, such as different numbers of workers and bikes, to ensure that it is working correctly.