## Minimum Number of Moves to Make Palindrome
**Problem Link:** https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description

**Problem Statement:**
- Input format: A string `s` of length `n` consisting of lowercase English letters.
- Constraints: `1 <= n <= 10^5`.
- Expected output format: The minimum number of moves required to make the string a palindrome.
- Key requirements: A move is defined as swapping two characters in the string.
- Edge cases: If the string is already a palindrome, the output should be `0`.

**Example Test Cases:**
- Input: `s = "aabb"` Output: `2`
- Input: `s = "abc"` Output: `2`
- Input: `s = "abcdcba"` Output: `0`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of swaps to see which one results in a palindrome with the minimum number of swaps.
- Step-by-step breakdown:
  1. Generate all permutations of the input string.
  2. For each permutation, check if it's a palindrome.
  3. If it's a palindrome, calculate the number of swaps required to reach this permutation from the original string.
  4. Keep track of the minimum number of swaps that result in a palindrome.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int minMovesToMakePalindromeBruteForce(string s) {
    int n = s.length();
    int minSwaps = INT_MAX;
    do {
        string temp = s;
        int swaps = 0;
        for (int i = 0; i < n / 2; i++) {
            if (temp[i] != temp[n - i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    if (temp[j] == temp[n - i - 1]) {
                        // Swap temp[j] and temp[i]
                        char t = temp[j];
                        temp[j] = temp[i];
                        temp[i] = t;
                        swaps++;
                        break;
                    }
                }
            }
        }
        if (isPalindrome(temp)) {
            minSwaps = min(minSwaps, swaps);
        }
    } while (next_permutation(s.begin(), s.end()));
    return minSwaps;
}

bool isPalindrome(string s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$ because we're generating all permutations of the string and for each permutation, we're checking if it's a palindrome which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ because we're storing a temporary string of the same length as the input string.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of swaps, which results in a factorial time complexity. The space complexity is linear because we only need to store a temporary string of the same length as the input.

---

### Optimal Approach
**Explanation:**
- The key insight is to use a two-pointer technique, starting from the beginning and end of the string, and moving towards the center. This way, we can count the number of mismatches and calculate the minimum number of swaps required to make the string a palindrome.
- Step-by-step breakdown:
  1. Initialize two pointers, one at the start and one at the end of the string.
  2. Initialize a counter for the number of mismatches.
  3. Move the pointers towards the center of the string. If the characters at the current positions don't match, increment the mismatch counter.
  4. The minimum number of swaps required is the mismatch counter divided by 2 (because each swap can fix two mismatches).

```cpp
int minMovesToMakePalindromeOptimal(string s) {
    int n = s.length();
    int mismatches = 0;
    for (int i = 0; i < n / 2; i++) {
        if (s[i] != s[n - i - 1]) {
            mismatches++;
        }
    }
    return (mismatches + 1) / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we're scanning the string once.
> - **Space Complexity:** $O(1)$ because we're only using a constant amount of space to store the mismatch counter.
> - **Optimality proof:** This approach is optimal because we're counting the minimum number of mismatches required to make the string a palindrome, and each swap can fix two mismatches. Therefore, the minimum number of swaps required is the mismatch counter divided by 2.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, counting mismatches.
- Problem-solving patterns identified: using a simple and efficient approach to solve a complex problem.
- Optimization techniques learned: reducing the time complexity from $O(n! \cdot n)$ to $O(n)$.
- Similar problems to practice: other string manipulation problems, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, such as when the input string is already a palindrome.
- Edge cases to watch for: when the input string has an odd length, we need to handle the middle character separately.
- Performance pitfalls: using a brute force approach that has a high time complexity.
- Testing considerations: testing the function with different input strings, including edge cases, to ensure it works correctly.