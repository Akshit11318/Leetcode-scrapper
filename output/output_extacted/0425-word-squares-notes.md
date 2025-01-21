## Word Squares

**Problem Link:** https://leetcode.com/problems/word-squares/description

**Problem Statement:**
- Input: A list of unique `words` of the same length.
- Constraints: All words are of the same length, and the length of the word list is not less than the length of a word and not more than 5000.
- Expected Output: A list of lists, where each sublist contains `k` words, forming a word square.
- Key Requirements: A word square is a square grid of words, where the `i-th` row consists of the `i-th` word in the square, and the `i-th` column consists of the `i-th` character of each word in the square.
- Edge Cases: The input list may be empty, or it may contain words of different lengths.

**Example Test Cases:**
- Input: `["area","lead","line","at"]`
- Output: `[["area","lead","line","at"]]`
- Explanation: The words form a square grid where each row and column consists of the same characters.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible combinations of words to form a square and then checking each combination to see if it satisfies the word square condition.
- This approach is straightforward but inefficient due to its exponential time complexity.
- It comes to mind first because it directly addresses the problem without considering optimizations.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        vector<vector<string>> result;
        vector<string> square(words.size());
        backtrack(result, square, words, 0);
        return result;
    }

private:
    void backtrack(vector<vector<string>>& result, vector<string>& square, vector<string>& words, int index) {
        if (index == square.size()) {
            result.push_back(square);
            return;
        }
        for (const string& word : words) {
            if (isValid(square, word, index)) {
                square[index] = word;
                backtrack(result, square, words, index + 1);
                square[index] = "";
            }
        }
    }

    bool isValid(vector<string>& square, const string& word, int index) {
        for (int i = 0; i < word.size(); i++) {
            if (index > 0 && square[i][index] != word[i]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n^{k})$, where $k$ is the length of a word and $n$ is the number of words. This is because we generate all possible combinations of words and check each one.
> - **Space Complexity:** $O(k \cdot n^{k})$, as we store all possible word squares in the result.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of words, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is using a `Trie` data structure to store the words and their prefixes.
- This allows us to efficiently check if a word can be appended to the current square.
- We also use a `backtrack` function to generate all possible word squares.
- The optimality of this approach comes from the fact that we prune branches that cannot lead to a valid word square, reducing the search space.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> words;
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->words.push_back(word);
    }
};

class Solution {
public:
    vector<vector<string>> wordSquares(vector<string>& words) {
        vector<vector<string>> result;
        Trie trie;
        for (const string& word : words) {
            trie.insert(word);
        }
        vector<string> square(words.size());
        backtrack(result, square, trie, 0);
        return result;
    }

private:
    void backtrack(vector<vector<string>>& result, vector<string>& square, Trie& trie, int index) {
        if (index == square.size()) {
            result.push_back(square);
            return;
        }
        TrieNode* node = trie.root;
        for (int i = 0; i < index; i++) {
            if (!node->children.count(square[i][index])) {
                return;
            }
            node = node->children[square[i][index]];
        }
        for (const string& word : node->words) {
            if (isValid(square, word, index)) {
                square[index] = word;
                backtrack(result, square, trie, index + 1);
                square[index] = "";
            }
        }
    }

    bool isValid(vector<string>& square, const string& word, int index) {
        for (int i = 0; i < word.size(); i++) {
            if (index > 0 && square[i][index] != word[i]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n \cdot m)$, where $k$ is the length of a word, $n$ is the number of words, and $m$ is the average number of words in the `Trie` node.
> - **Space Complexity:** $O(k \cdot n)$, as we store the `Trie` and the current square.
> - **Optimality proof:** This approach is optimal because it uses a `Trie` to efficiently prune branches that cannot lead to a valid word square, reducing the search space.

---

### Final Notes

**Learning Points:**
- Using a `Trie` data structure to store words and their prefixes can efficiently prune branches that cannot lead to a valid word square.
- The `backtrack` function is a useful technique for generating all possible solutions to a problem.
- Optimizing the search space by pruning branches that cannot lead to a valid solution can significantly improve the performance of an algorithm.

**Mistakes to Avoid:**
- Not using a `Trie` data structure to store words and their prefixes, leading to inefficient search.
- Not pruning branches that cannot lead to a valid word square, leading to unnecessary computation.
- Not using a `backtrack` function to generate all possible solutions, leading to incomplete results.