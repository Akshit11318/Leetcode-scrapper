## Number of Matching Subsequences
**Problem Link:** https://leetcode.com/problems/number-of-matching-subsequences/description

**Problem Statement:**
- Input format: Given a string `s` and an array of strings `words`, find the number of `words` that are a subsequence of `s`.
- Constraints: $1 \leq s.length \leq 5 \times 10^4$ and $1 \leq words.length \leq 5000$.
- Expected output format: The number of words that are a subsequence of `s`.
- Key requirements and edge cases to consider: 
    - Handling empty strings or arrays.
    - Ensuring case sensitivity or insensitivity as per the problem statement.
    - Understanding the definition of a subsequence.
- Example test cases with explanations: 
    - Input: `s = "abcde"`, `words = ["a","bb","acd","ace"]`. Output: `3`. Explanation: There are three strings in `words` that are a subsequence of `s`: `"a"`, `"acd"`, `"ace"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each word in the `words` array, check if it is a subsequence of `s`. This involves comparing characters one by one, ensuring that the order is maintained.
- Step-by-step breakdown of the solution:
    1. Iterate over each word in `words`.
    2. For each word, iterate through its characters and try to find them in `s` in the same order.
    3. If all characters of a word are found in `s` in the correct order, increment the count of matching subsequences.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement without requiring complex data structures or algorithms.

```cpp
int numMatchingSubseq(string s, vector<string>& words) {
    int count = 0;
    for (const string& word : words) {
        int sIndex = 0, wordIndex = 0;
        while (sIndex < s.size() && wordIndex < word.size()) {
            if (s[sIndex] == word[wordIndex]) {
                wordIndex++;
            }
            sIndex++;
        }
        if (wordIndex == word.size()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of words, and $k$ is the average length of a word. This is because for each word, we potentially scan through `s` once.
> - **Space Complexity:** $O(1)$, not counting the input, because we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The nested loops over `words` and `s` lead to the time complexity, while the minimal use of extra space results in the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of scanning through `s` for each word, we can use a more efficient data structure or approach that allows us to process `s` in a way that reduces the number of comparisons needed for each word.
- Detailed breakdown of the approach:
    1. Create a hashmap or similar data structure to store the indices of characters in `s`.
    2. For each word, use the hashmap to quickly find the next occurrence of each character in `s`, ensuring the order is maintained.
- Proof of optimality: This approach optimizes the scanning process by leveraging the hashmap for fast lookups, reducing the time complexity compared to the brute force method.

```cpp
int numMatchingSubseq(string s, vector<string>& words) {
    int count = 0;
    unordered_map<char, vector<int>> charIndices;
    for (int i = 0; i < s.size(); i++) {
        charIndices[s[i]].push_back(i);
    }
    for (const string& word : words) {
        int prevIndex = -1;
        bool isSubseq = true;
        for (char c : word) {
            auto it = charIndices.find(c);
            if (it == charIndices.end() || it->second.empty()) {
                isSubseq = false;
                break;
            }
            auto nextIndexIt = lower_bound(it->second.begin(), it->second.end(), prevIndex + 1);
            if (nextIndexIt == it->second.end()) {
                isSubseq = false;
                break;
            }
            prevIndex = *nextIndexIt;
        }
        if (isSubseq) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \cdot k \cdot \log(n))$, where $n$ is the length of `s`, $m$ is the number of words, and $k$ is the average length of a word. The $\log(n)$ factor comes from the binary search in the vector of indices for each character.
> - **Space Complexity:** $O(n)$, because we store the indices of characters in `s` in the hashmap.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to check each word against `s` by using a hashmap for fast lookups and binary search for finding the next index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - Use of hashmap for efficient lookups.
    - Binary search for finding the next index in a sorted list.
- Problem-solving patterns identified: 
    - Breaking down the problem into smaller, more manageable parts (e.g., checking each word individually).
    - Using data structures to optimize the solution.
- Optimization techniques learned: 
    - Reducing the number of comparisons needed by using a hashmap.
    - Applying binary search for efficient index finding.

**Mistakes to Avoid:**
- Common implementation errors: 
    - Incorrectly handling edge cases (e.g., empty strings or arrays).
    - Failing to validate inputs.
- Performance pitfalls: 
    - Using inefficient algorithms or data structures that lead to high time or space complexities.
- Testing considerations: 
    - Ensuring to test with various inputs, including edge cases, to validate the correctness and robustness of the solution.