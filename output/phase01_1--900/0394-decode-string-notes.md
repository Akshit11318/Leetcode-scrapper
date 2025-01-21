## Decode String

**Problem Link:** https://leetcode.com/problems/decode-string/description

**Problem Statement:**
- Input: A string `s` containing digits and letters, with optional `[]` to denote repetition.
- Constraints: `1 <= s.length <= 30`, `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- Expected Output: The decoded string.
- Key Requirements: Handle nested brackets, decode strings, and repeat substrings according to the given digits.
- Example Test Cases:
  - Input: `s = "3[a]2[bc]"`, Output: `"aaabcbc"`
  - Input: `s = "3[a2[c]]"`, Output: `"accaccacc"`
  - Input: `s = "2[abc]3[cd]ef"`, Output: `"abcabccdcdcdef"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves directly iterating through the string, identifying the brackets, and manually repeating the substrings.
- This approach is cumbersome and does not scale well for nested brackets or large inputs.
- It involves a lot of string concatenation and manual handling of indices, which can be error-prone.

```cpp
string decodeString(string s) {
    int i = 0;
    string res = "";
    while (i < s.size()) {
        if (isdigit(s[i])) {
            int count = 0;
            while (i < s.size() && isdigit(s[i])) {
                count = count * 10 + s[i++] - '0';
            }
            i++; // '['
            string sub = "";
            int balance = 1;
            while (balance > 0) {
                if (s[i] == '[') balance++;
                else if (s[i] == ']') balance--;
                sub += s[i++];
            }
            i--; // Skip ']'
            string temp = decodeString(sub);
            while (count-- > 0) res += temp;
        } else {
            res += s[i++];
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 4^n)$, where $n$ is the length of the string. This is because in the worst case, we might have to recursively decode a substring of length $n$ up to $n$ times.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the string concatenation.
> - **Why these complexities occur:** The brute force approach involves a lot of recursion and string concatenation, which are expensive operations.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a stack to keep track of the characters and the counts.
- When we encounter a digit, we calculate the count and push it onto the stack.
- When we encounter a `[`, we push the current string and count onto the stack and reset them.
- When we encounter a `]`, we pop the top string and count from the stack, repeat the current string that many times, and append it to the top string.
- This approach avoids the need for recursion and reduces the time complexity significantly.

```cpp
string decodeString(string s) {
    stack<string> strStack;
    stack<int> numStack;
    string res = "";
    int num = 0;
    for (char c : s) {
        if (isdigit(c)) {
            num = num * 10 + c - '0';
        } else if (c == '[') {
            strStack.push(res);
            numStack.push(num);
            res = "";
            num = 0;
        } else if (c == ']') {
            int count = numStack.top();
            numStack.pop();
            string prevStr = strStack.top();
            strStack.pop();
            while (count-- > 0) prevStr += res;
            res = prevStr;
        } else {
            res += c;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, due to the use of the stack to store the strings and counts.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Using a stack to keep track of the characters and counts is a key insight in solving this problem efficiently.
- Avoiding recursion and instead using a stack-based approach can significantly improve the time complexity.
- The problem requires careful handling of the indices and the brackets to ensure correct decoding.

**Mistakes to Avoid:**
- Incorrectly handling the indices and the brackets, leading to incorrect decoding.
- Not resetting the string and count correctly when encountering a `[`.
- Not correctly popping and appending the strings when encountering a `]`.
- Not considering the edge cases, such as an empty string or a string with no brackets.