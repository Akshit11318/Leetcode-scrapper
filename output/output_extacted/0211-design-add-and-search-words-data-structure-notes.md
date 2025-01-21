## Word Dictionary Design
**Problem Link:** https://leetcode.com/problems/design-add-and-search-words-data-structure/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a data structure to support two operations: adding a word and searching for a word that matches a given pattern. The pattern can contain a wildcard character '.' that matches any single character.
- Expected output format: The `addWord` operation should add a word to the data structure, and the `search` operation should return a boolean indicating whether there is any word in the data structure that matches the given pattern.
- Key requirements and edge cases to consider: The data structure should efficiently handle a large number of words and patterns. The search operation should correctly handle the wildcard character '.'.
- Example test cases with explanations:
  - Adding words "bad" and "dad" and then searching for the pattern "pad" should return False, while searching for the pattern "bad" should return True.
  - Searching for the pattern "ba." should return True if the word "bad" is in the dictionary.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The simplest approach is to store all the words in a list and then, for each search operation, iterate through the list to check if any word matches the given pattern.
- Step-by-step breakdown of the solution:
  1. Store all words in a list.
  2. For the `search` operation, iterate through the list of words.
  3. For each word, compare it character by character with the given pattern, considering the wildcard character '.'.
- Why this approach comes to mind first: It's straightforward and easy to implement, but it's not efficient for a large number of words and search operations.

```cpp
class WordDictionary {
public:
    vector<string> words;
    
    void addWord(string word) {
        words.push_back(word);
    }
    
    bool search(string word) {
        for (const auto& w : words) {
            if (w.size() != word.size()) continue;
            bool match = true;
            for (int i = 0; i < word.size(); ++i) {
                if (word[i] != '.' && word[i] != w[i]) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the length of a word. This is because for each search operation, we potentially iterate through all words and compare each character.
> - **Space Complexity:** $O(n \cdot m)$, as we store all words in memory.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves linear scanning of all words for each search operation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a Trie (prefix tree) data structure can significantly improve the efficiency of both `addWord` and `search` operations. The Trie allows us to store words in a way that facilitates fast lookup, especially when dealing with patterns containing a wildcard character.
- Detailed breakdown of the approach:
  1. Create a Trie node structure that includes a boolean to mark the end of a word and a map to store child nodes.
  2. Implement the `addWord` operation by iterating through the characters of the word and adding nodes to the Trie as necessary.
  3. Implement the `search` operation by using a recursive or iterative approach to traverse the Trie based on the pattern, handling the wildcard character '.' by exploring all possible child nodes.
- Proof of optimality: The Trie data structure allows for efficient storage and retrieval of words, especially when dealing with prefix matching or patterns with wildcards. This approach optimizes both time and space complexity compared to the brute force method.

```cpp
class WordDictionary {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isWord;
    };
    
    TrieNode* root;
    
    WordDictionary() : root(new TrieNode()) {}
    
    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isWord = true;
    }
    
    bool search(string word) {
        return searchFrom(root, word);
    }
    
    bool searchFrom(TrieNode* node, string word) {
        for (int i = 0; i < word.size(); ++i) {
            if (word[i] == '.') {
                for (auto& child : node->children) {
                    if (searchFrom(child.second, word.substr(i + 1))) {
                        return true;
                    }
                }
                return false;
            } else {
                if (node->children.find(word[i]) == node->children.end()) {
                    return false;
                }
                node = node->children[word[i]];
            }
        }
        return node->isWord;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ for both `addWord` and `search` operations, where $m$ is the length of a word. In the worst case for `search`, we might explore all branches for the wildcard character, but this is still bounded by the number of nodes in the Trie that correspond to the pattern length.
> - **Space Complexity:** $O(n \cdot m)$, as in the worst case, we store all characters of all words in the Trie.
> - **Optimality proof:** The Trie approach is optimal because it reduces the time complexity of both operations to be linear with respect to the word length, and it efficiently uses space by only storing unique prefixes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of Trie data structures for efficient prefix matching and handling patterns with wildcard characters.
- Problem-solving patterns identified: Recognizing the need for a more efficient data structure than a simple list for storing and searching words.
- Optimization techniques learned: Using a Trie to reduce the time complexity of search operations.
- Similar problems to practice: Other problems involving prefix matching, autocomplete, or efficient storage and retrieval of strings.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases such as an empty pattern or word, or not properly initializing the Trie.
- Edge cases to watch for: Patterns with multiple consecutive wildcard characters, or words that are prefixes of other words.
- Performance pitfalls: Using a data structure that does not efficiently support the required operations, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the implementation with a variety of words and patterns, including edge cases.