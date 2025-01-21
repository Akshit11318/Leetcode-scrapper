## Longest Common Suffix Queries
**Problem Link:** https://leetcode.com/problems/longest-common-suffix-queries/description

**Problem Statement:**
- Input: A list of strings `words` and a list of queries `queries`.
- Constraints: Each word in `words` and each query in `queries` consists of only lowercase English letters.
- Expected Output: For each query, find the longest common suffix among all words in `words` that end with the query string.
- Key Requirements:
  - Handle cases where no word ends with the query string.
  - Consider the query string as a suffix of itself.
- Example Test Cases:
  - Input: `words = ["ab","abc","abcd"], queries = ["d","c","b","a"]`
    - Output: `[1,2,3,0]`
    - Explanation: The longest common suffix for each query is as follows:
      - For "d", only "abcd" ends with "d", so the longest common suffix is 1.
      - For "c", both "abc" and "abcd" end with "c", so the longest common suffix is 2.
      - For "b", all three words end with "b", so the longest common suffix is 3.
      - For "a", none of the words end with "a", so the longest common suffix is 0.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking each word against each query to find the longest common suffix.
- Step-by-step breakdown:
  1. Iterate over each query.
  2. For each query, iterate over each word in `words`.
  3. Check if the word ends with the query string.
  4. If it does, find the length of the common suffix.
  5. Keep track of the maximum length of the common suffix found for each query.

```cpp
vector<int> longestCommonSuffix(vector<string>& words, vector<string>& queries) {
    vector<int> result;
    for (const string& query : queries) {
        int maxLen = 0;
        for (const string& word : words) {
            if (word.size() >= query.size() && word.compare(word.size() - query.size(), query.size(), query) == 0) {
                maxLen = max(maxLen, (int)query.size());
            }
        }
        result.push_back(maxLen);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ is the number of queries, $m$ is the number of words, and $k$ is the maximum length of a query. This is because for each query, we potentially check every word, and for each word, we check if it ends with the query string, which takes $k$ time.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops over queries and words, and the string comparison operation.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a **suffix tree** or **trie** data structure to store the words, but since we are only interested in suffixes, a simpler approach involves reversing the words and queries, then using a prefix tree (trie) to find the longest common prefix among words that match a query.
- Detailed breakdown:
  1. Reverse each word and each query.
  2. Build a trie from the reversed words.
  3. For each reversed query, traverse the trie to find the depth of the longest common prefix, which corresponds to the longest common suffix in the original strings.

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int count = 0;
};

vector<int> longestCommonSuffix(vector<string>& words, vector<string>& queries) {
    TrieNode* root = new TrieNode();
    for (string& word : words) {
        reverse(word.begin(), word.end());
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->count++;
        }
    }
    
    vector<int> result;
    for (string& query : queries) {
        reverse(query.begin(), query.end());
        TrieNode* node = root;
        int depth = 0;
        for (char c : query) {
            if (!node->children.count(c)) break;
            node = node->children[c];
            depth++;
        }
        result.push_back(depth);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k + m \cdot k)$ where $n$ is the number of queries, $m$ is the number of words, and $k$ is the maximum length of a word or query. This is because we spend time inserting words into the trie and then querying the trie.
> - **Space Complexity:** $O(m \cdot k)$ for storing the trie.
> - **Optimality proof:** This approach is optimal because it reduces the problem to finding the longest common prefix in a trie, which can be done in linear time with respect to the length of the input strings.

---

### Final Notes

**Learning Points:**
- Using a trie data structure for efficient prefix matching.
- Reversing strings to convert a suffix problem into a prefix problem.
- Understanding the trade-offs between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the reversal of strings as a simplification step.
- Overlooking the potential for using a trie for efficient string matching.
- Failing to account for edge cases, such as empty strings or queries that do not match any word.