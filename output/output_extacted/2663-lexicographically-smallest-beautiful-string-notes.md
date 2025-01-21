## Lexicographically Smallest Beautiful String
**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-beautiful-string/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= s.length <= 1000`, `s` consists of lowercase English letters.
- Expected output: The lexicographically smallest beautiful string of length `k` that can be formed from the characters of `s`. If no such string exists, return an empty string.
- Key requirements: A string is considered `beautiful` if it contains at least one distinct character for each of its first `i` characters.
- Example test cases:
  - Input: `s = "abc", k = 2`, Output: `"ac"`
  - Input: `s = "aab", k = 4`, Output: `""`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible strings of length `k` using the characters of `s`, and then check each string to see if it is `beautiful`.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `s` of length `k`.
  2. For each permutation, check if it is `beautiful` by verifying that it contains at least one distinct character for each of its first `i` characters.
  3. Keep track of the lexicographically smallest `beautiful` string found.

```cpp
#include <iostream>
#include <string>
#include <set>
using namespace std;

void generatePermutations(string s, string current, int k, string& smallestBeautiful) {
    if (current.length() == k) {
        set<char> distinctChars;
        bool isBeautiful = true;
        for (int i = 0; i < k; i++) {
            distinctChars.insert(current[i]);
            if (distinctChars.size() < i + 1) {
                isBeautiful = false;
                break;
            }
        }
        if (isBeautiful && (smallestBeautiful.empty() || current < smallestBeautiful)) {
            smallestBeautiful = current;
        }
        return;
    }
    for (char c : s) {
        current += c;
        generatePermutations(s, current, k, smallestBeautiful);
        current.pop_back();
    }
}

string lexicographicallySmallestBeautifulString(string s, int k) {
    string smallestBeautiful;
    generatePermutations(s, "", k, smallestBeautiful);
    return smallestBeautiful;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^k \cdot k)$, where $26^k$ is the number of permutations and $k$ is the time to check if a string is `beautiful`.
> - **Space Complexity:** $O(k)$, for the recursion stack and the `current` string.
> - **Why these complexities occur:** The brute force approach generates all possible permutations of `s` of length `k`, resulting in an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of generating all permutations, we can build the `beautiful` string character by character, ensuring that it remains `beautiful` at each step.
- Detailed breakdown of the approach:
  1. Start with an empty string `result`.
  2. At each step, try to append the smallest character to `result` that keeps it `beautiful`.
  3. If no such character exists, return an empty string.
  4. Repeat step 2 until `result` has length `k`.

```cpp
#include <iostream>
#include <string>
#include <set>
using namespace std;

string lexicographicallySmallestBeautifulString(string s, int k) {
    string result;
    set<char> distinctChars;
    for (int i = 0; i < k; i++) {
        char smallestChar = '\0';
        for (char c : s) {
            if (distinctChars.find(c) == distinctChars.end() || (result.length() > 0 && c < result.back())) {
                if (smallestChar == '\0' || c < smallestChar) {
                    smallestChar = c;
                }
            }
        }
        if (smallestChar == '\0') {
            return "";
        }
        result += smallestChar;
        distinctChars.insert(smallestChar);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n)$, where $n$ is the length of `s`.
> - **Space Complexity:** $O(k)$, for the `result` string and the `distinctChars` set.
> - **Optimality proof:** This approach is optimal because it builds the `beautiful` string character by character, ensuring that it remains `beautiful` at each step, and it does so in linear time with respect to the length of `s` and `k`.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, greedy algorithms, and set operations.
- Problem-solving patterns identified: Building a solution character by character and ensuring that it remains valid at each step.
- Optimization techniques learned: Avoiding unnecessary computations and using data structures to keep track of relevant information.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of characters in the `s` string before trying to append them to the `result` string.
- Edge cases to watch for: When `k` is larger than the length of `s`, or when `s` contains duplicate characters.
- Performance pitfalls: Generating all permutations of `s` of length `k`, resulting in an exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it produces the correct output.