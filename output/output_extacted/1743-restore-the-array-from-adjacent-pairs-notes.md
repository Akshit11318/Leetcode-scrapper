## Restore the Array from Adjacent Pairs
**Problem Link:** https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description

**Problem Statement:**
- Input: A list of pairs of integers `adjacentPairs` where each pair represents two adjacent elements in the original array.
- Expected Output: The original array `originalArray` that can be formed using the given adjacent pairs.
- Key Requirements:
  - The array should be formed by arranging the pairs such that each element appears in the array only once.
  - If there are multiple possible arrays, return any one of them.
- Edge Cases:
  - The input list `adjacentPairs` is not empty.
  - Each pair in `adjacentPairs` contains exactly two integers.
- Example Test Cases:
  - Input: `adjacentPairs = [[2,1],[3,4],[3,2]]`
    Output: `[1,2,3,4]`
  - Input: `adjacentPairs = [[4,-2],[1,4],[-3,1]]`
    Output: `[-2,4,1,-3]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible permutations of the elements in the pairs to form the array.
- Step-by-step breakdown:
  1. Extract all unique elements from the pairs.
  2. Generate all permutations of these elements.
  3. Check each permutation to see if it satisfies the condition that each pair in `adjacentPairs` appears adjacent in the permutation.
- Why this approach comes to mind first: It's a straightforward way to ensure all pairs are adjacent, but it's inefficient due to the large number of permutations.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
    // Extract unique elements
    vector<int> elements;
    for (auto& pair : adjacentPairs) {
        if (find(elements.begin(), elements.end(), pair[0]) == elements.end()) {
            elements.push_back(pair[0]);
        }
        if (find(elements.begin(), elements.end(), pair[1]) == elements.end()) {
            elements.push_back(pair[1]);
        }
    }

    // Generate permutations
    vector<int> result;
    do {
        // Check if each pair is adjacent in the current permutation
        bool valid = true;
        for (auto& pair : adjacentPairs) {
            auto it1 = find(elements.begin(), elements.end(), pair[0]);
            auto it2 = find(elements.begin(), elements.end(), pair[1]);
            if (abs(it1 - it2) != 1) {
                valid = false;
                break;
            }
        }
        if (valid) {
            result = elements;
            break;
        }
    } while (next_permutation(elements.begin(), elements.end()));

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$ where $n$ is the number of unique elements and $m$ is the number of pairs. This is because we generate all permutations of $n$ elements and check each pair in each permutation.
> - **Space Complexity:** $O(n)$ for storing the unique elements and permutations.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which leads to factorial time complexity, making it inefficient for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a graph data structure to represent the adjacency relationships between elements. Then, perform a depth-first search (DFS) or breadth-first search (BFS) to traverse the graph and construct the array.
- Detailed breakdown:
  1. Create a graph where each element is a node, and two nodes are connected if the corresponding elements are adjacent in a pair.
  2. Find a node with degree 1 (a node connected to only one other node) to start the traversal. This node will be the first element in the array.
  3. Perform DFS or BFS from the starting node, adding each visited node to the array and removing the edge between the current node and the previous node to avoid revisiting.
- Why further optimization is impossible: This approach has a linear time complexity with respect to the number of pairs and unique elements, which is the best possible complexity given the need to examine each pair at least once.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
    unordered_map<int, vector<int>> graph;
    for (auto& pair : adjacentPairs) {
        graph[pair[0]].push_back(pair[1]);
        graph[pair[1]].push_back(pair[0]);
    }

    int start;
    for (auto& node : graph) {
        if (node.second.size() == 1) {
            start = node.first;
            break;
        }
    }

    vector<int> result;
    unordered_set<int> visited;
    function<void(int)> dfs = [&](int node) {
        result.push_back(node);
        visited.insert(node);
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(neighbor);
            }
        }
    };

    dfs(start);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of unique elements and $m$ is the number of pairs. This is because we construct the graph and then traverse it once.
> - **Space Complexity:** $O(n + m)$ for storing the graph and the result.
> - **Optimality proof:** This approach is optimal because it examines each pair and element exactly once, leading to linear time complexity, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure (in this case, a graph) to represent the problem's relationships.
- How to apply graph traversal algorithms (DFS/BFS) to solve problems involving adjacency relationships.
- The value of identifying nodes with degree 1 as starting points for traversal in certain graph problems.

**Mistakes to Avoid:**
- Not considering the graph structure as a representation of the problem, leading to less efficient solutions.
- Failing to identify and handle nodes with degree 1 as starting points for traversal.
- Not optimizing the solution to achieve linear time complexity.