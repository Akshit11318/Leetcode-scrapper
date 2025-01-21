## Implement Trie II (Prefix Tree)

**Problem Link:** https://leetcode.com/problems/implement-trie-ii-prefix-tree/description

**Problem Statement:**
- Input format and constraints: The problem requires implementing a `Trie` class with methods `insert`, `search`, `startsWith`, and `countWordsEqualTo` and `countWordsStartingWithPrefix`. The `insert` method takes a string word as input and inserts it into the Trie. The `search` method takes a string word as input and returns the number of times the word is inserted into the Trie. The `startsWith` method takes a string prefix as input and returns the number of words in the Trie that start with the given prefix. The `countWordsEqualTo` method takes a string word as input and returns the number of times the word is inserted into the Trie. The `countWordsStartingWithPrefix` method takes a string prefix as input and returns the number of words in the Trie that start with the given prefix.
- Expected output format: The output of the `insert`, `search`, `startsWith`, `countWordsEqualTo`, and `countWordsStartingWithPrefix` methods should be the number of times the word is inserted into the Trie or the number of words that start with the given prefix.
- Key requirements and edge cases to consider: The Trie should handle words with lowercase English letters. The `insert` method should handle duplicate words. The `search` method should return 0 if the word is not in the Trie. The `startsWith` method should return 0 if there are no words that start with the given prefix.
- Example test cases with explanations:
  - Inserting a word into the Trie and then searching for it should return the correct count.
  - Inserting a word into the Trie and then checking if it starts with a certain prefix should return the correct count.
  - Inserting multiple words into the Trie and then searching for a word that is not in the Trie should return 0.
  - Inserting multiple words into the Trie and then checking if they start with a certain prefix should return the correct count.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to use a brute force approach where we store all the words in a list and then iterate over the list to find the words that start with a given prefix.
- Step-by-step breakdown of the solution: We can create a list to store all the words. When we insert a word, we add it to the list. When we search for a word, we iterate over the list and count the number of times the word appears. When we check if a word starts with a certain prefix, we iterate over the list and count the number of words that start with the prefix.
- Why this approach comes to mind first: This approach comes to mind first because it is simple and easy to implement. However, it is not efficient because it has a high time complexity.

```cpp
class Trie {
public:
    vector<string> words;
    void insert(string word) {
        words.push_back(word);
    }
    int search(string word) {
        int count = 0;
        for (string w : words) {
            if (w == word) {
                count++;
            }
        }
        return count;
    }
    int startsWith(string prefix) {
        int count = 0;
        for (string w : words) {
            if (w.find(prefix) == 0) {
                count++;
            }
        }
        return count;
    }
    int countWordsEqualTo(string word) {
        return search(word);
    }
    int countWordsStartingWithPrefix(string prefix) {
        return startsWith(prefix);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. This is because we iterate over all the words to find the words that start with a given prefix.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. This is because we store all the words in a list.
> - **Why these complexities occur:** These complexities occur because we use a brute force approach that involves iterating over all the words to find the words that start with a given prefix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to solve this problem efficiently. A Trie is a tree-like data structure that is used to store a dynamic set or associative array where the keys are usually strings.
- Detailed breakdown of the approach: We can create a Trie node class that has a `children` map to store the child nodes and a `count` variable to store the count of words that end at the current node. When we insert a word, we start at the root node and iterate over each character in the word. For each character, we create a new node if it does not exist and increment the count of the current node. When we search for a word, we start at the root node and iterate over each character in the word. For each character, we move to the child node that corresponds to the character. If we reach the end of the word, we return the count of the current node. When we check if a word starts with a certain prefix, we start at the root node and iterate over each character in the prefix. For each character, we move to the child node that corresponds to the character. If we reach the end of the prefix, we return the sum of the counts of all the nodes that are reachable from the current node.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(m)$ where $m$ is the maximum length of a word. This is because we only need to iterate over each character in the word to insert or search for it.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    int count;
    TrieNode() : count(0) {}
};

class Trie {
public:
    TrieNode* root;
    Trie() : root(new TrieNode()) {}
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->count++;
    }
    int search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                return 0;
            }
            node = node->children[c];
        }
        return node->count;
    }
    int startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
                return 0;
            }
            node = node->children[c];
        }
        return count(node);
    }
    int count(TrieNode* node) {
        int sum = node->count;
        for (auto& child : node->children) {
            sum += count(child.second);
        }
        return sum;
    }
    int countWordsEqualTo(string word) {
        return search(word);
    }
    int countWordsStartingWithPrefix(string prefix) {
        return startsWith(prefix);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ where $m$ is the maximum length of a word. This is because we only need to iterate over each character in the word to insert or search for it.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. This is because we store all the words in the Trie.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(m)$ where $m$ is the maximum length of a word. This is because we only need to iterate over each character in the word to insert or search for it.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, recursive counting.
- Problem-solving patterns identified: Using a Trie to solve string matching problems.
- Optimization techniques learned: Using a Trie to reduce the time complexity of string matching problems.
- Similar problems to practice: Other string matching problems that can be solved using a Trie.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a word is not in the Trie.
- Edge cases to watch for: Handling the case where a word is not in the Trie.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the Trie with different inputs to ensure it works correctly.