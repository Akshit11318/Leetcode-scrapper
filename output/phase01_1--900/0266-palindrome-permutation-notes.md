## Palindrome Permutation
**Problem Link:** https://leetcode.com/problems/palindrome-permutation/description

**Problem Statement:**
- Input format: A string `s`.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: A boolean indicating whether a permutation of `s` could form a palindrome.
- Key requirements and edge cases to consider: 
    - The input string may contain non-alphabetic characters and may be case-sensitive.
    - A palindrome can have at most one character with an odd frequency count, as it will be the middle character in the palindrome.
- Example test cases with explanations:
    - `s = "tactcoa"` returns `true` because a permutation of `s` ("tacocat") is a palindrome.
    - `s = "abc"` returns `false` because no permutation of `s` is a palindrome.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all permutations of the input string and check each one to see if it's a palindrome.
- Step-by-step breakdown of the solution:
    1. Generate all permutations of the input string.
    2. For each permutation, check if it's equal to its reverse.
    3. If any permutation is a palindrome, return `true`.
    4. If no permutations are palindromes after checking all, return `false`.
- Why this approach comes to mind first: It's a straightforward, brute-force method that checks all possibilities.

```cpp
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    bool canPermutePalindrome(string s) {
        // Generate all permutations of the input string
        sort(s.begin(), s.end());
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i < s.size() - 1 && s[i] == s[i + 1]) {
                i++;
            } else {
                count++;
            }
        }
        // More than one character with odd frequency means it's not a palindrome
        return count <= 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the string, where $n$ is the length of the string.
> - **Space Complexity:** $O(n)$ for the sorting algorithm's internal workings.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to the sorting algorithm's need for additional memory.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations, we can count the frequency of each character in the string and check if at most one character has an odd frequency.
- Detailed breakdown of the approach:
    1. Create a frequency map of characters in the string.
    2. Iterate through the frequency map and count the number of characters with odd frequencies.
    3. If more than one character has an odd frequency, return `false`.
    4. Otherwise, return `true`.
- Proof of optimality: This approach has a linear time complexity, which is the best we can achieve since we must examine each character in the string at least once.
- Why further optimization is impossible: We must examine each character at least once to determine its frequency, so the time complexity cannot be improved further.

```cpp
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> freqMap;
        for (char c : s) {
            freqMap[c]++;
        }
        int oddCount = 0;
        for (auto& pair : freqMap) {
            if (pair.second % 2 != 0) {
                oddCount++;
            }
            if (oddCount > 1) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate through the string once to count frequencies.
> - **Space Complexity:** $O(n)$ for the frequency map in the worst case (when all characters are unique).
> - **Optimality proof:** This approach is optimal because it examines each character exactly once, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, permutation properties, and optimization techniques.
- Problem-solving patterns identified: Reducing the problem to a simpler form (checking frequency counts instead of generating permutations).
- Optimization techniques learned: Using frequency maps to efficiently count character occurrences.

**Mistakes to Avoid:**
- Common implementation errors: Not handling case sensitivity or non-alphabetic characters correctly.
- Edge cases to watch for: Strings with all unique characters or strings with only one character.
- Performance pitfalls: Using inefficient algorithms like generating all permutations.
- Testing considerations: Ensure the solution works for both small and large input strings, and consider edge cases like empty strings or strings with non-alphabetic characters.