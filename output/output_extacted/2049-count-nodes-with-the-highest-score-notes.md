## Count Nodes with the Highest Score
**Problem Link:** https://leetcode.com/problems/count-nodes-with-the-highest-score/description

**Problem Statement:**
- Given an array `edges` where `edges[i] = [a, b]`, representing a directed edge from node `a` to node `b`, and an integer `n`, representing the number of nodes.
- Each node has an initial score of 1.
- For each edge, the score of the node at the start of the edge increases by 1.
- Find the maximum score that can be achieved and count the number of nodes with that score.
- Return the count of nodes with the maximum score.

**Input Format and Constraints:**
- `1 <= n <= 10^4`
- `0 <= edges.length <= 10^4`
- `edges[i].length == 2`
- `0 <= a, b < n`
- `a != b`

**Expected Output Format:**
- Return the count of nodes with the maximum score.

**Key Requirements and Edge Cases:**
- Handle cases where a node has no incoming or outgoing edges.
- Consider cases where multiple nodes have the same maximum score.

**Example Test Cases:**
- `n = 4, edges = [[1,0],[1,2],[1,3]]`
- `n = 2, edges = [[0,1]]`
- `n = 4, edges = [[1,0],[2,1],[3,2]]`

### Brute Force Approach
**Explanation:**
- Initialize an array `score` of size `n` with all elements as 1, representing the initial score of each node.
- Iterate over the `edges` array, and for each edge, increment the score of the node at the start of the edge by 1.
- After processing all edges, find the maximum score in the `score` array.
- Count the number of nodes with the maximum score.

```cpp
vector<int> countHighestScoreNodes(vector<vector<int>>& edges, int n) {
    vector<int> score(n, 1);
    for (auto& edge : edges) {
        score[edge[0]]++;
    }
    int maxScore = *max_element(score.begin(), score.end());
    int count = 0;
    for (int s : score) {
        if (s == maxScore) count++;
    }
    return {count};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we iterate over the `edges` array once and then over the `score` array twice.
> - **Space Complexity:** $O(n)$, because we use a `score` array of size $n$.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node and each edge. The space complexity is linear because we need to store the score of each node.

### Optimal Approach (Required)
**Explanation:**
- We can use an adjacency list representation of the graph to store the outgoing edges for each node.
- Then, we can iterate over the nodes and for each node, calculate its score as the number of outgoing edges plus 1.
- We can use a `map` to store the frequency of each score.
- Finally, we can find the maximum score and count the number of nodes with that score.

```cpp
vector<int> countHighestScoreNodes(vector<vector<int>>& edges, int n) {
    vector<vector<int>> graph(n);
    for (auto& edge : edges) {
        graph[edge[0]].push_back(edge[1]);
    }
    map<int, int> scoreCount;
    for (int i = 0; i < n; i++) {
        scoreCount[graph[i].size() + 1]++;
    }
    int maxScore = 0;
    int count = 0;
    for (auto& [score, freq] : scoreCount) {
        if (score > maxScore) {
            maxScore = score;
            count = freq;
        }
    }
    return {count};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes and $m$ is the number of edges, because we iterate over the `edges` array once and then over the `graph` and `scoreCount` data structures.
> - **Space Complexity:** $O(n + m)$, because we use a `graph` data structure to store the outgoing edges for each node and a `scoreCount` map to store the frequency of each score.
> - **Optimality proof:** This approach is optimal because we need to process each node and each edge at least once to calculate the scores and count the number of nodes with the maximum score.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: graph traversal, score calculation, and frequency counting.
- Problem-solving patterns identified: using adjacency list representation, calculating scores, and counting frequencies.
- Optimization techniques learned: using `map` to store frequency of scores, and iterating over data structures only once.

**Mistakes to Avoid:**
- Not handling cases where a node has no incoming or outgoing edges.
- Not considering cases where multiple nodes have the same maximum score.
- Not using efficient data structures to store scores and frequencies.