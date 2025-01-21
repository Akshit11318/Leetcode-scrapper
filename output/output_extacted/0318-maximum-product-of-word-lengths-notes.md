## Maximum Product of Word Lengths
**Problem Link:** https://leetcode.com/problems/maximum-product-of-word-lengths/description

**Problem Statement:**
- Input format: An array of strings `words`.
- Constraints: Each word consists of lowercase English letters, and the length of `words` is at most 1000.
- Expected output format: The maximum possible product of word lengths.
- Key requirements and edge cases to consider:
  - Two words cannot be used together if they have any character in common.
  - The goal is to find the maximum product of word lengths from non-overlapping words.

**Example Test Cases:**
- Input: `words = ["abcw","baz","foo","bar","xtfn","abc"]`
  - Output: `16`
  - Explanation: The two words are "abcw", "xtfn".
- Input: `words = ["a","ab","abc","d","cd","bcd","abcd"]`
  - Output: `4`
  - Explanation: The two words are "ab", "cd".

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible pair of words to see if they have any characters in common.
- For each pair of words that do not share any characters, calculate the product of their lengths.
- Keep track of the maximum product found.

```cpp
int maxProduct(vector<string>& words) {
    int n = words.size();
    int maxProduct = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (!hasCommonChar(words[i], words[j])) {
                maxProduct = max(maxProduct, (int)words[i].length() * (int)words[j].length());
            }
        }
    }
    return maxProduct;
}

bool hasCommonChar(const string& word1, const string& word2) {
    for (char c : word1) {
        if (word2.find(c) != string::npos) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because for each pair of words, we potentially scan through each character of both words.
> - **Space Complexity:** $O(1)$, not considering the space needed for the input. This is because we only use a constant amount of space to store the maximum product and other variables.
> - **Why these complexities occur:** The nested loops over the words and the potential scan through each character of the words cause these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use bit manipulation to efficiently check for common characters between words.
- For each word, create a bitmask where the $i^{th}$ bit is set if the word contains the $i^{th}$ letter of the alphabet.
- Then, for each pair of words, check if their bitmasks have any bits in common by performing a bitwise AND operation. If the result is 0, it means the words do not share any characters.

```cpp
int maxProduct(vector<string>& words) {
    int n = words.size();
    vector<int> masks(n);
    for (int i = 0; i < n; i++) {
        for (char c : words[i]) {
            masks[i] |= 1 << (c - 'a');
        }
    }
    
    int maxProduct = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (!(masks[i] & masks[j])) {
                maxProduct = max(maxProduct, (int)words[i].length() * (int)words[j].length());
            }
        }
    }
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. The $n^2$ term comes from the nested loops over the words, and the $n \cdot m$ term comes from creating the bitmasks for each word.
> - **Space Complexity:** $O(n)$, for storing the bitmasks of the words.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to check for common characters between words, leveraging the efficiency of bitwise operations.

---

### Final Notes

**Learning Points:**
- The importance of bit manipulation for efficient character set operations.
- How to approach problems involving string comparisons and set operations.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Failing to consider the efficiency of character set operations.
- Not utilizing bitwise operations for set operations.
- Overlooking the potential for reducing time complexity through clever data structures or algorithms.