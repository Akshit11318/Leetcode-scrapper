## Count the Number of Infection Sequences

**Problem Link:** https://leetcode.com/problems/count-the-number-of-infection-sequences/description

**Problem Statement:**
- Input format: `n` (number of people), `infections` (list of pairs where each pair represents a person and the person they infect)
- Constraints: `1 <= n <= 10^5`, `1 <= infections.length <= 10^5`
- Expected output format: The number of infection sequences
- Key requirements and edge cases to consider: Handle cycles, duplicate infections, and ensure that each person can only be infected once.

**Example Test Cases:**
- `n = 4`, `infections = [[1,2],[2,3],[3,4]]`: The only possible infection sequence is `1 -> 2 -> 3 -> 4`.
- `n = 5`, `infections = [[1,2],[2,3],[3,4],[4,5],[1,3]]`: There are multiple possible infection sequences due to the cycle.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible infection sequences and count them.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of people.
  2. For each permutation, check if it represents a valid infection sequence (i.e., each person is infected by the previous person in the sequence).
  3. Count the number of valid infection sequences.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int countInfectionSequencesBruteForce(int n, vector<vector<int>>& infections) {
    vector<int> people(n);
    for (int i = 0; i < n; i++) {
        people[i] = i + 1;
    }

    int count = 0;
    do {
        bool isValid = true;
        for (int i = 0; i < n - 1; i++) {
            bool isInfected = false;
            for (const auto& infection : infections) {
                if (infection[0] == people[i] && infection[1] == people[i + 1]) {
                    isInfected = true;
                    break;
                }
            }
            if (!isInfected) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            count++;
        }
    } while (next_permutation(people.begin(), people.end()));

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of people and $m$ is the number of infections. This is because we generate all permutations of people and for each permutation, we check all infections.
> - **Space Complexity:** $O(n)$, as we need to store the permutation of people.
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations of people, which leads to a high time complexity. The space complexity is relatively low as we only need to store the current permutation.

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a depth-first search (DFS) approach to count the number of infection sequences.
- Detailed breakdown of the approach:
  1. Create a graph where each person is a node and each infection is a directed edge.
  2. Perform a DFS from each person to count the number of infection sequences starting from that person.
  3. Use memoization to avoid counting the same sequence multiple times.

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

int countInfectionSequencesOptimal(int n, vector<vector<int>>& infections) {
    unordered_map<int, vector<int>> graph;
    for (const auto& infection : infections) {
        graph[infection[0]].push_back(infection[1]);
    }

    unordered_map<int, int> memo;
    function<int(int)> dfs = [&](int person) {
        if (memo.find(person) != memo.end()) {
            return memo[person];
        }

        int count = 1;
        for (const auto& neighbor : graph[person]) {
            count += dfs(neighbor);
        }
        memo[person] = count;
        return count;
    };

    int totalCount = 0;
    for (int i = 1; i <= n; i++) {
        totalCount += dfs(i);
    }

    return totalCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of infections. This is because we perform a DFS from each person and use memoization to avoid counting the same sequence multiple times.
> - **Space Complexity:** $O(n + m)$, as we need to store the graph and the memoization table.
> - **Optimality proof:** This approach is optimal because we only count each infection sequence once, and we use memoization to avoid redundant calculations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, memoization, and graph theory.
- Problem-solving patterns identified: Using DFS to count the number of sequences in a graph.
- Optimization techniques learned: Memoization to avoid redundant calculations.
- Similar problems to practice: Other problems involving graph theory and DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not using memoization, which can lead to exponential time complexity.
- Edge cases to watch for: Handling cycles and duplicate infections.
- Performance pitfalls: Not using an efficient data structure to store the graph and memoization table.
- Testing considerations: Testing the solution with different inputs, including large graphs and graphs with cycles.