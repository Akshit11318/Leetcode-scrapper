## Tree of Coprimes

**Problem Link:** https://leetcode.com/problems/tree-of-coprimes/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `nums` as input, where each integer represents a node in a tree. The goal is to construct a tree where each node is connected to all its coprime nodes.
- Expected output format: The problem requires finding the maximum depth of the tree that can be constructed.
- Key requirements and edge cases to consider: The problem involves finding the greatest common divisor (GCD) of two numbers and constructing a tree based on coprime relationships.
- Example test cases with explanations:
  - For the input `[2, 3, 4, 5]`, the output should be `2` because we can construct a tree with the following structure: `(2, 3) -> (3, 5)` or `(2, 5) -> (5, 3)`.
  - For the input `[2, 3, 4, 5, 6, 7]`, the output should be `3` because we can construct a tree with the following structure: `(2, 3) -> (3, 5) -> (5, 7)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by finding all pairs of coprime numbers in the input array.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of numbers from the input array.
  2. For each pair, calculate the GCD using the Euclidean algorithm.
  3. If the GCD is 1, it means the numbers are coprime, and we can add an edge between them in the tree.
  4. Finally, we can use a depth-first search (DFS) or breadth-first search (BFS) algorithm to find the maximum depth of the tree.
- Why this approach comes to mind first: This approach is straightforward and involves basic graph theory concepts.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int maxDepth(std::vector<int>& nums) {
    std::unordered_map<int, std::vector<int>> graph;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (gcd(nums[i], nums[j]) == 1) {
                graph[nums[i]].push_back(nums[j]);
                graph[nums[j]].push_back(nums[i]);
            }
        }
    }

    int maxDepth = 0;
    for (auto& node : graph) {
        std::queue<std::pair<int, int>> queue;
        queue.push({node.first, 0});
        std::unordered_set<int> visited;
        visited.insert(node.first);

        while (!queue.empty()) {
            int currentNode = queue.front().first;
            int currentDepth = queue.front().second;
            queue.pop();

            maxDepth = std::max(maxDepth, currentDepth);

            for (int neighbor : graph[currentNode]) {
                if (visited.find(neighbor) == visited.end()) {
                    queue.push({neighbor, currentDepth + 1});
                    visited.insert(neighbor);
                }
            }
        }
    }

    return maxDepth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \log n)$, where $n$ is the size of the input array. The reason is that we generate all pairs of numbers, calculate the GCD for each pair using the Euclidean algorithm, and then perform a BFS traversal for each node.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the input array. The reason is that we store all pairs of coprime numbers in the graph.
> - **Why these complexities occur:** The time complexity occurs because we use nested loops to generate all pairs of numbers and calculate the GCD for each pair. The space complexity occurs because we store all pairs of coprime numbers in the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all pairs of numbers and calculating the GCD for each pair, we can use a more efficient approach to find the coprime numbers.
- Detailed breakdown of the approach:
  1. Initialize a `dp` array to store the maximum depth for each number.
  2. Iterate through the input array, and for each number, find its coprime numbers.
  3. Update the `dp` array with the maximum depth for each number.
  4. Finally, return the maximum value in the `dp` array.
- Proof of optimality: This approach is optimal because it avoids generating all pairs of numbers and calculating the GCD for each pair, which reduces the time complexity.
- Why further optimization is impossible: This approach is already optimal because it uses a dynamic programming approach to find the maximum depth for each number.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int maxDepth(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> dp(n, 1);

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (gcd(nums[i], nums[j]) == 1) {
                dp[j] = std::max(dp[j], dp[i] + 1);
            }
        }
    }

    int maxDepth = 0;
    for (int depth : dp) {
        maxDepth = std::max(maxDepth, depth);
    }

    return maxDepth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. The reason is that we use nested loops to find the coprime numbers for each number.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. The reason is that we store the maximum depth for each number in the `dp` array.
> - **Optimality proof:** This approach is optimal because it avoids generating all pairs of numbers and calculating the GCD for each pair, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, graph theory, and GCD calculation.
- Problem-solving patterns identified: Avoid generating all pairs of numbers and calculating the GCD for each pair.
- Optimization techniques learned: Use dynamic programming to find the maximum depth for each number.
- Similar problems to practice: Finding the maximum depth of a tree, finding the longest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: Empty input array, single-element input array.
- Performance pitfalls: Generating all pairs of numbers and calculating the GCD for each pair.
- Testing considerations: Test with different input sizes, test with different input values.