## Count the Number of Complete Components
**Problem Link:** https://leetcode.com/problems/count-the-number-of-complete-components/description

**Problem Statement:**
- Input format and constraints: The problem involves counting the number of complete components in a given graph. A complete component is a subgraph where every pair of distinct vertices is connected by an edge. The input graph is represented as an adjacency list.
- Expected output format: The expected output is the number of complete components in the graph.
- Key requirements and edge cases to consider: The graph may contain multiple connected components, and each component may or may not be complete. We need to identify and count all complete components.
- Example test cases with explanations:
  - Example 1: A graph with a single complete component should return 1.
  - Example 2: A graph with multiple complete components should return the total count of these components.
  - Example 3: A graph with no complete components should return 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial approach involves checking every possible subset of vertices in the graph to see if they form a complete component.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of vertices.
  2. For each subset, check if every pair of distinct vertices is connected by an edge.
  3. If a subset forms a complete component, increment the count.
- Why this approach comes to mind first: This approach is straightforward and guarantees finding all complete components, but it is inefficient due to the exponential number of subsets to check.

```cpp
#include <vector>
#include <iostream>

// Function to check if a subset of vertices forms a complete component
bool isCompleteComponent(const std::vector<std::vector<int>>& graph, const std::vector<int>& subset) {
    for (int i = 0; i < subset.size(); ++i) {
        for (int j = i + 1; j < subset.size(); ++j) {
            // Check if there's an edge between every pair of vertices in the subset
            bool hasEdge = false;
            for (int neighbor : graph[subset[i]]) {
                if (neighbor == subset[j]) {
                    hasEdge = true;
                    break;
                }
            }
            if (!hasEdge) return false;
        }
    }
    return true;
}

int countCompleteComponentsBruteForce(const std::vector<std::vector<int>>& graph) {
    int n = graph.size();
    int count = 0;
    // Generate all possible subsets of vertices
    for (int mask = 1; mask < (1 << n); ++mask) {
        std::vector<int> subset;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subset.push_back(i);
            }
        }
        // Check if the subset forms a complete component
        if (isCompleteComponent(graph, subset)) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of vertices. This is because we generate $2^n$ subsets and for each subset, we check $n^2$ pairs of vertices.
> - **Space Complexity:** $O(n)$, for storing the current subset of vertices.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsets, and the quadratic term within the loop comes from checking every pair of vertices in each subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all subsets, we can use a more efficient algorithm that checks for complete components directly, such as using the concept of cliques in graph theory.
- Detailed breakdown of the approach:
  1. Use a clique detection algorithm to find all maximal cliques in the graph.
  2. Count the number of these maximal cliques, as they represent the complete components.
- Proof of optimality: This approach is optimal because it directly targets the complete components without unnecessary checks, reducing the time complexity significantly compared to the brute force approach.

```cpp
#include <vector>
#include <iostream>

// Function to find all maximal cliques in the graph
void findMaximalCliques(const std::vector<std::vector<int>>& graph, int vertex, std::vector<int>& clique, std::vector<bool>& visited, std::vector<std::vector<int>>& maximalCliques) {
    visited[vertex] = true;
    clique.push_back(vertex);
    bool isMaximal = true;
    for (int neighbor : graph[vertex]) {
        if (!visited[neighbor]) {
            findMaximalCliques(graph, neighbor, clique, visited, maximalCliques);
            isMaximal = false;
        }
    }
    if (isMaximal) {
        maximalCliques.push_back(clique);
    }
    clique.pop_back();
    visited[vertex] = false;
}

int countCompleteComponentsOptimal(const std::vector<std::vector<int>>& graph) {
    int n = graph.size();
    std::vector<std::vector<int>> maximalCliques;
    std::vector<bool> visited(n, false);
    for (int i = 0; i < n; ++i) {
        std::vector<int> clique;
        findMaximalCliques(graph, i, clique, visited, maximalCliques);
    }
    return maximalCliques.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{n/3})$, which is the worst-case time complexity for finding all maximal cliques in a graph, although in practice, it can be much faster for many graphs.
> - **Space Complexity:** $O(n)$, for storing the recursion stack and the current clique.
> - **Optimality proof:** This approach is considered optimal for finding complete components because it uses a clique detection algorithm, which directly identifies complete subgraphs without the need for generating all subsets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem illustrates the importance of clique detection in graph theory and how it can be applied to find complete components.
- Problem-solving patterns identified: The progression from a brute force to an optimal solution highlights the value of understanding graph theory concepts and applying them to solve complex problems efficiently.
- Optimization techniques learned: The solution demonstrates how to significantly reduce computational complexity by applying a more efficient algorithm tailored to the problem.
- Similar problems to practice: Other graph theory problems, such as finding strongly connected components, minimum spanning trees, or solving graph coloring problems, can help deepen understanding and improve problem-solving skills.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as empty graphs or graphs with isolated vertices, can lead to incorrect results.
- Edge cases to watch for: Always consider the smallest and largest possible inputs, as well as any special cases that might affect the algorithm's performance or correctness.
- Performance pitfalls: Using brute force approaches for problems that have more efficient solutions can lead to significant performance issues, especially with large inputs.
- Testing considerations: Thoroughly test the solution with a variety of inputs, including edge cases, to ensure correctness and robustness.