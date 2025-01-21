## Reconstruct Itinerary
**Problem Link:** https://leetcode.com/problems/reconstruct-itinerary/description

**Problem Statement:**
- Input: A list of `tickets` where each ticket is a pair of strings representing the source and destination airports.
- Constraints: The total number of tickets is in the range `[1, 300]`. The source and destination airports are in the range `[1, 10,000]`.
- Expected Output: Reconstruct the flight itinerary by returning a list of airport codes in the order they were visited.
- Key Requirements: The itinerary must start from the `JFK` airport, and if there are multiple possible itineraries, return the one with the lexicographically smallest order.
- Example Test Cases:
  - Input: `[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]`
  - Output: `["JFK", "MUC", "LHR", "SFO", "SJC"]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible permutations of the given tickets and checking if they form a valid itinerary.
- Step-by-step breakdown:
  1. Generate all permutations of the tickets.
  2. For each permutation, start from the `JFK` airport and try to build the itinerary by following the source and destination airports in the permutation.
  3. If an itinerary can be successfully built for a permutation, check if it is lexicographically smaller than the current smallest itinerary found.
- Why this approach comes to mind first: It's a straightforward approach that tries to brute-force all possible solutions.

```cpp
#include <vector>
#include <string>
#include <algorithm>

void backtrack(std::vector<std::vector<std::string>>& result, 
              std::vector<std::string>& path, 
              std::vector<std::vector<std::string>>& tickets, 
              std::vector<bool>& used) {
    if (path.size() == tickets.size() + 1) {
        result.push_back(path);
        return;
    }
    
    for (int i = 0; i < tickets.size(); ++i) {
        if (!used[i] && tickets[i][0] == path.back()) {
            used[i] = true;
            path.push_back(tickets[i][1]);
            backtrack(result, path, tickets, used);
            used[i] = false;
            path.pop_back();
        }
    }
}

std::vector<std::string> findItinerary(std::vector<std::vector<std::string>>& tickets) {
    std::vector<std::vector<std::string>> result;
    std::vector<std::string> path = {"JFK"};
    std::vector<bool> used(tickets.size(), false);
    
    backtrack(result, path, tickets, used);
    
    std::sort(result.begin(), result.end());
    return result[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ where $n$ is the number of tickets. This is because we are generating all permutations of the tickets.
> - **Space Complexity:** $O(n!)$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach generates all permutations, leading to high time and space complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a graph data structure to represent the airports and their connections. Then, perform a depth-first search (DFS) to find the lexicographically smallest itinerary.
- Detailed breakdown:
  1. Build a graph where each airport is a node, and each ticket represents a directed edge from the source to the destination airport.
  2. Sort the edges of each node in lexicographical order to ensure the DFS explores the smallest possible paths first.
  3. Perform DFS starting from the `JFK` airport, and whenever a node is visited, remove the edge that led to it to avoid revisiting the same path.
- Proof of optimality: This approach is optimal because it ensures that the lexicographically smallest itinerary is found by exploring all possible paths in the graph in a systematic and efficient manner.

```cpp
#include <vector>
#include <string>
#include <map>
#include <algorithm>

std::vector<std::string> findItinerary(std::vector<std::vector<std::string>>& tickets) {
    std::map<std::string, std::vector<std::string>> graph;
    for (const auto& ticket : tickets) {
        graph[ticket[0]].push_back(ticket[1]);
    }
    
    for (auto& node : graph) {
        std::sort(node.second.begin(), node.second.end());
    }
    
    std::vector<std::string> result;
    std::function<bool()> dfs = [&]() {
        if (result.size() == tickets.size() + 1) {
            return true;
        }
        
        for (auto it = graph[result.back()].begin(); it != graph[result.back()].end(); ++it) {
            if (*it != "") {
                std::string temp = *it;
                *it = "";
                result.push_back(temp);
                if (dfs()) {
                    return true;
                }
                *it = temp;
                result.pop_back();
            }
        }
        return false;
    };
    
    result.push_back("JFK");
    dfs();
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the edges of each node, where $n$ is the number of tickets.
> - **Space Complexity:** $O(n)$ for storing the graph and the result.
> - **Optimality proof:** This approach is optimal because it efficiently explores all possible itineraries in a systematic manner, ensuring the lexicographically smallest one is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph data structures, depth-first search, and sorting.
- Problem-solving patterns identified: Using graph theory to model complex problems and applying DFS to find solutions.
- Optimization techniques learned: Avoiding brute force by using efficient data structures and algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Failing to sort the edges of each node in the graph, which can lead to incorrect results.
- Edge cases to watch for: Handling cases where there are multiple possible itineraries and ensuring the lexicographically smallest one is returned.
- Performance pitfalls: Using brute force approaches that lead to high time and space complexities.
- Testing considerations: Thoroughly testing the solution with various inputs to ensure correctness and efficiency.