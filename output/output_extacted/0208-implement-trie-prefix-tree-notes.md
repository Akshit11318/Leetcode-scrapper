## Implement Trie (Prefix Tree)

**Problem Link:** https://leetcode.com/problems/implement-trie-prefix-tree/description

**Problem Statement:**
- Input format and constraints: Implement a `Trie` class that supports the following methods: `insert(String word)`, `search(String word)`, and `startsWith(String prefix)`. 
- Expected output format: 
    - `insert(String word)`: Insert a word into the trie.
    - `search(String word)`: Return if the word is in the trie.
    - `startsWith(String prefix)`: Return if there is any word in the trie that starts with the given prefix.
- Key requirements and edge cases to consider:
    - The input word will only contain lowercase letters `a-z`.
    - The input word's length will not exceed 100.
- Example test cases with explanations:
    - `Trie trie = new Trie(); trie.insert("apple"); trie.search("apple");   // returns True; trie.search("app");     // returns False; trie.startsWith("app"); // returns True; trie.insert("app");    trie.search("app");     // returns True`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a simple data structure like a `std::vector` or `std::set` to store all the words.
- Step-by-step breakdown of the solution:
    1. Store all the words in a `std::vector`.
    2. For `search(String word)`, iterate over all the words in the `std::vector` and check if the given word is present.
    3. For `startsWith(String prefix)`, iterate over all the words in the `std::vector` and check if any word starts with the given prefix.
- Why this approach comes to mind first: This approach is simple and straightforward, but it is not efficient for large inputs.

```cpp
class Trie {
public:
    std::vector<std::string> words;
    void insert(std::string word) {
        words.push_back(word);
    }
    bool search(std::string word) {
        for (const auto& w : words) {
            if (w == word) return true;
        }
        return false;
    }
    bool startsWith(std::string prefix) {
        for (const auto& w : words) {
            if (w.find(prefix) == 0) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word. This is because for each operation, we iterate over all the words.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word. This is because we store all the words in a `std::vector`.
> - **Why these complexities occur:** These complexities occur because we are using a simple data structure like a `std::vector` to store all the words, and we are iterating over all the words for each operation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `TrieNode` class to represent each node in the trie. Each `TrieNode` contains a `std::map` to store its children and a boolean to indicate if it is the end of a word.
- Detailed breakdown of the approach:
    1. Create a `TrieNode` class with a `std::map` to store its children and a boolean to indicate if it is the end of a word.
    2. For `insert(String word)`, start at the root and iterate over each character in the word. If the character is not in the current node's children, add a new node to the children. Move to the child node and repeat the process until the end of the word is reached. Mark the end of the word.
    3. For `search(String word)`, start at the root and iterate over each character in the word. If the character is not in the current node's children, return false. Move to the child node and repeat the process until the end of the word is reached. If the end of the word is marked, return true. Otherwise, return false.
    4. For `startsWith(String prefix)`, start at the root and iterate over each character in the prefix. If the character is not in the current node's children, return false. Move to the child node and repeat the process until the end of the prefix is reached. If the end of the prefix is reached, return true.
- Proof of optimality: This approach is optimal because it uses a trie data structure, which is designed for prefix matching. The time complexity is $O(m)$ where $m$ is the length of the word or prefix, which is optimal.

```cpp
class TrieNode {
public:
    std::map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(std::string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }
    bool search(std::string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
    bool startsWith(std::string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ where $m$ is the length of the word or prefix. This is because we iterate over each character in the word or prefix.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word. This is because we store each character of each word in the trie.
> - **Optimality proof:** This approach is optimal because it uses a trie data structure, which is designed for prefix matching. The time complexity is $O(m)$ where $m$ is the length of the word or prefix, which is optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, prefix matching.
- Problem-solving patterns identified: Using a trie to solve prefix matching problems.
- Optimization techniques learned: Using a trie to reduce the time complexity from $O(n \cdot m)$ to $O(m)$.
- Similar problems to practice: Implementing a trie for other types of strings, such as integers or characters.

**Mistakes to Avoid:**
- Common implementation errors: Not marking the end of a word, not checking if a character is in the current node's children before moving to the child node.
- Edge cases to watch for: Empty words or prefixes, words or prefixes with non-alphabet characters.
- Performance pitfalls: Using a simple data structure like a `std::vector` to store all the words, which can lead to a high time complexity.
- Testing considerations: Testing with different types of inputs, such as empty words or prefixes, words or prefixes with non-alphabet characters.