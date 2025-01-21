## Longest String Chain

**Problem Link:** [https://leetcode.com/problems/longest-string-chain/description](https://leetcode.com/problems/longest-string-chain/description)

**Problem Statement:**
- Input: A list of strings `words`.
- Constraints: Each string consists of lowercase English letters.
- Expected Output: The length of the longest string chain.
- Key Requirements: A string can be inserted into another string if it is possible to add a character to the string to get the other string.
- Edge Cases: An empty input list, a list with a single string, and a list with multiple strings of varying lengths.

**Example Test Cases:**
- Input: `["a","b","ba","bca","bda","bdca"]`
- Output: `4`
- Explanation: One of the longest string chains is `"a" -> "ba" -> "bda" -> "bdca"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible combinations of strings to form a chain.
- For each string, try adding a character to form a new string and check if the new string exists in the list.
- Keep track of the longest chain found.

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        int n = words.size();
        sort(words.begin(), words.end(), [](string a, string b) { return a.size() < b.size(); });
        
        int res = 0;
        for (int i = 0; i < n; i++) {
            int maxLen = 1;
            for (int j = 0; j < i; j++) {
                if (words[j].size() + 1 == words[i].size() && isPredecessor(words[j], words[i])) {
                    maxLen = max(maxLen, 1 + longestStrChainHelper(words, j));
                }
            }
            res = max(res, maxLen);
        }
        return res;
    }
    
    bool isPredecessor(string a, string b) {
        int i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a[i] == b[j]) {
                i++;
            }
            j++;
        }
        return i == a.size();
    }
    
    int longestStrChainHelper(vector<string>& words, int index) {
        int n = words.size();
        int maxLen = 0;
        for (int i = index + 1; i < n; i++) {
            if (words[index].size() + 1 == words[i].size() && isPredecessor(words[index], words[i])) {
                maxLen = max(maxLen, 1 + longestStrChainHelper(words, i));
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because for each string, we are checking all previous strings and comparing them character by character.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves nested loops and character comparisons, leading to high time complexity. The space complexity is low because we are only using a constant amount of space to store variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the length of the longest chain ending at each string.
- Sort the strings by length and for each string, check all previous strings of length one less.
- If a previous string is a predecessor of the current string, update the length of the longest chain ending at the current string.

```cpp
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        int n = words.size();
        sort(words.begin(), words.end(), [](string a, string b) { return a.size() < b.size(); });
        
        unordered_map<string, int> dp;
        int res = 0;
        for (string word : words) {
            dp[word] = 1;
            for (int i = 0; i < word.size(); i++) {
                string predecessor = word.substr(0, i) + word.substr(i + 1);
                if (dp.find(predecessor) != dp.end()) {
                    dp[word] = max(dp[word], dp[predecessor] + 1);
                }
            }
            res = max(res, dp[word]);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m^2)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because for each string, we are generating all possible predecessors and checking if they exist in the map.
> - **Space Complexity:** $O(n)$, as we are storing the length of the longest chain ending at each string in the map.
> - **Optimality proof:** This approach is optimal because we are only checking each string once and storing the result in the map, avoiding redundant computations. The time complexity is reduced by using a map to store the predecessors, allowing for constant time lookups.

---

### Final Notes

**Learning Points:**
- The importance of sorting the input to ensure that we are always checking predecessors of a string.
- The use of dynamic programming to store and reuse the results of subproblems.
- The optimization of using a map to store the length of the longest chain ending at each string.

**Mistakes to Avoid:**
- Not sorting the input, leading to incorrect results.
- Not using dynamic programming, leading to redundant computations and high time complexity.
- Not using a map to store the predecessors, leading to high time complexity due to repeated string comparisons.