## Longest Chunked Palindrome Decomposition

**Problem Link:** https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description

**Problem Statement:**
- Input: A string `text`.
- Constraints: `1 <= text.length <= 1000`, `text` consists of lowercase English letters.
- Expected Output: The longest decomposition of `text` into chunked palindromes such that every chunk is a palindrome.
- Key Requirements: The decomposition should be the longest possible, and every chunk must be a palindrome.
- Edge Cases: Single character strings, strings with no palindromic decomposition, and strings that are already palindromes.
- Example Test Cases:
  - Input: "ghiabcdefhelloadamhelloabcdefghi"
    - Output: 23
  - Input: "merchant"
    - Output: 1
  - Input: "antaprezatepzapreanteapapzanrezpa"
    - Output: 11

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible decomposition of the string into substrings and verifying if each substring is a palindrome.
- Step-by-step breakdown:
  1. Generate all possible decompositions of the input string.
  2. For each decomposition, check if every substring is a palindrome.
  3. Keep track of the longest decomposition that consists entirely of palindromic substrings.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding the optimal solution if the string is not too long.

```cpp
#include <iostream>
#include <string>
#include <vector>

bool isPalindrome(const std::string& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++, right--;
    }
    return true;
}

int longestDecomposition(const std::string& text) {
    int n = text.size();
    int maxLen = 0;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        std::vector<std::string> chunks;
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                std::string chunk = text.substr(start, i - start + 1);
                chunks.push_back(chunk);
                start = i + 1;
            }
        }
        if (start < n) {
            std::string chunk = text.substr(start);
            chunks.push_back(chunk);
        }
        
        bool allPalindrome = true;
        for (const auto& chunk : chunks) {
            if (!isPalindrome(chunk)) {
                allPalindrome = false;
                break;
            }
        }
        
        if (allPalindrome && chunks.size() > maxLen) {
            maxLen = chunks.size();
        }
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the length of the input string. This is because we generate $2^n$ possible decompositions and for each, we potentially check $n$ substrings, each taking $O(n)$ time to verify if it's a palindrome.
> - **Space Complexity:** $O(n)$, for storing the current decomposition and the substrings being checked.
> - **Why these complexities occur:** The brute force approach involves an exhaustive search through all possible decompositions, leading to exponential time complexity. The palindrome check for each substring adds a quadratic factor due to the nested loops.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a two-pointer technique to find the longest palindromic substrings from both ends of the remaining string.
- Detailed breakdown:
  1. Initialize two pointers, one at the start and one at the end of the string.
  2. Compare characters from the start and end pointers. If they match, move both pointers towards the center.
  3. If a match is found, it indicates a palindromic substring. Remove this substring from the string and increment the count of decomposed palindromes.
  4. Repeat the process until the entire string is decomposed.
- Proof of optimality: This approach ensures that we find the longest possible decomposition into palindromic substrings because it always chooses the longest palindromes first.

```cpp
int longestDecomposition(const std::string& text) {
    int left = 0, right = text.size() - 1;
    int count = 0;
    
    while (left < right) {
        int l = left, r = right;
        while (text[l] != text[r]) {
            l++, r--;
        }
        count++;
        left = l + 1;
        right = r - 1;
    }
    
    if (left == right) count++;
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the count.
> - **Optimality proof:** This approach is optimal because it always finds the longest palindromic substrings first, ensuring the maximum decomposition length.

---

### Final Notes

**Learning Points:**
- The importance of the two-pointer technique in solving string problems.
- How to approach problems involving palindromic substrings efficiently.
- The trade-off between brute force and optimal approaches in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the exponential growth of the brute force approach for larger inputs.
- Failing to optimize the palindrome check within the loop.
- Not recognizing the potential for a two-pointer technique to simplify the problem.