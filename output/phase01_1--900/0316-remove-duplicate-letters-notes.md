## Remove Duplicate Letters
**Problem Link:** [https://leetcode.com/problems/remove-duplicate-letters/description](https://leetcode.com/problems/remove-duplicate-letters/description)

**Problem Statement:**
- Input format: a string `s` containing lowercase English letters.
- Constraints: `1 <= s.length <= 10^4`.
- Expected output format: a string with no duplicate letters, preserving the original order of characters.
- Key requirements: remove duplicate letters while maintaining the lexicographically smallest result.
- Example test cases:
  - Input: `s = "bcabc"`
    Output: `"abc"`
  - Input: `s = "cbacdcbc"`
    Output: `"acdb"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: try all possible combinations of characters without duplicates and check if they form a valid result.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input string `s`.
  2. For each permutation, check if it contains duplicate letters.
  3. If a permutation has no duplicates, check if it is lexicographically smaller than the current result.
- Why this approach comes to mind first: it's a straightforward way to ensure all possibilities are considered, but it's inefficient due to the high number of permutations.

```cpp
#include <iostream>
#include <string>
#include <set>

using namespace std;

string removeDuplicateLettersBrute(string s) {
    int n = s.size();
    set<string> uniqueStrs;
    string result = "";
    
    // Generate all permutations
    for (int mask = 0; mask < (1 << n); mask++) {
        string currStr = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                currStr += s[i];
            }
        }
        
        // Check for duplicates
        set<char> charsInCurrStr;
        bool hasDuplicates = false;
        for (char c : currStr) {
            if (charsInCurrStr.find(c) != charsInCurrStr.end()) {
                hasDuplicates = true;
                break;
            }
            charsInCurrStr.insert(c);
        }
        
        if (!hasDuplicates) {
            uniqueStrs.insert(currStr);
        }
    }
    
    // Find the lexicographically smallest string
    for (const auto& str : uniqueStrs) {
        if (result.empty() || str < result) {
            result = str;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string `s`. This is because we generate all permutations of `s` and for each permutation, we check for duplicates in $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, for storing all unique permutations.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to the exponential number of permutations and the linear time complexity of checking each permutation for duplicates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: use a stack to keep track of the characters we've seen so far, and only add a character to the stack if it's smaller than the top of the stack and the top of the stack appears later in the string.
- Detailed breakdown of the approach:
  1. Initialize an empty stack `stk` and a frequency count `freq` for each character in `s`.
  2. Iterate through `s`. For each character `c`, decrement its frequency count `freq[c]`.
  3. While the stack is not empty and the top of the stack `stk.top()` is greater than `c` and `freq[stk.top()] > 0`, pop the top of the stack.
  4. Push `c` onto the stack.
  5. After iterating through all characters, the stack `stk` contains the lexicographically smallest result.

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

string removeDuplicateLetters(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    
    string result;
    unordered_set<char> seen;
    
    for (char c : s) {
        freq[c]--;
        
        if (seen.find(c) != seen.end()) {
            continue;
        }
        
        while (!result.empty() && c < result.back() && freq[result.back()] > 0) {
            seen.erase(result.back());
            result.pop_back();
        }
        
        result += c;
        seen.insert(c);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we make a single pass through `s`.
> - **Space Complexity:** $O(n)$, for storing the frequency count and the result string.
> - **Optimality proof:** This approach is optimal because it uses a single pass through the input string and maintains a stack of characters that are guaranteed to be in lexicographically increasing order, ensuring the result is the smallest possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using a stack to keep track of characters, frequency counting, and greedy selection.
- Problem-solving patterns identified: reducing the problem to a single pass through the input and using data structures to efficiently manage the solution.
- Optimization techniques learned: avoiding unnecessary work by using a stack and frequency count to prune the search space.

**Mistakes to Avoid:**
- Common implementation errors: failing to update frequency counts correctly, not handling edge cases (e.g., empty input string).
- Edge cases to watch for: duplicate characters, characters that appear only once, and the empty string.
- Performance pitfalls: using inefficient data structures or algorithms, such as the brute force approach.
- Testing considerations: thoroughly test the function with various input cases, including edge cases and large inputs.