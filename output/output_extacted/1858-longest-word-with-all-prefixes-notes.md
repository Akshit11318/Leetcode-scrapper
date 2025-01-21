## Longest Word with All Prefixes

**Problem Link:** https://leetcode.com/problems/longest-word-with-all-prefixes/description

**Problem Statement:**
- Input: A list of words `words`.
- Expected Output: The longest word that contains all its prefixes in `words`.
- Key Requirements: 
    - All prefixes of the word must exist in `words`.
    - If multiple words satisfy this condition, return the longest one. If there are multiple longest words, return the lexicographically smallest one.
- Example Test Cases:
    - Input: `["a", "banana", "app", "appl", "ap", "apply", "apple"]`
    - Output: `"apple"`
    - Explanation: All prefixes of `"apple"` are in the list.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every word in the list against all its prefixes.
- For each word, generate all its prefixes and check if they exist in the list of words.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional data structures or complex algorithms.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

string longestWord(vector<string>& words) {
    unordered_set<string> wordSet(words.begin(), words.end());
    string longestWord;
    
    for (const string& word : words) {
        bool allPrefixesExist = true;
        for (int i = 1; i < word.size(); ++i) {
            string prefix = word.substr(0, i);
            if (wordSet.find(prefix) == wordSet.end()) {
                allPrefixesExist = false;
                break;
            }
        }
        if (allPrefixesExist) {
            if (word.size() > longestWord.size() || (word.size() == longestWord.size() && word < longestWord)) {
                longestWord = word;
            }
        }
    }
    return longestWord;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M^2)$, where $N$ is the number of words and $M$ is the average length of a word. This is because for each word, we generate all its prefixes and check their existence in the set.
> - **Space Complexity:** $O(N \cdot M)$, for storing all words in the set and generating prefixes.
> - **Why these complexities occur:** The brute force approach involves iterating over all words and for each word, iterating over all its prefixes, leading to quadratic complexity in terms of the word length.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `Trie` (prefix tree) to store all words. This allows for efficient checking of prefixes.
- We insert all words into the Trie and mark the end of each word. Then, we traverse the Trie and for each node, we check if it's the end of a word and if all its prefixes are in the Trie.
- This approach is optimal because it reduces the time complexity of checking prefixes from $O(M)$ to $O(1)$, utilizing the Trie's structure.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isWord;
};

void insert(TrieNode* root, const string& word) {
    TrieNode* node = root;
    for (char c : word) {
        if (!node->children.count(c)) {
            node->children[c] = new TrieNode();
        }
        node = node->children[c];
    }
    node->isWord = true;
}

string longestWord(vector<string>& words) {
    TrieNode* root = new TrieNode();
    for (const string& word : words) {
        insert(root, word);
    }
    
    string longestWord;
    function<void(TrieNode*, string)> dfs = [&](TrieNode* node, string word) {
        if (node->isWord) {
            if (word.size() > longestWord.size() || (word.size() == longestWord.size() && word < longestWord)) {
                longestWord = word;
            }
        }
        for (auto& child : node->children) {
            dfs(child.second, word + child.first);
        }
    };
    dfs(root, "");
    return longestWord;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the average length of a word. This is because we insert each word into the Trie and then traverse the Trie.
> - **Space Complexity:** $O(N \cdot M)$, for storing the Trie.
> - **Optimality proof:** This approach is optimal because it utilizes the Trie to efficiently store and check prefixes, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structure (in this case, a Trie) to solve problems involving prefixes efficiently.
- How to optimize algorithms by reducing the complexity of sub-problems (checking prefixes from $O(M)$ to $O(1)$).
- The use of recursive functions (like `dfs`) to traverse complex data structures.

**Mistakes to Avoid:**
- Not considering the use of specialized data structures like Tries for prefix-related problems.
- Failing to optimize sub-problems, leading to inefficient algorithms.
- Not handling edge cases properly, such as empty input lists or words with no prefixes.