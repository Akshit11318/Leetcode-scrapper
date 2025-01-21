## Longest Common Subpath

**Problem Link:** https://leetcode.com/problems/longest-common-subpath/description

**Problem Statement:**
- Input: Two integer arrays `path1` and `path2` representing two paths where each element is a node in the path.
- Constraints: `1 <= path1.length, path2.length <= 10^5`, `1 <= path1[i], path2[i] <= 10^6`.
- Expected Output: The length of the longest common subpath.
- Key Requirements: Find the longest common subpath between the two given paths.
- Edge Cases: Paths can have different lengths, and nodes can have different values.

**Example Test Cases:**
- `path1 = [1,3,5,7], path2 = [2,3,5,6]`, Output: `3` (The common subpath is `[3,5]`).
- `path1 = [1,2,3,4], path2 = [1,2,4,5]`, Output: `2` (The common subpath is `[1,2]`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subpath in both `path1` and `path2` to find the longest common one.
- This approach involves generating all possible subpaths from both arrays and comparing them to find matches.

```cpp
class Solution {
public:
    int longestCommonSubpath(int n, vector<int>& path1, vector<int>& path2) {
        int maxLength = 0;
        for (int len = 1; len <= min(path1.size(), path2.size()); len++) {
            for (int i = 0; i <= path1.size() - len; i++) {
                for (int j = 0; j <= path2.size() - len; j++) {
                    bool match = true;
                    for (int k = 0; k < len; k++) {
                        if (path1[i + k] != path2[j + k]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        maxLength = max(maxLength, len);
                    }
                }
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot min(n, m)^2)$ where $n$ and $m$ are the lengths of `path1` and `path2`, respectively. This is because for each possible length of subpath, we are generating all possible subpaths and comparing them.
> - **Space Complexity:** $O(1)$ as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate and compare all possible subpaths, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a `hashmap` to store the hash values of subpaths in `path1` and then checking for these hash values in `path2`.
- We can use a rolling hash technique to efficiently calculate the hash values of subpaths.

```cpp
class Solution {
public:
    int longestCommonSubpath(int n, vector<int>& path1, vector<int>& path2) {
        int maxLength = 0;
        for (int len = 1; len <= min(path1.size(), path2.size()); len++) {
            unordered_map<int, int> hashCount;
            for (int i = 0; i <= path1.size() - len; i++) {
                int hashVal = 0;
                for (int j = 0; j < len; j++) {
                    hashVal = hashVal * 1000001 + path1[i + j];
                }
                hashCount[hashVal]++;
            }
            for (int i = 0; i <= path2.size() - len; i++) {
                int hashVal = 0;
                for (int j = 0; j < len; j++) {
                    hashVal = hashVal * 1000001 + path2[i + j];
                }
                if (hashCount.find(hashVal) != hashCount.end()) {
                    maxLength = max(maxLength, len);
                }
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot min(n, m))$ where $n$ and $m$ are the lengths of `path1` and `path2`, respectively. This is because we are using a hashmap to store and look up hash values.
> - **Space Complexity:** $O(n \cdot min(n, m))$ for storing the hashmap.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of comparing subpaths from $O(n^2)$ to $O(1)$ using the hashmap, resulting in an overall time complexity of $O(n \cdot m \cdot min(n, m))$.

---

### Final Notes

**Learning Points:**
- The importance of using hashmaps for efficient lookup and storage.
- The application of rolling hash technique for calculating hash values of subpaths.
- Optimization techniques for reducing time complexity.

**Mistakes to Avoid:**
- Not considering the use of hashmaps for efficient lookup.
- Not applying rolling hash technique for calculating hash values.
- Not optimizing the algorithm to reduce time complexity.