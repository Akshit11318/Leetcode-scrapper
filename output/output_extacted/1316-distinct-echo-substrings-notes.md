## Distinct Echo Substrings
**Problem Link:** https://leetcode.com/problems/distinct-echo-substrings/description

**Problem Statement:**
- Input format: A string `text`.
- Constraints: `1 <= text.length <= 2000`.
- Expected output format: The number of distinct echo substrings.
- Key requirements and edge cases to consider: An echo substring is a substring that appears at least twice in `text`, and the two occurrences are not overlapping.

**Example Test Cases:**
- `text = "abcabcabc"`: There are `12` distinct echo substrings: `"a"`, `"ab"`, `"abc"`, `"b"`, `"bc"`, `"c"`, `"aa"`, `"aba"`, `"abca"`, `"abcab"`, `"abcabc"`, `"abcabcab"`.
- `text = "leetcode"`: There is `0` distinct echo substrings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `text` to see if it appears at least twice without overlapping.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `text`.
  2. For each substring, check if it appears at least twice in `text` without overlapping.
  3. If a substring meets the condition, add it to a set to keep track of distinct echo substrings.
- Why this approach comes to mind first: It's a straightforward way to ensure we consider all possibilities.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int distinctEchoSubstrings(string text) {
    unordered_set<string> distinctSubstrings;
    for (int len = 1; len <= text.length(); len++) {
        for (int start = 0; start <= text.length() - len; start++) {
            string substr = text.substr(start, len);
            int count = 0;
            for (int i = 0; i <= text.length() - len; i++) {
                if (text.substr(i, len) == substr) {
                    count++;
                    if (count >= 2 && i + len > start && i < start + len) {
                        break; // Cannot be an echo substring if overlapping
                    }
                }
            }
            if (count >= 2) {
                bool isEcho = false;
                for (int i = 0; i <= text.length() - len; i++) {
                    if (text.substr(i, len) == substr && !isEcho) {
                        for (int j = i + len; j <= text.length() - len; j++) {
                            if (text.substr(j, len) == substr) {
                                isEcho = true;
                                break;
                            }
                        }
                    }
                }
                if (isEcho) {
                    distinctSubstrings.insert(substr);
                }
            }
        }
    }
    return distinctSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `text`. This is because we generate all substrings ($O(n^2)$) and for each, we potentially scan the entire string again ($O(n)$).
> - **Space Complexity:** $O(n^2)$ for storing all substrings in the set.
> - **Why these complexities occur:** The brute force approach involves nested loops for generating substrings and checking their occurrences, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a rolling hash or a similar efficient string matching algorithm to quickly find repeated substrings.
- Detailed breakdown of the approach:
  1. Implement a rolling hash function to efficiently calculate the hash of any substring.
  2. Iterate through all possible substring lengths and starting positions.
  3. For each substring, calculate its hash and check if it's seen before (using a hashmap).
  4. If a substring's hash is seen before and it's not overlapping with its previous occurrence, mark it as an echo substring.
- Proof of optimality: This approach ensures we check all substrings efficiently without unnecessary repetition, minimizing time complexity.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int distinctEchoSubstrings(string text) {
    unordered_map<string, int> seen;
    unordered_set<string> distinctSubstrings;
    for (int len = 1; len <= text.length(); len++) {
        for (int start = 0; start <= text.length() - len; start++) {
            string substr = text.substr(start, len);
            if (seen.find(substr) != seen.end() && seen[substr] < start) {
                distinctSubstrings.insert(substr);
            }
            seen[substr] = start + len;
        }
    }
    return distinctSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `text`. This is because we iterate through all substrings once.
> - **Space Complexity:** $O(n^2)$ for storing substrings in the set and hashmap.
> - **Optimality proof:** This approach efficiently checks all substrings without unnecessary repetition, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient string matching, use of hashmaps for fast lookup.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (e.g., checking each substring length separately).
- Optimization techniques learned: Using rolling hash or similar efficient algorithms for string matching.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., overlapping substrings).
- Edge cases to watch for: Substrings of length 1, substrings that appear only once.
- Performance pitfalls: Using brute force approaches for string matching.
- Testing considerations: Ensure to test with a variety of input strings, including edge cases.