## Find the Sequence of Strings Appeared on the Screen

**Problem Link:** https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/description

**Problem Statement:**
- Input format and constraints: The input will consist of an array of strings `words` and a string `s`.
- Expected output format: The function should return a list of strings representing the sequence of strings appeared on the screen.
- Key requirements and edge cases to consider: 
  - The input string `s` is the string displayed on the screen.
  - The array of strings `words` contains all the possible strings that can appear on the screen.
  - The function should return the sequence of strings in the order they appear on the screen.
- Example test cases with explanations:
  - For example, if `words = ["abc", "cba", "ab"]` and `s = "abcabc"`, the function should return `["abc", "abc"]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible substring of `s` to see if it matches any of the strings in `words`.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty list to store the sequence of strings.
  2. Iterate over the string `s` with a sliding window of size equal to the length of each string in `words`.
  3. For each substring, check if it matches any of the strings in `words`.
  4. If a match is found, add the matched string to the sequence and move the window forward by the length of the matched string.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
vector<string> findSequence(vector<string>& words, string s) {
    vector<string> sequence;
    int i = 0;
    while (i < s.size()) {
        bool found = false;
        for (string word : words) {
            if (s.substr(i, word.size()) == word) {
                sequence.push_back(word);
                i += word.size();
                found = true;
                break;
            }
        }
        if (!found) {
            break;
        }
    }
    return sequence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the string `s`, $m$ is the number of strings in `words`, and $k$ is the average length of the strings in `words`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, and the space complexity is linear because we need to store the sequence of strings.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the strings in `words` and then iterate over the string `s` to find the sequence of strings.
- Detailed breakdown of the approach: 
  1. Create a `Trie` and insert all the strings in `words` into the `Trie`.
  2. Initialize an empty list to store the sequence of strings.
  3. Iterate over the string `s` and for each character, check if it matches any of the strings in the `Trie`.
  4. If a match is found, add the matched string to the sequence and move forward by the length of the matched string.
- Why further optimization is impossible: This approach has a time complexity of $O(n \cdot k)$, where $n$ is the length of the string `s` and $k$ is the average length of the strings in `words`, which is optimal because we need to iterate over the string `s` at least once.

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    string word;
};

void insert(TrieNode* root, string word) {
    TrieNode* node = root;
    for (char c : word) {
        if (!node->children.count(c)) {
            node->children[c] = new TrieNode();
        }
        node = node->children[c];
    }
    node->word = word;
}

vector<string> findSequence(vector<string>& words, string s) {
    TrieNode* root = new TrieNode();
    for (string word : words) {
        insert(root, word);
    }
    vector<string> sequence;
    int i = 0;
    while (i < s.size()) {
        TrieNode* node = root;
        string temp;
        while (i < s.size() && node->children.count(s[i])) {
            temp += s[i];
            node = node->children[s[i]];
            i++;
            if (!node->word.empty()) {
                sequence.push_back(node->word);
                break;
            }
        }
    }
    return sequence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s` and $k$ is the average length of the strings in `words`.
> - **Space Complexity:** $O(m \cdot k)$, where $m$ is the number of strings in `words` and $k$ is the average length of the strings in `words`.
> - **Optimality proof:** This approach is optimal because we need to iterate over the string `s` at least once, and the `Trie` data structure allows us to find the sequence of strings in linear time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `Trie` data structure, string matching.
- Problem-solving patterns identified: Using a `Trie` to store a set of strings and then iterating over a string to find the sequence of strings.
- Optimization techniques learned: Using a `Trie` to reduce the time complexity from $O(n \cdot m \cdot k)$ to $O(n \cdot k)$.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a string in `words` is a substring of another string in `words`.
- Edge cases to watch for: The case where the input string `s` is empty, or the case where the array of strings `words` is empty.
- Performance pitfalls: Using a naive approach with a high time complexity, such as the brute force approach.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.