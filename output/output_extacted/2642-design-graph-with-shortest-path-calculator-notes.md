## Design Graph with Shortest Path Calculator

**Problem Link:** https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a graph class with methods to add edges and calculate the shortest path between two nodes using Dijkstra's algorithm. The graph is represented as an adjacency list, where each node is associated with a list of its neighboring nodes and the corresponding edge weights.
- Expected output format: The `addEdge` method adds a directed edge from node `node1` to node `node2` with a given weight, while the `shortestPath` method returns the shortest path from node `start` to node `end`.
- Key requirements and edge cases to consider: The graph may contain negative-weight edges, but Dijkstra's algorithm only works with non-negative weights. Therefore, we need to ensure that all edge weights are non-negative.
- Example test cases with explanations:
  - Creating a graph with multiple nodes and edges, then calculating the shortest path between two nodes.
  - Handling cases where there is no path between the start and end nodes.
  - Ensuring that the graph class can handle a large number of nodes and edges.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to use a brute force method to calculate the shortest path between two nodes. This involves exploring all possible paths from the start node to the end node and selecting the one with the minimum total weight.
- Step-by-step breakdown of the solution:
  1. Create an adjacency list representation of the graph.
  2. Implement a recursive function to explore all possible paths from the start node to the end node.
  3. Calculate the total weight of each path and keep track of the minimum weight found so far.
- Why this approach comes to mind first: The brute force approach is often the first solution that comes to mind because it is straightforward and easy to implement. However, it is not efficient for large graphs due to its exponential time complexity.

```cpp
class Graph {
public:
    vector<vector<pair<int, int>>> adjacencyList;
    Graph(int numNodes) : adjacencyList(numNodes) {}
    
    void addEdge(int node1, int node2, int weight) {
        adjacencyList[node1].push_back({node2, weight});
    }
    
    int shortestPath(int start, int end) {
        int minWeight = INT_MAX;
        function<void(int, int, int)> dfs = [&](int node, int weight, vector<int> path) {
            if (node == end) {
                minWeight = min(minWeight, weight);
                return;
            }
            for (auto& neighbor : adjacencyList[node]) {
                if (find(path.begin(), path.end(), neighbor.first) == path.end()) {
                    dfs(neighbor.first, weight + neighbor.second, path);
                }
            }
        };
        dfs(start, 0, {start});
        return minWeight == INT_MAX ? -1 : minWeight;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of nodes in the graph. This is because the brute force approach explores all possible paths from the start node to the end node.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the graph. This is because the adjacency list representation of the graph requires O(n) space.
> - **Why these complexities occur:** The brute force approach has exponential time complexity because it explores all possible paths from the start node to the end node. This results in a large number of recursive function calls, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Dijkstra's algorithm is an efficient method for finding the shortest path between two nodes in a weighted graph. It works by maintaining a priority queue of nodes to visit, where the priority of each node is its minimum distance from the start node.
- Detailed breakdown of the approach:
  1. Create an adjacency list representation of the graph.
  2. Implement Dijkstra's algorithm using a priority queue to keep track of nodes to visit.
  3. Calculate the minimum distance from the start node to each node in the graph.
- Proof of optimality: Dijkstra's algorithm has a time complexity of $O((n + m) \log n)$, where n is the number of nodes and m is the number of edges in the graph. This is because the algorithm uses a priority queue to efficiently select the next node to visit.
- Why further optimization is impossible: Dijkstra's algorithm is already an optimal solution for finding the shortest path between two nodes in a weighted graph. Further optimization is not possible because the algorithm has a guaranteed time complexity that is optimal for this problem.

```cpp
class Graph {
public:
    vector<vector<pair<int, int>>> adjacencyList;
    Graph(int numNodes) : adjacencyList(numNodes) {}
    
    void addEdge(int node1, int node2, int weight) {
        adjacencyList[node1].push_back({node2, weight});
    }
    
    int shortestPath(int start, int end) {
        vector<int> distances(adjacencyList.size(), INT_MAX);
        distances[start] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, start});
        
        while (!pq.empty()) {
            int node = pq.top().second;
            int weight = pq.top().first;
            pq.pop();
            
            if (node == end) {
                return weight;
            }
            
            if (weight > distances[node]) {
                continue;
            }
            
            for (auto& neighbor : adjacencyList[node]) {
                int newWeight = weight + neighbor.second;
                if (newWeight < distances[neighbor.first]) {
                    distances[neighbor.first] = newWeight;
                    pq.push({newWeight, neighbor.first});
                }
            }
        }
        
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O((n + m) \log n)$, where n is the number of nodes and m is the number of edges in the graph. This is because Dijkstra's algorithm uses a priority queue to efficiently select the next node to visit.
> - **Space Complexity:** $O(n + m)$, where n is the number of nodes and m is the number of edges in the graph. This is because the adjacency list representation of the graph requires O(n + m) space.
> - **Optimality proof:** Dijkstra's algorithm is an optimal solution for finding the shortest path between two nodes in a weighted graph because it has a guaranteed time complexity that is optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dijkstra's algorithm, priority queues, and adjacency list representation of graphs.
- Problem-solving patterns identified: Using Dijkstra's algorithm to find the shortest path between two nodes in a weighted graph.
- Optimization techniques learned: Using a priority queue to efficiently select the next node to visit in Dijkstra's algorithm.
- Similar problems to practice: Finding the shortest path between two nodes in an unweighted graph, finding the minimum spanning tree of a graph, and solving the traveling salesman problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for negative-weight edges, not handling the case where there is no path between the start and end nodes, and not using a priority queue to efficiently select the next node to visit.
- Edge cases to watch for: Handling the case where the start node is the same as the end node, handling the case where the graph is empty, and handling the case where the graph contains negative-weight edges.
- Performance pitfalls: Not using a priority queue to efficiently select the next node to visit, not using an adjacency list representation of the graph, and not handling the case where the graph contains negative-weight edges.
- Testing considerations: Testing the implementation with different types of graphs, testing the implementation with different start and end nodes, and testing the implementation with different edge weights.