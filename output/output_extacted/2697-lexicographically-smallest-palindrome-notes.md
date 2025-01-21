## Lexicographically Smallest Palindrome

**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-palindrome/description

**Problem Statement:**
- Input: A string `s`.
- Output: The lexicographically smallest palindrome that can be obtained by adding characters to the end of `s`.
- Key requirements: 
  - The resulting string must be a palindrome.
  - It must be lexicographically smaller than any other palindrome that can be obtained by adding characters to `s`.
- Edge cases: 
  - If `s` is already a palindrome, return `s`.
  - If `s` is empty, return an empty string.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible string that can be obtained by adding characters to the end of `s` and verifying if it's a palindrome.
- This approach involves generating all possible strings, checking for palindromes, and then comparing them lexicographically.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string generateNextString(string s) {
    // Generate all possible next strings by appending 'a' to 'z' to s
    vector<string> nextStrings;
    for (char c = 'a'; c <= 'z'; c++) {
        nextStrings.push_back(s + c);
    }
    return *min_element(nextStrings.begin(), nextStrings.end());
}

bool isPalindrome(string s) {
    // Check if s is a palindrome
    int i = 0, j = s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++; j--;
    }
    return true;
}

string bruteForceApproach(string s) {
    // Start with the input string
    string result = s;
    
    // Continue adding characters until a palindrome is found
    while (!isPalindrome(result)) {
        result = generateNextString(result);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n \cdot n)$ where $n$ is the length of the string `s`. This is because in the worst case, we might have to generate $26^n$ strings (by appending all possible characters to the end of `s` and its subsequent modifications) and check each for being a palindrome, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ for storing the current string being checked.
> - **Why these complexities occur:** The brute force approach involves generating a large number of strings and checking each for the palindrome property, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is recognizing that to achieve the lexicographically smallest palindrome, we should mirror the first half of the string `s` to the second half, unless `s` is already a palindrome.
- If `s` is not a palindrome, we append the reverse of the first half of `s` (excluding any part that matches the end of `s`) to the end of `s` to form the smallest palindrome.

```cpp
string optimalApproach(string s) {
    string reversed_s = s;
    reverse(reversed_s.begin(), reversed_s.end());
    
    for (int i = 0; i <= s.size(); i++) {
        if (s.substr(0, s.size() - i) == reversed_s.substr(i)) {
            return s + reversed_s.substr(0, i);
        }
    }
    
    // This should not occur given the logic above
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `s$. This is because we potentially iterate through `s` once to find the matching prefix with its reverse.
> - **Space Complexity:** $O(n)$ for storing the reversed string.
> - **Optimality proof:** This approach is optimal because it directly constructs the lexicographically smallest palindrome by appending the minimum necessary characters to `s`, without needing to generate and compare all possible palindromes.

---

### Final Notes

**Learning Points:**
- **Two-Pointer Technique:** Used in checking for palindromes.
- **String Manipulation:** Appending characters, reversing strings.
- **Optimization Techniques:** Avoiding unnecessary string generations and comparisons.

**Mistakes to Avoid:**
- **Inefficient String Generation:** Avoid generating all possible strings as in the brute force approach.
- **Incorrect Palindrome Checks:** Ensure the palindrome check is correct and efficient.
- **Not Considering Edge Cases:** Always consider the case where the input string is already a palindrome or is empty.