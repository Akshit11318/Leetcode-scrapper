## Lexicographically Smallest String After Applying a Swap Operation
**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description

**Problem Statement:**
- Given a string `s` and an integer array `indices` of length `n`, where `n` is the length of `s`, find the lexicographically smallest string after applying a swap operation.
- Each `indices[i]` represents the index of the character in `s` that will be swapped with the character at index `i`.
- The goal is to find the lexicographically smallest string after applying the swap operation.

**Example Test Cases:**
- Input: `s = "dcab", indices = [0,1,2,3]`
  - Output: `"bacd"`
- Input: `s = "dcab", indices = [0,3,2,1]`
  - Output: `"acbd"`
- Input: `s = "cba", indices = [0,1,2]`
  - Output: `"abc"`

### Brute Force Approach
**Explanation:**
- The initial thought process is to simply apply the swap operation to the input string `s` based on the provided `indices`.
- This involves iterating through the `indices` array and swapping the characters at the corresponding indices in the string `s`.

```cpp
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<int>& indices) {
        string result = s;
        for (int i = 0; i < indices.size(); i++) {
            swap(result[i], result[indices[i]]);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating through the `indices` array once.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the `indices` array, and the space complexity is constant because we are modifying the input string in-place.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a Union-Find data structure to group the indices that will be swapped together.
- We then sort the characters within each group and assign them back to their original positions.

```cpp
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<int>& indices) {
        int n = s.size();
        vector<int> parent(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // Union-Find to group indices
        for (int i = 0; i < indices.size(); i++) {
            unionSet(parent, i, indices[i]);
        }
        
        // Sort characters within each group
        vector<vector<char>> groups(n);
        for (int i = 0; i < n; i++) {
            groups[find(parent, i)].push_back(s[i]);
        }
        
        for (int i = 0; i < n; i++) {
            sort(groups[i].begin(), groups[i].end());
        }
        
        // Assign sorted characters back to original positions
        string result = s;
        vector<int> index(n, 0);
        for (int i = 0; i < n; i++) {
            result[i] = groups[find(parent, i)][index[find(parent, i)]];
            index[find(parent, i)]++;
        }
        
        return result;
    }
    
    int find(vector<int>& parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
    
    void unionSet(vector<int>& parent, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the string `s`. This is because we are sorting the characters within each group.
> - **Space Complexity:** $O(n)$, as we are using additional space to store the Union-Find data structure and the groups of characters.
> - **Optimality proof:** This approach is optimal because it ensures that the characters within each group are in the lexicographically smallest order, and it does so in a time-efficient manner.

### Final Notes

**Learning Points:**
- The importance of using a Union-Find data structure to group related elements.
- How to sort characters within each group to achieve the lexicographically smallest string.
- The use of a `find` function to determine the root of a set and a `unionSet` function to merge two sets.

**Mistakes to Avoid:**
- Not using a Union-Find data structure to group the indices, leading to incorrect results.
- Not sorting the characters within each group, resulting in a non-lexicographically smallest string.
- Not using a `find` function to determine the root of a set, leading to incorrect assignments of characters.