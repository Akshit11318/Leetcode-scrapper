## Similar String Groups

**Problem Link:** https://leetcode.com/problems/similar-string-groups/description

**Problem Statement:**
- Input: A list of strings `strs`.
- Constraints: The length of `strs` is between 1 and 100, and the length of each string in `strs` is between 1 and 10.
- Expected Output: The number of groups of similar strings in `strs`.
- Key Requirements:
  - Two strings are similar if they are the same length and differ by at most two characters.
  - Two strings are in the same group if they are similar to at least one string in the group.
- Edge Cases:
  - If two strings have different lengths, they cannot be similar.
  - If a string is similar to itself, it is considered part of the same group.
- Example Test Cases:
  - Input: `["tars","rats","arts","star"]`
    - Output: `2`
    - Explanation: The two groups are `["tars","rats","arts"]` and `["star"]`.
  - Input: `["omv","ovm"]`
    - Output: `1`
    - Explanation: The two strings are similar and form one group.

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: To determine the number of similar string groups, we can compare each string with every other string to check if they are similar.
- Step-by-Step Breakdown:
  1. Create a function to check if two strings are similar.
  2. Iterate through each pair of strings in the input list.
  3. If two strings are similar, group them together.
  4. Count the number of distinct groups.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

bool areSimilar(const std::string& s1, const std::string& s2) {
    if (s1.length() != s2.length()) return false;
    int diffCount = 0;
    for (int i = 0; i < s1.length(); i++) {
        if (s1[i] != s2[i]) diffCount++;
        if (diffCount > 2) return false;
    }
    return true;
}

int numSimilarGroups(std::vector<std::string>& strs) {
    int n = strs.size();
    std::unordered_map<std::string, std::vector<std::string>> groups;
    for (int i = 0; i < n; i++) {
        bool foundGroup = false;
        for (auto& group : groups) {
            if (areSimilar(strs[i], group.first)) {
                group.second.push_back(strs[i]);
                foundGroup = true;
                break;
            }
        }
        if (!foundGroup) {
            groups[strs[i]] = {strs[i]};
        }
    }
    // This approach does not efficiently handle the grouping of similar strings
    // and can lead to incorrect results due to its simplistic comparison strategy.
    return groups.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is due to comparing each pair of strings.
> - **Space Complexity:** $O(n \cdot m)$, for storing the groups and their members.
> - **Why these complexities occur:** The brute force approach involves comparing each string with every other string, leading to a high time complexity. The space complexity is high because we store all strings in groups.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Utilize a union-find data structure to efficiently group similar strings.
- Detailed Breakdown:
  1. Initialize a union-find data structure with each string as its own group.
  2. Compare each pair of strings to check if they are similar.
  3. If two strings are similar, union their groups.
  4. Count the number of distinct groups (i.e., the number of connected components in the union-find data structure).

```cpp
class UnionFind {
public:
    std::vector<int> parent;
    std::vector<int> rank;

    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int numSimilarGroups(std::vector<std::string>& strs) {
    int n = strs.size();
    UnionFind uf(n);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (areSimilar(strs[i], strs[j])) {
                uf.unionSets(i, j);
            }
        }
    }
    std::set<int> groups;
    for (int i = 0; i < n; i++) {
        groups.insert(uf.find(i));
    }
    return groups.size();
}

bool areSimilar(const std::string& s1, const std::string& s2) {
    if (s1.length() != s2.length()) return false;
    int diffCount = 0;
    for (int i = 0; i < s1.length(); i++) {
        if (s1[i] != s2[i]) diffCount++;
        if (diffCount > 2) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m + n \cdot \alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, which grows very slowly. The $n^2 \cdot m$ term comes from comparing each pair of strings, and the $n \cdot \alpha(n)$ term comes from the union-find operations.
> - **Space Complexity:** $O(n \cdot m + n)$, for storing the strings and the union-find data structure.
> - **Optimality Proof:** The optimal approach uses a union-find data structure to efficiently group similar strings, reducing the time complexity compared to the brute force approach. This is the best possible complexity for this problem, as we must compare each pair of strings to determine similarity.

---

### Final Notes

**Learning Points:**
- Key Algorithmic Concepts: Union-find data structure, string comparison.
- Problem-Solving Patterns: Using a union-find data structure to group similar elements.
- Optimization Techniques: Reducing the time complexity by using an efficient data structure.
- Similar Problems to Practice: Other problems involving grouping similar elements, such as graph connectivity problems.

**Mistakes to Avoid:**
- Common Implementation Errors: Incorrectly implementing the union-find data structure or the string comparison function.
- Edge Cases to Watch For: Handling strings with different lengths or characters.
- Performance Pitfalls: Using an inefficient data structure or algorithm, leading to high time or space complexity.
- Testing Considerations: Thoroughly testing the implementation with different input cases to ensure correctness.