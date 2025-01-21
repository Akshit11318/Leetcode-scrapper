## Sequence Reconstruction
**Problem Link:** https://leetcode.com/problems/sequence-reconstruction/description

**Problem Statement:**
- Input: Two arrays `org` and `seqs`, where `org` is an original sequence and `seqs` is a list of sequences.
- Constraints: `org.length >= 1` and `1 <= org[i] <= 10^4`.
- Expected Output: Determine if `org` can be uniquely reconstructed from `seqs`.
- Key Requirements: 
    1. **Uniqueness**: The reconstruction must be unique.
    2. **Sequence Reconstruction**: The original sequence `org` must be reconstructible from the given sequences `seqs`.
- Edge Cases: 
    1. **Empty Sequence List**: If `seqs` is empty, reconstruction is impossible.
    2. **Inconsistent Sequences**: If `seqs` contains inconsistent or contradictory information, reconstruction is impossible.

### Brute Force Approach
**Explanation:**
- Initial Thought Process: Try all possible combinations of sequences to see if they can reconstruct the original sequence.
- Step-by-Step Breakdown: 
    1. Generate all permutations of the numbers from `1` to `10^4`.
    2. Check each permutation against the given sequences `seqs` to see if it matches all of them.
    3. If a permutation matches all sequences and is of the same length as `org`, it's a potential reconstruction.
    4. If only one such permutation exists, return `true`; otherwise, return `false`.
- Why This Approach Comes to Mind First: This approach is straightforward and checks all possibilities, but it's highly inefficient due to the large number of permutations.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
    int n = org.size();
    // Generate all permutations of numbers from 1 to n
    vector<int> perm(n);
    for (int i = 0; i < n; ++i) {
        perm[i] = i + 1;
    }
    do {
        bool match = true;
        for (const auto& seq : seqs) {
            int idx = 0;
            for (int num : seq) {
                auto it = find(perm.begin(), perm.end(), num);
                if (it == perm.end() || it - perm.begin() != idx) {
                    match = false;
                    break;
                }
                ++idx;
            }
            if (!match) break;
        }
        if (match) {
            // Check if this permutation is the only one
            bool unique = true;
            do {
                if (perm == org) continue;
                bool match2 = true;
                for (const auto& seq : seqs) {
                    int idx = 0;
                    for (int num : seq) {
                        auto it = find(perm.begin(), perm.end(), num);
                        if (it == perm.end() || it - perm.begin() != idx) {
                            match2 = false;
                            break;
                        }
                        ++idx;
                    }
                    if (!match2) break;
                }
                if (match2) {
                    unique = false;
                    break;
                }
            } while (next_permutation(perm.begin(), perm.end()));
            if (unique) return true;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m \cdot k)$, where $n$ is the length of `org`, $m$ is the number of sequences in `seqs`, and $k$ is the average length of sequences in `seqs`. This is due to generating all permutations and checking each against all sequences.
> - **Space Complexity:** $O(n)$ for storing the permutation and other variables.
> - **Why These Complexities Occur:** The brute force approach involves generating all permutations of numbers from `1` to `n`, which leads to a factorial time complexity. Checking each permutation against all sequences adds a linear factor for each sequence.

### Optimal Approach (Required)
**Explanation:**
- Key Insight: Instead of trying all permutations, we can use a graph-based approach. Construct a directed graph where each node represents a number from `1` to `10^4`, and there's a directed edge from node `A` to node `B` if `A` appears before `B` in any sequence.
- Detailed Breakdown:
    1. Construct the graph based on the sequences.
    2. Perform a topological sort on the graph. If the graph contains a cycle or more than one node with in-degree `0`, the reconstruction is impossible.
    3. Check if the sorted nodes match the original sequence `org`.
- Proof of Optimality: This approach is optimal because it directly addresses the problem by constructing a graph that represents the relationships between numbers as given by the sequences. It avoids unnecessary permutations and directly checks for a valid reconstruction.

```cpp
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

bool sequenceReconstruction(vector<int>& org, vector<vector<int>>& seqs) {
    unordered_map<int, vector<int>> graph;
    unordered_map<int, int> inDegree;
    
    // Build the graph and calculate in-degrees
    for (const auto& seq : seqs) {
        for (int i = 0; i < seq.size() - 1; ++i) {
            graph[seq[i]].push_back(seq[i + 1]);
            inDegree[seq[i + 1]]++;
        }
    }
    
    // Find nodes with in-degree 0
    queue<int> q;
    for (int num : org) {
        if (inDegree[num] == 0) {
            q.push(num);
        }
    }
    
    vector<int> result;
    while (!q.empty()) {
        if (q.size() > 1) return false; // More than one node with in-degree 0
        int node = q.front();
        q.pop();
        result.push_back(node);
        
        for (int neighbor : graph[node]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    return result == org;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \cdot k)$, where $n$ is the length of `org`, $m` is the number of sequences in `seqs`, and $k` is the average length of sequences in `seqs`. This is due to building the graph and performing the topological sort.
> - **Space Complexity:** $O(n + m \cdot k)$ for storing the graph and other variables.
> - **Optimality Proof:** This approach is optimal because it directly constructs a graph representing the sequence relationships and checks for a valid reconstruction without unnecessary permutations, leading to a linear time complexity with respect to the input size.

### Final Notes

**Learning Points:**
- **Graph-Based Approach**: Using graphs to represent relationships between elements can significantly simplify complex problems.
- **Topological Sort**: A powerful tool for ordering elements based on their dependencies.
- **Optimization Techniques**: Directly addressing the problem's constraints and relationships can lead to highly efficient solutions.

**Mistakes to Avoid:**
- **Brute Force**: Avoid trying all permutations or combinations when a more structured approach is possible.
- **Inefficient Data Structures**: Choose data structures that fit the problem, such as graphs for representing relationships.
- **Ignoring Problem Constraints**: Always consider the constraints given in the problem to optimize the solution.