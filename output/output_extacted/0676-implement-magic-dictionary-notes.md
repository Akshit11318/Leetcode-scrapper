## Magic Dictionary
**Problem Link:** https://leetcode.com/problems/implement-magic-dictionary/description

**Problem Statement:**
- Input format and constraints: The problem requires implementing a `MagicDictionary` class that supports two operations: `buildDict` and `search`. The `buildDict` operation takes a list of strings as input and constructs a dictionary from it. The `search` operation takes a string as input and checks if it exists in the dictionary with at most one mismatch.
- Expected output format: The `search` operation returns a boolean indicating whether the input string is in the dictionary with at most one mismatch.
- Key requirements and edge cases to consider: The dictionary can contain duplicate strings, and the input strings can be of varying lengths.
- Example test cases with explanations:
  - `MagicDictionary magic = new MagicDictionary(); magic.buildDict(["hello", "leetcode"]);` Then, `magic.search("hello")` returns `False` because `hello` is in the dictionary, but `magic.search("hhllo")` returns `True` because `hhllo` is not in the dictionary but has only one mismatch with `hello`.

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to iterate over each string in the dictionary and compare it with the input string character by character. If the number of mismatches is less than or equal to 1, return `True`.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the input strings.
  2. Iterate over each string in the dictionary.
  3. Compare the input string with each string in the dictionary character by character.
  4. Count the number of mismatches.
  5. If the number of mismatches is less than or equal to 1, return `True`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
class MagicDictionary {
public:
    vector<string> dict;
    MagicDictionary() {}
    
    void buildDict(vector<string> dictionary) {
        dict = dictionary;
    }
    
    bool search(string searchWord) {
        for (const string& word : dict) {
            if (word.size() == searchWord.size()) {
                int mismatch = 0;
                for (int i = 0; i < word.size(); i++) {
                    if (word[i] != searchWord[i]) {
                        mismatch++;
                    }
                }
                if (mismatch <= 1) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings in the dictionary and $m$ is the maximum length of a string. This is because we iterate over each string in the dictionary and compare it with the input string character by character.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings in the dictionary and $m$ is the maximum length of a string. This is because we store all the strings in the dictionary.
> - **Why these complexities occur:** The high time complexity occurs because we use nested loops to compare the input string with each string in the dictionary. The space complexity occurs because we store all the strings in the dictionary.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the dictionary. This allows us to efficiently search for strings with at most one mismatch.
- Detailed breakdown of the approach:
  1. Create a `Trie` node class to represent each node in the Trie.
  2. Create a `MagicDictionary` class to manage the Trie.
  3. Implement the `buildDict` operation to insert each string in the dictionary into the Trie.
  4. Implement the `search` operation to search for the input string in the Trie with at most one mismatch.
- Proof of optimality: This approach is optimal because it reduces the time complexity of the `search` operation to $O(m)$, where $m$ is the length of the input string.
- Why further optimization is impossible: This approach is optimal because it uses a Trie data structure, which is the most efficient data structure for searching for strings with at most one mismatch.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
    TrieNode() : isWord(false) {}
};

class MagicDictionary {
public:
    TrieNode* root;
    MagicDictionary() : root(new TrieNode()) {}
    
    void buildDict(vector<string> dictionary) {
        for (const string& word : dictionary) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isWord = true;
        }
    }
    
    bool search(string searchWord) {
        return searchHelper(root, searchWord, 0, 0);
    }
    
    bool searchHelper(TrieNode* node, string& searchWord, int index, int mismatch) {
        if (index == searchWord.size()) {
            return node->isWord && mismatch == 1;
        }
        if (mismatch > 1) {
            return false;
        }
        for (auto& child : node->children) {
            if (child.first == searchWord[index]) {
                if (searchHelper(child.second, searchWord, index + 1, mismatch)) {
                    return true;
                }
            } else if (searchHelper(child.second, searchWord, index + 1, mismatch + 1)) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the length of the input string. This is because we use a Trie data structure to efficiently search for strings with at most one mismatch.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings in the dictionary and $m$ is the maximum length of a string. This is because we store all the strings in the dictionary in the Trie.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of the `search` operation to $O(m)$, where $m$ is the length of the input string.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, string matching with at most one mismatch.
- Problem-solving patterns identified: Using a Trie data structure to efficiently search for strings with at most one mismatch.
- Optimization techniques learned: Reducing the time complexity of the `search` operation by using a Trie data structure.
- Similar problems to practice: String matching with at most one mismatch, Trie data structure.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input string is empty, not checking for null pointers.
- Edge cases to watch for: The input string is empty, the dictionary is empty.
- Performance pitfalls: Using a naive approach with high time complexity, not using a Trie data structure.
- Testing considerations: Test the `buildDict` operation with an empty dictionary, test the `search` operation with an empty input string.