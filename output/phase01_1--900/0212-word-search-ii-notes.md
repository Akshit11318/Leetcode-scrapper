## Word Search II
**Problem Link:** [https://leetcode.com/problems/word-search-ii/description](https://leetcode.com/problems/word-search-ii/description)

**Problem Statement:**
- Input format: A 2D board consisting of characters and a list of words.
- Constraints: The board and words are non-empty, and each word is at least one character long.
- Expected output format: A list of words that can be found in the board.
- Key requirements and edge cases to consider:
  - Each word can only be used once in the board.
  - Words can be horizontally, vertically, or diagonally placed.
  - No word can be constructed by reusing characters in the board.
- Example test cases with explanations:
  - A simple 2x2 board with one word.
  - A larger board with multiple words.
  - A board with no words that can be found.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all words in the board, we can start by checking each cell in the board and see if we can construct any of the given words starting from that cell.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the board.
  2. For each cell, try to construct each of the given words by moving in all eight directions (horizontally, vertically, and diagonally).
  3. If a word can be constructed, add it to the result list.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities.

```cpp
class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                for (string word : words) {
                    if (dfs(board, i, j, word, 0)) {
                        result.push_back(word);
                        break;
                    }
                }
            }
        }
        return result;
    }

    bool dfs(vector<vector<char>>& board, int i, int j, string word, int k) {
        if (k == word.size()) return true;
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || word[k] != board[i][j]) return false;
        char temp = board[i][j];
        board[i][j] = '#';
        bool found = dfs(board, i + 1, j, word, k + 1) || dfs(board, i - 1, j, word, k + 1) || dfs(board, i, j + 1, word, k + 1) || dfs(board, i, j - 1, word, k + 1) || dfs(board, i + 1, j + 1, word, k + 1) || dfs(board, i - 1, j - 1, word, k + 1) || dfs(board, i + 1, j - 1, word, k + 1) || dfs(board, i - 1, j + 1, word, k + 1);
        board[i][j] = temp;
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 8^L \cdot W)$, where $N$ and $M$ are the dimensions of the board, $L$ is the maximum length of a word, and $W$ is the number of words. This is because we are checking all eight directions for each cell in the board and for each word.
> - **Space Complexity:** $O(N \cdot M + W)$, where $N$ and $M$ are the dimensions of the board and $W$ is the number of words. This is because we need to store the board and the result.
> - **Why these complexities occur:** The time complexity occurs because we are using a depth-first search (DFS) approach to check all possibilities, and the space complexity occurs because we need to store the board and the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to store the words and then use DFS to search for the words in the board.
- Detailed breakdown of the approach:
  1. Create a Trie and insert all the words into it.
  2. Iterate over each cell in the board and use DFS to search for words in the Trie.
  3. If a word is found, add it to the result list and remove it from the Trie to avoid duplicates.
- Proof of optimality: This approach is optimal because we are using a Trie to store the words, which allows us to search for words in $O(L)$ time, where $L$ is the length of the word.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = word;
        }
        vector<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, i, j, root, result);
            }
        }
        return result;
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result) {
        if (node->word != "") {
            result.push_back(node->word);
            node->word = "";
        }
        char temp = board[i][j];
        board[i][j] = '#';
        for (auto& child : node->children) {
            int ni = i, nj = j;
            if (child.first == temp) {
                ni += 0; nj += 0;
                if (ni >= 0 && ni < board.size() && nj >= 0 && nj < board[0].size() && board[ni][nj] == temp) {
                    dfs(board, ni + 1, nj, child.second, result);
                    dfs(board, ni - 1, nj, child.second, result);
                    dfs(board, ni, nj + 1, child.second, result);
                    dfs(board, ni, nj - 1, child.second, result);
                    dfs(board, ni + 1, nj + 1, child.second, result);
                    dfs(board, ni - 1, nj - 1, child.second, result);
                    dfs(board, ni + 1, nj - 1, child.second, result);
                    dfs(board, ni - 1, nj + 1, child.second, result);
                }
            }
        }
        board[i][j] = temp;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 8^L \cdot W)$, where $N$ and $M$ are the dimensions of the board, $L$ is the maximum length of a word, and $W$ is the number of words. This is because we are using DFS to search for words in the board.
> - **Space Complexity:** $O(N \cdot M + W)$, where $N$ and $M$ are the dimensions of the board and $W$ is the number of words. This is because we need to store the board and the Trie.
> - **Optimality proof:** This approach is optimal because we are using a Trie to store the words, which allows us to search for words in $O(L)$ time, where $L$ is the length of the word.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, DFS algorithm.
- Problem-solving patterns identified: Using a Trie to store words and then using DFS to search for words in a board.
- Optimization techniques learned: Using a Trie to reduce the time complexity of searching for words.
- Similar problems to practice: Word Search, Word Ladder, Boggle.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out of bounds when using DFS.
- Edge cases to watch for: Empty board or words list.
- Performance pitfalls: Not using a Trie to store words, which can lead to high time complexity.
- Testing considerations: Test the solution with different board sizes and word lengths to ensure it works correctly.