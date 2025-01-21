## Sum of Prefix Scores of Strings
**Problem Link:** https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `words`, calculate the sum of prefix scores of each string. A prefix score is the number of strings in the array that have the same prefix as the given string.
- Expected output format: An integer representing the sum of prefix scores of all strings.
- Key requirements and edge cases to consider: The input array may contain duplicate strings, and the prefix score should be calculated for each unique prefix.
- Example test cases with explanations: For example, given `words = ["abc","ab","abc","bcd"]`, the prefix scores are as follows:
  - For "abc": 2 (because "abc" and "abc" have the same prefix)
  - For "ab": 3 (because "abc", "ab", and "abc" have the same prefix)
  - For the second "abc": 2 (because "abc" and "abc" have the same prefix)
  - For "bcd": 1 (because only "bcd" has the same prefix)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over each string in the array, and for each string, iterate over the entire array again to find all strings that have the same prefix.
- Step-by-step breakdown of the solution:
  1. Iterate over each string in the array.
  2. For each string, iterate over the array again to find all strings that have the same prefix.
  3. Calculate the prefix score by counting the number of strings with the same prefix.
  4. Add the prefix score to the total sum.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the nested loops.

```cpp
int sumPrefixScores(vector<string>& words) {
    int sum = 0;
    for (int i = 0; i < words.size(); i++) {
        int score = 0;
        for (int j = 0; j < words.size(); j++) {
            if (words[i].find(words[j]) == 0) {
                score++;
            }
        }
        sum += score;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we have two nested loops that iterate over the array, and for each pair of strings, we check if one string is a prefix of the other.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the sum and the current score.
> - **Why these complexities occur:** The high time complexity occurs because we have to iterate over the array for each string, and for each pair of strings, we have to check if one string is a prefix of the other.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the strings and calculate the prefix scores.
- Detailed breakdown of the approach:
  1. Create a `Trie` and insert all strings into it.
  2. For each string, traverse the `Trie` to calculate its prefix score.
  3. Add the prefix score to the total sum.
- Proof of optimality: This approach is optimal because we only need to traverse the `Trie` once for each string, and the time complexity of traversing the `Trie` is $O(m)$, where $m$ is the length of the string.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    int count;
    TrieNode() : count(0) {}
};

int sumPrefixScores(vector<string>& words) {
    TrieNode* root = new TrieNode();
    for (const string& word : words) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->count++;
        }
    }
    int sum = 0;
    for (const string& word : words) {
        TrieNode* node = root;
        int score = 0;
        for (char c : word) {
            node = node->children[c];
            score += node->count;
        }
        sum += score;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we need to insert all strings into the `Trie` and then traverse the `Trie` for each string.
> - **Space Complexity:** $O(n \cdot m)$, because we need to store all strings in the `Trie`.
> - **Optimality proof:** This approach is optimal because we only need to traverse the `Trie` once for each string, and the time complexity of traversing the `Trie` is $O(m)$, where $m$ is the length of the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of `Trie` data structure to solve string-related problems.
- Problem-solving patterns identified: The use of a `Trie` to calculate prefix scores.
- Optimization techniques learned: The use of a `Trie` to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve calculating prefix scores or using `Trie` data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `Trie` correctly or not updating the `count` variable correctly.
- Edge cases to watch for: Handling duplicate strings or strings with the same prefix.
- Performance pitfalls: Using a naive approach with high time complexity.
- Testing considerations: Testing the solution with different input cases, including edge cases and large inputs.