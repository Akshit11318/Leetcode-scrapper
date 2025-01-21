## Break a Palindrome
**Problem Link:** https://leetcode.com/problems/break-a-palindrome/description

**Problem Statement:**
- Given a palindromic string `palindrome`, you need to change **exactly one character** by replacing a character to break the palindrome.
- If the palindrome has only one character, return an empty string `""`.
- Input constraints: `1 <= palindrome.length <= 1000`, and `palindrome` consists only of lowercase English letters.
- Expected output: Return a palindrome broken by changing exactly one character.

**Key Requirements and Edge Cases:**
- The input string is guaranteed to be a palindrome.
- If the length of the palindrome is 1, return an empty string.
- Changing a character means replacing it with a different lowercase English letter.

**Example Test Cases:**
- Input: `palindrome = "abccba"` Output: `"aaccba"`
- Input: `palindrome = "a"` Output: `""`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible replacement of a character in the palindrome string.
- For each character in the string, try replacing it with all possible lowercase English letters (26 options) and check if the resulting string is not a palindrome.
- If a replacement results in a non-palindrome string, return that string as it satisfies the condition of breaking the palindrome by changing exactly one character.

```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.length();
        if (n == 1) return "";
        
        for (int i = 0; i < n / 2; i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                if (palindrome[i] != c) {
                    string temp = palindrome;
                    temp[i] = c;
                    if (!isPalindrome(temp)) {
                        return temp;
                    }
                }
            }
        }
        
        // If no replacement is found in the first half, replace the last character with 'a'
        string temp = palindrome;
        temp[n - 1] = 'a';
        return temp;
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
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 26)$, where $n$ is the length of the palindrome string. This is because for each character in the first half of the string, we try 26 possible replacements.
> - **Space Complexity:** $O(n)$, as we create a temporary string for each replacement.
> - **Why these complexities occur:** The brute force approach involves exhaustive checking of all possible replacements for each character in the first half of the string, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves understanding the properties of palindromes and applying a more strategic replacement strategy.
- If the length of the palindrome is greater than 1, we can break it by replacing the first non-'a' character in the first half with 'a'. If all characters in the first half are 'a', then we can break the palindrome by replacing the last character with 'b'.
- This strategy ensures that we break the palindrome with the minimum number of replacements (exactly one) and avoids unnecessary checks.

```cpp
class Solution {
public:
    string breakPalindrome(string palindrome) {
        int n = palindrome.length();
        if (n == 1) return "";
        
        for (int i = 0; i < n / 2; i++) {
            if (palindrome[i] != 'a') {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        
        palindrome[n - 1] = 'b';
        return palindrome;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the palindrome string. This is because we potentially iterate through the first half of the string once.
> - **Space Complexity:** $O(1)$, as we modify the input string in-place.
> - **Optimality proof:** This approach is optimal because it breaks the palindrome with the minimum number of replacements (exactly one) and does so in linear time complexity, which is the best possible time complexity for this problem given that we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Understanding the properties of palindromes and how to strategically break them.
- Applying a more efficient replacement strategy to minimize the number of replacements.
- Recognizing the importance of handling edge cases, such as when the length of the palindrome is 1.

**Mistakes to Avoid:**
- Failing to handle the edge case where the length of the palindrome is 1.
- Using an exhaustive brute force approach without considering more efficient strategies.
- Not recognizing the properties of palindromes and how they can be broken with a single replacement.