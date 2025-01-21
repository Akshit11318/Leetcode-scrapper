## Minimum Genetic Mutation
**Problem Link:** https://leetcode.com/problems/minimum-genetic-mutation/description

**Problem Statement:**
- Input format and constraints: The problem takes four inputs: `start`, `end`, `bank`, and returns the minimum number of steps to reach the `end` from the `start`. The `bank` is a list of all possible genes.
- Expected output format: The minimum number of steps to reach the `end` from the `start`.
- Key requirements and edge cases to consider: If there is no possible way to reach the `end` from the `start`, return `-1`.
- Example test cases with explanations:
  - Example 1:
    - Input: `start = "AACCGGTA", end = "AACCGCTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]`
    - Output: `1`
    - Explanation: We can reach the `end` from the `start` by changing one character.
  - Example 2:
    - Input: `start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAAACCC","AAACCCCC","AACCCCCC"]`
    - Output: `2`
    - Explanation: We can reach the `end` from the `start` by changing two characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible mutations from the `start` and check if the mutated gene is in the `bank`.
- Step-by-step breakdown of the solution:
  1. Generate all possible mutations from the `start`.
  2. Check if each mutation is in the `bank`.
  3. If a mutation is in the `bank`, add it to a queue for further processing.
  4. Repeat the process until we reach the `end` or the queue is empty.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible mutations.

```cpp
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int minMutation(string start, string end, vector<string>& bank) {
    int steps = 0;
    queue<string> q;
    q.push(start);
    vector<string> visited;
    visited.push_back(start);

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            string current = q.front();
            q.pop();
            if (current == end) {
                return steps;
            }
            for (string& gene : bank) {
                if (isValidMutation(current, gene) && !isVisited(gene, visited)) {
                    q.push(gene);
                    visited.push_back(gene);
                }
            }
        }
        steps++;
    }
    return -1;
}

bool isValidMutation(string current, string gene) {
    int diff = 0;
    for (int i = 0; i < current.size(); i++) {
        if (current[i] != gene[i]) {
            diff++;
            if (diff > 1) {
                return false;
            }
        }
    }
    return diff == 1;
}

bool isVisited(string gene, vector<string>& visited) {
    for (string& v : visited) {
        if (v == gene) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n \cdot m)$ where $n$ is the length of the gene and $m$ is the size of the `bank`. This is because in the worst case, we need to generate all possible mutations and check if each mutation is in the `bank`.
> - **Space Complexity:** $O(4^n)$ for storing all possible mutations in the queue and visited set.
> - **Why these complexities occur:** The brute force approach tries all possible mutations, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) algorithm to explore all possible mutations in a level-by-level manner.
- Detailed breakdown of the approach:
  1. Create a set of visited genes to avoid revisiting the same gene.
  2. Create a queue to store genes to be processed.
  3. Start with the `start` gene and add it to the queue.
  4. Process each gene in the queue:
    - If the gene is the `end` gene, return the number of steps.
    - Generate all possible mutations of the gene.
    - For each mutation, check if it is in the `bank` and has not been visited.
    - If a mutation meets the conditions, add it to the queue and mark it as visited.
  5. Repeat step 4 until the queue is empty.
- Proof of optimality: The BFS algorithm ensures that we explore all possible mutations in a level-by-level manner, which guarantees that we find the minimum number of steps to reach the `end` gene.

```cpp
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int minMutation(string start, string end, vector<string>& bank) {
    unordered_set<string> visited;
    queue<pair<string, int>> q;
    q.push({start, 0});
    visited.insert(start);

    while (!q.empty()) {
        string current = q.front().first;
        int steps = q.front().second;
        q.pop();
        if (current == end) {
            return steps;
        }
        for (string& gene : bank) {
            if (isValidMutation(current, gene) && visited.find(gene) == visited.end()) {
                q.push({gene, steps + 1});
                visited.insert(gene);
            }
        }
    }
    return -1;
}

bool isValidMutation(string current, string gene) {
    int diff = 0;
    for (int i = 0; i < current.size(); i++) {
        if (current[i] != gene[i]) {
            diff++;
            if (diff > 1) {
                return false;
            }
        }
    }
    return diff == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of the gene and $m$ is the size of the `bank`. This is because we only need to generate all possible mutations for each gene in the queue.
> - **Space Complexity:** $O(m)$ for storing all genes in the queue and visited set.
> - **Optimality proof:** The BFS algorithm ensures that we explore all possible mutations in a level-by-level manner, which guarantees that we find the minimum number of steps to reach the `end` gene.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, level-by-level exploration.
- Problem-solving patterns identified: Using a queue to store genes to be processed, using a set to keep track of visited genes.
- Optimization techniques learned: Using a BFS algorithm to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other problems that involve exploring all possible mutations or combinations, such as finding the minimum number of steps to reach a target state.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a gene has been visited before adding it to the queue, not handling the case where the `end` gene is not reachable.
- Edge cases to watch for: The `start` and `end` genes are the same, the `bank` is empty, the `end` gene is not in the `bank`.
- Performance pitfalls: Using a brute force approach that tries all possible mutations, not using a BFS algorithm to explore all possible mutations in a level-by-level manner.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly and efficiently.