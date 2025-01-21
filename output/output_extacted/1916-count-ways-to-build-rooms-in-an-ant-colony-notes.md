## Count Ways to Build Rooms in an Ant Colony
**Problem Link:** https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/description

**Problem Statement:**
- Input format and constraints: The problem takes as input a 2D vector `prevRoom` where `prevRoom[i]` is the index of the room that the `i-th` room is connected to. The goal is to count the number of ways to build rooms in an ant colony such that each room is reachable from the previous one.
- Expected output format: The output should be the number of ways to build the rooms modulo `10^9 + 7`.
- Key requirements and edge cases to consider: The input `prevRoom` is a list of integers where `prevRoom[i]` is the index of the room that the `i-th` room is connected to. The rooms are 0-indexed. We need to handle cases where there are cycles in the graph and where there are not.
- Example test cases with explanations: For example, if `prevRoom = [0,-1,0]`, then the output should be `2` because there are two ways to build the rooms: `[0,1,2]` and `[0,2,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible permutations of the rooms and check if each permutation satisfies the condition that each room is reachable from the previous one.
- Step-by-step breakdown of the solution: We can use a recursive function to generate all permutations of the rooms. For each permutation, we check if the `i-th` room is reachable from the `(i-1)-th` room by following the `prevRoom` connections.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the recursive function calls and the permutation generation.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int countWays(vector<int>& prevRoom) {
    int n = prevRoom.size();
    vector<int> perm(n);
    for (int i = 0; i < n; i++) {
        perm[i] = i;
    }
    int count = 0;
    do {
        bool valid = true;
        for (int i = 1; i < n; i++) {
            int curr = perm[i];
            int prev = perm[i-1];
            while (prev != -1 && prev != curr) {
                prev = prevRoom[prev];
            }
            if (prev != curr) {
                valid = false;
                break;
            }
        }
        if (valid) {
            count++;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of rooms. The permutation generation has a time complexity of $O(n!)$, and the validation of each permutation has a time complexity of $O(n)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rooms. We need to store the permutation of the rooms.
> - **Why these complexities occur:** The high time complexity is due to the recursive function calls and the permutation generation. The space complexity is due to the storage of the permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a graph to represent the connections between the rooms. We can then use a depth-first search (DFS) to find all possible ways to build the rooms.
- Detailed breakdown of the approach: We create a graph where each room is a node, and there is a directed edge from room `i` to room `j` if `prevRoom[i] == j`. We then use a DFS to find all possible ways to build the rooms. The DFS function takes a room as input and returns the number of ways to build the rooms starting from that room.
- Proof of optimality: The DFS approach has a time complexity of $O(n)$, where $n$ is the number of rooms. This is because we visit each room at most once during the DFS.
- Why further optimization is impossible: The time complexity of $O(n)$ is optimal because we need to visit each room at least once to determine the number of ways to build the rooms.

```cpp
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int countWays(vector<int>& prevRoom) {
    int n = prevRoom.size();
    vector<vector<int>> graph(n);
    vector<int> inDegree(n, 0);
    for (int i = 0; i < n; i++) {
        if (prevRoom[i] != -1) {
            graph[prevRoom[i]].push_back(i);
            inDegree[i]++;
        }
    }
    vector<int> dp(n, 1);
    for (int i = 0; i < n; i++) {
        for (int j : graph[i]) {
            dp[i] = (dp[i] * (dp[j] + 1)) % MOD;
        }
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (inDegree[i] == 0) {
            count = (count + dp[i]) % MOD;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rooms. We visit each room at most once during the DFS.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rooms. We need to store the graph and the DP table.
> - **Optimality proof:** The time complexity of $O(n)$ is optimal because we need to visit each room at least once to determine the number of ways to build the rooms.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph theory, DFS, DP.
- Problem-solving patterns identified: The problem can be solved using a graph and a DFS.
- Optimization techniques learned: The use of a DP table to store the results of subproblems.
- Similar problems to practice: Problems that involve graph theory and DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where there are cycles in the graph.
- Edge cases to watch for: The case where there are no rooms, or the case where there is only one room.
- Performance pitfalls: Not using a DP table to store the results of subproblems, which can lead to a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.