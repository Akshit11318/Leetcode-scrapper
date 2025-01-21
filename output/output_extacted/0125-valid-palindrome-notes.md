## Valid Palindrome
**Problem Link:** https://leetcode.com/problems/valid-palindrome/description

**Problem Statement:**
- Input: a string `s` containing alphanumeric characters and spaces.
- Constraints: $1 \leq s.length \leq 2 \times 10^5$.
- Expected Output: a boolean indicating whether the string is a palindrome after removing non-alphanumeric characters and converting to lowercase.
- Key requirements: ignore non-alphanumeric characters, ignore case sensitivity.
- Example test cases:
  - Input: `s = "A man, a plan, a canal: Panama"`, Output: `true`.
  - Input: `s = "Not a palindrome"`, Output: `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: remove non-alphanumeric characters, convert to lowercase, and compare the resulting string with its reverse.
- Step-by-step breakdown:
  1. Create a new string with only alphanumeric characters.
  2. Convert this new string to lowercase.
  3. Compare the resulting string with its reverse.
- Why this approach comes to mind first: simplicity and straightforwardness.

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        string temp;
        // Create a new string with only alphanumeric characters and convert to lowercase
        for (char c : s) {
            if (isalnum(c)) {
                temp += tolower(c);
            }
        }
        
        // Compare the resulting string with its reverse
        string rev = temp;
        reverse(rev.begin(), rev.end());
        return temp == rev;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we iterate over the string once to create the new string and again to reverse it. The comparison operation also takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ because we create two new strings of length up to $n$.
> - **Why these complexities occur:** The need to create new strings and iterate over the input string leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: instead of creating new strings, we can use two pointers starting from both ends of the original string and move towards the center, skipping non-alphanumeric characters and ignoring case.
- Detailed breakdown:
  1. Initialize two pointers, one at the start and one at the end of the string.
  2. Move the pointers towards the center, skipping non-alphanumeric characters.
  3. Compare characters at the pointers (after converting to lowercase), and return false if they are not equal.
- Proof of optimality: this approach minimizes the number of operations by avoiding the creation of new strings and directly comparing characters in the original string.

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
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because in the worst case, we might end up scanning the entire string once.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the pointers and do not create any additional data structures that scale with input size.
> - **Optimality proof:** This approach is optimal because it achieves the same result as the brute force approach but with significantly reduced memory usage and without the overhead of creating new strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, string manipulation.
- Problem-solving patterns identified: optimizing memory usage by avoiding unnecessary data structure creation.
- Optimization techniques learned: reducing space complexity by using pointers instead of creating new strings.
- Similar problems to practice: other string manipulation and palindrome problems.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle case sensitivity, not checking for alphanumeric characters correctly.
- Edge cases to watch for: empty strings, strings with only non-alphanumeric characters.
- Performance pitfalls: creating unnecessary data structures, not optimizing for space complexity.
- Testing considerations: testing with a variety of inputs, including edge cases and large inputs to check for performance.