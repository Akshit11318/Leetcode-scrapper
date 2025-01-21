## Smallest String with Swaps
**Problem Link:** https://leetcode.com/problems/smallest-string-with-swaps/description

**Problem Statement:**
- Input format and constraints: The problem takes in a string `s` and a 2D array `pairs` where each pair represents two indices in the string that can be swapped.
- Expected output format: The smallest possible string that can be achieved by performing the given swaps.
- Key requirements and edge cases to consider: We need to consider all possible swaps and ensure that we are finding the smallest possible string. Edge cases include empty strings, no swaps, and multiple swaps involving the same character.
- Example test cases with explanations: For example, if we have the string "dcab" and the pairs [[0,3],[1,2]], the smallest possible string after performing the swaps is "bacd".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible swaps and checking the resulting string.
- Step-by-step breakdown of the solution:
  1. Initialize the result string as the input string.
  2. Generate all permutations of the string.
  3. For each permutation, check if it can be achieved by performing the given swaps.
  4. If it can, update the result string if the current permutation is smaller.
- Why this approach comes to mind first: This approach is straightforward and involves trying all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
    string result = s;
    vector<string> permutations;
    permute(s, 0, s.size() - 1, permutations);
    for (auto& permutation : permutations) {
        if (canBeAchieved(permutation, pairs)) {
            if (permutation < result) {
                result = permutation;
            }
        }
    }
    return result;
}

void permute(string s, int left, int right, vector<string>& permutations) {
    if (left == right) {
        permutations.push_back(s);
    } else {
        for (int i = left; i <= right; i++) {
            swap(s[left], s[i]);
            permute(s, left + 1, right, permutations);
            swap(s[left], s[i]); // backtrack
        }
    }
}

bool canBeAchieved(string s, vector<vector<int>>& pairs) {
    // This function checks if the given string can be achieved by performing the swaps
    // It's not implemented here as it's complex and not the focus of this problem
    return true; // placeholder
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ where $n$ is the length of the string, due to generating all permutations.
> - **Space Complexity:** $O(n!)$ for storing all permutations.
> - **Why these complexities occur:** Generating all permutations of a string of length $n$ results in $n!$ possible permutations, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a Union-Find data structure to group characters that can be swapped together.
- Detailed breakdown of the approach:
  1. Initialize a Union-Find data structure with each character in its own group.
  2. Iterate through the pairs and union the groups of the two characters in each pair.
  3. Iterate through the string and for each character, find its group and sort the characters in the group.
  4. Update the string with the sorted characters.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string and the pairs, resulting in a time complexity of $O(n + m \alpha(n))$ where $n$ is the length of the string and $m$ is the number of pairs.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};

string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
    int n = s.size();
    UnionFind uf(n);
    for (auto& pair : pairs) {
        uf.union_(pair[0], pair[1]);
    }
    vector<vector<char>> groups(n);
    for (int i = 0; i < n; i++) {
        groups[uf.find(i)].push_back(s[i]);
    }
    for (auto& group : groups) {
        sort(group.begin(), group.end());
    }
    string result = s;
    for (int i = 0; i < n; i++) {
        int groupIndex = uf.find(i);
        result[i] = groups[groupIndex].back();
        groups[groupIndex].pop_back();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$ where $n$ is the length of the string and $m$ is the number of pairs. $\alpha(n)$ is the inverse Ackermann function, which grows very slowly.
> - **Space Complexity:** $O(n + m)$ for the Union-Find data structure and the groups.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and the pairs, resulting in a time complexity of $O(n + m \alpha(n))$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-Find data structure, sorting, and string manipulation.
- Problem-solving patterns identified: Using a Union-Find data structure to group related elements together.
- Optimization techniques learned: Using a Union-Find data structure to reduce the time complexity from exponential to linear.
- Similar problems to practice: Problems involving graph traversal, Union-Find, and string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty string or no pairs.
- Edge cases to watch for: Empty string, no pairs, and multiple swaps involving the same character.
- Performance pitfalls: Using an exponential time complexity algorithm, such as generating all permutations.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.