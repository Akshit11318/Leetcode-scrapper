## Longest Duplicate Substring
**Problem Link:** [https://leetcode.com/problems/longest-duplicate-substring/description](https://leetcode.com/problems/longest-duplicate-substring/description)

**Problem Statement:**
- Input format and constraints: The input is a string `s` of length `n`. The goal is to find the longest duplicate substring within `s`.
- Expected output format: The output should be the longest duplicate substring. If there are multiple substrings of the same maximum length, return any one of them.
- Key requirements and edge cases to consider: The input string `s` will have a length between 1 and 10^5, and it will only contain lowercase English letters.
- Example test cases with explanations: For example, given the string "banana", the output should be "ana" because it is the longest substring that appears more than once.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible substrings of `s` and then check each one to see if it appears more than once. This can be done by iterating over all substrings and using a hash map to count their occurrences.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of `s`.
  2. Use a hash map to count the occurrences of each substring.
  3. Find the longest substring that appears more than once.
- Why this approach comes to mind first: It is straightforward and easy to implement, but it is not efficient for large inputs.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string longestDuplicateSubstringBruteForce(string s) {
    int n = s.length();
    unordered_map<string, int> count;
    string longest = "";

    // Generate all substrings and count their occurrences
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            count[substr]++;
            // Update the longest duplicate substring if necessary
            if (count[substr] > 1 && substr.length() > longest.length()) {
                longest = substr;
            }
        }
    }
    return longest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all substrings (which takes $O(n^2)$ time) and then iterate over each substring to count its occurrences (which takes $O(n)$ time in the worst case).
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we store all substrings in the hash map.
> - **Why these complexities occur:** These complexities occur because we are generating all possible substrings and then counting their occurrences, which results in a lot of repeated work.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a rolling hash to efficiently calculate the hash values of all substrings. This allows us to compare substrings in constant time.
- Detailed breakdown of the approach:
  1. Define a hash function that maps a string to a unique integer.
  2. Use a rolling hash to calculate the hash values of all substrings.
  3. Compare the hash values of substrings to find duplicates.
- Proof of optimality: This approach is optimal because it reduces the time complexity of comparing substrings from $O(n)$ to $O(1)$, resulting in an overall time complexity of $O(n^2)$.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

const int MOD = 1e9 + 7;
const int BASE = 31;

string longestDuplicateSubstringOptimal(string s) {
    int n = s.length();
    string longest = "";
    int maxLen = 0;

    // Calculate the hash values of all substrings
    for (int len = 1; len <= n; len++) {
        unordered_map<int, int> count;
        int hashVal = 0;
        int powVal = 1;

        // Calculate the hash value of the first substring
        for (int i = 0; i < len; i++) {
            hashVal = (hashVal * BASE + s[i] - 'a' + 1) % MOD;
            powVal = (powVal * BASE) % MOD;
        }

        // Update the count of the first substring
        count[hashVal]++;

        // Calculate the hash values of the remaining substrings
        for (int i = len; i < n; i++) {
            hashVal = (hashVal * BASE - (s[i - len] - 'a' + 1) * powVal % MOD + MOD) % MOD;
            hashVal = (hashVal + s[i] - 'a' + 1) % MOD;
            count[hashVal]++;

            // Update the longest duplicate substring if necessary
            if (count[hashVal] > 1 && len > maxLen) {
                maxLen = len;
                longest = s.substr(i - len + 1, len);
            }
        }
    }
    return longest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we calculate the hash values of all substrings and then compare them.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we store the hash values of substrings in the hash map.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of comparing substrings from $O(n)$ to $O(1)$, resulting in an overall time complexity of $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: rolling hash, hash map, substring comparison.
- Problem-solving patterns identified: using hash functions to reduce time complexity, comparing substrings efficiently.
- Optimization techniques learned: reducing time complexity by using rolling hash, optimizing space complexity by using a hash map.
- Similar problems to practice: finding the longest common substring, finding the shortest common supersequence.

**Mistakes to Avoid:**
- Common implementation errors: incorrect hash function, incorrect rolling hash calculation.
- Edge cases to watch for: empty input string, input string with only one character.
- Performance pitfalls: using a naive approach with high time complexity, using a hash function with high collision rate.
- Testing considerations: testing with different input sizes, testing with different input characters.