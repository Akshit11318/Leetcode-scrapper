## Valid Arrangement of Pairs
**Problem Link:** https://leetcode.com/problems/valid-arrangement-of-pairs/description

**Problem Statement:**
- Input format: Given a list of pairs `pairs` where `pairs[i] = [x, y]` and `x != y`.
- Constraints: `1 <= pairs.length <= 10^5`, `0 <= x, y <= 10^5`, and `0 <= x, y < 10^5`.
- Expected output format: Return a valid arrangement of pairs, or an empty list if no valid arrangement exists.
- Key requirements and edge cases to consider: 
  - Each pair can be used only once.
  - A valid arrangement of pairs is one where for each pair `[x, y]`, there exists a pair `[y, z]` for some `z`.
  - The arrangement is circular, meaning the last pair's second element must be the first pair's first element.
- Example test cases with explanations:
  - For example, given `pairs = [[1,2],[2,3],[3,1]]`, a valid arrangement is `[[1,2],[2,3],[3,1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of the given pairs and check each permutation to see if it forms a valid arrangement.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the given pairs.
  2. For each permutation, iterate through the pairs and check if the current pair's second element matches the next pair's first element.
  3. If a valid arrangement is found, return it. Otherwise, continue checking the remaining permutations.
- Why this approach comes to mind first: It's a straightforward approach that considers all possible arrangements, but it's inefficient due to the large number of permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
    sort(pairs.begin(), pairs.end());
    vector<vector<int>> result;
    do {
        bool valid = true;
        for (int i = 0; i < pairs.size(); i++) {
            if (i < pairs.size() - 1 && pairs[i][1] != pairs[i + 1][0]) {
                valid = false;
                break;
            }
        }
        if (valid && pairs[pairs.size() - 1][1] == pairs[0][0]) {
            result = pairs;
            break;
        }
    } while (next_permutation(pairs.begin(), pairs.end()));
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of pairs. This is because we're generating all permutations of the pairs.
> - **Space Complexity:** $O(n)$, as we need to store the current permutation.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the generation of all permutations, making it impractical for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an Eulerian path algorithm to find a valid arrangement of pairs. An Eulerian path is a path that visits every edge in a graph exactly once.
- Detailed breakdown of the approach:
  1. Create a graph where each node represents a number, and each pair represents a directed edge between two nodes.
  2. Use Hierholzer's algorithm to find an Eulerian path in the graph.
  3. The Eulerian path represents a valid arrangement of pairs.
- Proof of optimality: This approach is optimal because it ensures that every pair is used exactly once and that the arrangement is valid.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
    unordered_map<int, vector<int>> graph;
    unordered_map<int, int> inDegree;
    unordered_map<int, int> outDegree;
    
    for (auto& pair : pairs) {
        graph[pair[0]].push_back(pair[1]);
        outDegree[pair[0]]++;
        inDegree[pair[1]]++;
    }
    
    int start = pairs[0][0];
    for (auto& pair : pairs) {
        if (outDegree[pair[0]] > inDegree[pair[0]]) {
            start = pair[0];
            break;
        }
    }
    
    vector<vector<int>> result;
    vector<int> stack = {start};
    
    while (!stack.empty()) {
        if (!graph[stack.back()].empty()) {
            int next = graph[stack.back()].back();
            graph[stack.back()].pop_back();
            stack.push_back(next);
        } else {
            result.push_back({stack.back(), stack[stack.size() - 2]});
            stack.pop_back();
        }
    }
    
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges in the graph. This is because we're iterating over all nodes and edges once.
> - **Space Complexity:** $O(n + m)$, as we need to store the graph and the Eulerian path.
> - **Optimality proof:** This approach is optimal because it ensures that every pair is used exactly once and that the arrangement is valid, with a time complexity that is linear in the size of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Eulerian paths, graph traversal, and degree counting.
- Problem-solving patterns identified: Using graph theory to model and solve problems involving arrangements and permutations.
- Optimization techniques learned: Avoiding brute force approaches and using efficient algorithms like Hierholzer's algorithm.
- Similar problems to practice: Other problems involving graph traversal, such as finding Hamiltonian cycles or solving the Traveling Salesman Problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the input graph is empty or when there are multiple possible Eulerian paths.
- Edge cases to watch for: When the input graph is not connected or when there are nodes with odd degree.
- Performance pitfalls: Using brute force approaches or inefficient algorithms that have high time complexity.
- Testing considerations: Thoroughly testing the implementation with different input cases, including edge cases and large inputs.