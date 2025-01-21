## To Be or Not to Be
**Problem Link:** https://leetcode.com/problems/to-be-or-not-to-be/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, determine whether it is a palindrome or not. 
- Expected output format: Return `true` if the string is a palindrome and `false` otherwise.
- Key requirements and edge cases to consider: The input string `s` may contain non-alphanumeric characters and is case-insensitive.
- Example test cases with explanations: 
    - Input: `s = "A man, a plan, a canal: Panama"`
    - Output: `true`
    - Explanation: Ignoring non-alphanumeric characters and considering only alphanumeric characters in a case-insensitive manner, the string reads the same backward as forward.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare characters from the start and end of the string, moving towards the center.
- Step-by-step breakdown of the solution:
    1. Convert the string to lowercase to handle case-insensitivity.
    2. Initialize two pointers, one at the start and one at the end of the string.
    3. Compare the characters at the current positions of the two pointers. If they are not alphanumeric, move the pointer towards the center.
    4. If the characters are alphanumeric and not equal, return `false`.
    5. If the loop completes without finding any unequal alphanumeric characters, return `true`.
- Why this approach comes to mind first: It directly implements the definition of a palindrome, comparing characters from both ends towards the center.

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (!isalnum(s[left])) {
                left++;
            } else if (!isalnum(s[right])) {
                right--;
            } else {
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because each character is visited at most twice.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input string, because only a constant amount of space is used.
> - **Why these complexities occur:** The time complexity is linear because we potentially scan the entire string once. The space complexity is constant because we only use a fixed amount of space to store the pointers and do not allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, as it already has a linear time complexity and constant space complexity, making it optimal for this problem.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Any algorithm must at least read the input string once, resulting in a time complexity of at least $O(n)$. Therefore, the brute force approach is already optimal.

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (!isalnum(s[left])) {
                left++;
            } else if (!isalnum(s[right])) {
                right--;
            } else {
                if (tolower(s[left]) != tolower(s[right])) {
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because each character is visited at most twice.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input string, because only a constant amount of space is used.
> - **Optimality proof:** The time complexity is linear because we potentially scan the entire string once. The space complexity is constant because we only use a fixed amount of space to store the pointers and do not allocate any additional space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, case-insensitive comparison, and handling of non-alphanumeric characters.
- Problem-solving patterns identified: The importance of considering edge cases and non-alphanumeric characters in string manipulation problems.
- Optimization techniques learned: Using two pointers to compare characters from both ends of the string towards the center.
- Similar problems to practice: Other string manipulation problems involving palindromes or two-pointer techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not handling non-alphanumeric characters correctly, not considering case-insensitivity.
- Edge cases to watch for: Empty strings, strings with only non-alphanumeric characters, strings with different cases.
- Performance pitfalls: Using unnecessary loops or recursive calls that increase the time complexity.
- Testing considerations: Testing with a variety of inputs, including edge cases and different types of palindromes.