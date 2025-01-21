## Short Encoding of Words
**Problem Link:** https://leetcode.com/problems/short-encoding-of-words/description

**Problem Statement:**
- Input format: An array of strings `words`.
- Constraints: Each string consists of lowercase letters, and the length of the array does not exceed $10^4$.
- Expected output format: The minimum length of the shortest possible encoding.
- Key requirements: Find the shortest possible encoding of the given array of words such that any word can be uniquely decoded from the encoded string.
- Edge cases: Empty array, single-element array, array with duplicate words.

Example test cases:
- Input: `words = ["time", "me", "bell"]`
  Output: `10`
  Explanation: A possible encoding is `"time#me#bell#"` with a length of 10.
- Input: `words = ["t"]`
  Output: `2`
  Explanation: A possible encoding is `"t#"` with a length of 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of words and checking if they can be uniquely decoded.
- The brute force approach would generate all permutations of the given words and for each permutation, it checks if any word is a suffix of another word in the permutation.
- This approach comes to mind first because it ensures that we consider all possible orderings of the words.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int minimumLengthEncoding(std::vector<std::string>& words) {
    // Sort the words in descending order of their lengths
    std::sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
        return a.size() > b.size();
    });

    std::string encoded;
    for (const auto& word : words) {
        bool found = false;
        for (size_t i = 0; i < encoded.size(); ++i) {
            if (encoded.substr(i, word.size()) == word) {
                found = true;
                break;
            }
        }
        if (!found) {
            encoded += word + "#";
        }
    }
    return encoded.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n))$ where $n$ is the number of words and $m$ is the maximum length of a word. This is because we sort the words and then for each word, we check if it's a suffix of the encoded string so far.
> - **Space Complexity:** $O(n \cdot m)$ for storing the encoded string.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to storing the encoded string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `Trie` (prefix tree) data structure to store the words.
- We iterate through each word in reverse order and check if it's already present in the Trie. If not, we add it to the Trie.
- The minimum length of the encoding is the sum of the lengths of the words that are not suffixes of other words.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    TrieNode() : isEndOfWord(false) {}
};

int minimumLengthEncoding(std::vector<std::string>& words) {
    TrieNode* root = new TrieNode();
    for (const auto& word : words) {
        TrieNode* node = root;
        for (int i = word.size() - 1; i >= 0; --i) {
            if (node->children.find(word[i]) == node->children.end()) {
                node->children[word[i]] = new TrieNode();
            }
            node = node->children[word[i]];
        }
        node->isEndOfWord = true;
    }

    int length = 0;
    for (const auto& word : words) {
        TrieNode* node = root;
        for (int i = word.size() - 1; i >= 0; --i) {
            node = node->children[word[i]];
            if (node->children.size() > 1 || node->isEndOfWord) {
                length += word.size() - i + 1;
                break;
            }
        }
    }
    return length + words.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the maximum length of a word. This is because we iterate through each word and add it to the Trie.
> - **Space Complexity:** $O(n \cdot m)$ for storing the Trie.
> - **Optimality proof:** This approach is optimal because it ensures that we only include words that are not suffixes of other words in the encoding, resulting in the minimum possible length.

---

### Final Notes

**Learning Points:**
- Using a Trie data structure to efficiently store and retrieve words.
- Iterating through words in reverse order to check for suffixes.
- Calculating the minimum length of the encoding by summing the lengths of non-suffix words.

**Mistakes to Avoid:**
- Not sorting the words by length before checking for suffixes.
- Not using a Trie data structure to efficiently store and retrieve words.
- Not iterating through words in reverse order to check for suffixes.

---