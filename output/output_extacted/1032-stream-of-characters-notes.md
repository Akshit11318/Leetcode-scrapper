## Stream of Characters
**Problem Link:** https://leetcode.com/problems/stream-of-characters/description

**Problem Statement:**
- Input format: A list of words and a stream of characters.
- Constraints: The words can be of any length, and the stream of characters can be of any length.
- Expected output format: For each character in the stream, output whether it is part of any of the given words.
- Key requirements and edge cases to consider: Handling cases where the character is not part of any word, handling cases where the character is part of multiple words.
- Example test cases with explanations:
  - Example 1: Input: words = ["a","aa","aaa","aaaa"], stream = "aaaaa". Output: [0,1,1,1,0].
  - Example 2: Input: words = ["ab","aba","abba","abbab","abbaba"], stream = "ab". Output: [0,0].

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each character in the stream, check if it is part of any of the given words.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in the stream.
  2. For each character, iterate over each word in the list of words.
  3. Check if the character is part of the current word.
  4. If it is, return the index of the word.
- Why this approach comes to mind first: It is a straightforward and simple approach that checks every possibility.

```cpp
class WordFilter {
public:
    vector<string> words;
    vector<int> result;
    WordFilter(vector<string> words) {
        this->words = words;
    }
    
    int f(char letter, int index) {
        result.push_back(0);
        for (int i = 0; i < words.size(); i++) {
            if (words[i].find(letter) != string::npos) {
                result.back() = i;
                break;
            }
        }
        return result.back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where n is the length of the stream, m is the number of words, and k is the average length of a word.
> - **Space Complexity:** $O(n)$, where n is the length of the stream.
> - **Why these complexities occur:** The time complexity occurs because for each character in the stream, we are iterating over each word and checking if the character is part of the word. The space complexity occurs because we are storing the result for each character in the stream.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to store the words and then iterate over the stream to check if each character is part of any word.
- Detailed breakdown of the approach:
  1. Create a Trie data structure to store the words.
  2. Iterate over each character in the stream.
  3. For each character, check if it is part of any word in the Trie.
  4. If it is, return the index of the word.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n \cdot m \cdot k)$ to $O(n \cdot k)$, where n is the length of the stream and k is the average length of a word.

```cpp
class WordFilter {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        int index;
    };
    TrieNode* root;
    WordFilter(vector<string> words) {
        root = new TrieNode();
        for (int i = 0; i < words.size(); i++) {
            string word = words[i];
            TrieNode* node = root;
            for (int j = 0; j < word.size(); j++) {
                if (node->children.find(word[j]) == node->children.end()) {
                    node->children[word[j]] = new TrieNode();
                }
                node = node->children[word[j]];
                node->index = i;
            }
        }
    }
    
    int f(char letter, int index) {
        TrieNode* node = root;
        for (int i = 0; i < index; i++) {
            if (node->children.find(letter) == node->children.end()) {
                return 0;
            }
            node = node->children[letter];
        }
        return node->index;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where n is the length of the stream and k is the average length of a word.
> - **Space Complexity:** $O(m \cdot k)$, where m is the number of words and k is the average length of a word.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity by avoiding the need to iterate over each word for each character in the stream.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, string matching.
- Problem-solving patterns identified: Using a Trie to store words and then iterating over a stream to check for matches.
- Optimization techniques learned: Reducing time complexity by using a Trie data structure.
- Similar problems to practice: String matching problems, Trie-based problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for null pointers.
- Edge cases to watch for: Handling cases where the character is not part of any word, handling cases where the character is part of multiple words.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing with different inputs, testing with edge cases.