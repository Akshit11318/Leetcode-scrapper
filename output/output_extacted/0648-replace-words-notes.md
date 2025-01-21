## Replace Words
**Problem Link:** https://leetcode.com/problems/replace-words/description

**Problem Statement:**
- Input format: A dictionary of words and a sentence.
- Constraints: The dictionary and sentence are non-empty.
- Expected output format: The modified sentence after replacing words.
- Key requirements: Replace each word in the sentence with its shortest prefix that is not a prefix of any other word in the dictionary.
- Edge cases: Empty dictionary, empty sentence, words with same prefix.

**Example Test Cases:**
- Input: dictionary = ["cat","bat","rat"], sentence = "the cattle is littered with cats"
- Output: "the cat is littered with cats"
- Explanation: The word "cat" is replaced with itself because it is the shortest prefix that is not a prefix of any other word in the dictionary.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each word in the sentence, check all prefixes of the word against all words in the dictionary.
- Step-by-step breakdown of the solution:
  1. Split the sentence into words.
  2. For each word, generate all prefixes.
  3. For each prefix, check if it is a prefix of any other word in the dictionary.
  4. If not, replace the word with the prefix.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities.

```cpp
class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        istringstream iss(sentence);
        string word;
        string result;
        
        while (iss >> word) {
            bool found = false;
            for (int i = 1; i <= word.size(); i++) {
                string prefix = word.substr(0, i);
                bool isPrefix = false;
                for (const string& dictWord : dictionary) {
                    if (dictWord != prefix && dictWord.find(prefix) == 0) {
                        isPrefix = true;
                        break;
                    }
                }
                if (!isPrefix) {
                    result += prefix + " ";
                    found = true;
                    break;
                }
            }
            if (!found) {
                result += word + " ";
            }
        }
        result.pop_back(); // remove trailing space
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k \cdot d)$, where $n$ is the number of words in the sentence, $m$ is the maximum length of a word, $k$ is the number of words in the dictionary, and $d$ is the maximum length of a word in the dictionary.
> - **Space Complexity:** $O(n \cdot m)$, for storing the result and temporary strings.
> - **Why these complexities occur:** The brute force approach checks all prefixes of all words in the sentence against all words in the dictionary, resulting in high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a `Trie` data structure to store the dictionary words, allowing for efficient prefix matching.
- Detailed breakdown of the approach:
  1. Create a `Trie` and insert all dictionary words.
  2. Split the sentence into words.
  3. For each word, traverse the `Trie` to find the shortest prefix that is a word in the dictionary.
  4. If found, replace the word with the prefix.
- Proof of optimality: The `Trie` allows for $O(m)$ time complexity for prefix matching, where $m$ is the length of the word.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord;
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        TrieNode* root = new TrieNode();
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
        
        istringstream iss(sentence);
        string word;
        string result;
        
        while (iss >> word) {
            TrieNode* node = root;
            string prefix;
            for (char c : word) {
                if (!node->children.count(c)) {
                    break;
                }
                prefix += c;
                node = node->children[c];
                if (node->isWord) {
                    result += prefix + " ";
                    break;
                }
            }
            if (!node->isWord) {
                result += word + " ";
            }
        }
        result.pop_back(); // remove trailing space
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + k \cdot d)$, where $n$ is the number of words in the sentence, $m$ is the maximum length of a word, $k$ is the number of words in the dictionary, and $d$ is the maximum length of a word in the dictionary.
> - **Space Complexity:** $O(k \cdot d)$, for storing the `Trie`.
> - **Optimality proof:** The `Trie` allows for efficient prefix matching, reducing the time complexity from $O(n \cdot m \cdot k \cdot d)$ to $O(n \cdot m + k \cdot d)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `Trie` data structure, prefix matching.
- Problem-solving patterns identified: Using a `Trie` to optimize prefix matching.
- Optimization techniques learned: Reducing time complexity by using a `Trie`.
- Similar problems to practice: Problems involving prefix matching, such as autocomplete and spell-checking.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty dictionary or sentence.
- Edge cases to watch for: Words with same prefix, empty dictionary.
- Performance pitfalls: Using a brute force approach, resulting in high time complexity.
- Testing considerations: Test with different dictionary sizes, sentence lengths, and word lengths.