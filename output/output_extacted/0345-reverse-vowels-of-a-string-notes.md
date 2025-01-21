## Reverse Vowels of a String
**Problem Link:** https://leetcode.com/problems/reverse-vowels-of-a-string/description

**Problem Statement:**
- Input: A string `s` containing any ASCII characters.
- Constraints: The length of `s` is in the range `[1, 10^5]`.
- Expected Output: The input string with all vowels reversed.
- Key Requirements: Identify vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercase counterparts) and reverse their order within the string.
- Edge Cases: Strings with no vowels, strings with all vowels, and strings with a mix of characters and vowels.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves identifying all vowels in the string, storing them, and then replacing the vowels in the original string with the stored vowels in reverse order.
- Step-by-step breakdown:
  1. Create a string or array to store the vowels found in the input string.
  2. Iterate through the input string to find and store all vowels.
  3. Reverse the stored vowels.
  4. Iterate through the input string again, replacing each vowel with the corresponding vowel from the reversed list.

```cpp
#include <iostream>
#include <string>
using namespace std;

string reverseVowelsBruteForce(string s) {
    string vowels = "";
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            vowels += c;
        }
    }
    int n = s.length();
    int idx = 0;
    string res = s;
    for (int i = 0; i < n; i++) {
        if (res[i] == 'a' || res[i] == 'e' || res[i] == 'i' || res[i] == 'o' || res[i] == 'u' ||
            res[i] == 'A' || res[i] == 'E' || res[i] == 'I' || res[i] == 'O' || res[i] == 'U') {
            res[i] = vowels[vowels.length() - idx - 1];
            idx++;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're iterating through the string twice: once to find and store vowels and once to replace them.
> - **Space Complexity:** $O(n)$, because in the worst case, if all characters are vowels, the size of the `vowels` string will be equal to the length of the input string.
> - **Why these complexities occur:** The iteration through the string to find and replace vowels causes the time complexity. The storage of vowels in a separate string causes the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal solution involves using two pointers, one starting from the beginning of the string and one from the end, moving towards each other.
- When a vowel is found at either pointer, the vowels are swapped.
- This process continues until the pointers meet or cross over, ensuring all vowels have been reversed.

```cpp
string reverseVowelsOptimal(string s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (!isVowel(s[left])) left++;
        else if (!isVowel(s[right])) right--;
        else {
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
    return s;
}

bool isVowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because in the worst case, we're potentially scanning the entire string once.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the pointers and no additional data structures that scale with input size.
> - **Optimality proof:** This is optimal because we're making a single pass through the data, and the problem requires examining each character at least once to determine if it's a vowel and needs to be swapped.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, in-place modification.
- Problem-solving patterns identified: Identifying and reversing specific characters within a string.
- Optimization techniques learned: Reducing the number of iterations and minimizing extra space usage.
- Similar problems to practice: Reversing specific parts of a string or array, finding and modifying patterns within strings.

**Mistakes to Avoid:**
- Not checking for edge cases, such as an empty string or a string with no vowels.
- Failing to optimize the solution, leading to inefficient time or space complexity.
- Not validating the input string or handling non-ASCII characters if necessary.
- Testing considerations: Ensure to test with strings containing a mix of vowels and non-vowel characters, as well as edge cases like empty strings or strings with all vowels.