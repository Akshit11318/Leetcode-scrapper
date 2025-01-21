## Palindrome Permutation II

**Problem Link:** https://leetcode.com/problems/palindrome-permutation-ii/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: The length of `s` is at most `1000`.
- Expected Output: Generate all unique palindromic permutations of `s`.
- Key Requirements:
  - A palindromic permutation is a permutation of the characters of `s` that forms a palindrome.
  - If no such palindromic permutations exist, return an empty list.
- Edge Cases:
  - Empty string: The only palindromic permutation is an empty string itself.
  - Single-character string: The only palindromic permutation is the string itself.
- Example Test Cases:
  - Input: `s = "aabb"`, Output: `["abba","baab"]`
  - Input: `s = "abc"`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Generate all permutations of the input string and check if each permutation is a palindrome.
- Step-by-Step Breakdown:
  1. Generate all permutations of the input string.
  2. For each permutation, check if it is a palindrome.
  3. If a permutation is a palindrome, add it to the result list.
- Why This Approach Comes to Mind First: It directly addresses the problem statement by generating all possible permutations and checking for palindromes.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

void generatePermutations(std::string s, int start, int end, std::vector<std::string>& result) {
    if (start == end) {
        std::string temp = s;
        std::reverse(temp.begin(), temp.end());
        if (s == temp) {
            result.push_back(s);
        }
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(s[start], s[i]);
            generatePermutations(s, start + 1, end, result);
            std::swap(s[start], s[i]); // Backtrack
        }
    }
}

std::vector<std::string> generatePalindromes(std::string s) {
    std::vector<std::string> result;
    generatePermutations(s, 0, s.length() - 1, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the input string, because we are generating all permutations of the string.
> - **Space Complexity:** $O(n!)$ for storing all permutations and the recursion stack.
> - **Why These Complexities Occur:** Generating all permutations of a string of length $n$ requires $n!$ operations, and storing them requires $n!$ space. The recursion stack for generating permutations also uses up to $n$ space.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of generating all permutations and checking for palindromes, we can directly construct palindromic permutations by ensuring that the first half of the string is mirrored in the second half, except possibly for one character in the middle if the length of the string is odd.
- Detailed Breakdown:
  1. Count the frequency of each character in the input string.
  2. Identify characters with odd counts, as there can be at most one such character for a palindromic permutation to exist.
  3. Construct the first half of the palindromic permutation by using characters with even counts (each character appearing half as many times as in the input string) and one character with an odd count if it exists.
  4. Mirror the first half to construct the second half, ensuring the middle character (if any) is correctly placed.
- Proof of Optimality: This approach directly constructs palindromic permutations without generating unnecessary permutations, thus reducing the time and space complexity significantly.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

void backtrack(std::string& s, std::unordered_map<char, int>& freq, std::string& path, std::vector<std::string>& result, int oddCount) {
    if (path.size() == s.size() / 2) {
        std::string temp = path;
        std::reverse(temp.begin(), temp.end());
        if (s.size() % 2 == 1) {
            result.push_back(path + s[s.size() / 2] + temp);
        } else {
            result.push_back(path + temp);
        }
        return;
    }

    for (auto& p : freq) {
        if (p.second > 1 && p.second / 2 > 0) {
            p.second -= 2;
            path.push_back(p.first);
            path.push_back(p.first);
            backtrack(s, freq, path, result, oddCount);
            path.pop_back();
            path.pop_back();
            p.second += 2;
        }
    }
}

std::vector<std::string> generatePalindromes(std::string s) {
    std::unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }

    std::vector<std::string> result;
    std::string path;
    int oddCount = 0;
    char oddChar;

    for (auto& p : freq) {
        if (p.second % 2 != 0) {
            oddCount++;
            oddChar = p.first;
            if (oddCount > 1) {
                return result; // No palindromic permutation exists
            }
        }
    }

    for (auto& p : freq) {
        if (p.second % 2 == 0) {
            for (int i = 0; i < p.second / 2; i++) {
                path += p.first;
            }
        }
    }

    std::sort(path.begin(), path.end());
    do {
        std::string temp = path;
        std::reverse(temp.begin(), temp.end());
        if (s.size() % 2 == 1) {
            result.push_back(path + oddChar + temp);
        } else {
            result.push_back(path + temp);
        }
    } while (std::next_permutation(path.begin(), path.end()));

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n/2})$ in the worst case, considering the construction and permutation of the first half of the string.
> - **Space Complexity:** $O(2^{n/2})$ for storing the permutations and the recursion stack.
> - **Optimality Proof:** This approach directly constructs palindromic permutations, avoiding the generation of unnecessary permutations, thus achieving a significant reduction in time and space complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation generation, frequency counting, and backtracking.
- Problem-solving patterns identified: breaking down complex problems into manageable parts (e.g., constructing the first half of a palindrome).
- Optimization techniques learned: avoiding unnecessary computation by directly constructing solutions (palindromic permutations).

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of edge cases (e.g., empty strings, single-character strings).
- Edge cases to watch for: strings with more than one character appearing an odd number of times.
- Performance pitfalls: generating all permutations without filtering for palindromes.
- Testing considerations: thoroughly testing with various input strings to ensure correctness and performance.