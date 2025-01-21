## Shortest and Lexicographically Smallest Beautiful String

**Problem Link:** https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= 10` and `1 <= s.length <= 10^5`.
- Expected output: The lexicographically smallest beautiful string of length `k` that is not a substring of `s`.
- Key requirements: A beautiful string is a string that only contains the characters 'a', 'b', 'c', ..., 'k' where `k` is the given integer.
- Edge cases: If no such string exists, return an empty string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible strings of length `k` using characters 'a' to 'k', and then check each string to see if it is a substring of `s`.
- Step-by-step breakdown of the solution:
  1. Generate all possible strings of length `k`.
  2. For each generated string, check if it is a substring of `s`.
  3. If a string is not a substring of `s`, return it as the result.
- Why this approach comes to mind first: It is a straightforward approach that involves checking all possibilities.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void generateAllStrings(int k, int index, string current, string& s, string& result) {
    if (index == k) {
        if (s.find(current) == string::npos) {
            result = current;
        }
        return;
    }

    for (char c = 'a'; c <= 'a' + k - 1; c++) {
        generateAllStrings(k, index + 1, current + c, s, result);
        if (!result.empty()) {
            break;
        }
    }
}

string shortestAndLexicographicallySmallestBeautifulString(string s, int k) {
    string result;
    generateAllStrings(k, 0, "", s, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^k)$ where `k` is the given integer, because we generate all possible strings of length `k` and check if they are substrings of `s`.
> - **Space Complexity:** $O(k)$ for the recursive call stack, where `k` is the length of the string.
> - **Why these complexities occur:** The brute force approach generates all possible strings of length `k` and checks each one, resulting in exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible strings and checking if they are substrings of `s`, we can use a trie data structure to efficiently store and retrieve substrings of `s`.
- Detailed breakdown of the approach:
  1. Create a trie and insert all substrings of `s` of length `k` into the trie.
  2. Generate all possible strings of length `k` and check if they are in the trie.
  3. The first string that is not in the trie is the lexicographically smallest beautiful string of length `k` that is not a substring of `s`.
- Proof of optimality: This approach is optimal because it uses a trie to efficiently store and retrieve substrings of `s`, reducing the time complexity from exponential to linear.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
};

void insertIntoTrie(TrieNode* root, const string& word) {
    TrieNode* current = root;
    for (char c : word) {
        if (current->children.find(c) == current->children.end()) {
            current->children[c] = new TrieNode();
        }
        current = current->children[c];
    }
    current->isEndOfWord = true;
}

bool searchInTrie(TrieNode* root, const string& word) {
    TrieNode* current = root;
    for (char c : word) {
        if (current->children.find(c) == current->children.end()) {
            return false;
        }
        current = current->children[c];
    }
    return current->isEndOfWord;
}

string shortestAndLexicographicallySmallestBeautifulString(string s, int k) {
    TrieNode* root = new TrieNode();
    for (int i = 0; i <= s.length() - k; i++) {
        string substring = s.substr(i, k);
        insertIntoTrie(root, substring);
    }

    string result;
    for (char c = 'a'; c <= 'a' + k - 1; c++) {
        string current = "";
        for (int i = 0; i < k; i++) {
            current += c;
            if (!searchInTrie(root, current)) {
                result = current;
                break;
            }
        }
        if (!result.empty()) {
            break;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where `n` is the length of the string `s` and `k` is the given integer, because we insert all substrings of `s` of length `k` into the trie and then generate all possible strings of length `k` to check if they are in the trie.
> - **Space Complexity:** $O(n \cdot k)$ for the trie, where `n` is the length of the string `s` and `k` is the given integer.
> - **Optimality proof:** This approach is optimal because it uses a trie to efficiently store and retrieve substrings of `s`, reducing the time complexity from exponential to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, substring matching, and lexicographical ordering.
- Problem-solving patterns identified: Using a trie to efficiently store and retrieve substrings, and generating all possible strings to find the lexicographically smallest one.
- Optimization techniques learned: Using a trie to reduce the time complexity from exponential to linear.
- Similar problems to practice: Substring matching, lexicographical ordering, and trie data structure problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for substring existence in the trie, and not generating all possible strings.
- Edge cases to watch for: Empty string, string with length less than `k`, and string with no beautiful substrings.
- Performance pitfalls: Using a brute force approach with exponential time complexity.
- Testing considerations: Test with different string lengths, `k` values, and edge cases to ensure correctness and performance.