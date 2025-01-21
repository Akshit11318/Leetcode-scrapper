## Longest Word in Dictionary

**Problem Link:** https://leetcode.com/problems/longest-word-in-dictionary/description

**Problem Statement:**
- Input format: a list of strings `words` representing a dictionary.
- Constraints: `1 <= words.length <= 1000`, `1 <= words[i].length <= 30`, `words[i]` consists of lowercase English letters.
- Expected output format: the longest word in the dictionary that can be formed by other words.
- Key requirements and edge cases to consider: handling empty strings, single-word dictionaries, and ensuring that the longest word can be formed by concatenating other words in the dictionary.
- Example test cases with explanations:
  - Example 1: `words = ["w","wo","wor","word"]`, the longest word that can be formed is `"word"`.
  - Example 2: `words = ["a","banana","app","appl","ap","apply","apple"]`, the longest word that can be formed is `"apple"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible combination of words to see if they can form a longer word.
- Step-by-step breakdown of the solution:
  1. Sort the dictionary by word length in descending order.
  2. For each word in the sorted dictionary, check if it can be formed by concatenating other words in the dictionary.
  3. If a word can be formed, compare its length with the current longest word found.
- Why this approach comes to mind first: It directly addresses the problem statement by checking all possible combinations.

```cpp
class Solution {
public:
    string longestWord(vector<string>& words) {
        // Sort the dictionary by word length in descending order
        sort(words.begin(), words.end(), [](const string& a, const string& b) {
            if (a.length() != b.length()) return a.length() > b.length();
            return a < b;
        });
        
        unordered_set<string> wordSet(words.begin(), words.end());
        string longestWord = "";
        
        for (const string& word : words) {
            // Check if the word can be formed by other words
            if (canBeFormed(word, wordSet)) {
                if (word.length() > longestWord.length()) {
                    longestWord = word;
                }
            }
        }
        
        return longestWord;
    }
    
    bool canBeFormed(const string& word, unordered_set<string>& wordSet) {
        for (int i = 1; i < word.length(); ++i) {
            string prefix = word.substr(0, i);
            string suffix = word.substr(i);
            if (wordSet.find(prefix) == wordSet.end() || !canBeFormed(suffix, wordSet)) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot 2^m)$, where $n$ is the number of words and $m$ is the maximum length of a word. The reason for this complexity is the recursive nature of the `canBeFormed` function, which in the worst case can lead to exponential time complexity due to the recursive calls for each prefix and suffix.
> - **Space Complexity:** $O(n)$, for storing the words in the `wordSet`.
> - **Why these complexities occur:** The exponential time complexity is due to the recursive approach of checking all possible prefixes and suffixes for each word, which can lead to a large number of function calls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `Trie` data structure to efficiently store and check the words.
- Detailed breakdown of the approach:
  1. Build a `Trie` from the given dictionary.
  2. For each word in the dictionary, check if it can be formed by traversing the `Trie`.
  3. Keep track of the longest word that can be formed.
- Proof of optimality: This approach ensures that each word is checked only once, and the use of a `Trie` reduces the time complexity of checking if a word can be formed.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
};

class Solution {
public:
    string longestWord(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isWord = true;
        }
        
        string longestWord = "";
        for (const string& word : words) {
            if (canBeFormed(word, root)) {
                if (word.length() > longestWord.length()) {
                    longestWord = word;
                }
            }
        }
        
        return longestWord;
    }
    
    bool canBeFormed(const string& word, TrieNode* root) {
        TrieNode* node = root;
        for (int i = 0; i < word.length(); ++i) {
            if (node->children.find(word[i]) == node->children.end()) return false;
            node = node->children[word[i]];
            if (!node->isWord) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we are iterating over each word and its characters once.
> - **Space Complexity:** $O(n \cdot m)$, for storing the `Trie` nodes.
> - **Optimality proof:** This approach is optimal because it ensures that each word is checked only once, and the use of a `Trie` reduces the time complexity of checking if a word can be formed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `Trie` data structure for efficient string matching.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using a suitable data structure to solve them efficiently.
- Optimization techniques learned: Using a `Trie` to reduce the time complexity of string matching.
- Similar problems to practice: Other problems involving string matching and dictionary operations.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling edge cases, such as empty strings or single-word dictionaries.
- Edge cases to watch for: Ensuring that the longest word can be formed by concatenating other words in the dictionary.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with different input cases to ensure correctness and efficiency.