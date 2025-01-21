## Palindrome Pairs

**Problem Link:** https://leetcode.com/problems/palindrome-pairs/description

**Problem Statement:**
- Given a list of unique word strings, find all pairs of words that, when concatenated, form a palindrome.
- Input: A list of strings `words`.
- Output: A list of pairs of indices `[i, j]` where `words[i] + words[j]` is a palindrome.
- Key requirements and edge cases to consider:
  - Each word can be used at most once in a pair.
  - The order of the pairs matters (i.e., `[i, j]` and `[j, i]` are considered different pairs).
- Example test cases with explanations:
  - Input: `words = ["bat","tab","cat"]`
    - Output: `[[0,1],[1,0]]`
    - Explanation: `"bat" + "tab"` and `"tab" + "bat"` are both palindromes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all pairs of words that form a palindrome when concatenated, we can simply try all possible pairs and check if the resulting string is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of indices `[i, j]` from the input list `words`.
  2. For each pair, concatenate `words[i]` and `words[j]`.
  3. Check if the concatenated string is a palindrome by comparing characters from the start and end, moving towards the center.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> result;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words.size(); j++) {
                if (i != j) {
                    string combined = words[i] + words[j];
                    if (isPalindrome(combined)) {
                        result.push_back({i, j});
                    }
                }
            }
        }
        return result;
    }
    
    bool isPalindrome(string& s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word. This is because we generate $n^2$ pairs and for each pair, we potentially check up to $m$ characters to determine if the concatenated string is a palindrome.
> - **Space Complexity:** $O(n^2)$ for storing the result pairs.
> - **Why these complexities occur:** The brute force approach involves checking every possible pair of words, which leads to the quadratic time complexity. The space complexity comes from storing all valid pairs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every pair of words, we can use a `Trie` data structure to store the words and their reverses. This allows us to efficiently find words that are palindromes when concatenated.
- Detailed breakdown of the approach:
  1. Create a `Trie` and insert all words into it, along with their indices.
  2. For each word, check if its reverse is in the `Trie`. If so, and the word and its reverse are not the same (to avoid using a word twice in a pair), add the pair of indices to the result.
  3. Additionally, check for each word if there's a word in the `Trie` that, when appended to the end of the current word, forms a palindrome. Similarly, check for words that, when prepended to the current word, form a palindrome.
- Proof of optimality: This approach ensures that we check all possible pairs that could form a palindrome without needing to explicitly generate and check every pair, significantly reducing the number of checks for large inputs.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<int> indices;
};

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (int i = 0; i < words.size(); i++) {
            string word = words[i];
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->indices.push_back(i);
        }
        
        vector<vector<int>> result;
        for (int i = 0; i < words.size(); i++) {
            string word = words[i];
            string reversed = word;
            reverse(reversed.begin(), reversed.end());
            TrieNode* node = root;
            for (char c : reversed) {
                if (!node->children.count(c)) break;
                node = node->children[c];
            }
            if (node && !node->indices.empty()) {
                for (int idx : node->indices) {
                    if (idx != i) {
                        result.push_back({i, idx});
                    }
                }
            }
            
            // Check for words that, when appended or prepended, form a palindrome
            for (int j = 0; j <= word.size(); j++) {
                string left = word.substr(0, j);
                string right = word.substr(j);
                if (isPalindrome(left)) {
                    string target = right;
                    reverse(target.begin(), target.end());
                    if (findInTrie(root, target)) {
                        result.push_back({findIndex(root, target), i});
                    }
                }
                if (isPalindrome(right)) {
                    string target = left;
                    reverse(target.begin(), target.end());
                    if (findInTrie(root, target)) {
                        result.push_back({i, findIndex(root, target)});
                    }
                }
            }
        }
        return result;
    }
    
    bool isPalindrome(string& s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++;
            right--;
        }
        return true;
    }
    
    bool findInTrie(TrieNode* root, string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) return false;
            node = node->children[c];
        }
        return !node->indices.empty();
    }
    
    int findIndex(TrieNode* root, string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (!node->children.count(c)) return -1;
            node = node->children[c];
        }
        return node->indices[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \cdot m^2)$ where $n$ is the number of words and $m$ is the average length of a word. The first term accounts for building the `Trie`, and the second term accounts for checking palindromes.
> - **Space Complexity:** $O(n \cdot m)$ for storing the `Trie`.
> - **Optimality proof:** This approach efficiently uses a `Trie` to reduce the number of checks for forming palindromes, making it more efficient than the brute force approach for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `Trie` for efficient string matching, checking for palindromes.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (checking for palindromes, using a `Trie` for efficient lookup).
- Optimization techniques learned: Using data structures like `Trie` to reduce the time complexity of string matching tasks.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty strings, single-character strings).
- Edge cases to watch for: Words that are the same when reversed, words that are substrings of other words.
- Performance pitfalls: Using inefficient data structures or algorithms for string matching.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases.