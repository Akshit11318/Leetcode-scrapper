## Groups of Strings
**Problem Link:** https://leetcode.com/problems/groups-of-strings/description

**Problem Statement:**
- Input: A list of strings `words`.
- Constraints: Each string is composed of lowercase English letters.
- Expected Output: The number of groups that can be formed from the given strings such that every string in a group is a prefix of another string in the same group.
- Key Requirements: A group can have any number of strings, but every string in a group must be a prefix of another string in the same group.
- Edge Cases: The input list can be empty, or it can contain a single string. The strings can be of varying lengths.

**Example Test Cases:**
1. Input: `words = ["a","b","ab","abc"]`
   Output: `2`
   Explanation: Two groups can be formed: `["a","ab","abc"]` and `["b"]`.
2. Input: `words = ["abcd","xyz","abc","abcd"]`
   Output: `2`
   Explanation: Two groups can be formed: `["abcd","abcd"]` and `["xyz"]`, `["abc"]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible combination of strings to form groups.
- For each string, we check if it can be a prefix of any other string in the list.
- We then try to form groups by including strings that are prefixes of other strings.

```cpp
class Solution {
public:
    int numGroups(vector<string>& words) {
        int n = words.size();
        vector<bool> used(n, false);
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (!used[i]) {
                bool found = false;
                for (int j = 0; j < n; j++) {
                    if (i != j && !used[j] && isPrefix(words[i], words[j])) {
                        used[j] = true;
                        found = true;
                    }
                }
                if (found) {
                    count++;
                }
            }
        }
        
        return count;
    }
    
    bool isPrefix(const string& s1, const string& s2) {
        if (s1.size() > s2.size()) return false;
        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] != s2[i]) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we are comparing each string with every other string.
> - **Space Complexity:** $O(n)$ for the `used` vector.
> - **Why these complexities occur:** The brute force approach involves checking every possible pair of strings, leading to a quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a `Trie` data structure to efficiently store and compare the strings.
- We insert each string into the Trie and then traverse the Trie to find groups of strings where every string is a prefix of another string.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

class Solution {
public:
    int numGroups(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEndOfWord = true;
        }
        
        int count = 0;
        for (const string& word : words) {
            TrieNode* node = root;
            bool found = false;
            for (char c : word) {
                node = node->children[c];
                if (node->isEndOfWord) {
                    found = true;
                    break;
                }
            }
            if (found) {
                count++;
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we are inserting each string into the Trie and then traversing the Trie for each string.
> - **Space Complexity:** $O(n \cdot m)$ for the Trie data structure.
> - **Optimality proof:** The Trie data structure allows us to efficiently store and compare the strings, reducing the time complexity from $O(n^2 \cdot m)$ to $O(n \cdot m)$.

---

### Final Notes

**Learning Points:**
- The use of a Trie data structure to efficiently store and compare strings.
- The importance of choosing the right data structure for the problem.
- The trade-off between time and space complexity.

**Mistakes to Avoid:**
- Not considering the use of a Trie data structure.
- Not optimizing the comparison of strings.
- Not handling edge cases correctly.

By following this approach, we can efficiently solve the problem and avoid common mistakes. The use of a Trie data structure is key to achieving the optimal time complexity of $O(n \cdot m)$.